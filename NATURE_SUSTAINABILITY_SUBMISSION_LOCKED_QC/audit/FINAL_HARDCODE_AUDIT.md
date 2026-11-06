# FINAL_HARDCODE_AUDIT

Every numeric literal in manuscript template, figure builder, table builder and
docx builder was classified:

- **A. Analysis results** — must come from `analysis/canonical_results.json`.
  Status: **zero category-A literals remain** in builders. All manuscript numbers
  render from `{{key|fmt}}` placeholders resolved by `scripts/render_manuscript.py`;
  all figure estimates and Table 1 / ED Table 3 cells are `V(key)` lookups in
  `scripts/make_figures.py` and `scripts/build_docx.py`. Verified by
  `audit/NUMERICAL_PROVENANCE_MAP.csv` (92/92 MATCH) and by literal scans of the
  builders (remaining hits enumerated below, none category-A).
- **B. Design constants** (permitted): years/epochs (1975–2025), bootstrap
  B = 999, unit counts embedded in figure labels via registry lookups.
- **C. Formatting constants** (permitted): figure geometry, font sizes,
  axis limits, offsets, string-slice indices.
- **D. Prespecified thresholds** (permitted): type-I warning band 0.10, alpha.
- **E. Unrelated literals**: reference page/article numbers in the bibliography.

Residual literal scan (all non-category-A):
- `make_figures.py`: box coordinates (0.05–0.88), text offsets (0.28, 0.0012,
  0.006, 0.003), axis limits — category C.
- `build_docx.py`: slice indices (2:-2, 1:-1) — category C.
- `main_text_template.md`: "state clustering exceeded 0.10" — prespecified
  warning threshold (category D); bibliography page numbers — category E.

Decision: PASS — no number is manually transcribed; the registry is the sole
source of analysis values in every artifact.
