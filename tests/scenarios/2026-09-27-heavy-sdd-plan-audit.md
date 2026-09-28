# Heavy SDD intent, scope, and plan audit

**Observed:** 2026-09-27. **Verdict:** Task 1 complete; later slices remain gated by their own evidence. The operator approved the ADR, constitution, PRD, architecture, and plan after this audit's initial RED pass. A subsequent whole-release audit found that the initial eight-task plan stopped at handoff without scheduling the remaining host leaves, #4 operations/license, #5 self-hosting, #6 external pilot, and #7 integrated release review. The plan now includes Tasks 8–10 for these existing obligations; this is an execution-scope correction after the reviewed draft, not evidence that those tasks are complete.

## Intent to scope

| Candidate and operator intent | Scoped authority | Result |
| --- | --- | --- |
| SP-BP owns issue graph, IDs, traces, views, V&V, release gate; PRD owns requirement wording and approval; SP and gz-skills retain their roles. | ADR authority table and `docs/project/prd.md` requirements `BP-R001`–`BP-R012`. | Aligned; operator approval recorded in governing documents. |
| This repository targets `1.0.0` and migrates entirely, while heavy remains opt-in for other adopters. | ADR context/migration, PRD target, migration map #1/#7/#19. | Aligned design; live #1/#7/#19 still express the old target or plan pending reviewed migration. |
| Incidental work needs only an issue number until promotion. | ADR kind table and PRD `BP-R003`. | Aligned after correcting the initial draft's mandatory-block rule. |
| Derived views are generated from validated source and freshness checked. | ADR snapshot decision and PRD `BP-R008`. | Scope aligned; exact cross-harness generation/check mechanism remains unproved. |
| No silent reinterpretation of existing history. | 21-issue before snapshot and proposed-only migration map. | Aligned; reviewed PRD and per-issue after-map are still missing. |

## Scope to plan

| Requirement | Planned implementation and proof | Result |
| --- | --- | --- |
| Project governance and requirement authority | Task 2 drafts constitution, PRD, architecture, and human approval. | Approved; integration and issue-anchor migration pending. |
| Distinct kinds, IDs, statuses, typed links | Task 3 RED/GREEN skill and schema scenarios. | Planned; not started until design review. |
| Forward/reverse trace, current evidence, verification versus validation | Task 4 stale and many-to-many scenarios. | Planned. |
| `ROADMAP.md`/`BACKLOG.md` with snapshot race and freshness checks | Task 5 names outputs and failure probes. | **Missing implementation mechanism:** no runtime-neutral generator/check command has been selected or proved. Task 5 explicitly returns to design review if this fails. |
| Release record, SemVer review, exact human publication decision | Task 6 negative and positive gate scenarios. | Planned; no publication authorized. |
| Full deliberate migration | Task 7 reviewed mapping and per-issue re-fetch. | Before-map exists; after-map and approval missing. The 21 old issues have no approved 1.0 requirement anchors or new heavy delivery outcomes yet. |
| Host installation and lifecycle | Task 8 reconciles and finishes #19/#11 and #20–#24/#12, then refreshes affected Codex/Claude evidence. | Planned; the old host graph remains live and its v0.1 acceptance is insufficient for a 1.0 claim. |
| Operations, self-hosting, external pilot | Task 9 reconciles #4–#6 and records distinct 1.0 validation. | Planned; license selection and authorized pilot repository are external inputs. |
| Integrated supported-harness and release evidence | Task 10 conformance, #1/#7 gate, and candidate review. | Planned; no new host run or release authorization. |

## Cross-repository readiness dependency

The candidate proposal assigns first-use profile selection, `.gz-skills/settings.json` creation, tested compatibility-set publication, and four MPAS adaptations to `gz-skills`. Its commit is design input, not a released implementation. This SP-BP worktree has no `.gz-skills/settings.json`, and no tested three-component compatibility set or fresh heavy-host proof has been recorded here. The heavy issue reader can be specified and exercised locally, but this repository cannot yet claim its own heavy profile ready. Task 8/9 host and self-hosting evidence must include the actual gz-skills release and setup path once available; SP-BP must not duplicate that setup implementation.

## Python implementation correction

The exact committed candidate did not specify SP-BP's implementation language. Later uncommitted gz-skills design text and the operator's direct 2026-09-27 correction identify SP-BP as a Python project and exclude the exploratory Go core. The Go prototype was removed uncommitted. The operator also required exclusively Astral Python tooling: `uv`/`uvx`, Ruff, and ty. The [Python core ADR](../../docs/superpowers/specs/2026-09-27-python-core-adr.md) records the explicit supersession of the old skills-only language-neutral implementation assumption while retaining adopting-project language freedom and the no-pytest rule. `.python-version`, `pyproject.toml`, and `uv.lock` now declare the source toolchain. Python source tests alone do not prove the installed runtime or view freshness.

## Required corrections before later slices

1. Preserve the operator's approval record and reviewed draft hashes in the ADR and governing documents. Substantive edits to the approved requirement wording need renewed review before issue-anchor migration.
2. Decide and prove Task 5's mechanism before generating views. The first probe should use `gh`'s built-in `--json`/`--jq`/`--template` and pagination with Git hashing, because `gh` and Git are already required. If it cannot validate and reproduce the full graph on each declared harness, propose a small SP-BP-owned packaged helper; do not add a consuming-project runtime silently.
3. Complete and approve a per-issue after-map before live GitHub edits. The recommended #1 release record and #7 gate classifications remain candidates; #7 may need a separate executable publication outcome.
4. Reconcile the unapproved #19 plan in its own branch after the 1.0 authority is accepted. Do not fold the unrelated draft into this worktree.
5. Reconcile the implementation's `authorized_by` and `compatibility_reviewed_by` release link types with the approved ADR's baseline list before publishing the schema. They express approved release facts, but the exact typed schema is an implementation clarification that must be visible in design review.

The first two corrections are design and implementation gates, not defects in the old v0.1 delivery. Existing v0.1 work remains governed by its approved contract until deliberately migrated.
