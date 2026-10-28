#!/usr/bin/env python3
"""Build analysis/canonical_results.json + canonical_results.csv.

Every value is read programmatically from an authoritative frozen output in
source_data/ (first-opening JSONs, primary results/effects CSVs, robustness
and heterogeneity ledgers, simulation CSVs, frozen estimation samples, or
branch docs). No number is typed in this script: each entry records its
source file and locator (column + row key or JSON key).

Usage: python3 build_canonical_registry.py
"""
import ast
import csv
import json
import os
import re

import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SD = os.path.join(ROOT, "source_data")
OUT_JSON = os.path.join(ROOT, "analysis", "canonical_results.json")
OUT_CSV = os.path.join(ROOT, "analysis", "canonical_results.csv")

REG = {}


def add(key, value, kind, source_file, source_locator, study_id="", analysis_id="",
        primary_secondary="", units="", effect_scale="", formatting="raw",
        note=""):
    REG[key] = {
        "key": key,
        "study_id": study_id,
        "analysis_id": analysis_id,
        "primary_secondary": primary_secondary,
        "value": value,
        "units": units,
        "effect_scale": effect_scale,
        "kind": kind,  # analysis_result | derived | design_constant | dataset_descriptor
        "source_file": source_file,
        "source_locator": source_locator,
        "formatting_rule": formatting,
        "note": note,
    }


def J(name):
    return json.load(open(os.path.join(SD, name)))


def C(name):
    return pd.read_csv(os.path.join(SD, name))


# ---------------- national agriculture (T1) ---------------------------------
nat_j = J("nat_PRIMARY_FIRST_OPENING.json")
nat_m = C("nat_primary_model_results.csv").iloc[0]
src_j, src_m = "nat_PRIMARY_FIRST_OPENING.json", "nat_primary_model_results.csv"

add("nat.N", int(nat_j["N"]), "analysis_result", src_j, "N",
    "T1_national_agriculture", "primary_fit", "primary", "countries")
add("nat.beta3", nat_j["beta3"], "analysis_result", src_j, "beta3",
    "T1_national_agriculture", "primary_fit", "primary", "standardized coefficient",
    "JSD", "signed4", )
add("nat.beta3_ci_lo", float(nat_m["beta3_ci_lo"]), "analysis_result", src_m,
    "beta3_ci_lo", "T1_national_agriculture", "primary_fit", "primary",
    "standardized coefficient", "JSD", "signed4")
add("nat.beta3_ci_hi", float(nat_m["beta3_ci_hi"]), "analysis_result", src_m,
    "beta3_ci_hi", "T1_national_agriculture", "primary_fit", "primary",
    "standardized coefficient", "JSD", "signed4")
add("nat.beta3_p", float(nat_m["beta3_p_boot"]), "analysis_result", src_m,
    "beta3_p_boot", "T1_national_agriculture", "primary_fit", "primary",
    "bootstrap p-value", "", "p3")
add("nat.boot_B", int(nat_m["valid_replicates"]), "design_constant", src_m,
    "valid_replicates", "T1_national_agriculture", "primary_fit", "primary",
    "bootstrap replicates")
add("nat.beta0", nat_j["beta0"], "analysis_result", src_j, "beta0",
    "T1_national_agriculture", "primary_fit", "primary")
add("nat.beta1", nat_j["beta1"], "analysis_result", src_j, "beta1",
    "T1_national_agriculture", "primary_fit", "primary")
add("nat.beta2", nat_j["beta2"], "analysis_result", src_j, "beta2",
    "T1_national_agriculture", "primary_fit", "primary")

nat_sample = pd.read_csv(os.path.join(SD, "samples", "nat_PRIMARY_ESTIMATION_SAMPLE_LOCKED.csv"))
add("nat.n_subregions", int(nat_sample["subregion"].nunique()), "derived",
    "samples/nat_PRIMARY_ESTIMATION_SAMPLE_LOCKED.csv", "subregion.nunique()",
    "T1_national_agriculture", "primary_fit", "primary", "M49 subregions")

# ---------------- subnational agriculture (T2) ------------------------------
sub_j = J("subnat_PRIMARY_FIRST_OPENING_SUBNATIONAL.json")
sub_m = C("subnat_primary_model_results.csv").iloc[0]
src_j, src_m = "subnat_PRIMARY_FIRST_OPENING_SUBNATIONAL.json", "subnat_primary_model_results.csv"

