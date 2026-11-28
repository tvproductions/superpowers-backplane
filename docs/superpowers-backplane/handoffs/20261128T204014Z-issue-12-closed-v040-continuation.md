# Session handoff

- Format: `superpowers-backplane-handoff/v1`
- Creation time: VERIFIED — 2026-11-28T20:40:14Z. Evidence: UTC clock at exclusive creation.
- Repository identity: VERIFIED — Standalone `tvproductions/superpowers-backplane` and its registered `.sp-bp/work/issue-12/publication` worktree share the project Git directory and canonical GitHub origin. Evidence: Git roots, origin, and worktree readback.
- Branch: VERIFIED — Detached publication worktree. Standalone `main` and GitHub `main` pointed to the same commit at creation. Evidence: native branch and ref reads. The standalone working tree has separate development changes.
- HEAD: VERIFIED — `13cc12315c1cea01a6bdcb3eef9a0cb94f7ba1c0` before storing this handoff. Evidence: live GitHub ref, fetch, and standalone fast-forward.
- Incoming purpose: VERIFIED — Preserve completed OpenCode V2 acceptance and the remaining checks for the selected 0.4.0 bundle. Evidence: the operator requested this handoff and Git sync after #12 closure.
- Work item: VERIFIED — [#12](https://github.com/tvproductions/superpowers-backplane/issues/12) is closed completed, observed revision `2026-11-28T20:28:44Z`. Evidence: current full native issue intake.
- Specification: VERIFIED — [Adoption and installation design](../../superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md) blob `a790d953691d178f711757e9164afb60932eb65a` and [host leaf rescope](../../superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md) blob `e1e42d0b89bf950b988b05097dd011c6490aefe6` govern the completed V2 work as narrowed by #12. Evidence: tracked Git objects and native artifact links.
- Plan: VERIFIED — [V2 integrated acceptance](../plans/2026-11-28-issue-12-opencode-v2-integrated-acceptance.md) blob `9108806d19027b636c71c74399a78a46800a61d7`, approved at the bytes recorded in the acceptance assessment. The [0.4.0 scope](../releases/2026-11-28-v0.4.0.md) is blob `6093bfaa3aab81996eda3b966ac0582972bcdd50`. Evidence: tracked objects and approved-scope records.
- Superpowers derivation provenance: VERIFIED — The active Codex v7.0.2 catalog exposed installed `skills/<name>/SKILL.md` for `using-superpowers` (`069d578445805a28b8dacbf70cdf045e1673def0`), `brainstorming` (`9eb0edc7fedf26e1d3e2f3f223e5bcc5058aed6a`), `writing-plans` (`4cf0275d88d67aa4ef09f4bbca9970ed6ff74a00`), `executing-plans` (`ea23196d745043eefb0287387112825d2ca99f05`), and `verification-before-completion` (`7d45333cc4a49c57a80df6c1fe2fa777a207afbc`). Evidence: active discovery, installed skill reads and blob readback, and [upstream Codex guidance](https://github.com/obra/superpowers/blob/v7.0.2/README.md#codex-app).
- Predecessors: VERIFIED — [OpenCode V2 integrated acceptance](20261128T015158Z-issue-12-opencode-v2-integrated-acceptance.md), blob `6f2d17ea18f5ff6164c4ad54ef3d0474ceaef440`. Evidence: canonical contained predecessor path, tracked blob, and the #12 execution and closeout receipts.
- Storage location: VERIFIED — `docs/superpowers-backplane/handoffs/20261128T204014Z-issue-12-closed-v040-continuation.md`. Evidence: canonical Backplane handoff directory and exclusive creation.

## Incoming purpose

VERIFIED — Preserve the #12 delivery and the approval boundary for the selected, unpublished 0.4.0 bundle. Evidence: direct operator handoff and sync request, [release scope](../releases/2026-11-28-v0.4.0.md), and [native closeout](../../../tests/scenarios/2026-11-28-issue-12-closeout.json).

## Authority anchors

VERIFIED — The accepted #12 assessment is recorded at `650cb09606f94c1f3a29dcea6389055bbabd7462`, based on exact merged delivery `3b03a49db79b6a276314d1477dfb3c68e1a4bac9`. Native closure and receipt storage came after acceptance. Evidence: [assessment](../../../tests/scenarios/2026-11-28-issue-12-opencode-v2-acceptance.md), [PR #42](https://github.com/tvproductions/superpowers-backplane/pull/42), and [closeout receipt](../../../tests/scenarios/2026-11-28-issue-12-closeout.json).

VERIFIED — The selected release scope and [release-policy binding](../../release-policy.md) govern the remaining candidate work. GitHub's latest published release is [v0.3.0](https://github.com/tvproductions/superpowers-backplane/releases/tag/v0.3.0). Evidence: tracked release record and current release readback.

## Verified current state

VERIFIED — #12 closed completed at `2026-11-28T20:28:41Z) and has no lifecycle label. All 41 rows passed, including the actual V2 2.0.3 refusal. The exact merged package passed a fresh Windows V2 2.1.4 install with all 110 files and three attributed native Skill calls. Evidence: current issue readback, [installed-package receipt](../../../tests/scenarios/2026-11-28-issue-12-opencode-v2-integrated-delivery.json), and [exact delivery CI](https://github.com/tvproductions/superpowers-backplane/actions/runs/46186109415).

VERIFIED — Closeout storage `13cc12315c1cea01a6bdcb3eef9a0cb94f7ba1c0) has passing Windows, macOS, and Ubuntu CI. Evidence: [exact closeout CI](https://github.com/tvproductions/superpowers-backplane/actions/runs/46186837739), published receipt blob `35d26deb67277f88c086d145414dc37a5913c8d2`, and live GitHub ref.

VERIFIED — The standalone fast-forward to the closeout commit preserved eleven pre-existing local paths. The three local README edits merged cleanly with the delivered V2 wording, and the other ten paths retained their original SHA-256 digests. Evidence: the clean three-way preview, local diff comparison and post-fast-forward file checks. This handoff is authored in the clean registered publication worktree.

## Live implementation thread

INFERRED — The next scoped step is to qualify the selected 0.4.0 candidate after operator direction. Evidence and reasoning: #12's issue gate is complete and the release record still calls for candidate-specific version metadata, CI, and native installed-package verification. The package includes `docs/`, so the new handoff changes the expected manifest for any later source that includes it.

## Corrections to durable artifacts

VERIFIED — The predecessor's pending plan reconciliation and acceptance are now complete. The V2-only approved plan and immutable delivery supersede that pending observation. Evidence: plan blob, reviewed candidate `73be83a6ecf7ee097c187e87f0758edc86165299`, and closeout receipt. The original dual-host plan retains its historical edition.

## Decisions and provenance

VERIFIED — The operator approved the V2-only plan, then approved publication, CI-gated integration, evidence publication and completed closure. The current request authorizes handoff creation and Git sync. Evidence: direct operator responses and the published [closeout](../../../tests/scenarios/2026-11-28-issue-12-closeout.json). Version and release publication require their applicable operator direction.

VERIFIED — Use of the registered publication worktree isolates handoff content from the independent local development edits. Evidence: exact changed paths in the standalone checkout, the clean worktree at creation, and the selected release boundary.

## Negative results

VERIFIED — The older #23 archive used a fixed 70-file count, and the #24 replay helper originally asserted issue #24. These assumptions failed when the exact #12 package and issue were used. The corrected procedures derived the Git manifest, checked the named issue, and passed the repeated probes. Evidence: the [review and reconciliation](../../../tests/scenarios/2026-11-28-issue-12-opencode-v2-acceptance.md#independent-review). Use the recorded #12 verification driver and recompute the candidate manifest before a later native run.

VERIFIED — The earlier V2 2.4.2 observation covers inventory and file identity. Evidence: [#23 satisfaction](../../../tests/scenarios/2026-11-27-issue-23-satisfaction.md). Qualification at that version would require three completed attributed native Skill calls.

## Deferred obligations

VERIFIED — Parent #1 remains open with 14 of 17 children complete. Pilot #6 remains open with #4 unresolved. #4 still owns adopter-operations follow-up and can consume the accepted #12 evidence when selected. Evidence: fresh full intake of #1, #4 and #6 and the closeout receipt.

## Risks and unknowns

UNVERIFIED — Release-candidate identity and exact 0.4.0 verification. Required probe: obtain the operator's selected release action, review the current canonical GZ Starter policy, reconcile the release inputs, and qualify the exact candidate's source, CI and installed package before publication.

UNVERIFIED — Availability of the incoming host's isolated native verification profile and authentication. Required probe: verify its owned profile and host binary, independent upstream package, full `gh` capabilities, and fresh model availability before running the candidate verification. Historical native runs retain their original inputs.

## Proposed next steps

1. INFERRED — Reconcile live #12, GitHub `main`, current release and scoped worktree before selecting any next action. Evidence and reasoning: native closure, exact delivery and separate receipt commits are individually anchored, and the current standalone checkout contains independent local edits.
2. INFERRED — If directed to prepare 0.4.0, review current GZ Starter policy and bind the verified #12 scope to the exact versioned candidate. Evidence and reasoning: the release record requires version consistency, complete local and hosted checks, and a fresh exact package/Skill comparison after candidate changes.
3. INFERRED — Apply the release publication and readback gates under the applicable operator direction. Evidence and reasoning: the selected bundle owns its verification and immutable source identities. #4 and #6 retain their own obligations.

## Suggested skills

VERIFIED — `superpowers-backplane:managing-superpowers-handoffs`, `superpowers-backplane:managing-superpowers-backlog`, and `superpowers:verification-before-completion` are available. Evidence: active installed skill catalog and successful reads.

## Resume instruction

Invoke `superpowers-backplane:managing-superpowers-handoffs` RESUME against `docs/superpowers-backplane/handoffs/20261128T204014Z-issue-12-closed-v040-continuation.md`.
