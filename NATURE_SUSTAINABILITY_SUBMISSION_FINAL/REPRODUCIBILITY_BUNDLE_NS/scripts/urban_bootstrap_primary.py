import pandas as pd, numpy as np, json
rng=np.random.default_rng(20261003)
d=pd.read_pickle("/tmp/flood_d.pkl"); y=d['net_hazard_avoidance_reallocation'].values
def design(dd):
    X=np.column_stack([np.ones(len(dd)),dd['z_legacy'],dd['z_flood'],dd['z_int'],
        dd['ln_pop_2000'],dd['GE_ELV_AVG_2025'],np.log1p(dd['dist_port_km']),np.log1p(dd['uc_within50km'])])
    fe=pd.get_dummies(dd['GC_CNT_GAD_2025'],drop_first=True).values.astype(float)
    return np.hstack([X,fe])
Xf=np.load("/tmp/flood_Xf.npy")
b3_obs=np.linalg.lstsq(Xf,y,rcond=None)[0][3]
# ME machinery: ME_flood(L) = b2 + b3*z_legacy(L); legacy P25/50/75 -> z
m_l,s_l=d['ln_buv_2000'].mean(),d['ln_buv_2000'].std()
def zp(v): return (v-m_l)/s_l
Lp=[zp(d['ln_buv_2000'].quantile(q)) for q in (.25,.5,.75)]
blk_ids=np.asarray(pd.factorize(d['blk'])[0]); blk_u=np.unique(blk_ids)
blist=[np.where(blk_ids==i)[0] for i in blk_u]
def fit(idx):
    b=np.linalg.lstsq(Xf[idx],y[idx],rcond=None)[0]
    mes=[b[2]+b[3]*l for l in Lp]
    return [b[3]]+mes+[mes[2]-mes[0]]
B=999; E=[]
for i in range(B):
    pk=rng.integers(0,len(blist),len(blist))
    idx=np.concatenate([blist[p] for p in pk])
    try: E.append(fit(idx))
    except Exception: pass
E=np.array(E)
cols=['b3','ME_P25','ME_P50','ME_P75','Delta_ME']
res={}
for j,c in enumerate(cols):
    res[c]=dict(est=float([b3_obs,*[np.linalg.lstsq(Xf,y,rcond=None)[0][2]+b3_obs*l for l in Lp]][0] if c=='b3' else np.nan),
                ci_low=float(np.nanpercentile(E[:,j],2.5)),ci_high=float(np.nanpercentile(E[:,j],97.5)))
# proper point estimates
b=np.linalg.lstsq(Xf,y,rcond=None)[0]; mes=[b[2]+b[3]*l for l in Lp]
obs=dict(b3=b[3],ME_P25=mes[0],ME_P50=mes[1],ME_P75=mes[2],Delta_ME=mes[2]-mes[0])
out=[]
for j,c in enumerate(cols):
    p=float(2*min((E[:,j]<=0).mean(),(E[:,j]>=0).mean()))
    out.append(dict(term=c,estimate=float(obs[c]),ci_low=float(np.percentile(E[:,j],2.5)),
        ci_high=float(np.percentile(E[:,j],97.5)),p_boot=p))
pd.DataFrame(out).to_csv("FLOOD_SETTLEMENT_PRIMARY_RESULTS/analysis/primary_effects.csv",index=False)
pd.DataFrame(E,columns=cols).to_csv("FLOOD_SETTLEMENT_PRIMARY_RESULTS/analysis/primary_block_bootstrap_999.csv",index=False)
print(pd.DataFrame(out))
print("valid reps:",len(E))
