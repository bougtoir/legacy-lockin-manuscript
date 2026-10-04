"""PART A-D: departure-specific capacity + action-type audit + V4 risk set."""
import pandas as pd, numpy as np, hashlib, re

ROOT = __file__.rsplit("/scripts/",1)[0]
STF = ROOT.rsplit("/",1)[0]
V3 = f"{STF}/SETTLEMENT_TRANSITION_LOCK_V3"

proj = pd.read_csv(f"{STF}/data/fema_hma/HMA_Projects_v4.csv.gz",
    usecols=["projectType","programFy","stateNumberCode","countyCode","projectAmount"],low_memory=False)
proj["fips"] = proj.stateNumberCode.astype("Int64").astype(str).str.zfill(2)+proj.countyCode.astype("Int64").astype(str).str.zfill(3)
proj["projectAmount"] = proj.projectAmount.fillna(0)

# --- action-type audit: classify each unique projectType value ---
DEP = re.compile(r"(20[01]\.[0-9]+A?)\s*:", re.I)
def classify(t):
    """departure_specific if any component is a 200.x Acquisition (not 200.5 vacant land) or 201.x Relocation."""
    if not isinstance(t,str): return ("no","no","no","yes","no structured type")
    comps = [c.strip() for c in t.split(";")]
    dep=False; inplace=False
    for c in comps:
        m = re.match(r"(\d+\.\d+A?)\s*:\s*(.+)", c)
        if not m: continue
        code,label = m.group(1), m.group(2).lower()
        if code.startswith("200.") and "acquisition" in label and code!="200.5": dep=True
        elif code.startswith("201.") and "relocation" in label: dep=True
        elif code.startswith("200.5"): inplace=True      # vacant land = no structure departs
        elif code.startswith("207.") or any(k in label for k in ["elevation","floodproof","retrofit","safe room","stormwater","flood control","stabilization","erosion","sewer","wetland","generator","warning","plan","awareness","education","management cost","studies","codes","equipment","miscellaneous","advanced assistance","feasibility"]):
            inplace=True
    return ("yes" if dep else "no","yes" if (inplace and not dep) else ("no" if dep else "yes"),
            "yes" if dep else "no","yes",
            "200.x acquisition of real property/structures or 201.x relocation -> departure of structures off prior site" if dep
            else "no departure-type component (in-place mitigation, planning, equipment, or vacant land only)")
vc = proj.projectType.value_counts().rename_axis("project_type").reset_index(name="count")
cls = vc.project_type.map(classify)
vc[["departure_specific_yes_no","in_place_possible_yes_no","primary_capacity_include","secondary_capacity_include","reason"]] = pd.DataFrame(cls.tolist(),index=vc.index)
vc.to_csv(f"{ROOT}/01_CAPACITY_ACTION_TYPE_AUDIT.csv",index=False)

qual = proj[proj.project_type_qual] if "project_type_qual" in proj else None
proj["depart"] = proj.projectType.map(lambda t: classify(t)[0]=="yes")
dep = proj[proj.depart]
years = pd.DataFrame({"year":range(1989,2021)})
fips_all = pd.DataFrame({"fips":sorted(proj.fips.unique())})
dense = fips_all.assign(k=1).merge(years.assign(k=1),on="k").drop(columns="k").sort_values(["fips","year"])
for df_,prefix in [(dep,"dep"),(proj,"prop")]:
    a = df_.groupby(["fips","programFy"]).agg(oblig=("projectAmount","sum"),n=("projectAmount","size")).reset_index().rename(columns={"programFy":"year"})
    d = dense[["fips","year"]].merge(a,how="left",on=["fips","year"]).fillna({"oblig":0,"n":0})
    d["oblig"]=d.oblig.clip(lower=0)
    d[f"cum_{prefix}_oblig_lag"]=d.sort_values(["fips","year"]).groupby("fips").oblig.cumsum()-d.oblig
    d[f"cum_{prefix}_proj_lag"]=d.sort_values(["fips","year"]).groupby("fips").n.cumsum()-d.n
    dense = dense.merge(d[["fips","year",f"cum_{prefix}_oblig_lag",f"cum_{prefix}_proj_lag"]],on=["fips","year"])
