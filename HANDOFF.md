# Handoff

## Current state

The standalone local repository is at
`C:\Users\Jeff\source\repos\agents\superpowers-backplane` on feature branch `feat/codex-installation-surface`.
Before Git mutation, continue to require `git rev-parse --show-toplevel` to resolve
exactly to that Backplane root.

The initial design is approved in principle:

- Everything assumes and is fitted to upstream Superpowers.
- Native GitHub Issues provide backlog continuity.
- GitHub CLI (`gh`) is a hard dependency.
- GitHub Projects are optional visualization only and never authoritative;
  IssueOps is not used.
- The project is language-neutral and must never assume pytest.
- Backplane can adopt a compatible native Superpowers plugin or sibling
  checkout, or obtain upstream for the user while preserving provenance and
  independent updateability.

The first skill and its reference contracts have passed the bootstrap
pressure scenarios plus a five-control/five-skill read-only status and
selection micro-test. The no-skill arm supplied complete native intake in 0/5
samples; the skill-enabled arm supplied it in 5/5 while both arms refused to
invent priority or mutate state. The verbatim response records are under
`tests/scenarios/transcripts/`.

Stable upstream Superpowers `v6.4.1` is installed at
`.agents/superpowers` at commit
`5bf4e78011075bcfc0dc295f0724994cd123ee71`. Discovery junctions expose
upstream Superpowers, `managing-superpowers-backlog`, and
`managing-superpowers-handoffs` under `.agents/skills`. The local update and
fresh Codex conformance evidence are recorded in
`tests/scenarios/2026-09-19-superpowers-v6.4.1-compatibility.md`.
The repository is published publicly at
`https://github.com/tvproductions/superpowers-backplane`, and `main` tracks
`origin/main`. GitHub CLI authentication was verified for `ahuimanu` with
keyring-stored credentials. The repository-local Git identity uses GitHub's
noreply address. Re-check `gh auth status` before real backlog operations.

## Re-entry sequence

1. Read `AGENTS.md`.
2. Read the bootstrap design and plan linked there, then the approved
   v0.1 adoption spec and plan named below.
3. Read `SUPERPOWERS.md` and confirm that the installed checkout matches it.
4. Confirm that the Git top-level directory is exactly this repository root.
5. Inspect `skills/managing-superpowers-backlog/`.
6. Review the RED/GREEN/REFACTOR evidence in `tests/scenarios/`.
7. Confirm `gh auth status` succeeds before any real backlog operation.
8. Confirm `origin` resolves exactly to
   `https://github.com/tvproductions/superpowers-backplane.git` before any
   real backlog operation or push.

## Issue #2 adoption contract

The operator approved native plugin installation for Codex, Claude Code, and
OpenCode V1 and V2; one canonical Backplane `skills/` tree; a separate upstream
Superpowers installation; and evidence-gated lifecycle transitions within an
authorized workflow. Status and recommendation requests are read-only, and
selection alone does not change a label.

The written specification is
`docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md`.
Its native-package adoption correction has RED/GREEN evidence in
`tests/scenarios/2026-09-19-native-superpowers-package-adoption.md`.
The user approved the written specification and selected Native inline execution
on 2026-09-19. The approved plan is
`docs/superpowers/plans/2026-09-19-v0.1-adoption-contract-completion.md`.
It records issue #2's consumed semantic revision `2026-09-19T13:06:19Z`.
The issue body now links both approved artifacts and was reconciled at
`2026-09-19T14:07:17Z`. Issue #2 was closed with reason `completed` on
2026-09-19 after independent review found no Critical or Important findings
and fresh integrated verification passed on published `main` at
`77625553fd0238770689f968721c674d5740e1c6`. Its final issue state has
no lifecycle label. Recheck the live issue and remote state on re-entry.

The review and closure comments on issue #2 record the verification commands,
native graph checks, and scored design evidence. One Minor review finding
remains for host-leaf tests: the audit's F3 checkout probe combines dirty
state with lookalike provenance, so it does not isolate dirty authoritative
adoption from an unsafe update.

The design verification records are:

- `tests/scenarios/2026-09-19-v0.1-contract-review.md` — 14/14 scored document checks, including native upstream package and checkout failures.
- `tests/scenarios/2026-09-19-v0.1-four-host-verification-matrix.md` — 6/6 scored ownership assignments for four host variants and two unsupported OpenCode floors.
- `tests/scenarios/2026-09-19-v0.1-lifecycle-walkthrough.md` — 17/17 scored document walkthroughs plus issue #2 revision reconciliation.