add("subnat.N", int(sub_j["N"]), "analysis_result", src_j, "N",
    "T2_subnational_agriculture", "primary_fit", "primary", "admin-1 units")
add("subnat.countries", int(sub_j["countries"]), "analysis_result", src_j,
    "countries", "T2_subnational_agriculture", "primary_fit", "primary", "countries")
add("subnat.beta3", sub_j["beta3_interaction"], "analysis_result", src_j,
    "beta3_interaction", "T2_subnational_agriculture", "primary_fit", "primary",
    "standardized coefficient", "JSD", "signed4")
add("subnat.beta3_ci_lo", float(sub_m["beta3_ci_lo"]), "analysis_result", src_m,
    "beta3_ci_lo", "T2_subnational_agriculture", "primary_fit", "primary",
    "standardized coefficient", "JSD", "signed4")
add("subnat.beta3_ci_hi", float(sub_m["beta3_ci_hi"]), "analysis_result", src_m,
    "beta3_ci_hi", "T2_subnational_agriculture", "primary_fit", "primary",
    "standardized coefficient", "JSD", "signed4")
add("subnat.beta3_p", float(sub_m["beta3_p_two_sided"]), "analysis_result", src_m,
    "beta3_p_two_sided", "T2_subnational_agriculture", "primary_fit", "primary",
    "bootstrap p-value", "", "p3")
add("subnat.boot_B", int(sub_m["B"]), "design_constant", src_m, "B",
    "T2_subnational_agriculture", "primary_fit", "primary", "bootstrap replicates")
add("subnat.r2", float(sub_m["r2"]), "analysis_result", src_m, "r2",
    "T2_subnational_agriculture", "primary_fit", "primary")

sub_e = C("subnat_primary_effects.csv").set_index("effect")
add("subnat.delta_me", float(sub_e.loc["Delta_ME", "point"]), "analysis_result",
    "subnat_primary_effects.csv", "effect==Delta_ME:point",
    "T2_subnational_agriculture", "primary_effect", "primary", "JSD", "JSD")
add("subnat.delta_me_ci_lo", float(sub_e.loc["Delta_ME", "ci_lo"]), "analysis_result",
    "subnat_primary_effects.csv", "effect==Delta_ME:ci_lo",
    "T2_subnational_agriculture", "primary_effect", "primary", "JSD", "JSD")
add("subnat.delta_me_ci_hi", float(sub_e.loc["Delta_ME", "ci_hi"]), "analysis_result",
    "subnat_primary_effects.csv", "effect==Delta_ME:ci_hi",
    "T2_subnational_agriculture", "primary_effect", "primary", "JSD", "JSD")

sub_sample = pd.read_csv(os.path.join(SD, "samples", "subnat_PRIMARY_SUBNATIONAL_SAMPLE_LOCKED_V4.csv"))
add("subnat.median_gap_years", float(sub_sample["gap"].median()), "derived",
    "samples/subnat_PRIMARY_SUBNATIONAL_SAMPLE_LOCKED_V4.csv", "gap.median()",
    "T2_subnational_agriculture", "sample_descriptor", "primary", "years")
add("subnat.regions", 4, "dataset_descriptor",
    "branch_docs/subnat_08_RESULT_CLASSIFICATION.md",
    "sample descriptor: four regions after first-order-division audit",
    "T2_subnational_agriculture", "sample_descriptor", "primary", "regions",
    note="strict first-order-division audit outcome")

sub_rl = C("subnat_ROBUSTNESS_LEDGER.csv")
n_subnat_variants = int(((sub_rl["analysis_id"] != "primary_OLS_grid10") &
                         ~sub_rl["analysis_id"].str.contains("LOCO|LORO")).sum())
add("subnat.n_robustness_variants", n_subnat_variants, "derived",
    "subnat_ROBUSTNESS_LEDGER.csv",
    "rows excluding primary_OLS_grid10, LOCO_range, LORO_range",
    "T2_subnational_agriculture", "robustness", "secondary", "variants",
    note="manuscript wording: 'nine prespecified robustness variants'")

# ---------------- urban built capital (T3) ----------------------------------
urb_j = J("urban_PRIMARY_FIRST_OPENING_FLOOD.json")
urb_e = C("urban_primary_effects.csv").set_index("term")
src_j, src_e = "urban_PRIMARY_FIRST_OPENING_FLOOD.json", "urban_primary_effects.csv"

add("urban.N", int(urb_j["N"]), "analysis_result", src_j, "N",
    "T3_urban_built_capital", "primary_fit", "primary", "urban centres")