for c in ["cum_dep_oblig_lag","cum_prop_oblig_lag","cum_dep_proj_lag","cum_prop_proj_lag"]:
    diff = dense.sort_values(["fips","year"]).groupby("fips")[c].diff().dropna()
    assert (diff>=-1e-6).all(), c
dense = dense.rename(columns={"cum_dep_oblig_lag":"cum_departure_oblig_lag",
    "cum_dep_proj_lag":"cum_departure_proj_lag","cum_prop_oblig_lag":"cum_property_mitigation_lag",
    "cum_prop_proj_lag":"cum_property_mitigation_proj_lag"})
dense.to_csv(f"{ROOT}/analysis/capacity_v4.csv",index=False)

# --- rebuild V4 risk set: replace only capacity ---
r = pd.read_csv(f"{V3}/analysis/PRIMARY_TRANSITION_RISKSET_V3.csv",dtype={"fips":str})
r = r.drop(columns=["cum_acq_lag_v3"])
r = r.merge(dense[["fips","year","cum_departure_oblig_lag","cum_departure_proj_lag",
                   "cum_property_mitigation_lag","cum_property_mitigation_proj_lag"]],
            on=["fips","year"],how="left")
for c in ["cum_departure_oblig_lag","cum_departure_proj_lag","cum_property_mitigation_lag","cum_property_mitigation_proj_lag"]:
    r[c] = r[c].fillna(0)
r.to_csv(f"{ROOT}/analysis/PRIMARY_TRANSITION_RISKSET_V4.csv",index=False)
h=hashlib.sha256(open(f"{ROOT}/analysis/PRIMARY_TRANSITION_RISKSET_V4.csv","rb").read()).hexdigest()
open(f"{ROOT}/analysis/PRIMARY_TRANSITION_RISKSET_V4.sha256","w").write(h+"  PRIMARY_TRANSITION_RISKSET_V4.csv\n")

# --- diagnostics ---
cd = dense[dense.year.between(2000,2020)].set_index(["fips","year"]).cum_departure_oblig_lag
pm = dense[dense.year.between(2000,2020)].set_index(["fips","year"]).cum_property_mitigation_lag
rank_dep = dense[dense.year==2020].set_index("fips").cum_departure_oblig_lag.rank()
rank_prop = dense[dense.year==2020].set_index("fips").cum_property_mitigation_lag.rank()
moved = int((abs(rank_dep-rank_prop)>len(rank_dep)*0.1).sum())
wvar = dense[dense.year.between(2000,2020)].groupby("fips").cum_departure_oblig_lag.std()
diag = pd.DataFrame({"metric":[
 "counties_ever_positive_dep","frac_zero_2000","frac_zero_2020","median_2020","p75_2020","p95_2020","max_2020",
 "within_county_sd_mean","corr_with_property_mitigation","counties_rank_shift_gt10pct","departure_projects","departure_counties"],
 "value":[int((dense.groupby('fips').cum_departure_oblig_lag.max()>0).sum()),
  float((dense[dense.year==2000].cum_departure_oblig_lag==0).mean()),
  float((dense[dense.year==2020].cum_departure_oblig_lag==0).mean()),
  float(dense[dense.year==2020].cum_departure_oblig_lag.median()),
  float(dense[dense.year==2020].cum_departure_oblig_lag.quantile(.75)),
  float(dense[dense.year==2020].cum_departure_oblig_lag.quantile(.95)),
  float(dense.cum_departure_oblig_lag.max()),
  float(wvar.mean()),
  float(cd.corr(pm)),
  moved, len(dep), dep.fips.nunique()]})
diag.to_csv(f"{ROOT}/analysis/capacity_scope_diagnostics.csv",index=False)
print(diag.to_string())
print("riskset counties",r.fips.nunique(),"cells",len(r),"events",int(r.event.sum()),"sha",h[:16])
