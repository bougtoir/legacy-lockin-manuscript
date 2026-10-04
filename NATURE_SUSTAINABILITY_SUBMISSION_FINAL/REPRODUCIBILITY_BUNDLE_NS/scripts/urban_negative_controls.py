import pandas as pd, numpy as np
d=pd.read_pickle("/tmp/flood_d2.pkl")
m_l,s_l=d['ln_buv_2000'].mean(),d['ln_buv_2000'].std(); m_h,s_h=d['flood_share_2000'].mean(),d['flood_share_2000'].std()
d['z_legacy']=(d['ln_buv_2000']-m_l)/s_l; d['z_flood']=(d['flood_share_2000']-m_h)/s_h
def est(dd,ycol='net_hazard_avoidance_reallocation',zlc='z_legacy',zhc='z_flood',extra=[]):
    dd=dd.dropna(subset=[ycol,zlc,zhc]+extra)
    Z=np.column_stack([dd[zlc],dd[zhc],dd[zlc]*dd[zhc]]+[dd[c] for c in extra])
    cc=pd.factorize(dd['GC_CNT_GAD_2025'])[0]; nc=cc.max()+1
    cnt=np.maximum(np.bincount(cc,minlength=nc),1)
    Zr=Z.copy(); yr=dd[ycol].values.copy()
    for j in range(Z.shape[1]): Zr[:,j]-=np.bincount(cc,weights=Z[:,j],minlength=nc)[cc]/cnt[cc]
    yr-=np.bincount(cc,weights=yr,minlength=nc)[cc]/cnt[cc]
    return np.linalg.solve(Zr.T@Zr+1e-10*np.eye(Z.shape[1]),Zr.T@yr)[2],len(dd)
EXTRA=['ln_pop_2000','GE_ELV_AVG_2025']
def d2(dd): 
    dd=dd.copy(); dd['dport']=np.log1p(dd['dist_port_km']); dd['duc50']=np.log1p(dd['uc_within50km']); return dd
d=d2(d); EXTRA=['ln_pop_2000','GE_ELV_AVG_2025','dport','duc50']
rows=[]
def add(n,v,n_,note=""): rows.append(dict(control=n,estimate=v,N=n_,notes=note))
# 1 low-hazard matched control
lh=pd.read_csv("FLOOD_SETTLEMENT_FINAL_LOCK/analysis/low_hazard_control_sample.csv") if __import__('os').path.exists("FLOOD_SETTLEMENT_FINAL_LOCK/analysis/low_hazard_control_sample.csv") else None
if lh is not None:
    lh=d2(lh)
    lh['net_hazard_avoidance_reallocation']=1-(lh['EX_010_BUS_2020']-lh['EX_010_BUS_2000'])/(lh['GH_BUS_TOT_2020']-lh['GH_BUS_TOT_2000'])
    lh['z_legacy']=(lh['ln_buv_2000']-lh['ln_buv_2000'].mean())/lh['ln_buv_2000'].std()
    lh['z_flood']=(lh['flood_share_2000']-lh['flood_share_2000'].mean())/max(lh['flood_share_2000'].std(),1e-9)
    v,n=est(lh)
    add("low_hazard_matched_control",v,n,"flood_share<1% matched controls; near-zero hazard variance limits identification")
else: add("low_hazard_matched_control",np.nan,0,"control file missing")
# 2 future exposure predicting prior change: use EX_010_SHB_2020 (future share) as 'hazard' predictor of reallocation -> placebo timing
dd=d.copy(); dd['z_flood_f']=(dd['EX_010_SHB_2020']-dd['EX_010_SHB_2020'].mean())/dd['EX_010_SHB_2020'].std()
v,n=est(dd,zhc='z_flood_f'); add("future_exposure_placebo",v,n,"2020 flood share replacing baseline 2000")
# 3 spatially shifted hazard: permute hazard within country
rng=np.random.default_rng(5); dd=d.copy()
dd['z_flood_s']=dd.groupby('GC_CNT_GAD_2025')['z_flood'].transform(lambda s: rng.permutation(s.values))
v,n=est(dd,zhc='z_flood_s'); add("spatially_shifted_hazard",v,n,"hazard permuted within country")
# 4 wrong window: outcome redefined as pre-period change? no pre-2000 reallocation available -> use population growth 2000-2020 share change? use delta_expo_share of BUS (pre-treatment proxy unavailable) -> report infeasible partially: use 2020->2030 projection? epochs to 2030 exist in UCDB but not extracted -> mark infeasible
add("wrong_window_1990_2000",np.nan,0,"INFEASIBLE: no extracted pre-2000 reallocation measure (1975-2000 BU components not in locked sample)")
# 5 thresholds already in robustness (elig 2/5%) -> reference
add("eligibility_thresholds",np.nan,0,"covered in ROBUSTNESS_LEDGER elig_2.0pct/-0.0075; elig_5.0pct/-0.0043")
# 6 leave-one-country-out range
X=np.load("/tmp/flood_Xf.npy"); y=d['net_hazard_avoidance_reallocation'].values
def b3x(idx): return np.linalg.lstsq(X[idx],y[idx],rcond=None)[0][3]
loco=[b3x(d.index[d['GC_CNT_GAD_2025']!=c].values) for c in d['GC_CNT_GAD_2025'].unique()]
add("leave_one_country_out_range",f"{min(loco):.4f}..{max(loco):.4f}",len(loco),"primary b3=-0.0083")
# 7 leave-one-region-out
loro=[b3x(d.index[d['GC_DEV_WIG_2025']!=c].values) for c in d['GC_DEV_WIG_2025'].unique()]
add("leave_one_region_out_range",f"{min(loro):.4f}..{max(loro):.4f}",len(loro),"regions="+",".join(d['GC_DEV_WIG_2025'].astype(str).unique()))
# 8 megacity exclusion
v,n=est(d[~d.index.isin(d.nlargest(10,'GH_BUV_TOT_2000').index)]); add("top10_BUV_excl",v,n)
# 9 port-city exclusion <25km
v,n=est(d[d['dist_port_km']>25]); add("port25_excl",v,n)
# 10 capital-city exclusion
v,n=est(d[d['GC_UCM_CAP']!='Capital'] if (d['GC_UCM_CAP']=='Capital').any() else d[d['GC_UCM_CAP']!=d['GC_UCM_CAP'].value_counts().idxmax()])
add("capital_excl",v,n,"GC_UCM_CAP categories: "+str(d['GC_UCM_CAP'].unique()[:5]))
pd.DataFrame(rows).to_csv("FLOOD_SETTLEMENT_PRIMARY_RESULTS/analysis/NEGATIVE_CONTROL_LEDGER.csv",index=False)
print(pd.DataFrame(rows).to_string())
