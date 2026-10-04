import pandas as pd, numpy as np
d=pd.read_pickle("/tmp/flood_d2.pkl")
m_l,s_l=d['ln_buv_2000'].mean(),d['ln_buv_2000'].std(); m_h,s_h=d['flood_share_2000'].mean(),d['flood_share_2000'].std()
d['z_legacy']=(d['ln_buv_2000']-m_l)/s_l; d['z_flood']=(d['flood_share_2000']-m_h)/s_h
def est(dd):
    Z=np.column_stack([dd['z_legacy'],dd['z_flood'],dd['z_legacy']*dd['z_flood'],dd['ln_pop_2000'],dd['GE_ELV_AVG_2025'],np.log1p(dd['dist_port_km']),np.log1p(dd['uc_within50km'])])
    cc=pd.factorize(dd['GC_CNT_GAD_2025'])[0]; nc=cc.max()+1
    cnt=np.maximum(np.bincount(cc,minlength=nc),1)
    Zr=Z.copy(); yr=dd['net_hazard_avoidance_reallocation'].values.copy()
    for j in range(Z.shape[1]): Zr[:,j]-=np.bincount(cc,weights=Z[:,j],minlength=nc)[cc]/cnt[cc]
    yr-=np.bincount(cc,weights=yr,minlength=nc)[cc]/cnt[cc]
    return np.linalg.solve(Zr.T@Zr+1e-10*np.eye(Z.shape[1]),Zr.T@yr)[2]
def boot_diff(dd_A,dd_B,B=300,seed=11):
    """bootstrap diff of b3 between subgroups: resample blocks within each."""
    rng=np.random.default_rng(seed); diffs=[]
    def boot1(dd):
        bk=np.asarray(pd.factorize(dd['blk'])[0]); bu=np.unique(bk)
        bl=[np.where(bk==i)[0] for i in bu]
        pk=rng.integers(0,len(bl),len(bl)); return dd.iloc[np.concatenate([bl[p] for p in pk])]
    for _ in range(B):
        try: diffs.append(est(boot1(dd_A))-est(boot1(dd_B)))
        except Exception: pass
    return np.nanpercentile(diffs,[2.5,97.5]), np.nanmean(diffs)
rows=[]
groups={'coastal_le10km':d[d['dist_coast_km']<=10],'coastal_le25km':d[d['dist_coast_km']<=25],
        'coastal_le50km':d[d['dist_coast_km']<=50],'inland_gt50km':d[d['dist_coast_km']>50],'full':d}
ests={}
for name,dd in groups.items():
    e=est(dd); ests[name]=e
    rows.append(dict(subgroup=name,N=len(dd),countries=dd['GC_CNT_GAD_2025'].nunique(),
     blocks=dd['blk'].nunique(),b3=e,median_flood=dd['flood_share_2000'].median(),median_buv=dd['ln_buv_2000'].median()))
# formal difference tests vs complement
for name in ['coastal_le10km','coastal_le25km','coastal_le50km']:
    thr={'coastal_le10km':10,'coastal_le25km':25,'coastal_le50km':50}[name]
    A=d[d['dist_coast_km']<=thr]; Bc=d[d['dist_coast_km']>thr]
    ci,mn=boot_diff(A,Bc,B=200,seed=thr)
    rows.append(dict(subgroup=f"diff_{name}_vs_complement",N=len(A)+len(Bc),countries=np.nan,
     blocks=np.nan,b3=np.nan,diff_est=ests[name]-est(Bc),diff_boot_mean=mn,diff_ci_low=ci[0],diff_ci_high=ci[1],
     median_flood=np.nan,median_buv=np.nan))
ci,mn=boot_diff(d[d['dist_coast_km']>50],d[d['dist_coast_km']<=50],B=200,seed=77)
rows.append(dict(subgroup="diff_inland_vs_le50",N=len(d),countries=np.nan,blocks=np.nan,b3=np.nan,
 diff_est=ests['inland_gt50km']-ests['coastal_le50km'],diff_boot_mean=mn,diff_ci_low=ci[0],diff_ci_high=ci[1],
 median_flood=np.nan,median_buv=np.nan))
pd.DataFrame(rows).to_csv("FLOOD_SETTLEMENT_PRIMARY_RESULTS/analysis/COASTAL_HETEROGENEITY.csv",index=False)
print(pd.DataFrame(rows).to_string())
