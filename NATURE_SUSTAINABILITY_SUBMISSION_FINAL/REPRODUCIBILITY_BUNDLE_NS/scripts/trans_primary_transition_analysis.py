"""PART G-I: verify lock/sample, ONE real primary opening, interpretable effects."""
import pandas as pd, numpy as np, statsmodels.api as sm, hashlib, json, datetime, warnings, sys
warnings.filterwarnings("ignore")
ROOT = __file__.rsplit("/scripts/",1)[0]

def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(1<<20),b''): h.update(c)
    return h.hexdigest()

r_path=f"{ROOT}/analysis/PRIMARY_TRANSITION_RISKSET_V4.csv"
l_path=f"{ROOT}/TRANSITION_PRIMARY_ANALYSIS_LOCK_V4.yaml"
s_sha=open(f"{ROOT}/analysis/PRIMARY_TRANSITION_RISKSET_V4.sha256").read().split()[0]
l_sha=open(f"{ROOT}/TRANSITION_PRIMARY_ANALYSIS_LOCK_V4.sha256").read().split()[0]
assert sha(r_path)==s_sha, "sample sha mismatch - ABORT"
assert sha(l_path)==l_sha, "lock sha mismatch - ABORT"

r=pd.read_csv(r_path,dtype={"fips":str})
first_ev=r.loc[r.event==1].groupby("fips").size()
assert r.fips.nunique()==3062 and len(r)==51686 and int(r.event.sum())==1021, "sample structure mismatch - ABORT"
assert r.state_fips.nunique()==49
assert r.groupby("fips").event.sum().max()<=1
never=r.fips.nunique()-r.loc[r.event==1].fips.nunique()
assert never==2041

r["legacy"]=(-r.median_year_built_2000-(-r.median_year_built_2000).mean())/r.median_year_built_2000.std()
r["demand"]=r.demand_decl_flood_lag3
r["capacity"]=np.log1p(r.cum_departure_oblig_lag)
r["capacity"]=(r.capacity-r.capacity.mean())/r.capacity.std()
r["lx_d"]=r.legacy*r.demand; r["cx_d"]=r.capacity*r.demand
r["loghu"]=np.log(r.housing_units)
r["demand_cm"]=r.groupby("fips").demand.transform("mean")
r["capacity_cm"]=r.groupby("fips").capacity.transform("mean")
X=sm.add_constant(pd.concat([
    r[["demand","capacity","legacy","lx_d","cx_d","loghu","demand_cm","capacity_cm"]],
    pd.get_dummies(r.year.astype(str),prefix="y",drop_first=True,dtype=float),
    pd.get_dummies(r.state_fips.astype(str).str.zfill(2),prefix="st",drop_first=True,dtype=float)],axis=1))
m=sm.GLM(r.event,X,family=sm.families.Binomial(sm.families.links.cloglog())
        ).fit(cov_type="cluster",cov_kwds={"groups":r.fips})
ci=m.conf_int()
rec={"timestamp_utc":datetime.datetime.utcnow().isoformat()+"Z",
 "lock_sha256":l_sha,"sample_sha256":s_sha,"N":len(r),"counties":int(r.fips.nunique()),
 "events":int(r.event.sum()),
 "H1_demand_x_legacy":{"coef":float(m.params.lx_d),"se":float(m.bse.lx_d),
    "ci95":[float(ci.loc["lx_d",0]),float(ci.loc["lx_d",1])],
    "p":float(m.pvalues.lx_d)},
 "H2_demand_x_capacity":{"coef":float(m.params.cx_d),"se":float(m.bse.cx_d),
    "ci95":[float(ci.loc["cx_d",0]),float(ci.loc["cx_d",1])],
    "p":float(m.pvalues.cx_d)},
 "demand":{"coef":float(m.params.demand),"p":float(m.pvalues.demand)},
 "converged":bool(m.converged),"llf":float(m.llf)}
import os
jpath=f"{ROOT}/analysis/PRIMARY_FIRST_OPENING_TRANSITION.json"
if not os.path.exists(jpath):
    json.dump(rec,open(jpath,"w"),indent=1)
    oh=hashlib.sha256(open(jpath,"rb").read()).hexdigest()
    open(f"{ROOT}/analysis/PRIMARY_FIRST_OPENING_TRANSITION.sha256","w").write(oh+"  PRIMARY_FIRST_OPENING_TRANSITION.json\n")
else:
    rec=json.load(open(jpath))  # first opening is immutable; reuse recorded result

# interpretable effects: predicted hazard at demand low/high x legacy and capacity quartiles
base=r.iloc[0:0].copy()
grid=[]
def pred(dval,modval,which):
    row={c:0.0 for c in X.columns}
    row["const"]=1.0; row["loghu"]=float(r.loghu.median())
    row["demand"]=dval; row["demand_cm"]=float(r.demand_cm.median()); row["capacity_cm"]=float(r.capacity_cm.median())
    leg=float(r.legacy.quantile(.5)); cap=float(r.capacity.quantile(.5))
    if which=="legacy": leg=modval
    else: cap=modval
    row["legacy"]=leg; row["capacity"]=cap; row["lx_d"]=leg*dval; row["cx_d"]=cap*dval
    eta=sum(m.params[k]*row[k] for k in row if k in m.params.index)
    return 1-np.exp(-np.exp(eta))
# demand is sparse (93% zero): low=0 (no recent flood declaration), high=1 (>=1 declaration in lag window)
d_lo,d_hi=0.0,1.0
for lab,q in [("P25",.25),("P50",.5),("P75",.75)]:
    lv=float(r.legacy.quantile(q))
    h_lo,h_hi=pred(d_lo,lv,"legacy"),pred(d_hi,lv,"legacy")
    grid.append(("H1_legacy_"+lab,lv,h_lo,h_hi,h_hi-h_lo))
# capacity is ~60% zero: P25-P75 coincide; use P50/P90/P99 for a spread of observed values
for lab,q in [("P50",.5),("P90",.9),("P99",.99)]:
    cp=float(r.capacity.quantile(q))
    c_lo,c_hi=pred(d_lo,cp,"capacity"),pred(d_hi,cp,"capacity")
    grid.append(("H2_capacity_"+lab,cp,c_lo,c_hi,c_hi-c_lo))
eff=pd.DataFrame(grid,columns=["contrast","moderator_value","hazard_demand_low","hazard_demand_high","abs_risk_diff"])
eff.to_csv(f"{ROOT}/analysis/primary_transition_effects.csv",index=False)
print(json.dumps(rec,indent=1)[:2000]); print(eff.to_string())
