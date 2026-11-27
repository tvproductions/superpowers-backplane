# Session handoff

- Format: `superpowers-backplane-handoff/v1`
- Creation time: VERIFIED — 2026-11-27T22:26:52Z. Evidence: UTC clock immediately before exclusive creation.
- Repository identity: VERIFIED — Standalone `tvproductions/superpowers-backplane` and a registered publication worktree sharing its Git directory. Evidence: canonical top-level paths, worktree registration, common Git directory, and origin.
- Branch: VERIFIED — Detached publication worktree based on live `origin/main`. Evidence: Git worktree and branch probes.
- HEAD: VERIFIED — `8e1e2005025890776eb99bd4b9161996fbbe68ed` before handoff storage. Evidence: worktree HEAD, fetched `origin/main`, live Git ref, and merged PR #38.
- Incoming purpose: VERIFIED — Preserve exact #23 delivery and verification for later closeout, with a side note to pass to gzlite and gzkit when their current work is ready for it. Evidence: the operator's handoff and sync request and explicit hold on companion policy work.
- Work item: VERIFIED — [#23](https://github.com/tvproductions/superpowers-backplane/issues/23), open in `backplane:review`, `updatedAt=2026-11-27T21:26:44Z`. Evidence: full native intake and completed PR #38.
- Specification: VERIFIED — `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md` blob `a790d953691d178f711757e9164afb60932eb65a` and `docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md` blob `e1e42d0b89bf950b988b05097dd011c6490aefe6`. Evidence: Git objects on the exact delivered tree and the current V2-only issue scope.
- Plan: VERIFIED — `docs/superpowers-backplane/plans/2026-11-01-issue-23-opencode-v2-setup.md` blob `8e1a6e35765410b0ea917eaee586aad8fa08af02`, consuming `2026-09-20T01:30:21Z`. Probe contract blob `1b856ff783c9cfd88d0e06184be894f16651898b` and approval receipt blob `351746621c2dccf28ab9a7840dd587f5a64821dd`. Evidence: Git objects and immutable links in the current issue.
- Superpowers derivation provenance: VERIFIED — The active Codex Superpowers 7.0.2 cache exposes `using-superpowers` (`069d578445805a28b8dacbf70cdf045e1673def0`), `brainstorming` (`9eb0edc7fedf26e1d3e2f3f223e5bcc5058aed6a`), `writing-plans` (`4cf0275d88d67aa4ef09f4bbca9970ed6ff74a00`), `executing-plans` (`ea23196d745043eefb0287387112825d2ca99f05`), and `verification-before-completion` (`7d45333cc4a49c57a80df6c1fe2fa777a207afbc`). Evidence: active skill inventory, file reads and measured blobs. [Upstream installation guidance](https://github.com/obra/superpowers/blob/v7.0.2/README.md#codex-app).
- Predecessors: VERIFIED — `docs/superpowers-backplane/handoffs/20261127T211111Z-issue-23-task-2-and-opencode-freshness.md`, blob `c613dd2cd327966a9d01c1327d09cdac57d61591`. Evidence: contained tracked path and delivery ancestry.
- Storage location: VERIFIED — `docs/superpowers-backplane/handoffs/20261127T222652Z-issue-23-integrated-delivery-and-companion-notes.md`. Evidence: canonical Backplane handoff directory, verified worktree registration and exclusive creation.

## Incoming purpose

VERIFIED — Carry the integrated #23 proof into the next session and preserve the deferred companion policy note. Evidence: operator direction to make a fresh handoff and sync, with both companion projects still under construction.

## Authority anchors

VERIFIED — #20 is completed and is #23's sole prerequisite. #23 is a leaf under #1 and blocks open #24. #12 remains the integrated OpenCode acceptance owner. Evidence: native #23 intake, approved plan and predecessor handoff. The submitted PR used a neutral issue reference, and #23 has no closing-PR relationship.

## Verified current state

VERIFIED — [PR #38](https://github.com/tvproductions/superpowers-backplane/pull/38) merged reviewed head `b0df3cfda494e1f51a27df3621168e39beffc3c9` as `8e1e2005025890776eb99bd4b9161996fbbe68ed`. The trees match. [CI attempt 2](https://github.com/tvproductions/superpowers-backplane/actions/runs/46073095079/attempts/2) passed on Windows, macOS and Ubuntu after the Backplane settings changes. Evidence: live PR/ref/CI queries and commit tree comparison.

VERIFIED — The corrected [Task 2 matrix](../../../tests/scenarios/2026-11-01-issue-23-opencode-acceptance.md) passed 17/17 with the three successful modes rerun on 2.1.4 and the other 14 rows preserved. The exact hosted merge separately passed Windows 2.1.4 native setup and three authenticated Skill calls with 105/105 installed file blobs matching. A separate Windows 2.4.2 inventory confirmed both pinned package revisions and the three skill blobs in an empty-auth profile. Evidence: corrected tracked matrix and [screened exact-delivery receipt](../../../tests/scenarios/2026-11-27-issue-23-integrated-delivery.json).

VERIFIED — Backplane's Actions token defaults to read, workflow PR creation and approval are disabled, secret scanning and push protection are enabled, and GitHub release immutability is enabled for future publications. Auto-merge and automatic branch deletion are off, and there are no effective rules on `main`. Evidence: GitHub API readback and post-change exact-main CI.

## Live implementation thread

VERIFIED — Local matrix evidence and exact hosted package verification are available for #23 closeout. The standalone checkout has an independent dirty dependency-maintenance batch, and the clean issue worktree retains the screened captures. Evidence: worktree status, tracked matrix, and exact-delivery receipt. This sync's paths are the handoff, its entry pointer and delivery receipt.

## Corrections to durable artifacts

VERIFIED — The predecessor's pending hosted check is superseded by observed exact delivery. Use the reviewed matrix and separate integrated receipt. The older #20-specific 70-file expectation remains tied to that historical package. Evidence: immutable #38 review commit, corrected matrix, and exact delivery manifest.

## Decisions and provenance

VERIFIED — The operator approved the exact #38 merge and scoped Backplane settings batch. The operator then paused codifying or applying companion workflow and settings policy while both projects are under construction. Evidence: direct instructions in this session.

## Negative results

VERIFIED — The first exact PR-package scoring reused the historical 70-file count and failed despite all observed blobs matching. The exact-commit manifest control then qualified all 105 files, and a fresh run qualified merged main. Evidence: retained candidate and integrated receipts with separate source identities. Do not reuse the historical file count for another revision.

## Deferred obligations

VERIFIED — #23 remains open in review. Publishing/linking a satisfaction evaluation and closing the issue require their applicable closeout authority. #24 lifecycle verification and #12 integrated OpenCode acceptance remain separate. Evidence: native issue state and approved plan.

- **Side note for gzlite.** VERIFIED — The operator put the proposed workflow and GitHub settings policy on hold during the rename/rework. Pass along the proposal when asked. Use trunk-based development with [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow) for substantive changes, short-lived PRs, maintainer-controlled merge, and explicit direct-push exceptions for routine documentation and handoffs. Put repository settings in an explicit bootstrap step. Apply token and secret defaults, observe the intended PR CI checks before requiring them, then consider opt-in auto-merge. The adopter verification command retains its existing scope. Evidence: session decision and gz-starter bootstrap ADR-0003 edition 1. The remote still used `tvproductions/gz-starter` at the policy check.
- **Side note for gzkit.** VERIFIED — The operator put policy adoption on hold during the rework and flagged the local checkout as stale. Reconcile the current direct-main/no-feature-branches directive through gzkit's owning canon before adopting the shared workflow. Check actual required CI jobs and preserve the advisory role of `full-strength-report`. The published release workflow attaches binaries after publication, so qualify draft-first assembly and the docs deployment trigger before enabling immutability there. Evidence: gzkit's verified remote main `67958969520f8f6a13b38a7d7eb101745156b7d5` and the operator's hold. An isolated scratch clone read that revision. The companion checkouts and settings received no edits in this session.

## Risks and unknowns

UNVERIFIED — Authenticated 2.4.2 Skill calls. Required probe: run them in a separately authorized isolated profile if that tuple becomes a delivery requirement.

UNVERIFIED — Hosting arrival and CI of this handoff storage commit at creation. Required probe: compare live `main`, all new tracked blobs, and exact storage CI. The storage identity is distinct from the verified delivery.

## Proposed next steps

1. INFERRED — Reconcile this handoff's transported identity, current #23 native fields and the exact merged receipt before undertaking closeout. Evidence and reasoning: delivery passed, while issue closeout remains a separate operation.
2. INFERRED — Pass the companion side notes only when the operator resumes that thread. Evidence and reasoning: both projects are mid-rework and the current request preserves the discussion for later.

## Suggested skills

VERIFIED — `superpowers-backplane:managing-superpowers-handoffs`, `superpowers-backplane:managing-superpowers-backlog`, and `superpowers:verification-before-completion` are discoverable. Evidence: active session skill inventory and successful reads.

## Resume instruction

Invoke `superpowers-backplane:managing-superpowers-handoffs` RESUME against `docs/superpowers-backplane/handoffs/20261127T222652Z-issue-23-integrated-delivery-and-companion-notes.md`.
