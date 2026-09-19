# Handoff

## Current state

The standalone local repository is at
`C:\Users\Jeff\source\repos\agents\superpowers-backplane` on local `main`.
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

## Current issue #2 design

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
`2026-09-19T14:07:17Z`; its only lifecycle label is `backplane:active`.
Issue #2 remains open. Its design evidence is committed on `main`.
Verify remote alignment independently on re-entry. Issue closure requires
fresh integrated verification and an authorized native issue update.

The design verification records are:

- `tests/scenarios/2026-09-19-v0.1-contract-review.md` — 14/14 scored document checks, including native upstream package and checkout failures.
- `tests/scenarios/2026-09-19-v0.1-four-host-verification-matrix.md` — 6/6 scored ownership assignments for four host variants and two unsupported OpenCode floors.
- `tests/scenarios/2026-09-19-v0.1-lifecycle-walkthrough.md` — 17/17 scored document walkthroughs plus issue #2 revision reconciliation.

The native release hierarchy under [issue #1](https://github.com/tvproductions/superpowers-backplane/issues/1)
now has installation leaves [Codex #3](https://github.com/tvproductions/superpowers-backplane/issues/3),
[Claude Code #11](https://github.com/tvproductions/superpowers-backplane/issues/11), and
[OpenCode V1/V2 #12](https://github.com/tvproductions/superpowers-backplane/issues/12).
Each is blocked by #2 and blocks the one external pilot #6. Issue #5 owns
self-hosted native lifecycle tests. The package implementations, live host
checks, pilot, integration, and release remain future work in those leaves.
V0.1 does not assume a standalone Backplane executable.
