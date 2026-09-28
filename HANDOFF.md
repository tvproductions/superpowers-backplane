# Handoff

## Active 1.0 heavy SDD migration (2026-09-28, handoff)

The operator requested a second git-sync. The append-only [post-sync handoff](docs/superpowers/handoffs/20260928T012304Z-heavy-sdd-post-sync-resume.md) is the explicit RESUME target; it links its [predecessor](docs/superpowers/handoffs/20260928T010454Z-heavy-sdd-1-0-task-3-continuation.md). Reconcile its observations against current Git, PRD, plan, and issue state on resume; neither handoff grants issue-migration or release authorization. The plan-scoped `.superpowers/sdd/` execution ledger is ignored scratch and is not transported by Git; the tracked plan checkpoint and handoffs carry the durable continuation state.

**Execution checkpoint:** Follow `docs/superpowers/plans/2026-09-27-heavy-sdd-migration-and-implementation.md`, especially its execution checkpoint and Task 3 acceptance checks. Tasks 1–2 are complete; Tasks 3–6 have partial slices and open gates; Task 7 has a read-only proposed map but no live mutation; Tasks 8–10 have not started. Finish Task 3, then Tasks 4–6, before treating the proposed map as an executable migration. The user requested a visible spec/plan trail; record each closed gate in that plan rather than treating code or passing unit tests alone as completion.

The original standalone checkout remains on `plan/issue-19-claude-lifecycle-draft`; its unrelated draft is untouched. The active 1.0 work is isolated in ignored `.worktrees/sdd-ecosystem` on `design/sdd-ecosystem-v1`, based on main `d0eeee829c491da02351e793544aa16ad96461bf`. The operator has requested a branch commit and push for handoff; inspect Git for the resulting identity. No live GitHub issue edit, tag, or release has been made for this work. Before Git mutation, the standalone root check in `AGENTS.md` still applies.

The operator approved the 1.0 heavy SDD ADR, constitution, PRD, architecture, and migration plan, then required SP-BP's catalog, reconciliation, traceability, V&V, views, release logic, CLI/helpers, and tests to use Python with thin host adapters. The exploratory Go prototype was removed uncommitted; do not rebuild a parallel Go core. The operator also approved a bounded bundled helper for deterministic views, with exact installed Python invocation and runtime packaging still to be proved. See `docs/superpowers/specs/2026-09-27-heavy-sdd-backplane-adr.md`, `2026-09-27-python-core-adr.md`, the helper ADR, and `docs/superpowers/plans/2026-09-27-heavy-sdd-migration-and-implementation.md`.

A read-only 21-issue before-snapshot and candidate migration map exist. The map now proposes a disposition and stable ID for every existing planned issue, twelve approved PRD requirement anchors, seven capability anchors, and six new implementation outcomes. It is not an approved exact mutation payload. A read-only recheck found the same 21 issue numbers and unchanged `updatedAt` values as the before-snapshot. The old live issue contract remains in force until the exact before/after issue map is reviewed and applied. The current Python core under `src/superpowers_backplane/` has focused `unittest` coverage for record parsing, stable graph IDs and many-to-many links, kind-specific execution labels, PRD table extraction, a bounded evidence parser/verification-claim assessor, forward/reverse link currency, snapshot hash/race behavior, `gh` intake, deterministic view bytes, candidate digests, and fact-level release assessment. An unrecorded incidental issue is accepted; a reviewed set of planned legacy issue numbers prevents silently treating those as incidental. The read-only `gh` adapter returned all 21 current issues with an independent count of 21; this is not a migrated heavy snapshot. The evidence and trace slices do not yet constitute a complete V&V engine; the release assessor consumes fact statuses and has no authenticated human-decision adapter. `uv build` succeeded and the wheel's read-only `backplane preflight` entry point ran through `uvx --offline` from the separate root checkout; see `tests/scenarios/transcripts/2026-09-27-python-uvx-local-preflight.md`. There is still no integrated generate/check CLI, clean-adopter runtime proof, cross-host proof, or current derived view. The Python project uses only Astral tooling: `uv sync --locked`, then `uv run --locked python -m unittest discover -s tests/unit -v`, `uv run --locked ruff check src tests/unit`, `uv run --locked ruff format --check src tests/unit`, and `uv run --locked ty check src tests/unit`. Do not call the heavy workflow or generated views ready from those results.

## Current state

The standalone local repository is at
C:\Users\Jeff\source\repos\agents\superpowers-backplane. Determine the
current branch from git status. The approved host-leaf rescope design and plan
are integrated on main at 150c7039013a77fbc87f6cca5f79363a2714bc6c.
Before Git mutation, continue to require `git rev-parse --show-toplevel` to resolve
exactly to that Backplane root.

The initial design is approved in principle:

- Everything assumes and is fitted to upstream Superpowers.
- Native GitHub Issues provide backlog continuity.
- GitHub CLI (`gh`) is a hard dependency.
- GitHub Projects are optional visualization only and never authoritative;
  IssueOps is not used.