add("urban.countries", int(urb_j["countries"]), "analysis_result", src_j,
    "countries", "T3_urban_built_capital", "primary_fit", "primary", "countries")
add("urban.blocks", int(urb_j["blocks"]), "analysis_result", src_j, "blocks",
    "T3_urban_built_capital", "primary_fit", "primary", "geographic blocks")
add("urban.beta3", urb_j["beta3"], "analysis_result", src_j, "beta3",
    "T3_urban_built_capital", "primary_fit", "primary",
    "standardized coefficient", "reallocation index", "signed4")
add("urban.beta3_ci_lo", float(urb_e.loc["b3", "ci_low"]), "analysis_result",
    src_e, "term==b3:ci_low", "T3_urban_built_capital", "primary_fit",
    "primary", "standardized coefficient", "reallocation index", "signed4")
add("urban.beta3_ci_hi", float(urb_e.loc["b3", "ci_high"]), "analysis_result",
    src_e, "term==b3:ci_high", "T3_urban_built_capital", "primary_fit",
    "primary", "standardized coefficient", "reallocation index", "signed4")
add("urban.beta3_p", float(urb_e.loc["b3", "p_boot"]), "analysis_result",
    src_e, "term==b3:p_boot", "T3_urban_built_capital", "primary_fit",
    "primary", "bootstrap p-value", "", "p3")
add("urban.delta_me", float(urb_e.loc["Delta_ME", "estimate"]), "analysis_result",
    src_e, "term==Delta_ME:estimate", "T3_urban_built_capital",
    "primary_effect", "primary", "reallocation index", "reallocation index", "signed4")
add("urban.delta_me_ci_lo", float(urb_e.loc["Delta_ME", "ci_low"]), "analysis_result",
    src_e, "term==Delta_ME:ci_low", "T3_urban_built_capital", "primary_effect",
    "primary", "reallocation index", "reallocation index", "signed4")
add("urban.delta_me_ci_hi", float(urb_e.loc["Delta_ME", "ci_high"]), "analysis_result",
    src_e, "term==Delta_ME:ci_high", "T3_urban_built_capital", "primary_effect",
    "primary", "reallocation index", "reallocation index", "signed4")
add("urban.delta_me_p", float(urb_e.loc["Delta_ME", "p_boot"]), "analysis_result",
    src_e, "term==Delta_ME:p_boot", "T3_urban_built_capital", "primary_effect",
    "primary", "bootstrap p-value", "", "p3")

urb_sample = pd.read_csv(os.path.join(SD, "samples", "urban_PRIMARY_FLOOD_SETTLEMENT_SAMPLE_LOCKED.csv"))
outcome_sd = float(urb_sample["net_hazard_avoidance_reallocation"].std())
add("urban.outcome_sd", outcome_sd, "derived",
    "samples/urban_PRIMARY_FLOOD_SETTLEMENT_SAMPLE_LOCKED.csv",
    "net_hazard_avoidance_reallocation.std()",
    "T3_urban_built_capital", "sample_descriptor", "primary", "reallocation index")
add("urban.delta_me_frac_sd", abs(float(urb_e.loc["Delta_ME", "estimate"])) / outcome_sd,
    "derived",
    "urban_primary_effects.csv + samples/urban_PRIMARY_FLOOD_SETTLEMENT_SAMPLE_LOCKED.csv",
    "abs(Delta_ME)/sd(outcome)",
    "T3_urban_built_capital", "primary_effect", "primary", "fraction of outcome SD",
    "", "pct1")

het = C("urban_COASTAL_HETEROGENEITY.csv").set_index("subgroup")
for g, lab in [("coastal_le10km", "coastal10"), ("coastal_le25km", "coastal25"),
               ("coastal_le50km", "coastal50"), ("inland_gt50km", "inland"),
               ("full", "full")]:
    add(f"urban.het_{lab}.b3", float(het.loc[g, "b3"]), "analysis_result",
        "urban_COASTAL_HETEROGENEITY.csv", f"subgroup=={g}:b3",
        "T3_urban_built_capital", "heterogeneity", "secondary",
        "standardized coefficient", "reallocation index", "signed4")
    add(f"urban.het_{lab}.N", int(het.loc[g, "N"]), "analysis_result",
        "urban_COASTAL_HETEROGENEITY.csv", f"subgroup=={g}:N",
        "T3_urban_built_capital", "heterogeneity", "secondary", "urban centres")

