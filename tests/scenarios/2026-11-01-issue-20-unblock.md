# Issue #20 unblocking and authenticated acceptance — 2026-11-01

Both selected native hosts now pass the approved basic installed-package smoke. The final gate exits 0 with all eight checks true for each variant. Product candidate remains `bc6d30e54621c8a1747a0f2baa0551f25080b06a`; adapter, package, guide and approved plan/spec bytes are unchanged. This later record stores verification corrections and evidence only.

See [screened receipt](2026-11-01-issue-20-unblock.json) for session/tool outcomes, exact paths, host/package/upstream identities, preservation snapshots and capture hashes. Raw streams and credentials remain ignored. V1 1.18.31 and V2 2.1.4 each loaded independent upstream using-superpowers and both Backplane skills in fresh `openai/gpt-6.1-sol` sessions. Native authentication was performed manually by the operator; no credential copying or desktop/browser control occurred.

## Corrections and negative results

The V2 visitor expected input.name, but native V2 uses input.id. A new regression observed assertion-level RED then GREEN covers both host formats and failed calls. The corrected visitor records actual native completions; no model narrative substitutes for tool evidence.

V1 could discover skills but failed while spawning ripgrep in its installed skill directory. Pinned host skill.ts sets ripgrep cwd to that directory; core ripgrep maps subprocess failures to the observed message. Direct read-only process probes reproduced WinError267 at lengths293,268 and259. Keeping the same native package and credentials, a255-character installed directory allowed rg exit0 with13 files and the fresh three-skill run passed. Earlier failed attempts remain FAIL.

Ruling: use V1 child XDG_CACHE_HOME at owned AREA/cache/v1, with unchanged authentication/data/config/home roots. Its marker and canonical containment are checked before launch and the receipt classifier binds that precise cache location. A second regression observed RED then GREEN covers cache selection and escape rejection. V1 now installs the already-published candidate through `git+https://github.com/tvproductions/superpowers-backplane#bc6d30e54621c8a1747a0f2baa0551f25080b06a`; omitting the optional .git suffix keeps native cwd below the observed Windows limit. Other installations or arbitrary longer paths are not certified. No shipped host or upstream files were patched. Wrong path-length assumptions would prevent the fresh native smoke from passing, rather than weaken its score.

Ruling: V1 hosted source was verified available at the exact product SHA before use. This is hosted installation evidence for V1 only. V2 retains the same verified immutable local Git-package installation. Publication and hosted acceptance are separate; no new source publication occurred. Re-run affected seams when cache/config/source inputs change.

## Verification and review

- Adapter suite:9/9 PASS; git diff --check PASS.
- Owned helpers:15/15 unittest PASS; Ruff lint/format and ty PASS on six helpers.
- Final evidence gate:both PASS; all16 checks true, including actual-file inventory, capture integrity, effective configuration, authoritative upstream, executable identity and current protected state.
- Fresh independent review:zero Critical/Important/Minor findings in the bounded helper delta against tracked originals. The adapter has no new product delta and retains its prior independent review. Reviewer independently rehashed48 V1 and27 V2 captures at its observation. V2 was then refreshed after the final intentional V1 config change; the executor final gate covers that latest result.
- Reviewer declined to judge executor full-gate execution, publication/integration/closure, other host versions and credential handling beyond inspected orchestration. Executor observed exit0 for the full gate; publication/integration/closure are not performed; other versions are not claimed; sign-in was terminal-only and completed manually. No review test rerun is claimed (its uv probe hit a cache-lock permission denial).

## Lifecycle and remaining boundaries

Native #20 was restored from blocked to its recorded active target after fresh complete intake confirmed unchanged approved semantics, no blockers, no children and the same parent/outgoing edges. Observed revision after transition:`2026-11-01T16:25:09Z`. The authentication/model blocker is resolved. This record does not close #20 or establish integrated acceptance. Submission, local integration or PR choice, publication and closure remain separate. Profiles, source branch/worktree and scratch are retained. No #4/#5 execution, release or cleanup occurred.