The native release hierarchy under [issue #1](https://github.com/tvproductions/superpowers-backplane/issues/1)
now has installation leaves [Codex #3](https://github.com/tvproductions/superpowers-backplane/issues/3),
[Claude Code #11](https://github.com/tvproductions/superpowers-backplane/issues/11), and
[OpenCode V1/V2 #12](https://github.com/tvproductions/superpowers-backplane/issues/12).
Their native dependency edges from completed #2 are now resolved. The user
approved the Codex #3 plan on 2026-09-19 after reviewing its execution risks.
`docs/superpowers/plans/2026-09-19-codex-installation-surface.md` is published
on `main` at `057e80f67e8b6235548030a236415576163fb239` and linked from the
issue. Issue #3 moved from `backplane:designing` to `backplane:ready` after
the plan was published; its resulting issue revision is
`2026-09-19T19:01:03Z`. The plan covers the root Codex package, installation
guide, isolated lifecycle checks, and fresh conformance. Its plan commit is
already complete; execution starts by creating a feature branch from the
synced `main`, re-reading the issue, and moving #3 to `backplane:active` as
Task 1 begins. Resolve the review's command-context, isolated-session, and
review-transition gaps during execution before claiming their acceptance
checks pass. Claude Code #11, OpenCode #12, and self-hosting #5 remain open in
`backplane:backlog`. The three installation leaves still block the one external
pilot #6. The package implementations, live host checks, pilot, integration,
and release remain future work. V0.1 does not assume a standalone Backplane
executable.

## Issue #3 Codex implementation checkpoint (2026-09-19)

Issue #3 is open with `backplane:active`; last observed `updatedAt` is `2026-09-19T19:37:32Z`. Work is on `feat/codex-installation-surface`. The user approved pushing that branch to make immutable refs reachable for disposable Git tests. It is not merged or released.

Task 1 package commit: `8bfba888599568cc8f729ba6f0c030ace8e6377f`. Task 2 guide commit: `6c26f0354b0bf231172a13327e2dc898b8b772b5`. Task 3 is in progress; read `.superpowers/sdd/2026-09-19-codex-installation-surface/progress.md` and `tests/scenarios/2026-09-19-codex-installation.md` before resuming.

Disposable Codex CLI checks passed for local install, repeat install, fixture-only version change and rollback, pinned Git SHA switch and restoration, and Backplane-only uninstall while preserving upstream and unrelated plugin files. The initial update preflight accepted an alternate Backplane marketplace ID; this was reproduced RED and corrected GREEN in `docs/installing-codex.md`.

The isolated `state-native` profile completed browser OAuth once; device-code authorization remained disabled. Do not start another login flow. Fresh Codex sessions from the disposable fixture root cataloged and directly read upstream `superpowers:using-superpowers` and both namespaced Backplane skills from separate installed plugin caches, without repository junctions. The first read-only sandbox file read was blocked; a fresh `--approve-for-me` session read all three files. The installed Backplane cache initially held an older installation reference. Its sole differing skill file was refreshed to current SHA-256 `50D82CCACBF71D368E983984157ABE91D1FAFD977F1F4D654C0FD58B5393329D`; the earlier behavioral responses were excluded. Four fresh current-cache behavioral scenarios passed their named expectations, and an installed-skill probe separated dirty authoritative adoption from a refused update. Read `tests/scenarios/transcripts/2026-09-19-codex-installed-plugin-discovery.md` and `tests/scenarios/transcripts/2026-09-19-codex-installed-plugin-conformance.md` for exact prompts, responses, caveats, and session IDs.

The Codex guide now uses the actual namespaced Backplane skill IDs observed in the native catalog. The prior guide update/rollback commands passed the disposable replay; a later claim that they lose a same-marketplace sentinel was retracted after the existing fixture evidence showed Codex restored that plugin on marketplace re-add. No guide lifecycle command was changed for that mistaken claim.

Issue #3 remains OPEN at `backplane:active` and `updatedAt=2026-09-19T19:37:32Z` at the last full intake. Disposable lifecycle issue #13 remains open at `backplane:review` after tested review reversal. The tested native upstream mode now has fresh discovery, `gh` preflight, and all five conformance checks. The separately seeded sibling and absent states have CLI provenance/install evidence but no authenticated fresh setup sessions; all six disposable failure cases now have current-cache installed-skill hypothetical responses; none changed a real issue or an authoritative versionless release. Remote integrated-package discovery, the final whole-branch review, issue #3 review/completion, and fixture closure remain open. An early read-only reviewer found no implementation defect through `96bdae2` but correctly assessed the branch as not ready to merge. A process-only Codex config override failed to hide the installed upstream plugin, so it cannot stand in for sibling or absent-mode fresh sessions; no saved profile state changed. Do not mark #3 complete or merge based on the current matrix. The feature branch includes the native evidence and guide correction checkpoint; inspect `git status`, recent commits, and the ledger before continuing.
