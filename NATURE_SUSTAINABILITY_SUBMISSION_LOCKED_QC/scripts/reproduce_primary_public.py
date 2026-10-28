#!/usr/bin/env python3
"""Clean-environment reproduction of the four frozen primary estimates.

Run inside the public repo:
    pip install pandas numpy statsmodels
    python3 REPRODUCIBILITY_BUNDLE_NS/scripts/reproduce_primary_public.py <bundle_dir>

<bundle_dir> defaults to the directory containing this script's parent
(i.e. REPRODUCIBILITY_BUNDLE_NS). Compares refit coefficients to the frozen
results/*.json values with tolerance 1e-6 (deterministic refits).
"""
import json
import os
import sys
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

BUNDLE = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.join(BUNDLE, "samples")
R = os.path.join(BUNDLE, "results")
ok_all = True


def rec(name, frozen, got, tol=1e-6):
    global ok_all
    ok = got is not None and abs(frozen - got) <= tol
    ok_all = ok_all and ok
    print(f"{name}: frozen={frozen} reproduced={got} {'PASS' if ok else 'FAIL'}")


def z(s):
    return (s - s.mean()) / s.std(ddof=0)


# T1 national — fractional logit, outcome jsd/sqrt(ln2), stored standardization
nat = pd.read_csv(f"{S}/nat_PRIMARY_ESTIMATION_SAMPLE_LOCKED.csv")
fro = json.load(open(f"{R}/nat_PRIMARY_FIRST_OPENING.json"))
st = fro["standardization"]
nat["z_hhi"] = (nat["hhi"] - st["means"]["hhi"]) / st["sds"]["hhi"]
nat["z_mm"] = (nat["mismatch"] - st["means"]["mismatch"]) / st["sds"]["mismatch"]
nat["int"] = nat["z_hhi"] * nat["z_mm"]
nat["y"] = nat["jsd"] / np.sqrt(np.log(2))
m = smf.glm("y ~ z_hhi + z_mm + int", data=nat, family=sm.families.Binomial()).fit()
rec("nat.beta3", fro["beta3"], m.params["int"])

# T2 subnational — OLS + country FE, raw irr_share_base2000 x mismatch_T
sub = pd.read_csv(f"{S}/subnat_PRIMARY_SUBNATIONAL_SAMPLE_LOCKED_V4.csv")
fro2 = json.load(open(f"{R}/subnat_PRIMARY_FIRST_OPENING_SUBNATIONAL.json"))
d = sub.dropna(subset=["irr_share_base2000", "mismatch_T", "jsd"]).copy()
d["i"] = d["irr_share_base2000"] * d["mismatch_T"]
mm = smf.ols("jsd ~ irr_share_base2000 + mismatch_T + i + C(country)", data=d).fit()
rec("subnat.beta3", fro2["beta3_interaction"], mm.params["i"])

# T3 urban — OLS + country FE, stored standardization, exact design of the locked script
u = pd.read_csv(f"{S}/urban_PRIMARY_FLOOD_SETTLEMENT_SAMPLE_LOCKED.csv")
fro3 = json.load(open(f"{R}/urban_PRIMARY_FIRST_OPENING_FLOOD.json"))
stu = fro3["standardization"]
u["zl"] = (u["ln_buv_2000"] - stu["ln_buv_2000"]["mean"]) / stu["ln_buv_2000"]["sd"]
u["zf"] = (u["flood_share_2000"] - stu["flood_share_2000"]["mean"]) / stu["flood_share_2000"]["sd"]
u["i"] = u["zl"] * u["zf"]
X = np.column_stack([np.ones(len(u)), u["zl"], u["zf"], u["i"],
                     u["ln_pop_2000"], u["GE_ELV_AVG_2025"],
                     np.log1p(u["dist_port_km"]), np.log1p(u["uc_within50km"])])
fe = pd.get_dummies(u["GC_CNT_GAD_2025"], drop_first=True).values.astype(float)
beta, *_ = np.linalg.lstsq(np.hstack([X, fe]), u["net_hazard_avoidance_reallocation"].values, rcond=None)
rec("urban.beta3", fro3["beta3"], float(beta[3]))

# T4 transition — county cloglog hazard with Mundlak means, year & state FE
tr = pd.read_csv(f"{S}/trans_PRIMARY_TRANSITION_RISKSET_V4.csv", dtype={"fips": str})
fro4 = json.load(open(f"{R}/trans_PRIMARY_FIRST_OPENING_TRANSITION.json"))
tr["legacy"] = (-tr["median_year_built_2000"] - (-tr["median_year_built_2000"]).mean()) / tr["median_year_built_2000"].std()
tr["demand"] = tr["demand_decl_flood_lag3"]
tr["capacity"] = np.log1p(tr["cum_departure_oblig_lag"])
tr["capacity"] = (tr["capacity"] - tr["capacity"].mean()) / tr["capacity"].std()
tr["lx_d"] = tr["legacy"] * tr["demand"]; tr["cx_d"] = tr["capacity"] * tr["demand"]
tr["loghu"] = np.log(tr["housing_units"])
tr["demand_cm"] = tr.groupby("fips")["demand"].transform("mean")
tr["capacity_cm"] = tr.groupby("fips")["capacity"].transform("mean")
X = sm.add_constant(pd.concat([
    tr[["demand", "capacity", "legacy", "lx_d", "cx_d", "loghu", "demand_cm", "capacity_cm"]],
    pd.get_dummies(tr["year"].astype(str), prefix="y", drop_first=True, dtype=float),
    pd.get_dummies(tr["state_fips"].astype(str).str.zfill(2), prefix="st", drop_first=True, dtype=float)], axis=1))
mm = sm.GLM(tr["event"], X, family=sm.families.Binomial(sm.families.links.cloglog())).fit()
rec("trans.H1", fro4["H1_demand_x_legacy"]["coef"], mm.params["lx_d"])
rec("trans.H2", fro4["H2_demand_x_capacity"]["coef"], mm.params["cx_d"])
rec("trans.demand", fro4["demand"]["coef"], mm.params["demand"], tol=1e-3)

print("VERDICT:", "PASS" if ok_all else "FAIL")
sys.exit(0 if ok_all else 1)
