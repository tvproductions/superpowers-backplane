# Codex Issue #3 whole-branch review

Reviewed range: 307bcf43a2b8e48ea3b657424274b02b62643152..080ec72382e15a69aaae64fb922be0bd190842e4.
Review package: .superpowers/sdd/2026-09-19-codex-installation-surface-plans/review-307bcf4..080ec72.diff.
Reviewer: independent fresh-context read-only review using the approved plan, spec, Review Focus, and ledger rulings.

## Findings and disposition

- Critical: none.
- Important: tests/scenarios/transcripts/2026-09-19-codex-host-lifecycle.md previously compared preservation hashes only before and after the whole candidate, rollback, and uninstall sequence. A candidate could have changed unrelated state that rollback later restored. Fixed with a bounded disposable replay. Before the new section, an evidence-completeness check returned RED. After the replay, the transcript's embedded JSON parsed and the check returned GREEN: candidate, rollback, and uninstall each retained both unrelated plugin IDs and all five baseline SHA-256 values. The replay restored the disposable profile to its initial scoped IDs and hashes. No second reviewer was dispatched.
- Minor: tests/scenarios/transcripts/2026-09-19-codex-failure-probes.md line 239 contains U+000B control characters in two version labels. Deferred under the execution workflow; it affects transcript rendering, not package behavior.

## Reviewer limits and executor rulings

- Integrated remote install/update/rollback discovery and verified issue closure were reserved by the approved plan for after authorized integration. They remain open and issue #3 stays active. If this ruling is wrong, closure would be premature; final integration checks must run before completion.
- The reviewer did not independently repeat lifecycle mutations because the review was read-only. The executor relies on the separately captured disposable issue #13 mutation evidence. If this ruling is wrong, the lifecycle evidence could miss a mutation defect; issue #3 remains open through integrated verification.
- Marketplace signature verification was not an approved setup gate. The official Codex catalog source and plugin version, required skill hashes, and gh preflight were observed. If this ruling is wrong, the test does not independently establish the marketplace's supply-chain integrity.

The reviewer found no package or guide defect. Before the bounded replay the verdict was with fixes; the Important evidence gap is now covered by the recorded RED-to-GREEN check. This record does not claim the post-integration gates have passed.
