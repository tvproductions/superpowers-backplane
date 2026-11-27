# Session handoff

- Format: `superpowers-backplane-handoff/v1`
- Creation time: VERIFIED — 2026-11-27T12:13:11Z. Evidence: UTC clock at creation.
- Repository identity: VERIFIED — standalone `superpowers-backplane`, origin `https://github.com/tvproductions/superpowers-backplane.git`. Evidence: canonical repository root, origin and worktree registration on the producing Mac.
- Branch: VERIFIED — `main`. Evidence: branch status after the guarded fast-forward.
- HEAD: VERIFIED — `6362be0da9ad9f0eba8889b94bf1047671156f88` before handoff storage. Evidence: local HEAD, fetched `origin/main`, and live remote main agreed.
- Incoming purpose: INFERRED — Reconcile and resume the approved OpenCode V2 setup verification. Evidence and reasoning: the operator chose V2-only support and authorized preparing #23 for execution.
- Work item: VERIFIED — https://github.com/tvproductions/superpowers-backplane/issues/23 is open with `backplane:ready`, observed `updatedAt=2026-11-27T08:48:29Z`. Evidence: fresh full native intake through `gh issue view`.
- Specification: VERIFIED — `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md`, blob `a790d953691d178f711757e9164afb60932eb65a`, and `docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md`, blob `e1e42d0b89bf950b988b05097dd011c6490aefe6`. Evidence: tracked Git objects at pre-handoff HEAD. The updated #12 and #23 record the V2-only scope decision.
- Plan: VERIFIED — `docs/superpowers-backplane/plans/2026-11-01-issue-23-opencode-v2-setup.md`, blob `8e1a6e35765410b0ea917eaee586aad8fa08af02`, consumes #23 revision `2026-09-20T01:30:21Z`. Evidence: tracked and GitHub-served blob match the November 1 approval receipt `docs/superpowers-backplane/plans/2026-11-01-opencode-wrap-approval.json`, blob `351746621c2dccf28ab9a7840dd587f5a64821dd`. The shared probe contract beside it has blob `1b856ff783c9cfd88d0e06184be894f16651898b`.
- Superpowers derivation provenance: VERIFIED — `using-superpowers`, `brainstorming`, `writing-plans`, and `executing-plans` were read through `.agents/skills/superpowers/<skill>/SKILL.md`, resolving to the independent upstream checkout at `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` (v7.0.1). Evidence: active Codex skill inventory, successful skill reads and path/revision probes, with current upstream Codex installation guidance read from the upstream README through GitHub CLI.
- Predecessors: VERIFIED — `docs/superpowers-backplane/handoffs/20261101T233052Z-opencode-preflight-and-release-accounting.md` (OpenCode thread, blob `75def8ba9c5acb810472121f1ca2122ca7987e13`) and `HANDOFF.md` (November 15 release checkpoint, blob `f3bbb15f5aa729fff5738bd5e3394a07e6fac54f`). Evidence: tracked blobs, contained canonical paths and inspected content.
- Storage location: VERIFIED — `docs/superpowers-backplane/handoffs/20261127T121311Z-opencode-v2-only-issue-23-ready.md`. Evidence: canonical repository and storage parent, with exclusive creation.

## Incoming purpose

INFERRED — Resume #23 from its first task and establish current V2 host and fixture prerequisites. Evidence and reasoning: V2 is the approved support scope and #23 now has the ready label and a linked approved plan.

## Authority anchors

VERIFIED — #12 records the V2-only decision and updated integrated acceptance. #23 preserves the V2 criteria and verification seams, links its immutable plan and approval, and limits the shared probe contract to its V2 portions and shared preservation checks. Evidence: current issue bodies and tracked artifacts above. Retain the November 1 approved artifact bytes and reconcile current tooling requirements before running the older command examples.

## Verified current state

