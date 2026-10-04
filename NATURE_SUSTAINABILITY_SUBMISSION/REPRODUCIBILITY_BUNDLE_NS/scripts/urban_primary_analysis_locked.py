# PHASE 0-9: lock verification, first-and-only primary fit, 999 block bootstrap, effects, influence, figures.
import hashlib, json, sys, datetime
import pandas as pd, numpy as np
A="FLOOD_SETTLEMENT_PRIMARY_RESULTS"; R="FLOOD_SETTLEMENT_FINAL_LOCK"
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
lock_sha=sha(f"{R}/FLOOD_SETTLEMENT_PRIMARY_LOCK_V3.yaml")
smp_sha=sha(f"{R}/analysis/PRIMARY_FLOOD_SETTLEMENT_SAMPLE_LOCKED.csv")
assert lock_sha=="eccd89bfd1537b9181129e05d10d945b1fce354315a0eb358f225a6c55982e45","LOCK SHA MISMATCH — ABORT"
assert smp_sha=="15233d49b21b8a80a1196a16525ae9fbb6621c68be36b8d7abec7208c902a9f7","SAMPLE SHA MISMATCH — ABORT"
d=pd.read_csv(f"{R}/analysis/PRIMARY_FLOOD_SETTLEMENT_SAMPLE_LOCKED.csv")
N=len(d); NC=d['GC_CNT_GAD_2025'].nunique(); NB=d['blk'].nunique()
assert (N,NC,NB)==(4598,143,175)
open(f"{A}/00_LOCK_VERIFICATION.md","w").write(
 f"# Lock Verification — PASS\n\nlock_sha256={lock_sha}\nsample_sha256={smp_sha}\nN={N} countries={NC} blocks={NB}\n")
# standardization on locked sample
m_l,s_l=d['ln_buv_2000'].mean(),d['ln_buv_2000'].std()
m_h,s_h=d['flood_share_2000'].mean(),d['flood_share_2000'].std()
d['z_legacy']=(d['ln_buv_2000']-m_l)/s_l
d['z_flood']=(d['flood_share_2000']-m_h)/s_h
d['z_int']=d['z_legacy']*d['z_flood']
def design(dd):
    X=np.column_stack([np.ones(len(dd)),dd['z_legacy'],dd['z_flood'],dd['z_int'],
        dd['ln_pop_2000'],dd['GE_ELV_AVG_2025'],np.log1p(dd['dist_port_km']),np.log1p(dd['uc_within50km'])])
    fe=pd.get_dummies(dd['GC_CNT_GAD_2025'],drop_first=True).values.astype(float)
    return np.hstack([X,fe])
y=d['net_hazard_avoidance_reallocation'].values
Xf=design(d)
beta,res,*_=np.linalg.lstsq(Xf,y,rcond=None)
yhat=Xf@beta; e=y-yhat
r2=1-e.var()/y.var()
b1,b2,b3=beta[1],beta[2],beta[3]
rec=dict(timestamp_utc=datetime.datetime.utcnow().isoformat()+"Z",lock_sha256=lock_sha,sample_sha256=smp_sha,
 N=N,countries=NC,blocks=NB,standardization=dict(ln_buv_2000=dict(mean=float(m_l),sd=float(s_l)),
 flood_share_2000=dict(mean=float(m_h),sd=float(s_h))),
 beta0=float(beta[0]),beta1=float(b1),beta2=float(b2),beta3=float(b3),r2=float(r2),resid_sd=float(e.std()),
 outcome="net_hazard_avoidance_reallocation",model="OLS + country FE",note="FIRST AND ONLY opening; immutable")
json.dump(rec,open(f"{A}/analysis/PRIMARY_FIRST_OPENING_FLOOD.json","w"),indent=2)
s=sha(f"{A}/analysis/PRIMARY_FIRST_OPENING_FLOOD.json")
open(f"{A}/analysis/PRIMARY_FIRST_OPENING_FLOOD.sha256","w").write(s+"  PRIMARY_FIRST_OPENING_FLOOD.json\n")
pd.DataFrame([dict(term=t,est=float(beta[i])) for i,t in
 enumerate(['intercept','z_legacy','z_flood','z_legacy:z_flood','ln_pop','elevation','ln1p_dist_port','ln1p_uc50'])]
 ).to_csv(f"{A}/analysis/primary_model_results.csv",index=False)
print("FIRST OPENING b3=%.5f b1=%.5f b2=%.5f R2=%.3f sha=%s"%(b3,b1,b2,r2,s))
np.save("/tmp/flood_Xf.npy",Xf); d.to_pickle("/tmp/flood_d.pkl")