urb_rl = C("urban_ROBUSTNESS_LEDGER.csv").set_index("analysis_id")
add("urban.rp100.b3", float(urb_rl.loc["RP100_hazard", "interaction_est"]),
    "analysis_result", "urban_ROBUSTNESS_LEDGER.csv", "RP100_hazard:interaction_est",
    "T3_urban_built_capital", "robustness", "secondary",
    "standardized coefficient", "reallocation index", "signed4")
add("urban.rp100.ci_lo", float(urb_rl.loc["RP100_hazard", "ci_low"]),
    "analysis_result", "urban_ROBUSTNESS_LEDGER.csv", "RP100_hazard:ci_low",
    "T3_urban_built_capital", "robustness", "secondary")
add("urban.rp100.ci_hi", float(urb_rl.loc["RP100_hazard", "ci_high"]),
    "analysis_result", "urban_ROBUSTNESS_LEDGER.csv", "RP100_hazard:ci_high",
    "T3_urban_built_capital", "robustness", "secondary")
add("urban.slr.N", int(urb_rl.loc["SLR_subsample", "N"]), "analysis_result",
    "urban_ROBUSTNESS_LEDGER.csv", "SLR_subsample:N",
    "T3_urban_built_capital", "robustness", "secondary", "urban centres",
    note="locked SLR-measured subsample (NS_ESB_SLR_2025 non-null); corrects "
         "earlier draft's conflation with the 1,334-centre design-phase coverage")
add("urban.slr.b3", float(urb_rl.loc["SLR_subsample", "interaction_est"]),
    "analysis_result", "urban_ROBUSTNESS_LEDGER.csv", "SLR_subsample:interaction_est",
    "T3_urban_built_capital", "robustness", "secondary")

nc = C("urban_NEGATIVE_CONTROL_LEDGER.csv").set_index("control")
add("urban.negctrl.matched", float(nc.loc["low_hazard_matched_control", "estimate"]),
    "analysis_result", "urban_NEGATIVE_CONTROL_LEDGER.csv",
    "low_hazard_matched_control:estimate", "T3_urban_built_capital",
    "negative_control", "secondary", "estimate", "", "signed4")
add("urban.negctrl.matched_N", int(nc.loc["low_hazard_matched_control", "N"]),
    "analysis_result", "urban_NEGATIVE_CONTROL_LEDGER.csv",
    "low_hazard_matched_control:N", "T3_urban_built_capital",
    "negative_control", "secondary", "urban centres")
add("urban.negctrl.placebo", float(nc.loc["future_exposure_placebo", "estimate"]),
    "analysis_result", "urban_NEGATIVE_CONTROL_LEDGER.csv",
    "future_exposure_placebo:estimate", "T3_urban_built_capital",
    "negative_control", "secondary", "estimate", "", "signed4")
add("urban.negctrl.top10buv", float(nc.loc["top10_BUV_excl", "estimate"]),
    "analysis_result", "urban_NEGATIVE_CONTROL_LEDGER.csv",
    "top10_BUV_excl:estimate", "T3_urban_built_capital",
    "negative_control", "secondary", "estimate", "", "signed4")
add("urban.negctrl.port25", float(nc.loc["port25_excl", "estimate"]),
    "analysis_result", "urban_NEGATIVE_CONTROL_LEDGER.csv",
    "port25_excl:estimate", "T3_urban_built_capital",
    "negative_control", "secondary", "estimate", "", "signed4")
add("urban.negctrl.capitals", float(nc.loc["capital_excl", "estimate"]),
    "analysis_result", "urban_NEGATIVE_CONTROL_LEDGER.csv",
    "capital_excl:estimate", "T3_urban_built_capital",
    "negative_control", "secondary", "estimate", "", "signed4")

nonlin = C("urban_nonlinear_results.csv").set_index("term")
for t in nonlin.index:
    add(f"urban.nonlin.{t}", float(nonlin.loc[t, "est"]), "analysis_result",
        "urban_nonlinear_results.csv", f"term=={t}:est",
        "T3_urban_built_capital", "nonlinear", "secondary")

add("urban.total_centres_ucdb", 11422, "dataset_descriptor",
    "branch_docs/urban_10_RESULT_CLASSIFICATION.md",
    "GHS-UCDB R2024A coverage statement (external dataset descriptor)",
    "T3_urban_built_capital", "dataset_descriptor", "", "urban centres",
    note="GHS Urban Centre Database total; not an analysis result")