VERIFIED — #20 is closed completed (`2026-11-01T17:01:53Z`) and is #23's only prerequisite. #24 remains open/backlog (`2026-09-20T01:30:23Z`) and depends on #23. #12 remains open/backlog (`2026-11-27T08:47:30Z`), with #24 open and #2 closed as its native blockers. Evidence: complete native intake of #12, #20, #23 and #24. The accepted #20 evidence is in `tests/scenarios/2026-11-01-issue-20-closeout.md`.

VERIFIED — #21 and #22 are closed as not planned, with no lifecycle labels. Observed revisions are `2026-11-27T08:48:01Z` (#21) and `2026-11-27T08:47:54Z` (#22). The #22 dependency was removed from #12. Evidence: fresh native issue states and #12 dependency query.

VERIFIED — Local `main` fast-forwarded from `b0d702f` to `6362be0` after fetch. The earlier local branch `recovery/issue-19-native` at `742392c` was an ancestor of fetched main and had zero unique commits. Evidence: clean pre-switch status, two revision comparisons, guarded fast-forward and clean `main` afterward.

## Live implementation thread

VERIFIED — This session performed backlog reconciliation. #23 remained ready and no implementation, test runs, or issue-23 workspace/scratch were established in this checkout. Evidence: final #23 lifecycle intake and workspace/status checks.

## Corrections to durable artifacts

VERIFIED — The November 1 OpenCode predecessor starts with V1 #21. The operator's later scope decision retires that step; #23 is the selected continuation. The prior #12 integrated plan retains both versions and needs reconciliation before its acceptance work. Evidence: updated #12, the two V1 closures and the approved plan references.

## Decisions and provenance

VERIFIED — The operator chose V2-only OpenCode support, authorized the backlog changes, and requested this handoff and Git sync. Evidence: direct user instructions and verified issue changes. Upstream recommends V2, restricts V1 changes to critical fixes, and documents the changed plugin API. [Upstream guidance](https://github.com/anomalyco/opencode/issues/54813) · [Migration guide](https://opencode.ai/docs/migrate-v1).

## Negative results

VERIFIED — The local independent Superpowers checkout is clean at v7.0.1, while synced `SUPERPOWERS.md` records stable v7.0.2 at `22f0b463e7a5e579904dd6211a520321035526f7`. Evidence: upstream checkout status and revision versus the tracked dependency record. Reconcile the receiving host and test tuple before drawing compatibility conclusions.

## Deferred obligations

VERIFIED — #24 still requires V2 lifecycle and conformance evidence, and #12 still requires V2 integrated acceptance. The current user-facing guide and remaining plan references may include earlier V1 commitments. Evidence: current issue states and the November 1 plan lineage. Backplane v0.3.0 is already published under the November 15 checkpoint.

## Risks and unknowns

UNVERIFIED — Receiving-host V2 binary, isolated profile, native authentication, and private-server ownership. Required probe: inspect and revalidate those exact inputs under Task 1 and the shared probe contract before reusing prior setup or claiming a PASS.

UNVERIFIED — This artifact's later storage commit at creation. Required probe: verify live remote `main`, containing commit and hosted file blob after the requested sync.

## Proposed next steps

1. INFERRED — Reconcile current `main`, #23/#20, the plan, the approval receipt, and local dependency identity. Evidence and reasoning: readiness and source identities were verified here, while the receiving host and tool state require current probes.
2. INFERRED — Start #23 Task 1 with a verified isolated workspace and fixture ownership, then qualify the V2 runner and discovery controls. Evidence and reasoning: the approved plan places these checks before the native setup and failure matrix.

## Suggested skills

VERIFIED — `superpowers-backplane:managing-superpowers-handoffs`, `superpowers-backplane:managing-superpowers-backlog`, `superpowers:executing-plans`, and `superpowers:verification-before-completion` are discoverable. Evidence: active session skill inventory and repository skill reads.

## Resume instruction

VERIFIED — Invoke `superpowers-backplane:managing-superpowers-handoffs` RESUME against `docs/superpowers-backplane/handoffs/20261127T121311Z-opencode-v2-only-issue-23-ready.md` before selecting the next action. Evidence: this append-only handoff and its recorded lineage.
