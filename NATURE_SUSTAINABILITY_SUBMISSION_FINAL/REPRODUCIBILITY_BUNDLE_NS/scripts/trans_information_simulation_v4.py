"""Extensive-margin information simulation: discrete-time cloglog hazard,
state FE + year FE (baseline hazard) + Mundlak county means; candidates
county-CRV1 vs state-CRV1. Exact estimator = statsmodels GLM Binomial(cloglog).
"""
import pandas as pd, numpy as np, warnings, time
import statsmodels.api as sm
warnings.filterwarnings("ignore")

ROOT = __file__.rsplit("/scripts/",1)[0]
r = pd.read_csv(f"{ROOT}/analysis/PRIMARY_TRANSITION_RISKSET_V4.csv", dtype={"fips":str})
r["legacy"] = -r.median_year_built_2000
r["legacy"] = (r.legacy - r.legacy.mean()) / r.legacy.std()
r["demand"] = r.demand_decl_flood_lag3
r["capacity"] = np.log1p(r.cum_departure_oblig_lag)
r["capacity"] = (r.capacity - r.capacity.mean()) / r.capacity.std()
r["lx_d"] = r.legacy * r.demand
r["cx_d"] = r.capacity * r.demand
r["loghu"] = np.log(r.housing_units)
r["demand_cm"] = r.groupby("fips").demand.transform("mean")
r["capacity_cm"] = r.groupby("fips").capacity.transform("mean")
r["year_f"] = r.year.astype(str)
r["state"] = r.state_fips.astype(str).str.zfill(2)
OBS_EV = r.event.mean()

X = sm.add_constant(pd.concat([
    r[["demand","capacity","legacy","lx_d","cx_d","loghu","demand_cm","capacity_cm"]],
    pd.get_dummies(r.year_f, prefix="y", drop_first=True, dtype=float),
    pd.get_dummies(r.state, prefix="st", drop_first=True, dtype=float)], axis=1))
EVENT_IDX = list(X.columns[:1+8])

def draw(eff_h1, eff_h2, seed, shift):
    g = np.random.default_rng(seed)
    a = pd.Series(g.normal(0,0.5,r.fips.nunique()), index=sorted(r.fips.unique()))
    z = pd.Series(g.normal(0,0.35,r.state.nunique()), index=sorted(r.state.unique()))
    yr = pd.Series(g.normal(0,0.35,21), index=list(range(2000,2021)))
    eta = (a[r.fips].to_numpy() + z[r.state].to_numpy() + yr[r.year].to_numpy()
           + 0.15*r.demand + 0.10*r.capacity + eff_h1*r.lx_d + eff_h2*r.cx_d - shift)
    p = 1 - np.exp(-np.exp(np.clip(eta,-30,10)))   # cloglog inverse
    return g.binomial(1,p)

lo, hi = 2.0, 8.0
for _ in range(20):
    mid=(lo+hi)/2
    if draw(0,0,7,mid).mean() < OBS_EV: hi=mid
    else: lo=mid
SHIFT=(lo+hi)/2
print("SHIFT",SHIFT,"target",OBS_EV,flush=True)

def fit(y, cluster):
    try:
        m = sm.GLM(r.event, X, family=sm.families.Binomial(sm.families.links.cloglog())
                   ).fit(cov_type="cluster", cov_kwds={"groups": r[cluster]})
        return m.params[["lx_d","cx_d"]], m.conf_int().loc[["lx_d","cx_d"]].values
    except Exception:
        return None

rows=[]; t0=time.time()
RAW=f'{ROOT}/analysis/information_simulation_v4_raw.csv'
import os
def flush():
    global rows
    pd.DataFrame(rows,columns=["hypothesis","true_effect","rep","inference","b","lo","hi","converged"]).to_csv(RAW,mode='a',header=not os.path.exists(RAW),index=False)
    rows=[]
def rep(hyp,eff1,eff2,seed):
    y=draw(eff1,eff2,seed,SHIFT)
    r["event"]=y
    for cn in ["fips","state"]:
        f=fit(y,cn)
        for hyp_,key in [("H1",0),("H2",1)]:
            if f is None: rows.append((hyp_,eff1 if hyp_=="H1" else eff2,seed,cn,np.nan,np.nan,np.nan,0))
            else:
                b=f[0][key]; lo_,hi_=f[1][key]
                rows.append((hyp_,eff1 if hyp_=="H1" else eff2,seed,cn,b,lo_,hi_,1))

import sys
grid=[("H1",-0.15,0),("H1",-0.05,0),("H1",0.10,0),("H2",0,0.05),("H2",0,0.15),("H2",0,-0.10)]
tasks=[("null",0,0,1000+i) for i in range(250)]
tasks+=[(hyp,e1,e2,9000+1000*grid.index((hyp,e1,e2))+i) for hyp,e1,e2 in grid for i in range(100)]
# already-completed seeds are skipped
done=set()
if os.path.exists(RAW):
    try: done=set(pd.read_csv(RAW,usecols=["rep"]).rep.unique())
    except Exception: pass
for hyp,e1,e2,seed in tasks:
    if seed in done: continue
    rep(hyp,e1,e2,seed)
    flush()
print("ALL TASKS DONE",f"{time.time()-t0:.0f}s",flush=True)

if "--agg-only" in sys.argv: pass
else:
    import sys; sys.exit(0)
df=pd.read_csv(RAW)
out=[]
for (h,e,v),g in df.groupby(["hypothesis","true_effect","inference"]):
    te=g.true_effect
    out.append((h,e,v,len(g),float(g.converged.mean()),float((g.b-te).mean()),
        float(np.sqrt(((g.b-te)**2).mean())),
        float((((g.lo<=te)&(te<=g.hi))).mean()),
        float((((g.lo>0)|(g.hi<0))).mean()),float((g.hi-g.lo).median())))
agg=pd.DataFrame(out,columns=["hypothesis","true_effect","inference","n","conv","bias","rmse","coverage","reject","ciw"])
agg.to_csv(f"{ROOT}/analysis/information_simulation_v4.csv",index=False)

print(agg.to_string())
