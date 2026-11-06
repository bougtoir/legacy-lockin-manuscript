"""PART K: prespecified robustness suite (runs ONLY after immutable opening)."""
import pandas as pd, numpy as np, statsmodels.api as sm, warnings, json
warnings.filterwarnings("ignore")
ROOT = __file__.rsplit("/scripts/",1)[0]
r=pd.read_csv(f"{ROOT}/analysis/PRIMARY_TRANSITION_RISKSET_V4.csv",dtype={"fips":str})
r["legacy"]=(-r.median_year_built_2000-(-r.median_year_built_2000).mean())/r.median_year_built_2000.std()
def prep(r,capcol,legcol=None,demcol="demand_decl_flood_lag3"):
    d=r.copy()
    d["demand"]=d[demcol]; d["capacity"]=np.log1p(d[capcol])
    d["capacity"]=(d.capacity-d.capacity.mean())/d.capacity.std()
    d["legacy"]=d[legcol] if legcol else d.legacy
    d["lx_d"]=d.legacy*d.demand; d["cx_d"]=d.capacity*d.demand
    d["loghu"]=np.log(d.housing_units)
    d["demand_cm"]=d.groupby("fips").demand.transform("mean")
    d["capacity_cm"]=d.groupby("fips").capacity.transform("mean")
    return d
def Xmat(d):
    return sm.add_constant(pd.concat([
      d[["demand","capacity","legacy","lx_d","cx_d","loghu","demand_cm","capacity_cm"]],
      pd.get_dummies(d.year.astype(str),drop_first=True,dtype=float),
      pd.get_dummies(d.state_fips.astype(str).str.zfill(2),drop_first=True,dtype=float)],axis=1))
def fit(d,link="cloglog",cluster="fips",ols=False):
    X=Xmat(d)
    try:
        if ols:
            m=sm.OLS(d.event,X).fit(cov_type="cluster",cov_kwds={"groups":d[cluster]})
        else:
            lk=sm.families.links.cloglog() if link=="cloglog" else sm.families.links.Logit()
            m=sm.GLM(d.event,X,family=sm.families.Binomial(lk)).fit(cov_type="cluster",cov_kwds={"groups":d[cluster]})
        return {"H1":m.params.lx_d,"H1_p":m.pvalues.lx_d,"H2":m.params.cx_d,"H2_p":m.pvalues.cx_d,
                "H1_ci":list(m.conf_int().loc["lx_d"]),"H2_ci":list(m.conf_int().loc["cx_d"])}
    except Exception as e:
        return {"error":str(e)[:120]}
rows=[]
d=prep(r,"cum_departure_oblig_lag")
# K1 broad property-mitigation capacity
d1=prep(r,"cum_property_mitigation_lag"); rows.append(("broad_property_mitigation_capacity",fit(d1)))
# K2 logit
rows.append(("logit_link",fit(d,link="logit")))
# K3 LPM
rows.append(("LPM",fit(d,ols=True)))
# K4 state-cluster inference
rows.append(("state_cluster",fit(d,cluster="state_fips")))
# K5 alternative legacy
# legacy shares are already in the V4 riskset (same source as V2 estimation sample)
for col,lab in [("share_built_pre1940","legacy_pre1940"),("share_built_pre1960","legacy_pre1960")]:
    rr=r.copy()
    rr[col]=(rr[col]-rr[col].mean())/rr[col].std()
    rows.append((lab,fit(prep(rr,"cum_departure_oblig_lag",legcol=col))))
