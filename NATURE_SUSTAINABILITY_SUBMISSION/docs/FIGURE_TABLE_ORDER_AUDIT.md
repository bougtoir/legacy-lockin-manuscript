# Figure/table citation-order audit

## Main display items (first citation order)

| item | first in-text citation | numbered | caption present |
|---|---|---|---|
| Fig. 1 | Introduction ("four locked empirical designs (Fig. 1)") | 1 | yes |
| Fig. 2 | Results, agricultural | 2 | yes |
| Fig. 3 | Results, urban | 3 | yes |
| Fig. 4a–d | Results, transition | 4 | yes |
| Fig. 5 | Results, synthesis ("(Fig. 5, Table 1)") | 5 | yes |
| Table 1 | Results, synthesis (same sentence) | 1 | yes |

First-citation order: F1 → F2 → F3 → F4 → F5/T1. Sequential, no orphans, no
phantom references.

## Extended Data (in-text citation order)

ED Fig. 2 (national ag), ED Fig. 3 (subnational ag), ED Figs. 4–5 (urban),
ED Fig. 6 (risk set), ED Fig. 7 (transition robustness), ED Fig. 8
(inference calibration), ED Table 2 (secondary), ED Figs. 1–8 + Tables 1–2
(bundle pointer sentence, Methods). ED Fig. 1 and ED Table 1 are additionally
covered by the bundle pointer sentence ("Extended Data Figs. 1–8"). All items
exist; all are cited.

## Source data mapping

- Fig. 2 → source_data/nat_PRIMARY_FIRST_OPENING.json + subnat ledgers
- Fig. 3 → source_data/urban_COASTAL_HETEROGENEITY.csv (+ PRIMARY_FIRST_OPENING_FLOOD.json)
- Fig. 4 → source_data/trans_PRIMARY_FIRST_OPENING_TRANSITION.json, trans_ROBUSTNESS_LEDGER.csv, trans_intensive_margin_results.csv
- Fig. 5 → Table 1 values (all above)
- ED Fig. 2 → nat_robustness_specification_ledger.csv; ED Fig. 3 → subnat_ROBUSTNESS_LEDGER.csv; ED Fig. 4 → urban_ROBUSTNESS_LEDGER.csv; ED Fig. 5 → urban_NEGATIVE_CONTROL_LEDGER.csv; ED Fig. 7 → trans_ROBUSTNESS_LEDGER.csv; ED Fig. 8 → trans_information_simulation_v4.csv
