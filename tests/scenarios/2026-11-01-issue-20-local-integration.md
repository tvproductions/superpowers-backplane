# Issue #20 local integration — 2026-11-01

The operator selected local merge (option1). Main merge `2c969915aac2049211cad86ea78143d50776beb4` joins former main `4cb634b` and reviewed source/evidence `3d90ac4`. Only HANDOFF.md conflicted; both dated histories were preserved below a current entry. Adapter/package/guide/skills exactly match the reviewed branch. The approved #20 plan and unapproved #4/#5 drafts retain their original blobs.

Post-merge verification:9/9 adapter tests,15/15 helper tests, Ruff lint/format and ty on six helpers, and git diff --check pass. The initial sandboxed Node run failed before tests with spawn EPERM; the authorized outside-sandbox rerun passed. Both fresh authenticated native sessions load all three skills; final gate exits0 with all16 checks true, explicitly using merged main as WORKTREE. See [screened receipt](2026-11-01-issue-20-local-integration.json) for exact commands, sessions, identities and preservation snapshots.

Installed package candidate remains `bc6d30e`; this is current installed-candidate applicability against merged main, not a new merge-SHA installation or complete inventory claim for additional planning documents. V1 uses hosted immutable Git source and the verified shorter cache; V2 retains local immutable Git-package source. Historical results remain at their original identities.

The later evidence-storage commit is distinct from the merge/tested target. Main has not been pushed; no PR, issue lifecycle change/closure, release or cleanup occurred. #20 remains open/active at the last verified revision2026-11-01T16:33:53Z. Keep the source branch and native host-owned worktree/profiles; they remain needed for test provenance and later authorized acceptance.
