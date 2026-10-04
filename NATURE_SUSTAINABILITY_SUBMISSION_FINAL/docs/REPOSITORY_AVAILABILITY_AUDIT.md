# REPOSITORY AVAILABILITY AUDIT — 2026-10-04

Verified from session environment via unauthenticated HTTP HEAD/GET.

| claim in manuscript | URL | status | verdict |
|---|---|---|---|
| integrated public repository (data + code availability) | https://github.com/bougtoir/legacy-lockin-manuscript | HTTP 200 | TRUE — mirror of `legacy_lockin_manuscript/` incl. this package |
| (context) national/subnational agricultural design-freeze artefacts | https://github.com/bougtoir/crop-rigidity-design-freeze | HTTP 200 | TRUE — exists, but NOT cited as availability source |
| (context) urban branch artefacts | https://github.com/bougtoir/urban-legacy-rigidity-feasibility | HTTP 404 | NOT PUBLIC — manuscript does not claim it |
| (context) transition branch artefacts | https://github.com/bougtoir/settlement-transition-feasibility | HTTP 404 | NOT PUBLIC — manuscript does not claim it |

Manuscript claims audit: all derived datasets and all analysis code are stated to live in (a) the reproducibility bundle accompanying the submission and (b) the single integrated repository bougtoir/legacy-lockin-manuscript. The bundle contains the frozen samples, locks, scripts and results copied verbatim from the three locked analysis branches, so claim (b) is sufficient and literally true. No companion-mirror claims remain. Third-party raw data are not redistributed (licence); acquisition ledgers carry retrieval metadata.