- Historical v0.1 guidance called the implementation language-neutral. The active 1.0 Python ADR supersedes that implementation choice; adopting projects remain free to use any language. Never assume or introduce pytest.
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
issue. At plan publication, issue #3 moved to backplane:ready at
2026-09-19T19:01:03Z. The plan covers the root Codex package, installation
guide, isolated lifecycle checks, and fresh conformance. Its execution and
completion are recorded below. Claude Code #11 and OpenCode #12 remain the
other installation leaves before the external pilot #6. V0.1 does not assume
a standalone Backplane executable.

## Issue #3 Codex completion checkpoint (2026-09-19)

PR #14 merged the reviewed Codex package and installation guide at
40b7df7ec8ff477972ae2b9a8f87bdea0a0fb119. PR #15 merged the
post-integration verification record at e66ff822c0f29036e4dd104956c3961520c26e53.
The first root-package commit 8bfba888599568cc8f729ba6f0c030ace8e6377f
and both merge commits are reachable from the expected origin. The evidence PR
changed no package or guide files.

The disposable authenticated Codex profile passed fresh installed-cache
discovery at first, integrated, and rollback Git refs. Marketplace HEAD matched
each immutable SHA; the installation-reference hash changed and returned on
rollback. Native removal of the exact Backplane plugin succeeded while upstream
remained. One extra session confused an unrelated preservation sentinel with the
canonical plugin; its plugin-identity inference is excluded. The profile was
restored with three original scoped plugin IDs and 9/9 saved hashes unchanged.
No further login or credential copy is needed. See
tests/scenarios/2026-09-19-codex-installation.md and its linked transcripts.

Final integrated checks found the tested package and guide on main, 12/12
acceptance-matrix entries passing, five named conformance checks passing, and
complete native issue intake. Issue #3 is CLOSED/COMPLETED with no lifecycle
label (observed 2026-09-20T00:19:36Z). Disposable issue #13 is also
CLOSED/COMPLETED, retaining only its unrelated documentation label (observed
2026-09-20T00:20:11Z). The independent reviewer found no package or guide
defect; its Important preservation-evidence gap was fixed. One Minor control
character in a failure-probe transcript remains deferred.

This repository has one standalone worktree at its root; do not remove it as a
feature worktree. The merged feature and verification branches and ignored
plan scratch directories were removed. Claude Code #11 and OpenCode #12 remain
the installation leaves; the external pilot #6 still waits for them. No release was part of issue #3.

For the remaining host leaves, make each reviewable slice smaller: package and guide;
one host setup mode with its failures; then integrated lifecycle evidence and closure.
Treat host authentication as an external prerequisite and reuse an authorized isolated
profile. Issue #3 combined all of these and took too long.

## Host installation leaf rescope (2026-09-19 local)

The user approved eight bounded host implementation issues and the revised
native graph. Planning PR #16 merged to main on 2026-09-20 UTC at
150c7039013a77fbc87f6cca5f79363a2714bc6c. The approved design and plan
are docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md
and docs/superpowers/plans/2026-09-19-host-installation-leaf-rescoping.md.
The v0.1 functional host contract remains unchanged.

All eight new issues are open sibling children of release parent #1 with one
backplane:backlog label and no implementation plan yet:

- Claude Code: package/guide #17 -> setup/failures #18 -> lifecycle/conformance
  #19 -> final integrated acceptance #11.
- Shared OpenCode adapter #20 branches to V1 setup/failures #21 ->
  lifecycle/conformance #22 and V2 setup/failures #23 ->
  lifecycle/conformance #24. Both branches feed final acceptance #12.

#11 and #12 remain executable sibling leaves under #1, not continuity
parents. Their bodies now require passing integrated host evidence. Both
retain historical closed blocker #2 and continue to block external pilot #6.
#11 was last observed at 2026-09-20T01:31:32Z; #12 at
2026-09-20T01:31:34Z. #6 still has exactly its original blockers
#3, #4, #5, #11, and #12. The native graph, bodies, labels, and pilot gate
were verified with full gh intake of #1, #6, #11, #12, and #17-#24.

The four-host ownership matrix assigns actual issue URLs and keeps the old
assignment as dated history. Claude, OpenCode V1, and OpenCode V2 live host
verification remains pending; this graph rescope did not install a host,
authenticate, change upstream, or run live host tests. No new issue has been
selected or readied. #17 and #20 have no new unresolved dependency, but the
project has no priority policy. Each selected issue needs a current approved
Superpowers plan before execution.

Graph-record PR #25 merged the current ownership matrix and handoff on
2026-09-20 UTC at 96728cfd8cd0eabdd0f89cf5b7409625a8c573ea. Fresh
post-merge gh intake of #1, #3, #6, #11, #12, and #17-#24 matched the matrix
read from origin/main: 17 direct children under #1, all eight new leaves
open with one backlog label, both final leaves still blocking #6, and the
original five #6 blockers intact. #3 remains CLOSED/COMPLETED. The
redistribution is complete; Claude Code and OpenCode implementation and
live host verification remain future work.
