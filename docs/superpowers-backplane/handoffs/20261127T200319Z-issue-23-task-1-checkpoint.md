# Session handoff

- Format: `superpowers-backplane-handoff/v1`
- Creation time: VERIFIED — 2026-11-27T20:03:19Z. Evidence: UTC clock at exclusive file creation.
- Repository identity: VERIFIED — `tvproductions/superpowers-backplane`, origin `https://github.com/tvproductions/superpowers-backplane.git`, Windows native worktree `c191` registered to the standalone repository's shared Git directory. Evidence: verified worktree and common Git directory identities, clean status, fetch and origin checks.
- Branch: VERIFIED — `work/issue-23-opencode-v2-setup`. Evidence: active worktree branch and exact base `a9bc1ec28d56176b704e3f791eb9ea0d1b76b2cf` on fetched `origin/main`.
- HEAD: VERIFIED — `8c799095a00b3d0c9348bc2eba9591eb14e611b2` before handoff storage. Evidence: Task 1 commit with enabled hooks and a clean worktree.
- Incoming purpose: INFERRED — Resume #23 at Task 2, beginning with native fixture and authentication revalidation. Evidence and reasoning: Task 1 is committed and Task 2 owns the remaining setup acceptance.
- Work item: VERIFIED — https://github.com/tvproductions/superpowers-backplane/issues/23 is open with `backplane:active`, observed `updatedAt=2026-11-27T19:40:02Z`. Evidence: fresh full native intake and prior guarded start transition.
- Specification: VERIFIED — `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md` at blob `a790d953691d178f711757e9164afb60932eb65a` and `docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md` at `e1e42d0b89bf950b988b05097dd011c6490aefe6`. Evidence: tracked Git objects and the V2-only scope on #23 and #12.
- Plan: VERIFIED — `docs/superpowers-backplane/plans/2026-11-01-issue-23-opencode-v2-setup.md`, blob `8e1a6e35765410b0ea917eaee586aad8fa08af02`, consumes `2026-09-20T01:30:21Z`. The shared probe contract and the approval receipt are blobs `1b856ff783c9cfd88d0e06184be894f16651898b` and `351746621c2dccf28ab9a7840dd587f5a64821dd`. Evidence: current issue links, reconciled V2 semantics and exact tracked identities.
- Superpowers derivation provenance: VERIFIED — `using-superpowers`, `brainstorming`, `writing-plans`, and `executing-plans` resolve at `.agents/skills/superpowers/<skill>/SKILL.md` to the standalone checkout's independent Superpowers v7.0.1, `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`. The execution also used `using-git-worktrees`, `test-driven-development`, and `verification-before-completion` from that source. Evidence: active skill reads, independent checkout identity, fresh Codex inventory and file-read probes. Current upstream Codex installation guidance was reviewed at v7.0.2.
- Predecessors: VERIFIED — `docs/superpowers-backplane/handoffs/20261127T121311Z-opencode-v2-only-issue-23-ready.md`, blob `0741e83cb462ff5e5680479e3940550c1f23df2a`, continues `docs/superpowers-backplane/handoffs/20261101T233052Z-opencode-preflight-and-release-accounting.md`. Evidence: contained tracked files and the ready handoff's predecessor reference.
- Storage location: VERIFIED — `docs/superpowers-backplane/handoffs/20261127T200319Z-issue-23-task-1-checkpoint.md`. Evidence: canonical project handoff directory in the registered worktree and exclusive creation.

## Incoming purpose

INFERRED — Continue V2 setup and failure verification under the approved plan. Evidence and reasoning: #23 is active, Task 1 is committed, and the remaining work starts with Task 2 fixture revalidation.

## Authority anchors

VERIFIED — #20 is closed as completed at accepted delivery `386bdb5a8570360f5d34359c68f68947eb7a90fc` and is #23's sole prerequisite. #23 still blocks #24. ADR-0001 edition 1 and the existing shared adapter apply. Evidence: full #20 and #23 intake, the approved plan, and the preserved ADR approval.

## Verified current state

VERIFIED — Task 1 passed 14 fixture tests, 5 repository tests, 9 Node adapter tests, Ruff lint and format, ty, lock, whitespace, Lizard, guide examples and installed commit hooks. Evidence: committed [Task 1 record](../../../tests/scenarios/2026-11-27-issue-23-task-1.md), blob `2bfbb6839acbe8616f7f0017e9d1281c5ac64e12`, and retained fixture sources at Task 1 HEAD.

## Live implementation thread

VERIFIED — The owned private OpenCode V2 2.1.4 server resolved all three skills from the two pinned package caches, and their Git blobs matched. It used the published #20 Backplane package and plan-baseline Superpowers v7.0.1. Evidence: Task 1 record. Authenticated native tool calls and case receipts belong to Task 2.

## Corrections to durable artifacts

VERIFIED — Apply the repository's current locked commands to the approved plan's older `--no-project` examples. The guide and fixture archive carry the V2-only changes. Evidence: `AGENTS.md`, `docs/engineering/python.md`, current issue semantics and Task 1 commit. Approved specifications, plan, probe contract and receipt retain their original bytes.

## Decisions and provenance

VERIFIED — The operator authorized Task 1 and requested this handoff and Git sync. The Task 1 start transition is recorded on #23. The scoped sync contains the Task 1 branch, with the prior dependency refresh in the standalone working tree. Evidence: direct requests, current issue state and branch/file reconciliation.

## Negative results

VERIFIED — The first private probe timed out after installation because `/api/config` returned a direct array. The focused regression failed against the old parser and passed after the wire-format correction. Parent checkout skill discovery also cannot satisfy the package-origin check. Evidence: Task 1 record and archived controls.

## Deferred obligations

VERIFIED — Task 2 owns the authenticated native setup and failure cases, an actual below-2.0.4 binary, screened model-driven Skill results and complete acceptance evidence. #24 lifecycle and #12 integrated acceptance remain downstream. Evidence: task boundaries and native dependency graph.

## Risks and unknowns

UNVERIFIED — The receiving host's exact V2 executable, retained profile ownership, model availability, isolated private server and actual below-floor binary. Required probe: revalidate each using the approved plan and shared contract, using native credential reuse where authorized. On another machine, reconstruct fixtures from the committed sources.

UNVERIFIED — This artifact's containing commit and hosted CI at creation. Required probe: verify the new branch head, handoff and evidence blobs, and the exact-head CI run after the requested sync.

## Proposed next steps

1. INFERRED — Open the synced Task 1 branch and reconcile #23, #20, the approved artifacts and fixture identity. Evidence and reasoning: the active issue and Task 1 commit supply a concrete continuation point, and task-specific scratch is host-local.
2. INFERRED — Start Task 2 by validating native auth/model access and the isolated V2 tuple, then run the approved native matrix. Evidence and reasoning: the private inventory and the tested wire parser supply Task 1 controls for the matrix.

## Suggested skills

VERIFIED — `superpowers-backplane:managing-superpowers-handoffs`, `superpowers-backplane:managing-superpowers-backlog`, `superpowers:executing-plans`, and `superpowers:verification-before-completion` are available in the current session. Evidence: active discovery and reads.

## Resume instruction

Invoke `superpowers-backplane:managing-superpowers-handoffs` RESUME against `docs/superpowers-backplane/handoffs/20261127T200319Z-issue-23-task-1-checkpoint.md` before selecting the next action.