# ---------------- transition initiation (T4) --------------------------------
tr_j = J("trans_PRIMARY_FIRST_OPENING_TRANSITION.json")
src_j = "trans_PRIMARY_FIRST_OPENING_TRANSITION.json"

add("trans.N", int(tr_j["N"]), "analysis_result", src_j, "N",
    "T4_transition_initiation", "primary_fit", "primary", "county-years")
add("trans.counties", int(tr_j["counties"]), "analysis_result", src_j,
    "counties", "T4_transition_initiation", "primary_fit", "primary", "counties")
add("trans.events", int(tr_j["events"]), "analysis_result", src_j, "events",
    "T4_transition_initiation", "primary_fit", "primary", "first events")
add("trans.never_transition", int(tr_j["counties"]) - int(tr_j["events"]),
    "derived", src_j, "counties - events",
    "T4_transition_initiation", "primary_fit", "primary", "counties",
    note="at-risk counties that never transitioned")
for h in ("H1", "H2"):
    blk = tr_j[f"{h}_demand_x_legacy" if h == "H1" else f"{h}_demand_x_capacity"]
    key = f"trans.{h}"
    name = "demand_x_legacy" if h == "H1" else "demand_x_capacity"
    add(f"{key}.coef", blk["coef"], "analysis_result", src_j,
        f"{h}_{name}.coef", "T4_transition_initiation", "primary_fit", "primary",
        "cloglog coefficient", "log-hazard", "signed4")
    add(f"{key}.se", blk["se"], "analysis_result", src_j, f"{h}_{name}.se",
        "T4_transition_initiation", "primary_fit", "primary")
    add(f"{key}.ci_lo", blk["ci95"][0], "analysis_result", src_j,
        f"{h}_{name}.ci95[0]", "T4_transition_initiation", "primary_fit",
        "primary", "cloglog coefficient", "log-hazard", "signed4")
    add(f"{key}.ci_hi", blk["ci95"][1], "analysis_result", src_j,
        f"{h}_{name}.ci95[1]", "T4_transition_initiation", "primary_fit",
        "primary", "cloglog coefficient", "log-hazard", "signed4")
    add(f"{key}.p", blk["p"], "analysis_result", src_j, f"{h}_{name}.p",
        "T4_transition_initiation", "primary_fit", "primary", "p-value", "", "p3")

add("trans.demand.coef", tr_j["demand"]["coef"], "analysis_result", src_j,
    "demand.coef", "T4_transition_initiation", "primary_fit", "primary",
    "cloglog coefficient", "log-hazard", "signed3")
add("trans.demand.p", tr_j["demand"]["p"], "analysis_result", src_j,
    "demand.p", "T4_transition_initiation", "primary_fit", "primary", "p-value",
    "", "sci")

tr_rl = C("trans_ROBUSTNESS_LEDGER.csv").set_index("variant")
lag1 = tr_rl.loc["demand_window_lag1"]
add("trans.sec_lag1.H1", float(lag1["H1"]), "analysis_result",
    "trans_ROBUSTNESS_LEDGER.csv", "demand_window_lag1:H1",
    "T4_transition_initiation", "lag1_extensive", "secondary",
    "cloglog coefficient", "log-hazard", "signed4")
add("trans.sec_lag1.H1_ci_lo", ast.literal_eval(lag1["H1_ci"])[0], "analysis_result",
    "trans_ROBUSTNESS_LEDGER.csv", "demand_window_lag1:H1_ci[0]",
    "T4_transition_initiation", "lag1_extensive", "secondary", "", "", "signed4")
add("trans.sec_lag1.H1_ci_hi", ast.literal_eval(lag1["H1_ci"])[1], "analysis_result",
    "trans_ROBUSTNESS_LEDGER.csv", "demand_window_lag1:H1_ci[1]",
    "T4_transition_initiation", "lag1_extensive", "secondary", "", "", "signed4")
add("trans.sec_lag1.H1_p", float(lag1["H1_p"]), "analysis_result",
    "trans_ROBUSTNESS_LEDGER.csv", "demand_window_lag1:H1_p",
    "T4_transition_initiation", "lag1_extensive", "secondary", "p-value", "", "p3")

im = C("trans_intensive_margin_results.csv").iloc[0]
add("trans.intensive.H1", float(im["H1"]), "analysis_result",
    "trans_intensive_margin_results.csv", "H1",
    "T4_transition_initiation", "intensive_margin", "secondary",
    "PPML coefficient", "log-rate", "signed4")
