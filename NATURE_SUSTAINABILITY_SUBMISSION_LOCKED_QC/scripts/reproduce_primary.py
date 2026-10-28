#!/usr/bin/env python3
"""Reproduce the four primary estimates from the frozen locked samples and
compare against the frozen FIRST_OPENING canonical outputs.

pip install pandas numpy statsmodels
Writes repro_results.json. Point estimates are deterministic refits (tol 1e-6).
"""
import json
import os
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SD = os.path.join(ROOT, "source_data", "samples")
OUT = {"checks": [], "verdict": "PASS"}


def rec(name, frozen, got, tol=1e-6, note=""):
    ok = got is not None and abs(frozen - got) <= tol
    OUT["checks"].append({"branch": name, "frozen": frozen, "reproduced": got,
                          "tol": tol, "ok": bool(ok), "note": note})
    if not ok:
        OUT["verdict"] = "FAIL"


def z(s):
    return (s - s.mean()) / s.std(ddof=0)


import statsmodels.api as sm
import statsmodels.formula.api as smf

# ---------- T1 national: fractional logit ----------
nat = pd.read_csv(f"{SD}/nat_PRIMARY_ESTIMATION_SAMPLE_LOCKED.csv")
fro = json.load(open(f"{ROOT}/source_data/nat_PRIMARY_FIRST_OPENING.json"))
st = fro["standardization"]
nat["z_hhi"] = (nat["hhi"] - st["means"]["hhi"]) / st["sds"]["hhi"]
nat["z_mm"] = (nat["mismatch"] - st["means"]["mismatch"]) / st["sds"]["mismatch"]
nat["int"] = nat["z_hhi"] * nat["z_mm"]
nat["y"] = nat["jsd"] / np.sqrt(np.log(2))
m = smf.glm("y ~ z_hhi + z_mm + int", data=nat,
            family=sm.families.Binomial()).fit()
rec("nat.beta3", fro["beta3"], m.params["int"], note=f"N={int(m.nobs)}")

# ---------- T2 subnational: OLS + country FE (raw irr_share_base2000 x mismatch_T) ----------
sub = pd.read_csv(f"{SD}/subnat_PRIMARY_SUBNATIONAL_SAMPLE_LOCKED_V4.csv")
fro2 = json.load(open(f"{ROOT}/source_data/subnat_PRIMARY_FIRST_OPENING_SUBNATIONAL.json"))
d = sub.dropna(subset=["irr_share_base2000", "mismatch_T", "jsd"]).copy()
d["i"] = d["irr_share_base2000"] * d["mismatch_T"]
mm = smf.ols("jsd ~ irr_share_base2000 + mismatch_T + i + C(country)", data=d).fit()
rec("subnat.beta3", fro2["beta3_interaction"], mm.params["i"], note=f"N={int(mm.nobs)}")
rec("subnat.beta1", fro2["beta1_irr"], mm.params["irr_share_base2000"])

# ---------- T3 urban: OLS + country FE ----------
u = pd.read_csv(f"{SD}/urban_PRIMARY_FLOOD_SETTLEMENT_SAMPLE_LOCKED.csv")
fro3 = json.load(open(f"{ROOT}/source_data/urban_PRIMARY_FIRST_OPENING_FLOOD.json"))
d = u.copy()
stu = fro3["standardization"]
d["zl"] = (d["ln_buv_2000"] - stu["ln_buv_2000"]["mean"]) / stu["ln_buv_2000"]["sd"]
d["zf"] = (d["flood_share_2000"] - stu["flood_share_2000"]["mean"]) / stu["flood_share_2000"]["sd"]
d["i"] = d["zl"] * d["zf"]
ctrl = [c for c in ["ln_pop_2000", "GE_ELV_AVG_2025", "dist_port_km", 
                    "uc_cover_share_50km"] if c in d.columns]
ycol = "net_hazard_avoidance_reallocation"
form = ycol + " ~ zl + zf + i" + (" + " + " + ".join(ctrl) if ctrl else "") + " + C(GC_CNT_GAD_2025)"
X = np.column_stack([np.ones(len(d)), d["zl"], d["zf"], d["i"],
    d["ln_pop_2000"], d["GE_ELV_AVG_2025"], np.log1p(d["dist_port_km"]), np.log1p(d["uc_within50km"])])
fe = pd.get_dummies(d["GC_CNT_GAD_2025"], drop_first=True).values.astype(float)
Xf = np.hstack([X, fe])
beta, *_ = np.linalg.lstsq(Xf, d["net_hazard_avoidance_reallocation"].values, rcond=None)
rec("urban.beta3", fro3["beta3"], float(beta[3]), note=f"N={len(d)}")

# ---------- T4 transition: cloglog hazard ----------
tr = pd.read_csv(f"{SD}/trans_PRIMARY_TRANSITION_RISKSET_V4.csv")
fro4 = json.load(open(f"{ROOT}/source_data/trans_PRIMARY_FIRST_OPENING_TRANSITION.json"))
trd = tr.copy()
trd["legacy"] = (-trd["median_year_built_2000"] - (-trd["median_year_built_2000"]).mean()) / trd["median_year_built_2000"].std()
trd["demand"] = trd["demand_decl_flood_lag3"]
trd["capacity"] = np.log1p(trd["cum_departure_oblig_lag"])
trd["capacity"] = (trd["capacity"] - trd["capacity"].mean()) / trd["capacity"].std()
trd["lx_d"] = trd["legacy"] * trd["demand"]; trd["cx_d"] = trd["capacity"] * trd["demand"]
trd["loghu"] = np.log(trd["housing_units"])
trd["demand_cm"] = trd.groupby("fips")["demand"].transform("mean")
trd["capacity_cm"] = trd.groupby("fips")["capacity"].transform("mean")
X = sm.add_constant(pd.concat([
    trd[["demand", "capacity", "legacy", "lx_d", "cx_d", "loghu", "demand_cm", "capacity_cm"]],
    pd.get_dummies(trd["year"].astype(str), prefix="y", drop_first=True, dtype=float),
    pd.get_dummies(trd["state_fips"].astype(str).str.zfill(2), prefix="st", drop_first=True, dtype=float)], axis=1))
mm = sm.GLM(trd["event"], X, family=sm.families.Binomial(sm.families.links.cloglog())).fit()
rec("trans.H1", fro4["H1_demand_x_legacy"]["coef"], mm.params["lx_d"], note=f"N={int(mm.nobs)}")
rec("trans.H2", fro4["H2_demand_x_capacity"]["coef"], mm.params["cx_d"])
rec("trans.demand", fro4["demand"]["coef"], mm.params["demand"], tol=1e-3)

json.dump(OUT, open(os.path.join(ROOT, "repro_results.json"), "w"), indent=2)
for c in OUT["checks"]:
    print(c["branch"], "frozen", c["frozen"], "got", c["reproduced"], "ok", c["ok"])
print("VERDICT:", OUT["verdict"])
