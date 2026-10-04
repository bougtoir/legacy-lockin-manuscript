# 09 — Intensive margin (secondary, pre-declared secondary estimand)

PPML with county + year FE and offset log housing units on annual
departure-programme property counts (LOCK_V2 design, county CRV1), on the
full 64,302-cell V2 estimation panel re-scoped to departure capacity.
**This is NOT transition probability** — it conditions on the count volume of
programme entries including repeat activity, a different estimand from the
primary first-entry hazard.

`analysis/intensive_margin_results.csv`:

| term | coef | 95% CI | p |
|---|---|---|---|
| demand × legacy | **−0.548** | [−0.910, −0.187] | 0.003 |
| demand × capacity | −0.223 | [−0.448, +0.002] | 0.052 |
| capacity (main) | −0.409 | [−0.668, −0.151] | 0.002 |
| demand (main) | +0.261 | [−0.180, +0.703] | 0.246 |

## Interpretation (secondary, does not reclassify the primary)

- Conditional on the programme-flow estimand, flood demand triggers *smaller*
  entry volumes in high-legacy counties — the same barrier direction as the
  primary point estimate, here with precision. Consistent corroboration of a
  real but modest legacy barrier; the primary estimand remains the frozen
  first-entry hazard and stays RESULT B.
- Capacity's near-zero/negative interaction here says prior programme
  experience does not amplify the demand-driven flow volume either — again
  consistent with the primary H2 null.
- The negative capacity main effect reflects that high-capacity counties
  entered earlier (capacity is cumulative experience; most of their first
  entries predate or anchor the panel) — a level compositional effect, not
  enablement.
