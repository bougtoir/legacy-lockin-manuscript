# FINAL_VISUAL_QC

MAIN_MANUSCRIPT_NS_inline_LOCKED.docx rendered to PDF (LibreOffice) — 16
pages, every page inspected at render resolution; clean docx checked
textually.

| pages | content | result |
|---|---|---|
| 1 | title, affiliation, abstract, intro start | PASS |
| 2 | intro cont., citations superscript | PASS |
| 3 | Fig.1 embedded + caption, Results start | PASS |
| 4-7 | Results sections, Figs 2-5 embedded with captions | PASS |
| 8-9 | Discussion, limitations | PASS |
| 10-12 | Methods, 5 OMML display equations rendering natively | PASS |
| 13-15 | Competing interests, References 1-48, Figure legends | PASS |
| 16 | Extended Data list, Supplementary Information heading + SI Table 1 (registry values) | PASS |

Defects found and repaired this pass: literal "## Supplementary Information"
heading (fixed — heading now emitted properly); supplementary table placed
under its own heading. No markdown remnants, no layout double-spaces (OMML
extraction artifact explained in LINEBREAK audit), no stale numbers.

MAIN_MANUSCRIPT_NS_clean_LOCKED.docx: same content without embedded figures
(for EM upload) — PASS.
COVER_LETTER_NS_LOCKED.docx: ~2,700-word claim, 48 refs, 7-word title — PASS.

Decision: PASS
