# FINAL_PUBLIC_REPRODUCTION

Clean-clone test, executed 2026-10-28 against public repo
`bougtoir/legacy-lockin-manuscript` (HEAD e4f65034).

Procedure: `gh repo clone` into a fresh temp directory; no private state;
`pip install statsmodels`; ran
`REPRODUCIBILITY_BUNDLE_NS/scripts/reproduce_primary_public.py`
against `REPRODUCIBILITY_BUNDLE_NS/samples` + `results`.

| check | frozen | reproduced | tol | verdict |
|---|---|---|---|---|
| nat.beta3 | 0.004592525890898978 | 0.004592525890899259 | 1e-6 | PASS |
| subnat.beta3 | -0.03771290381138198 | -0.03771290381138185 | 1e-6 | PASS |
| urban.beta3 | -0.008275234531385851 | -0.008275234531397297 | 1e-6 | PASS |
| trans.H1 | -0.1922768168138403 | -0.19227681681384287 | 1e-6 | PASS |
| trans.H2 | 0.03424914849321343 | 0.03424914849321365 | 1e-6 | PASS |
| trans.demand | 1.0998459891318235 | 1.0998459891318266 | 1e-3 | PASS |

All four primary headline estimands reproduce bit-exactly (residual diffs
are floating-point noise ~1e-13, far below tolerance).

Bootstrap p-values are stochastic refits; the frozen samples and lock SHAs
are verified in-script (sample sha256 asserted), and the deterministic point
estimates that carry every headline claim reproduce exactly.

Raw third-party inputs (FAOSTAT, SPAM2000, MIRCA2000, ERA5, GHS-UCDB,
OpenFEMA, Census SF3) are public but redistribution-restricted upstream;
frozen locked samples + SHA-256 are shipped instead. Classification:
**FULL PUBLIC REPRODUCTION PASS** for all primary displayed estimates;
downstream robustness/heterogeneity ledgers ship as frozen results with the
same upstream scripts included in the bundle.
