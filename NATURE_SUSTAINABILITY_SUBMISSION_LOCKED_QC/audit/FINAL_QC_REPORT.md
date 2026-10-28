# FINAL_QC_REPORT — Nature Sustainability locked package

Date: 2026-10-28. Package: NATURE_SUSTAINABILITY_SUBMISSION_LOCKED_QC.
Every gate re-derived from final artifacts; no prior PASS inherited.

| # | gate | verdict | evidence |
|---|---|---|---|
| 1 | canonical registry | PASS | analysis/canonical_results.json: 101 entries, every number traced to frozen JSON/CSV/sample |
| 2 | hardcode removal | PASS | FINAL_HARDCODE_AUDIT: 0 category-A literals in builders; all via {{key}} / V(key) |
| 3 | numerical provenance | PASS | NUMERICAL_PROVENANCE_MAP.csv: 92/92 MATCH |
| 4 | figure/table numerical audit | PASS | FIGURE_TABLE_NUMERICAL_AUDIT.csv: all estimates from registry or source_data ledgers |
| 5 | national p-value correction | PASS | p=0.851 everywhere; no ~1.0/≈1.0/p=0.850 remnants (consistency audit) |
| 6 | consistency across artifacts | PASS | FINAL_NUMERICAL_CONSISTENCY_AUDIT: 13/13 key values match, 0 stale variants |
| 7 | citation integrity | PASS | FINAL_CITATION_AUDIT: 48 refs, first-appearance order PASS, uncited=0, orphan=0 |
| 8 | display-item citation | PASS | FINAL_DISPLAY_CITATION_AUDIT: all 5 figs + 8 ED figs + tables cited (ED Fig.1 defect repaired) |
| 9 | OMML mathematics | PASS | FINAL_OMML_AUDIT: 18 inline + 5 display OMML equations; no LaTeX/screenshots |
| 10 | markdown artifacts | PASS | FINAL_MARKDOWN_ARTIFACT_AUDIT: none in docx |
| 11 | linebreak/layout artifacts | PASS | FINAL_LINEBREAK_AUDIT: none |
| 12 | hostile review | PASS | FINAL_HOSTILE_REVIEW: no FATAL; 2 disclosed MAJOR limitations (stapled design, null power) |
| 13 | reference existence | PASS | REFERENCE_EXISTENCE_AUDIT.csv: 48/48 verified (Crossref + DOI resolution + publisher/data-repo) |
| 14 | public repository | PASS | PUBLIC_REPOSITORY_AUDIT: README + LICENSE added; no private paths/secrets |
| 15 | public reproduction | PASS | FINAL_PUBLIC_REPRODUCTION: clean clone, all 4 primary estimands bit-exact (6/6 checks) |
| 16 | code traceability | PASS | PUBLIC_CODE_TRACEABILITY.csv: every displayed estimate mapped to script + frozen source |
| 17 | figure visual QC | PASS | FINAL_FIGURE_VISUAL_AUDIT: 13 figures inspected |
| 18 | document visual QC | PASS | FINAL_VISUAL_QC: 16 PDF pages inspected; SI-table heading defect repaired |
| + | journal requirements | PASS | JOURNAL_REQUIREMENTS_AUDIT: format limits met; ED item cap fixed (Table 3 -> SI) |

Final decision: SUBMISSION READY — ALL FIXED QC GATES PASS
