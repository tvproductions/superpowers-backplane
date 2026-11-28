# Session handoff

- Format: `superpowers-backplane-handoff/v1`
- Creation time: VERIFIED — 2026-11-28T00:59:52Z. Evidence: UTC clock at exclusive creation.
- Repository identity: VERIFIED — Standalone `tvproductions/superpowers-backplane` and its registered publication and #24 worktrees share the standalone Git directory and the canonical GitHub origin. Evidence: canonical roots, Git common directory, worktree list, and remote readback.
- Branch: VERIFIED — Detached publication worktree based on live `origin/main`. The separate registered #24 source worktree is on `work/issue-24-opencode-v2-lifecycle`. Evidence: observed worktree registration and branch state.
- HEAD: VERIFIED — Publication base `6f0c295d6e34d86dd516140092d91e628f52e8ec` before writing this handoff. The exact synced candidate is `29ac21a553596efac73c11236fa64f5fc153f5d7`. Evidence: worktree HEADs, fetched refs, and GitHub ref and blob readback.
- Incoming purpose: VERIFIED — Reconcile the OpenCode work with Backplane's release policy before choosing the next integration or closeout step. Evidence: the operator's release-policy questions followed by the handoff and Git sync request.
- Work item: VERIFIED — [#24](https://github.com/tvproductions/superpowers-backplane/issues/24) is open in `backplane:active` at `2026-11-27T23:54:01Z`. Evidence: full native intake.
- Specification: VERIFIED — `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md` blob `a790d953691d178f711757e9164afb60932eb65a` and `docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md` blob `e1e42d0b89bf950b988b05097dd011c6490aefe6`. Evidence: Git objects.
- Plan: VERIFIED — `docs/superpowers-backplane/plans/2026-11-01-issue-24-opencode-v2-lifecycle.md` blob `882b389bf49ced3e7de517a4146cfd822e9c29e5` consumes `2026-09-20T01:30:23Z`. Shared probe contract blob `1b856ff783c9cfd88d0e06184be894f16651898b` and approval receipt blob `351746621c2dccf28ab9a7840dd587f5a64821dd`. Evidence: tracked objects and immutable links in the current issue.
- Superpowers derivation provenance: VERIFIED — The active Codex Superpowers 7.0.2 catalog and installed cache expose `using-superpowers` (`069d578445805a28b8dacbf70cdf045e1673def0`), `brainstorming` (`9eb0edc7fedf26e1d3e2f3f223e5bcc5058aed6a`), `writing-plans` (`4cf0275d88d67aa4ef09f4bbca9970ed6ff74a00`), `executing-plans` (`ea23196d745043eefb0287387112825d2ca99f05`), `verification-before-completion` (`7d45333cc4a49c57a80df6c1fe2fa777a207afbc`) and `finishing-a-development-branch` (`fa8aecaf8813f1b19d19996f7957d1b0121f2d9c`). Evidence: active skill inventory, successful reads and file blob identities. [Official Codex installation guidance](https://github.com/obra/superpowers/blob/v7.0.2/README.md#codex-app).
- Predecessors: VERIFIED — `docs/superpowers-backplane/handoffs/20261127T222652Z-issue-23-integrated-delivery-and-companion-notes.md`, blob `59cca4813f6bdd61b56181dba948520e45500f6f`. Evidence: contained tracked predecessor and the observed continuation from #23 closeout through #24.
- Storage location: VERIFIED — `docs/superpowers-backplane/handoffs/20261128T005952Z-opencode-v2-release-accounting.md`. Evidence: contained Backplane handoff directory and exclusive creation.

## Incoming purpose

VERIFIED — Resume with a concrete OpenCode release disposition and then reconcile the verified #24 branch with that decision. Evidence: the operator asked what governs major, minor and patch releases, then asked for this handoff and Git sync.

## Authority anchors

VERIFIED — [Backplane's release-policy binding](../../release-policy.md) adopts the shared [GZ Starter versioning policy](https://github.com/tvproductions/gz-starter/blob/98acc5aeec3f3b6ad61171a647dbc0ab7a44b7c6/docs/versioning.md#required-version-decision-procedure), read at canonical main `98acc5aeec3f3b6ad61171a647dbc0ab7a44b7c6`. The policy requires release accounting during planning and closeout. The last published Backplane release is [v0.3.0](https://github.com/tvproductions/superpowers-backplane/releases/tag/v0.3.0), whose tag peels to `39fbe3065c16ac119c4c10a3c2428fda39d57e61`. Evidence: tracked policy, canonical source, GitHub release and live Git tag.

VERIFIED — [#23](https://github.com/tvproductions/superpowers-backplane/issues/23) is CLOSED/COMPLETED at `2026-11-27T23:49:13Z`. #24 is its downstream lifecycle leaf, and [#12](https://github.com/tvproductions/superpowers-backplane/issues/12) remains the integrated V2 acceptance owner at `2026-11-27T08:47:30Z`. The earlier #12 plan blob `60a8904e0d2286c03d898a10aedfe575440c3468` covers both host variants and needs reconciliation with the current V2-only issue. Evidence: full native intake and tracked approval and plan identities.

## Verified current state

VERIFIED — #23's [published satisfaction record](https://github.com/tvproductions/superpowers-backplane/blob/71a75066d2626a7f91025428cf1077a46f6a7be3/tests/scenarios/2026-11-27-issue-23-satisfaction.md) supports completed V2 setup and failure acceptance. Evidence: immutable served record and final native issue readback.

VERIFIED — [Fixture #39](https://github.com/tvproductions/superpowers-backplane/issues/39) is CLOSED/COMPLETED at `2026-11-28T00:30:46Z) with `documentation` preserved. Its two-document [PR #40](https://github.com/tvproductions/superpowers-backplane/pull/40) merged as `6f0c295d6e34d86dd516140092d91e628f52e8ec). Both link destinations and served blobs resolved and [exact-main CI](https://github.com/tvproductions/superpowers-backplane/actions/runs/46088154550) passed on Windows, macOS and Ubuntu. Evidence: GitHub PR, contents, rendered headings, workflow and native closure readback.

VERIFIED — The #24 branch reached GitHub at `29ac21a553596efac73c11236fa64f5fc153f5d7`, tree `b73bd923ffa7e7bdef7027628cde1c682c4ce3f0`. All 16 changed blobs match GitHub and [exact branch CI](https://github.com/tvproductions/superpowers-backplane/actions/runs/46090605813) passed. The [candidate assessment and receipts](https://github.com/tvproductions/superpowers-backplane/blob/29ac21a553596efac73c11236fa64f5fc153f5d7/tests/scenarios/2026-11-01-issue-24-opencode-acceptance.md) preserve eight native lifecycle cases, the before-apply refusal, five conformance checks, eleven real fixture stages, review corrections and the full local gate. Evidence: branch ref, Git tree, GitHub contents and workflow. The #24 branch remains separate from main.

VERIFIED — Backplane has auto-merge off, a default read-only Actions token, Actions PR creation and approval disabled, and no effective rules on `main`. The current workflow runs checks on pushes and PRs. Evidence: live repository and Actions settings readback and tracked workflow.

## Live implementation thread

- **Tactical.** VERIFIED — The exact #24 candidate is synced and technically qualified for the observed local and branch scopes. The next work is release disposition, followed by guarded integration and an exact merged-package check under current authority. Evidence: candidate gate and previous pause before the PR.
- **Operational.** VERIFIED — #23 setup evidence and #24 lifecycle evidence feed #12 integrated V2 acceptance. The broader pilot [#6](https://github.com/tvproductions/superpowers-backplane/issues/6) retains independent dependencies. Evidence: native issue dependencies and the V2-only issue terms.
- **Strategic.** INFERRED — A release that newly establishes supported OpenCode V2 adoption fits a minor from v0.3.0, conditionally `0.4.0`. Evidence and reasoning: the shared 0.x classification, current baseline, and the new support outcome. This is a classification contingent on scope selection.

## Corrections to durable artifacts

VERIFIED — The predecessor's #23 review status is superseded by actual completion. The #23 and #24 work needs release disposition in the existing release authority. The earlier #12 plan needs V2-only scope reconciliation while its approved bytes remain historical evidence. Evidence: full issue reads, the published #23 evaluation, the release policy, and the current #12 artifact section.

## Decisions and provenance

VERIFIED — The operator approved the exact #39 fixture and previously approved the #24 PR, merge and hosted-verification sequence at the exact candidate. The assistant paused before a #24 push when the operator challenged what the work was delivering and how releases advance. The current request covers the handoff and branch sync. Evidence: direct session instructions and current branch and PR observations. Reconcile current scope and intent before resuming any release or integration decision.

## Negative results

VERIFIED — The first independent #24 review found that the verifier could accept five wrong-shaped observations and that the preflight and exact guide discovery replay were missing. The follow-up at `29ac21a` records the failing-to-passing controls, full Git manifests, the real unavailable-pin lookup with an unchanged prior configuration, and the corrected native replay. Evidence: accepted candidate report and screened receipts. Use the corrected receipt for revalidation.

VERIFIED — The release audit found the historic adoption issue [#1](https://github.com/tvproductions/superpowers-backplane/issues/1) still titled v0.1.0 and found no selected OpenCode V2 release target in the checked release records or open milestones. The published v0.3.0 release scope excludes historical OpenCode, pilot and adoption completion. Evidence: current issue and milestone queries and the [v0.3.0 release scope](../releases/2026-11-15-v0.3.0.md).

## Deferred obligations

VERIFIED — Full #24 integration, its exact hosted Windows V2 package verification and completed closeout remain open. #12 and pilot obligations retain their own gates. Independent dirty dependency maintenance in the standalone checkout remains outside the scoped sync. The gzlite and gzkit policy notes remain deferred in the predecessor. Evidence: live issue graph, the candidate's explicit acceptance limits, standalone Git status, and predecessor.

## Risks and unknowns

UNVERIFIED — Intended next release outcome and approved target. Required probe: reconcile the v0.3.0 baseline, current adopter-facing change set, #23/#24 disposition, #12 and #1, then record included, deferred and required gates under current operator direction.

UNVERIFIED — Exact Windows V2 installed package and fresh three-Skill results for a future merged #24 SHA. Required probe: verify current PR authority and exact merged Git tree and CI, run a fresh owned 2.1.4 install, compare the complete manifest with Git and confirm all three native Skill results before satisfaction closeout.

UNVERIFIED — Handoff transport and exact storage CI at artifact creation. Required probe: compare live main and both new blobs, then observe the workflow for the exact storage commit.

## Proposed next steps

1. INFERRED — Start with the release disposition before integrating #24. Evidence and reasoning: the source policy requires planning and closeout accounting. Reconcile scope against the verified v0.3.0 baseline and record #23/#24 disposition, the intended OpenCode outcome, and applicable gates in the existing release authority.
2. INFERRED — Re-read #24 and the exact synced head after that decision. Evidence and reasoning: unchanged native inputs and verified branch CI support a guarded PR. Confirm current integration authority, exact reviewed source, hosted CI, and fresh native merged-package proof before publishing its satisfaction evaluation and closing the issue.
3. INFERRED — Reconcile #12's V2-only requirements and identify affected verification rows after #24 closes. Evidence and reasoning: #12 still depends on #24, and its older dual-variant plan needs a V2-only reading with changed-input rechecks. Treat any release and broader adoption gates according to the selected bundle.

## Suggested skills

VERIFIED — `superpowers-backplane:managing-superpowers-handoffs`, `superpowers-backplane:managing-superpowers-backlog`, and `superpowers:verification-before-completion` were used for current continuity and verification. Evidence: active skill catalog and file reads.

## Resume instruction

Invoke `superpowers-backplane:managing-superpowers-handoffs` RESUME against `docs/superpowers-backplane/handoffs/20261128T005952Z-opencode-v2-release-accounting.md`.
