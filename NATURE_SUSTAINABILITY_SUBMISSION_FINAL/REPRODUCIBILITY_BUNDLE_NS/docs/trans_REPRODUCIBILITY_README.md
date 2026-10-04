# Reproducibility — SETTLEMENT_TRANSITION_PRIMARY_RESULTS

Environment: Python 3.10, pandas, numpy, statsmodels, pyfixest 0.60.
Run from `settlement_transition_feasibility/SETTLEMENT_TRANSITION_PRIMARY_RESULTS/`.

Order (each step verifies the previous artifact's sha256 before proceeding):

1. `python3 scripts/capacity_scope_v4.py`
   → `01_CAPACITY_ACTION_TYPE_AUDIT.csv`, `analysis/capacity_v4.csv`,
     `analysis/PRIMARY_TRANSITION_RISKSET_V4.csv` + `.sha256`,
     `analysis/capacity_scope_diagnostics.csv`.
   Inputs: `data/fema_hma/*` (gitignored raw OpenFEMA snapshots, see
   `DATA_SOURCE_LEDGER_v6.csv`), V3 risk set (unchanged cells: capacity columns
   replaced only).

2. `python3 scripts/information_simulation_v4.py` (chunked runner on
   memory-limited VMs; `--agg-only` to aggregate)
   → `analysis/information_simulation_v4_raw.csv` + `_v4.csv`.
   Outcome-blind: only marginal moments used; gate table in
   `03_INFORMATION_RECHECK.md`.

3. `python3 scripts/primary_transition_analysis.py`
   → verifies sample + lock sha256 and structure (aborts on mismatch), then
   performs THE single authorized opening:
   `analysis/PRIMARY_FIRST_OPENING_TRANSITION.json` + `.sha256` (immutable —
   the script will not overwrite it) and
   `analysis/primary_transition_effects.csv`.

4. `python3 scripts/robustness_transition.py`
   → `analysis/ROBUSTNESS_LEDGER.csv`, `analysis/intensive_margin_results.csv`,
     `analysis/leave_one_state_out.csv`. Runs only after the opening exists.

5. `python3 scripts/package_validator_results.py` → exits 0 on PASS.

Locks: `TRANSITION_PRIMARY_ANALYSIS_LOCK_V4.yaml` + `.sha256`. Locks V1–V3 in
`SETTLEMENT_TRANSITION_FINAL_LOCK/` and `SETTLEMENT_TRANSITION_LOCK_V3/` are
preserved unmodified.

Raw data note: `data/fema_hma/*.csv.gz` and census UF3 gzips are raw snapshots
(gitignored where required); derived committed inputs are enumerated in
`DATA_SOURCE_LEDGER_v6.csv` with SHA-256s.
