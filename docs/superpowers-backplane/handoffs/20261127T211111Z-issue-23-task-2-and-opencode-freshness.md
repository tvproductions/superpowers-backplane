# Session handoff

- Format: `superpowers-backplane-handoff/v1`
- Creation time: VERIFIED — 2026-11-27T21:11:11Z. Evidence: UTC clock at exclusive file creation.
- Repository identity: VERIFIED — `tvproductions/superpowers-backplane`, origin `https://github.com/tvproductions/superpowers-backplane.git`, Windows worktree `c191` registered to the standalone repository’s shared Git directory. Evidence: canonical worktree, registration, origin and common Git directory probes.
- Branch: VERIFIED — `work/issue-23-opencode-v2-setup`. Evidence: current branch and fetched upstream ref.
- HEAD: VERIFIED — `a1060b4b68550b784ae70bf96f9e768a2c9d4df3` before handoff storage. Evidence: clean local worktree, commit identity and fetched divergence of one local commit and zero remote-only commits.
- Incoming purpose: INFERRED — Reconcile the synced Task 2 branch, then resume at hosted verification and the current OpenCode V2 compatibility check when the delivery target is selected. Evidence and reasoning: the local setup matrix passed and the operator requested this handoff, Git sync and a version-freshness note.
- Work item: VERIFIED — https://github.com/tvproductions/superpowers-backplane/issues/23 is OPEN with `backplane:active`, `updatedAt=2026-11-27T19:40:02Z`. Evidence: fresh complete native `gh issue view` intake after verifying origin.
- Specification: VERIFIED — `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md`, blob `a790d953691d178f711757e9164afb60932eb65a`, and `docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md`, blob `e1e42d0b89bf950b988b05097dd011c6490aefe6`. Evidence: tracked Git objects. Current #23 restricts the approved design to its V2 scope.
- Plan: VERIFIED — `docs/superpowers-backplane/plans/2026-11-01-issue-23-opencode-v2-setup.md`, blob `8e1a6e35765410b0ea917eaee586aad8fa08af02`, consumes #23 revision `2026-09-20T01:30:21Z`. Shared probe contract blob `1b856ff783c9cfd88d0e06184be894f16651898b` and approval receipt blob `351746621c2dccf28ab9a7840dd587f5a64821dd`. Evidence: current immutable issue links and exact Git blobs.
- Superpowers derivation provenance: VERIFIED — `using-superpowers`, `brainstorming`, `writing-plans`, `executing-plans`, and `verification-before-completion` were read through the repository discovery surface `.agents/skills/superpowers/<skill>/SKILL.md` at upstream v7.0.1 `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`. The active Codex inventory also exposed the native v7.0.2 cache. Its corresponding skill blobs in the same order are `069d578445805a28b8dacbf70cdf045e1673def0`, `9eb0edc7fedf26e1d3e2f3f223e5bcc5058aed6a`, `4cf0275d88d67aa4ef09f4bbca9970ed6ff74a00`, `ea23196d745043eefb0287387112825d2ca99f05`, and `7d45333cc4a49c57a80df6c1fe2fa777a207afbc`. Evidence: current inventory, successful reads, path and blob probes, and [upstream Codex installation guidance](https://github.com/obra/superpowers/blob/v7.0.2/README.md#codex-app).
- Predecessors: VERIFIED — `docs/superpowers-backplane/handoffs/20261127T200319Z-issue-23-task-1-checkpoint.md`, blob `e632c682d444ad139620d18c9b53e13845bfa49a`. Evidence: canonical contained tracked path and inspection of its issue, branch and predecessor lineage.
- Storage location: VERIFIED — `docs/superpowers-backplane/handoffs/20261127T211111Z-issue-23-task-2-and-opencode-freshness.md`. Evidence: exclusive creation in the established Backplane handoff directory inside the verified worktree.

## Incoming purpose

INFERRED — Verify arrival and exact-head CI for the Task 2 branch, then continue toward hosted acceptance of the selected delivery and assess the currently distributed V2 host. Evidence and reasoning: Task 2 local qualification is complete and the operator asked to preserve the OpenCode version gap in this handoff.

## Authority anchors

VERIFIED — #23 remains the V2 setup and compatibility-failure leaf. Its sole blocker #20 is closed and #23 blocks #24. ADR-0001 edition 1, the existing adapter and the approved artifact bytes govern execution. Evidence: fresh native intake, the named Git blobs and the retained architectural approval.

## Verified current state

VERIFIED — Local Task 2 commit `a1060b4b68550b784ae70bf96f9e768a2c9d4df3` contains the [local acceptance record](../../../tests/scenarios/2026-11-01-issue-23-opencode-acceptance.md) and [screened receipt](../../../tests/scenarios/2026-11-01-issue-23-opencode-acceptance.json), blobs `bbc6e46f5e7caa7af52e8dc240ab393bdbf51e93` and `8f099830994c6745c688c4b90b1c2c3f93c21bf7`. The fresh receipt verifier observed 17/17 distinct native rows. Normal hooks, 19 helper tests, nine adapter tests, Ruff, ty, lock, complexity and whitespace checks passed for the local Task 2 candidate. Evidence: fresh verifier output, recorded quality gate and commit with hooks.

VERIFIED — The approved V2 2.1.4 executable is above the supported floor of 2.0.4. Its Windows SHA-256 was `b12b0613e9b4a491e5b12d90a5e9bbae6d261fe9688c82bf73125a036963d399`. The below-floor row used an actual 2.0.3 executable. Evidence: approved plan/probe contract and screened native host observations.

VERIFIED — At handoff preparation the official npm `@opencode/cli` `latest` tag resolved to **2.4.2**, with a matching Windows x64 distribution and upstream tag commit `fc31a485317970bcf6be7b431a9830aaef875731`. The repository-wide GitHub latest release endpoint returned V1.19.6. Evidence: [V2 npm channel](https://registry.npmjs.org/@opencode%2fcli/latest), [Windows distribution](https://registry.npmjs.org/@opencode%2fcli-windows-x64/2.4.2), [upstream V2 tag](https://github.com/anomalyco/opencode/tree/v2.4.2), and native `gh release view`.

## Live implementation thread

VERIFIED — The Task 2 receipt preserves an authenticated Windows setup and failure matrix on the approved V2 2.1.4 tuple. Independent review found incomplete preservation and recovery evidence and a permissive matrix verifier. Corrective replay retained same-server native package inventories and manifests, observed recovery, exact Skill paths and blobs, and reproducible special cases. Evidence: Task 2 report and screened receipt.

INFERRED — The newer V2 distribution matters to current adopter compatibility and hosted verification. The 2.1.4 result remains valid for its approved tuple. Evidence and reasoning: `latest` is 2.4.2, the upstream tag comparison reported diverged history, and this plan exercises private-server selection, native package/config/skill inventories and tool-result fields that must be checked against any newly selected executable. Preserve the original result and record any newer run under its own tuple.

## Corrections to durable artifacts

VERIFIED — The Task 2 evidence replaces the earlier Task 1 stopping point for this branch. Historical 2.1.4 acceptance remains labeled at that exact version and the approved plan and specifications retain their original bytes. Evidence: commit ancestry, receipt invariants and approved artifact blob matches.

## Decisions and provenance

VERIFIED — The operator requested a fresh handoff, Git sync, and an explicit version-freshness note. The selected transport scope is the #23 branch and its screened evidence. Evidence: direct operator messages, active #23 branch and separately dirty standalone dependency-maintenance checkout.

## Negative results

VERIFIED — The shared pre-commit hook’s historical temporary interpreter was missing. The original launcher exited 1, and its normal fallback passed when the verified worktree `.venv/Scripts` directory was first on the child PATH. Evidence: traced hook, successful hook rerun and Task 2 commit output. Recheck the fallback before the next local commit.

## Deferred obligations

VERIFIED — Hosted delivery verification, integration, issue submission or closure, #24 lifecycle, and #12 integrated acceptance remain separate obligations. Evidence: approved Task 2 publication and closure gates, current #23 active status and downstream dependency.

## Risks and unknowns

UNVERIFIED — Native OpenCode V2 2.4.2 compatibility and the stability of any still newer V2 release at resume. Required probe: refresh `@opencode/cli` `latest`, identify the exact binary version and digest, and use a separate owned profile to verify private-server startup, exact package revisions, native inventories and a fresh three-skill load. Assess affected setup/failure rows if those observations differ.

UNVERIFIED — The handoff’s containing commit and exact-head CI at creation. Required probe: compare fetched and live remote branch heads, verify the GitHub-served handoff and evidence blobs, and inspect CI for the exact synced SHA. Hosted native acceptance requires its own exact-target evidence.

## Proposed next steps

1. INFERRED — Verify the synced issue-23 branch, approved artifact identities, live #23 state and exact-head CI. Evidence and reasoning: the local pre-handoff commit and fetched remote base establish an expected fast-forward; the outgoing sync must verify actual arrival independently.
2. INFERRED — Recheck current V2, select the hosted delivery target and qualify its exact setup in an owned native profile. Evidence and reasoning: the newer V2 tuple has no native acceptance record and branch transport alone does not exercise the installed package. Revalidate the impacted rows and request any required integration or closure decision under the plan.

## Suggested skills

VERIFIED — `superpowers-backplane:managing-superpowers-handoffs`, `superpowers-backplane:managing-superpowers-backlog`, `superpowers:executing-plans`, and `superpowers:verification-before-completion` are discoverable. Evidence: active skill inventory and successful reads.

## Resume instruction

Invoke `superpowers-backplane:managing-superpowers-handoffs` RESUME against `docs/superpowers-backplane/handoffs/20261127T211111Z-issue-23-task-2-and-opencode-freshness.md` before selecting the next action.