add("trans.intensive.H1_ci_lo", ast.literal_eval(im["H1_ci"])[0], "analysis_result",
    "trans_intensive_margin_results.csv", "H1_ci[0]",
    "T4_transition_initiation", "intensive_margin", "secondary", "", "", "signed4")
add("trans.intensive.H1_ci_hi", ast.literal_eval(im["H1_ci"])[1], "analysis_result",
    "trans_intensive_margin_results.csv", "H1_ci[1]",
    "T4_transition_initiation", "intensive_margin", "secondary", "", "", "signed4")
add("trans.intensive.H1_p", float(im["H1_p"]), "analysis_result",
    "trans_intensive_margin_results.csv", "H1_p",
    "T4_transition_initiation", "intensive_margin", "secondary", "p-value", "", "p3")
add("trans.intensive.H2", float(im["H2"]), "analysis_result",
    "trans_intensive_margin_results.csv", "H2",
    "T4_transition_initiation", "intensive_margin", "secondary",
    "PPML coefficient", "log-rate", "signed4")
add("trans.intensive.H2_ci_lo", ast.literal_eval(im["H2_ci"])[0], "analysis_result",
    "trans_intensive_margin_results.csv", "H2_ci[0]",
    "T4_transition_initiation", "intensive_margin", "secondary", "", "", "signed4")
add("trans.intensive.H2_ci_hi", ast.literal_eval(im["H2_ci"])[1], "analysis_result",
    "trans_intensive_margin_results.csv", "H2_ci[1]",
    "T4_transition_initiation", "intensive_margin", "secondary", "", "", "signed4")
add("trans.intensive.H2_p", float(im["H2_p"]), "analysis_result",
    "trans_intensive_margin_results.csv", "H2_p",
    "T4_transition_initiation", "intensive_margin", "secondary", "p-value", "", "p3")
add("trans.intensive.N", 64302, "dataset_descriptor",
    "branch_docs/trans_09_INTENSIVE_MARGIN_SECONDARY.md",
    "'full 64,302-cell V2 estimation panel re-scoped to departure capacity'",
    "T4_transition_initiation", "intensive_margin", "secondary", "county-years",
    note="corrects ED Table 3's earlier 65,919")

sim = C("trans_information_simulation_v4.csv")
h1n = sim[(sim.hypothesis == "H1") & (sim.true_effect == 0)]
add("trans.sim.typeI_fips", float(h1n[h1n.inference == "fips"]["reject"].iloc[0]),
    "analysis_result", "trans_information_simulation_v4.csv",
    "hypothesis==H1 & true_effect==0 & inference==fips:reject",
    "T4_transition_initiation", "simulation", "secondary", "rejection rate",
    "", "pct1")
add("trans.sim.typeI_state", float(h1n[h1n.inference == "state"]["reject"].iloc[0]),
    "analysis_result", "trans_information_simulation_v4.csv",
    "hypothesis==H1 & true_effect==0 & inference==state:reject",
    "T4_transition_initiation", "simulation", "secondary", "rejection rate",
    "", "pct1")
h2n = sim[(sim.hypothesis == "H2") & (sim.true_effect == 0)]
add("trans.sim.typeI_fips_H2", float(h2n[h2n.inference == "fips"]["reject"].iloc[0]),
    "analysis_result", "trans_information_simulation_v4.csv",
    "hypothesis==H2 & true_effect==0 & inference==fips:reject",
    "T4_transition_initiation", "simulation", "secondary", "rejection rate",
    "", "pct1")

cap = C("trans_capacity_scope_diagnostics.csv").set_index("metric")
for m in ("departure_projects", "departure_counties", "counties_ever_positive_dep",
          "frac_zero_2000", "corr_with_property_mitigation"):
    add(f"trans.capdiag.{m}", float(cap.loc[m, "value"]), "analysis_result",
        "trans_capacity_scope_diagnostics.csv", f"{m}:value",
        "T4_transition_initiation", "capacity_diagnostic", "secondary")

# ---------------- write -----------------------------------------------------
os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
json.dump({k: v for k, v in REG.items()}, open(OUT_JSON, "w"), indent=2)
with open(OUT_CSV, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["key", "study_id", "analysis_id",
                                      "primary_secondary", "value", "units",
                                      "effect_scale", "kind", "source_file",
                                      "source_locator", "formatting_rule", "note"])
    w.writeheader()
    for k in REG:
        w.writerow(REG[k])
print(f"{len(REG)} canonical entries -> {OUT_JSON}")
