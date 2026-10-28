# legacy-lockin-manuscript

Submission package and reproducibility materials for the manuscript
*"When does inherited structure become adaptation lock-in?"*
(four frozen empirical tests of adaptation lock-in: national crop
specialization, subnational irrigation dependence, urban built capital under
flood exposure, and institutional transition initiation via US FEMA
property-acquisition programmes).

## Contents

- `NATURE_SUSTAINABILITY_SUBMISSION_LOCKED_QC/` — QC-locked submission package
  (manuscript docx, cover letter, figures, extended data, source data,
  canonical results registry, audit files).
- `NATURE_SUSTAINABILITY_SUBMISSION_FINAL/` — previous submission package,
  retained for history.
- `REPRODUCIBILITY_BUNDLE_NS_LOCKED.zip` — frozen analysis bundle
  (locked estimation samples with SHA-256, locks, results, scripts).

## Reproduce the primary estimates

Requirements: Python 3, `pandas`, `numpy`, `statsmodels`.

```bash
python3 REPRODUCIBILITY_BUNDLE_NS/scripts/reproduce_primary_public.py \
    NATURE_SUSTAINABILITY_SUBMISSION_FINAL/REPRODUCIBILITY_BUNDLE_NS
```

The script refits each primary model on the frozen locked samples
(`samples/`) and compares the interaction coefficients to the immutable
first-opening records (`results/*_PRIMARY_FIRST_OPENING*.json`) with
tolerance 1e-6. All four primary tests reproduce bit-exactly
(see `audit/FINAL_PUBLIC_REPRODUCTION.md` in the locked package).

## Data availability

All third-party raw inputs (FAOSTAT, SPAM2000, MIRCA2000, ERA5, GHSL-UCDB,
OpenFEMA, Census SF3) are public datasets. Redistribution-restricted sources
are documented with acquisition metadata; the frozen, analysis-ready locked
samples used for every headline estimate are included under `samples/`
with SHA-256 manifests.

## License

Code: MIT (see `LICENSE`). Manuscript text and figures: CC BY 4.0.
