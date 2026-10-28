# FINAL_HOSTILE_REVIEW — adversarial review of the final package

Verdict-first: no FATAL defects found in the final artifacts; one MAJOR
limitation (stapled-design coherence) is real but disclosed in-text; all
other criticisms are either already handled by design or require only
editorial care.

| # | criticism | severity | evidence | repairable? | required repair / status |
|---|---|---|---|---|---|
| A | Four studies stapled under one banner — heterogeneous scales, outcomes, estimators make "lock-in" not a single test | MAJOR | national crop JSD, admin-1 JSD, urban reallocation index, county hazard — different units & margins | partly | Disclosed: manuscript states estimands are deliberately not comparable, no pooled effect (Fig. 5 note). Boundary framing replaces common effect. ACCEPTED as design statement |
| B | "Mostly null" headline could be underpowered nulls sold as boundary | MAJOR | nat CI [-0.131,+0.143] on standardized scale excludes large rigidity; subnat CI [-0.251,+0.077] wider | yes (wording) | Manuscript says "insufficient evidence", not "no effect"; CIs shown everywhere; power limits acknowledged via interval widths. HANDLED |
| C | Inconsistent operationalization of "legacy" across branches | MODERATE | portfolio HHI vs irrigation share vs built volume vs stock age — construct drift | disclosed | Manuscript frames these as the three canonical legacy forms (specialization/fixed capital/institutional) chosen before outcome knowledge; each is defensible per domain |
| D | Urban significant result vs "no lock-in" conclusion — selective storytelling | MAJOR | urban beta3=-0.0083, p=0.002 is precise | no repair needed | Paper retains it as WEAK/CONTEXT: ~3.5% of SD, inland-concentrated, RP100 sign reversal, SLR subset fails. Conclusion says conditioning-at-margin not lock-in. CONSISTENT |
| E | Locking is not external preregistration — HARKing risk | MODERATE | design lock is internal | yes | Cover letter + Methods state explicitly it is outcome-blind internal locking, not preregistration; locks + shas public. HANDLED |
| F | FEMA buyout branch overgeneralizes US institutional context | MODERATE | only US counties; HMA data quirks | yes | Framed as the discrete-transition margin test, not a general institutional claim; scope diagnostics (trans_capacity_scope) reported |
| G | Absence-of-effect overstatement in abstract | MINOR | abstract says "no evidence systems with greater inherited structure showed systematically attenuated transformation" | check | Abstract says tests "did not support" the general prediction — not that lock-in never occurs. ACCEPTABLE |
| H | Secondary estimates could be cherry-picked to rescue the story | MODERATE | lag-1 & intensive margins larger, negative | no | Explicitly labelled SECONDARY, "strengthen the hypothesis not the finding", need independent confirmation. HANDLED |
| I | Collider/endogeneity: conditioning on adaptation activity | MODERATE | outcomes measure realized change; demand main effects huge | acknowledged | Interpretation limited to conditioning pattern; causal reading explicitly cautioned (falsification note in subnat) |
| J | Novelty: "null result" claim may be seen as incremental | MINOR | framing is stress-test of a rhetorical claim | — | Selling point is the frozen cross-domain design + transparent nulls; editorial judgment, not a defect |
| K | Data quality: FAOSTAT/GHSL/OpenFEMA measurement error | MODERATE | standard limitations | yes | Frozen samples + ledgers public; heterogeneity/robustness ledgers document sensitivity; SLR subset failure disclosed |
| L | Urban reallocation index is constructed, not observed | MODERATE | net hazard-avoidance reallocation is model-derived | yes | Disclosed as an index; negative controls (placebo, spatial permutation) PASS/partial-FAIL documented |
| M | Sample N claims inconsistent across artifacts (1,334 vs 542 SLR) | was FATAL | stale 1,334 in earlier draft | FIXED | Manuscript now reports 542 (authoritative ledger) via registry |
| N | Number transcription errors (p≈1.0 vs 0.851; 65,919 vs 64,302; ~4% vs 3.5%) | was FATAL | stale literals in prior build | FIXED | registry-driven rendering; provenance map 92/92 MATCH; consistency audit PASS |

Summary: the honest headline is a boundary claim ("accumulated legacy alone
is insufficient evidence of adaptation lock-in"), which the assembled
evidence supports. A hostile reader can still dispute construct
comparability (A) and null-power (B) — both are disclosed limitations, not
concealed defects. No FATAL issues remain.

Decision: PASS — wording revisions applied where real defects existed (M, N
repaired; urban/conclusion alignment verified); no unresolved FATAL items.