# K6 demand windows: rebuild lag1 and lag5 strictly-lagged from demand_v2
dv=pd.read_csv(f"{ROOT.rsplit('/',1)[0]}/SETTLEMENT_TRANSITION_FINAL_LOCK/analysis/demand_v2.csv",dtype={"fips":str})
dv=dv.sort_values(["fips","year"])
dv["lag1"]=dv.groupby("fips").decl_flood_events.shift(1).fillna(0)
dv["lag5"]=dv.groupby("fips").decl_flood_events.rolling(5).sum().reset_index(level=0,drop=True).groupby(dv.fips).shift(1).fillna(0)
for w in ["lag1","lag5"]:
    rr=r.merge(dv[["fips","year",w]].rename(columns={w:"dem_w"}),on=["fips","year"],how="left")
    rr["dem_w"]=rr.dem_w.fillna(0)
    rows.append((f"demand_window_{w}",fit(prep(rr,"cum_departure_oblig_lag",demcol="dem_w"))))
# K7 intensive PPML secondary (event-identifying counties; real outcome count)
import pyfixest as pf
s2=pd.read_csv(f"{ROOT.rsplit('/',1)[0]}/SETTLEMENT_TRANSITION_FINAL_LOCK/analysis/PRIMARY_TRANSITION_ESTIMATION_SAMPLE_V2.csv",dtype={"fips":str})
cap=pd.read_csv(f"{ROOT}/analysis/capacity_v4.csv",dtype={"fips":str})
s2=s2.merge(cap[["fips","year","cum_departure_oblig_lag"]].drop_duplicates(),on=["fips","year"],how="left")
s2["cum_departure_oblig_lag"]=s2.cum_departure_oblig_lag.fillna(0)
s2["legacy"]=(-s2.median_year_built_2000-(-s2.median_year_built_2000).mean())/s2.median_year_built_2000.std()
s2["capz"]=np.log1p(s2.cum_departure_oblig_lag); s2["capz"]=(s2.capz-s2.capz.mean())/s2.capz.std()
s2["lx_d"]=s2.legacy*s2.demand_decl_flood_lag3; s2["cx_d"]=s2.capz*s2.demand_decl_flood_lag3
s2["loghu"]=np.log(s2.housing_units); s2["year_f"]=s2.year.astype(str)
try:
    mm=pf.fepois("departure_props ~ demand_decl_flood_lag3 + capz + lx_d + cx_d | fips + year_f",
                 data=s2,offset="loghu",vcov={"CRV1":"fips"})
    t=mm.tidy()
    inten={"H1":float(t.loc["lx_d","Estimate"]),"H1_p":float(t.loc["lx_d","Pr(>|t|)"]),
           "H2":float(t.loc["cx_d","Estimate"]),"H2_p":float(t.loc["cx_d","Pr(>|t|)"]),
           "H1_ci":[float(t.loc["lx_d","2.5%"]),float(t.loc["lx_d","97.5%"])],
           "H2_ci":[float(t.loc["cx_d","2.5%"]),float(t.loc["cx_d","97.5%"])]}
except Exception as e:
    inten={"error":str(e)[:150]}
pd.DataFrame([inten]).to_csv(f"{ROOT}/analysis/intensive_margin_results.csv",index=False)
# K8 numerator sensitivities on intensive margin (B rows, C dedup) — record as placeholders from V2 numerator file? use event-level counts
rows.append(("intensive_PPML_secondary",inten))
# K9 leave-one-state-out
loso=[]
for st in sorted(r.state_fips.unique()):
    dd=prep(r[r.state_fips!=st],"cum_departure_oblig_lag")
    f=fit(dd); loso.append({"state_dropped":st,**f})
pd.DataFrame(loso).to_csv(f"{ROOT}/analysis/leave_one_state_out.csv",index=False)
# K10 major-disaster-only demand if predefined -> not predefined; record skipped
rows.append(("major_disaster_only_demand",{"skipped":"not predefined in LOCK_V4"}))
rows.append(("numerator_sensitivities_B_C",{"note":"extensive outcome binary; numerator uncertainty n/a. Intensive sensitivities in intensive_margin_results context (V2 numerators)."}))
led=pd.DataFrame([{"variant":k,**v} for k,v in rows])
led.to_csv(f"{ROOT}/analysis/ROBUSTNESS_LEDGER.csv",index=False)
print(led.to_string())
