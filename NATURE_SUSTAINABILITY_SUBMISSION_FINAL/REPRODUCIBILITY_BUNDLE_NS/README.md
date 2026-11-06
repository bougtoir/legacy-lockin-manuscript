# REPRODUCIBILITY_BUNDLE_NS

Verification bundle for "When does inherited structure become adaptation lock-in?"

- `locks/` — immutable analysis locks (YAML + SHA-256) for all four branches.
  Historical locks preserved; nothing overwritten.
- `samples/` — frozen estimation inputs the scripts consume (locked primary
  samples and the V4 transition risk set), each with its SHA-256 sidecar;
  checksums verified byte-identical to the locked originals.
- `results/` — frozen analysis outputs (first-opening JSONs, effects tables,
  robustness ledgers, heterogeneity, negative controls, simulations).
- `scripts/` — the single-opening analysis scripts, robustness suites,
  simulations and manuscript figure/docx builders.
- `environment/` — Python version and pip freeze.
- `docs/` — classification and viability documents from each branch package.

Full per-branch packages (with complete documentation sets 00–13) are in the
source monorepo under `crop_rigidity_design_freeze/`,
`urban_legacy_rigidity_feasibility/` and
`settlement_transition_feasibility/` and their public mirrors.
