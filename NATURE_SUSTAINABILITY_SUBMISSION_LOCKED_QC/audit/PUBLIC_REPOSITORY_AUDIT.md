# PUBLIC_REPOSITORY_AUDIT

Repo: https://github.com/bougtoir/legacy-lockin-manuscript (exists, public,
synced from wip subdir `legacy_lockin_manuscript`).

| item | status |
|---|---|
| repo exists / URLs work | PASS — cloned cleanly; browseable |
| code public | PASS — full upstream per-branch scripts + reproduce_primary_public.py in bundle |
| analysis scripts present | PASS — 20 branch scripts + lock-verification sha guards |
| README | FIXED — root README.md added (structure, reproduction command, data availability, license) |
| license | FIXED — MIT LICENSE added for code; CC BY 4.0 stated for text/figures |
| locks/checksums | PASS — .sha256 sidecars for every locked sample; lock yaml shas asserted in scripts |
| private paths | PASS — scanned: no /home/, /Users/, internal URLs |
| secrets | PASS — no tokens/keys found |
| machine-specific paths | PASS — scripts use repo-relative paths |
| journal name in repo address | PASS — repo name contains no journal name |

Decision: PASS (after README/LICENSE repair committed this cycle).
