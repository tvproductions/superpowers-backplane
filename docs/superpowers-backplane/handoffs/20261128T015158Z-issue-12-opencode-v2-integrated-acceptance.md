# Session handoff

- Format: `superpowers-backplane-handoff/v1`
- Creation time: VERIFIED — 2026-11-28T01:51:58Z. Evidence: UTC clock at exclusive creation.
- Repository identity: VERIFIED — Standalone `tvproductions/superpowers-backplane` and its registered `.sp-bp/work/issue-12/publication` worktree share one Git directory and the canonical GitHub origin. Evidence: verified root, worktree registration, common Git directory, and origin.
- Branch: VERIFIED — Detached #12 publication worktree based on fetched `origin/main`. Evidence: worktree and ref readback.
- HEAD: VERIFIED — `eba4874ab869f19f563234415698aec66f7c8001` before storing this handoff. Evidence: live main, fetch, and registered worktree HEAD.
- Incoming purpose: VERIFIED — Re-enter #12 at V2-only plan reconciliation and prepare final integrated OpenCode V2 acceptance. Evidence: the operator requested a fresh #12 handoff and Git sync after #24 closed.
- Work item: VERIFIED — [#12](https://github.com/tvproductions/superpowers-backplane/issues/12) is open in `backplane:backlog` at `2026-11-27T08:47:30Z`. Evidence: complete native issue intake.
- Specification: VERIFIED — [Adoption and installation design](../../superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md) blob `a790d953691d178f711757e9164afb60932eb65a` and [host leaf rescope](../../superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md) blob `e1e42d0b89bf950b988b05097dd011c6490aefe6`. The current issue narrows the OpenCode acceptance scope to V2. Evidence: tracked Git objects and live issue artifact section.
- Plan: VERIFIED — [November 1 dual-host plan](../plans/2026-11-01-issue-12-opencode-final-acceptance.md) blob `60a8904e0d2286c03d898a10aedfe575440c3468` consumes `2026-09-20T01:31:34Z`. [Shared probe contract](../plans/2026-11-01-opencode-remaining-acceptance-probe-contract.md) blob `1b856ff783c9cfd88d0e06184be894f16651898b` and [approval receipt](../plans/2026-11-01-opencode-wrap-approval.json) blob `351746621c2dccf28ab9a7840dd587f5a64821dd` preserve the earlier approval. Evidence: tracked objects, receipt, and live issue links.
- Superpowers derivation provenance: VERIFIED — The active Codex Superpowers 7.0.2 catalog and installed cache expose `using-superpowers` (`069d578445805a28b8dacbf70cdf045e1673def0`), `brainstorming` (`9eb0edc7fedf26e1d3e2f3f223e5bcc5058aed6a`), `writing-plans` (`4cf0275d88d67aa4ef09f4bbca9970ed6ff74a00`), `executing-plans` (`ea23196d745043eefb0287387112825d2ca99f05`) and `verification-before-completion` (`7d45333cc4a49c57a80df6c1fe2fa777a207afbc`). Evidence: active discovery, installed skill reads, blob readback, and [upstream Codex guidance](https://github.com/obra/superpowers/blob/v7.0.2/README.md#codex-app).
- Predecessors: VERIFIED — [OpenCode V2 release accounting](20261128T005952Z-opencode-v2-release-accounting.md), blob `5bf2eaebd3411c75d7652cb2479178e7082e4d39`. Evidence: canonical contained path, tracked blob, and #24 closeout continuity.
- Storage location: VERIFIED — `docs/superpowers-backplane/handoffs/20261128T015158Z-issue-12-opencode-v2-integrated-acceptance.md`. Evidence: canonical Backplane handoff directory and exclusive creation.

## Incoming purpose

VERIFIED — Hand off final integrated acceptance of the OpenCode V2 support surface that gates the selected 0.4.0 bundle. Evidence: the operator's release discussion and #12 handoff request.

## Authority anchors

VERIFIED — #12 has parent #1, blocks external pilot #6, and has two native blockers, #2 and #24, both closed completed. Its acceptance criteria also consume completed #20 and #23. Evidence: complete #12, #2, #20, #23, #24, and #6 issue reads.

VERIFIED — [The selected 0.4.0 scope](../releases/2026-11-28-v0.4.0.md) applies the [release-policy binding](../../release-policy.md) to the verified v0.3.0 baseline, whose tag peels to `39fbe3065c16ac119c4c10a3c2428fda39d57e61`. Evidence: operator direction, reconciled scope saved from `2e5dace24ddc4a578982ba9d5e4a94d986235938`, shared source policy at `98acc5aeec3f3b6ad61171a647dbc0ab7a44b7c6`, and current GitHub release readback.

## Verified current state

VERIFIED — The owning evidence is reachable from main: [#20 shared adapter](../../../tests/scenarios/2026-11-01-issue-20-satisfaction.md), [#23 V2 setup](../../../tests/scenarios/2026-11-27-issue-23-satisfaction.md), and [#24 lifecycle and conformance](../../../tests/scenarios/2026-11-28-issue-24-satisfaction.md). Evidence: tracked reports and native issue bodies with completed closure.

VERIFIED — [PR #41](https://github.com/tvproductions/superpowers-backplane/pull/41) merged reviewed head `8b78f22f8d92772b3a0b798f413e1993d8f23214` as `d6f0f6a378b4b91e2fab2c2987f8f18dd357f23d`. Windows OpenCode V2 2.1.4 with independent Superpowers v7.0.1 matched all 107 package files and loaded all three Skills. #24 closed completed at `2026-11-28T01:45:55Z`. Evidence: [delivery CI](https://github.com/tvproductions/superpowers-backplane/actions/runs/46094332153), [screened installed-package receipt](../../../tests/scenarios/2026-11-28-issue-24-integrated-delivery.json), and native readback. The separate evidence commit `eba4874ab869f19f563234415698aec66f7c8001` passed [storage CI](https://github.com/tvproductions/superpowers-backplane/actions/runs/46094628524) on Ubuntu, macOS, and Windows.

## Live implementation thread

INFERRED — Start with plan reconciliation and then compare the current installed-package inputs row by row. Evidence and reasoning: #12's live V2-only contract supersedes the dual-host plan for this work, and the setup and lifecycle receipts preserve exact host, upstream, `gh`, source, and protected-state observations. Retain matching V2 rows and rerun affected seams. The guide changed for lifecycle maintenance, compatibility preflight, and capability checks between the setup and lifecycle deliveries.

## Corrections to durable artifacts

VERIFIED — #24 completion and the selected 0.4.0 scope supersede the predecessor's pending integration and release-disposition observations. The November 1 #12 plan preserves its reviewed bytes as historical authority for the old scope. Evidence: current #12 and #24 native reads, exact merged receipt, and operator-approved release accounting.

## Decisions and provenance

VERIFIED — The operator selected the recommended V2 0.4.0 bundle and separately authorized #24 branch integration, evidence publication, and closeout. The current instruction authorizes this handoff and Git sync. Evidence: direct conversation and the selected release record. Current #12 execution and release publication derive their authority from their own requests and required evidence.

## Negative results

VERIFIED — #23's evidence contains Windows V2 2.4.2 inventory and file identities, with authenticated Skill calls still unverified for that version. Evidence: [#23 setup satisfaction](../../../tests/scenarios/2026-11-27-issue-23-satisfaction.md). Reuse this observation only within its inventory scope.

VERIFIED — The #24 independent review uncovered archived-receipt validation gaps and incomplete guide checks. The corrected head adds eight negative assertions and a fresh native capability replay. Evidence: [review and replay record](../../../tests/scenarios/2026-11-01-issue-24-opencode-acceptance.md#corrected-candidate-review-and-capability-replay). Use the corrected guide and verifier for changed-input analysis.

## Deferred obligations

VERIFIED — #4 adopter operations, #6 external pilot, and #1's adoption arc retain their own gates. 0.4.0 is selected and unpublished. V1 remains outside #12's current acceptance scope. Evidence: release scope and native graph. The standalone checkout contained independent dependency edits before the handoff, and the publication worktree isolates the scoped changes.

## Risks and unknowns

UNVERIFIED — Current approved V2-only execution plan and final integrated satisfaction. Required probe: reconcile issue revision `2026-11-27T08:47:30Z` or its current successor with the original design and approved probe contract, obtain approval of the reconciled plan, and capture a passing fixed V2 matrix and exact hosted package verification.

UNVERIFIED — The incoming harness's native OpenCode host, scoped authentication, and package delivery identity. Required probe: establish owned isolated configuration, executable and upstream identities, verified authentication, complete `gh` intake/capabilities, and exact Git manifests before retaining or replaying evidence.

## Proposed next steps

1. INFERRED — Invoke RESUME on this exact path, refresh full #12 intake and accepted prerequisites, and prepare the V2-only revision of the plan for review. Evidence and reasoning: both blockers are closed and the live issue's V2 scope differs from the approved plan edition. Preserve the old plan and approval receipt.
2. INFERRED — After current plan approval, compare all required setup, failure, lifecycle, conformance, and native lifecycle rows against the intended integrated source. Evidence and reasoning: prior owning receipts can carry matching inputs, while changed ones need the corresponding native checks. Keep the actual 2.0.3 below-floor refusal and require a PASS for every supported row, all three fresh Skill results, and protected-state evidence.
3. INFERRED — Obtain fresh review and prove the exact hosted delivery before publishing satisfaction and closing #12 under applicable authority. Evidence and reasoning: approved acceptance requires recorded integration and fresh native verification. Then prepare the selected 0.4.0 candidate against its own release gate.

## Suggested skills

VERIFIED — `superpowers-backplane:managing-superpowers-handoffs`, `superpowers-backplane:managing-superpowers-backlog`, `superpowers:writing-plans`, and `superpowers:verification-before-completion` are discoverable. Evidence: active skill catalog and file reads.

## Resume instruction

Invoke `superpowers-backplane:managing-superpowers-handoffs` RESUME against `docs/superpowers-backplane/handoffs/20261128T015158Z-issue-12-opencode-v2-integrated-acceptance.md`.
