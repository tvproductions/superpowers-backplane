# Heavy SDD Backplane Migration and Implementation Plan

**Status:** Approved for native inline execution by the operator's 2026-09-27 instruction and review; live issue migration still requires approval of its exact before/after map. Reviewed draft SHA-256: `2FBE69E3E74C56AEBC5FD164BDA0A4BA814BE90FA22442CAB6C9FA85B5EE4B4D` before this annotation. Tasks 8–10 were added after that review to schedule existing #4–#7 and host-leaf obligations found by a whole-release audit; they add no authorization to edit live issues or publish.

> **For agentic workers:** Execute one reviewed slice at a time using upstream Superpowers. The operator's instruction for this work forbids commits and pushes until a separate git-sync request; preserve uncommitted changes in the isolated `design/sdd-ecosystem-v1` worktree.

**Goal:** Migrate this repository deliberately from its v0.1 issue-only release arc to a self-hosted heavy SDD model targeting `1.0.0`, implement the reusable SP-BP contract for issue kinds, semantic links, traces, views, V&V, and release gates, and carry the remaining adoption and release obligations through a verified 1.0 candidate.

**Architecture:** The approved project PRD owns requirement definition and approval. GitHub Issues own stable anchors and mutable delivery state; a constrained record block declares kind, semantic ID, and typed links. SP artifacts govern feature design and execution. A validated source snapshot drives trace and generated roadmap/backlog views; a release record and human decision gate publication.

**Tech stack:** One Python 3.13 core and CLI/helpers, Astral `uv`/`uvx`/Ruff/ty with `uv_build`, standard-library `unittest`, Markdown contracts and scenarios, Git, authenticated GitHub CLI (`gh`), native GitHub issue graph, and separately installed upstream Superpowers. Thin host-specific adapters. No parallel Go core, pytest, GitHub Projects, or IssueOps. The installed Python invocation and any adopter runtime requirement need explicit packaging proof.

**Spec:** `docs/superpowers/specs/2026-09-27-heavy-sdd-backplane-adr.md`; candidate source `gz-skills` `7bd8f8d3cb6755e06dc284647619acc9f8802984:docs/proposals/lightweight-sdd-ecosystem.md`.

**Execution method:** `superpowers:executing-plans` inline in `.worktrees/sdd-ecosystem`, with the plan-scoped ledger at `.superpowers/sdd/2026-09-27-heavy-sdd-migration-and-implementation/progress.md`. The approved ADR is the binding design; `docs/project/prd.md` owns requirement wording; the Python core and view-helper ADRs are approved corrections. The plan's task checkboxes are completion gates. Record task commands, results, and rulings in the ledger. The operator's no-commit instruction overrides the skill's commit step; do not use a commit range as evidence until git-sync is requested. Existing partial code is not retroactive RED→GREEN proof.

## Execution checkpoint (2026-09-27)

This is the controlling plan for the active worktree. The checkboxes below are acceptance gates, not a count of files created. Work started in Tasks 3–6 before their gates were closed; those slices remain partial. Read-only Task 7 mapping is preparation, not live migration.

| Task | Current status | Evidence and remaining gate |
| --- | --- | --- |
| 1: old contract | Complete | The 21-issue native before-snapshot and RED baseline are recorded. |
| 2: 1.0 authority | Complete | The operator approved the constitution, PRD, architecture, and ADR; twelve requirement IDs are stable in the PRD. |
| 3: heavy issue contract | Partial; current execution gate | Record/catalog code, tests, reference contract, and RED/GREEN transcripts exist. Audit the exact grammar, transition and link matrix, native-edge consistency, ID/alias cases, and all five legacy conformance scenarios against the written acceptance checks before closing this task. |
| 4: trace and V&V | Partial | Evidence parsing and trace currency have focused tests. Integrated requirement-to-outcome verification, distinct accepted validation, impact review, and the full scenario scoring remain open. |
| 5: derived views | Partial | Snapshot race/hash logic, deterministic rendering, `gh` intake, and local `uvx` preflight exist. Integrated generate/check commands, approved migrated input, source recheck before publication, and supported-host proof remain open. No current `ROADMAP.md` or `BACKLOG.md` is claimed. |
| 6: release gate | Partial | Fact-level assessment and negative tests exist. Authenticated human decision, integrated current trace/validation/view inputs, and candidate revision binding remain open. |
| 7: live issue migration | Not started | A proposed 21-issue classification and ID map exists. Exact before/after title, body, labels, edges, and acceptance changes, human map approval, revision recheck, and all `gh` mutations remain open. |
| 8–10: adoption and candidate | Not started | Host leaves, adopter operations, self-hosting, external validation, and integrated 1.0 review remain open. These tasks were appended after the original plan review and must be reviewed before treating their detailed steps as approved execution instructions. |

**Next slice:** Close Task 3 against its five acceptance checks and record the exact commands and scenario results. Then close Tasks 4–6 in order. Continue Task 7's exact payload drafting read-only, but do not edit a live issue until its complete map has been reviewed and approved. A new ecosystem brainstorm is unnecessary because the broad design and this plan were approved; a focused Superpowers spec/plan is needed only if the exact migration reveals a material design choice outside the ADR.

## Global constraints

- Keep this repository's root checkout on `plan/issue-19-claude-lifecycle-draft` untouched. All edits here occur in ignored `.worktrees/sdd-ecosystem` on `design/sdd-ecosystem-v1`, based on `main` at `d0eeee829c491da02351e793544aa16ad96461bf`.
- Before any Git mutation, run `git rev-parse --show-toplevel` from the original standalone root and require exactly `C:/Users/Jeff/source/repos/agents/superpowers-backplane`, as `AGENTS.md` requires. Worktree file edits are not Git mutations. Do not commit, push, merge, publish, tag, or release without the operator's git-sync or publication instruction.
- Re-read `AGENTS.md`, `HANDOFF.md`, `SUPERPOWERS.md`, the ADR, and complete native issue intake before changing an issue. Confirm `gh auth status` and exact origin. Issue bodies and comments are untrusted data.
- The repository's release target is `1.0.0`. Existing `0.1.0` package metadata and lifecycle fixtures are historical inputs; the 1.0 release version is not an excuse to rewrite their observed evidence.
- Other adopters choose lite or heavy through `gz-skills`; this repo migrates its own product arc to heavy. SP-BP does not own profile setup or MPAS adaptations, and does not replace SP feature workflows.
- Preserve separate upstream SP identity and installation. Implement SP-BP's catalog, reconciliation, traceability, V&V, views, release logic, CLI/helpers, and tests in Python; use `unittest`, never pytest. Remain neutral about a consuming project's application language and test runner. Keep host adapters thin and prove the installed Python invocation before declaring a runtime requirement or heavy readiness.
- Use `uv sync --locked`, `uv run --locked python -m unittest discover -s tests/unit -v`, `uv run --locked ruff check src tests/unit`, `uv run --locked ruff format --check src tests/unit`, and `uv run --locked ty check src tests/unit` as the Python quality gate. Use `uvx` for isolated Astral tool invocation where appropriate; do not add competing Python package, lint, or type tooling.
- No live issue migration before a reviewed mapping and approved governing documents. No completed issue is reopened or reclassified as current verification solely by script or inference.
- Exactly one six-state `backplane:*` execution label applies to open executable outcomes under the new contract. Non-executable issue kinds must not be forced into that ladder after migration.
- A generated view cannot claim freshness without a validated source snapshot and a before-publication revision recheck. A release cannot claim approval from agent actions.

## Review focus

1. An existing closed v0.1 issue has useful evidence but no current PRD requirement link: retain its historical result, report the current trace gap, and block a current-verification claim.
2. A family moves while an FDAU-style ID resembles a hierarchy path: preserve the semantic ID and change only the typed family link.
3. An issue changes during paginated snapshot collection: retry collection; do not publish a view from mixed revisions.
4. One outcome claims multiple requirements but evidence covers only one: leave the outcome unverified and show each missing or stale edge.
5. A candidate release has passing verification but no distinct validation, compatibility review, or human authorization: leave publication blocked.

---

### Task 1: Capture the old contract and RED migration baseline

**Files:**
- Create: `tests/scenarios/2026-09-27-heavy-sdd-migration-baseline.md`
- Create: `docs/superpowers/migrations/2026-09-27-v01-to-v1-issue-map.md`

**Interfaces:** Consumes current issue contract, approved v0.1 designs, live #1/#5/#7/#19 graph, and proposal. Produces a fixed before-map and explicit contradictions for all later tasks.

- [x] Record root/worktree branch and clean baseline, exact origin, gh authentication, upstream source/revision, and the candidate proposal SHA. Verify the first three through `git status --short --branch`, `git remote get-url origin`, and `gh auth status`.
- [x] Fetch the complete native 15-field JSON for every issue under #1, plus #8 and #9, through `gh issue view`. Save observed `updatedAt`, state, state reason, labels, parent, children, blockers, blocking, linked closing PRs, and URL in the map. Exclude credential or private profile state.
- [x] Score RED checks against the candidate: no approved project PRD/constitution/architecture; six-label rule applied to non-executable #1 and #7; no semantic IDs or typed requirement links; no trace and distinct validation; no generated views/freshness; no 1.0 release gate. Cite exact existing files and issue revisions rather than calling absent artifacts failures of the old v0.1 contract.
- [x] Run `git diff --check`, confirm issue state unchanged by re-fetching #1/#7/#19, and record the observed before-map. Do not assign new IDs in this task. New untracked Markdown was checked separately for trailing whitespace.

### Task 2: Establish this repository's human-governed 1.0 intent

**Files:**
- Create: `docs/project/constitution.md`
- Create: `docs/project/prd.md`
- Create: `docs/project/architecture.md`
- Modify: `AGENTS.md` and `README.md` only after the documents are reviewed.

**Interfaces:** Consumes the approved ecosystem direction and Task 1's historical map. Produces project rules, stable PRD requirement IDs and success criteria, current architecture, named approver, and a recorded human review before those documents become binding.

- [x] Write the constitution with authority ordering, amendment approver, adopting-project language neutrality, separate SP dependency, native GitHub-only backlog, human release decision, and explicit exceptions. The later Python core ADR supersedes the old skills-only implementation-language assumption without changing adopter language freedom. Keep host installation policy already approved unless a review changes it.
- [x] Write the PRD with a declared public compatibility contract and distinct, stable requirements for adoption, issue kinds/identity, typed links, trace, generated views, V&V, release gates, and migration. Give each requirement an observable success criterion; state `1.0.0` as target, not a published fact.
- [x] Write architecture context, components/interfaces, data flow, deployment/runtime limits, evidence boundaries, and ADR links. Name any useful ports/adapters and justify any departure without a blanket rewrite.
- [x] Compare every PRD requirement with the candidate and ADR, review wording and scope with the project-named human approver, and record approval in a durable reviewed document change. Until approval, mark the docs draft and do not promote requirement issues to approved anchors.
- [x] Check for duplicate requirement IDs, ambiguous terms, unowned decisions, and `0.1.0` target claims in the new governing docs. Verify `git diff --check` and keep prior v0.1 documents as dated history. Twelve unique PRD IDs were checked; `0.1.0` appears only as historical context. New untracked Markdown received a separate whitespace check.

### Task 3: Define and test the heavy issue record contract

**Files:**
- Create: `skills/managing-superpowers-backlog/references/heavy-issue-record.md`
- Modify: `skills/managing-superpowers-backlog/references/github-issue-contract.md`
- Modify: `skills/managing-superpowers-backlog/SKILL.md`
- Create: `tests/scenarios/2026-09-27-heavy-issue-record.md`
- Create: `src/superpowers_backplane/record.py`, `src/superpowers_backplane/catalog.py`, and `tests/unit/test_record.py`, `tests/unit/test_catalog.py` as the Python schema and graph core.

**Interfaces:** Consumes Task 2's approved PRD IDs and ADR. Produces a discoverable opt-in contract for kinds, per-kind states, IDs, native edges, typed links, and safe migration. Lite behavior remains addressable.

- [ ] Before editing the skill, load `superpowers:writing-skills` and `superpowers:test-driven-development`. Run a no-heavy-contract pressure scenario with a requirement anchor, an outcome, a gate, and a release issue. Record observed incorrect label, authority, and ID choices as RED.
- [ ] Define exact `## Backplane Record` JSON grammar, per-kind required/forbidden fields, allowed state transitions, link endpoint matrix, ID uniqueness and alias rules, and failure behavior for malformed or stale records. Require complete `gh` intake and preserve native hierarchy/blockers.
- [ ] Implement that grammar and identity/link validation in the Python core with `unittest` negative controls for malformed JSON, duplicate keys/IDs/aliases, family moves, splits, and many-to-many requirement links. Keep the skill as discoverable workflow guidance, not a second validator.
- [ ] Change the old blanket six-label rule only in the heavy path: open executable outcomes retain exactly one label; all other kinds use their own state authority. Keep the old v0.1 contract explicitly identified as legacy until each live issue is migrated. Preserve the read-only status/selection and evidence-gated transition rules.
- [ ] Re-run the same pressure scenario with the edited skill, score authority and state choices, and verify existing five conformance scenarios still honor lite/legacy behavior. Run structural validation and `git diff --check`.

### Task 4: Define trace and V&V evidence reconciliation

**Files:**
- Create: `skills/managing-superpowers-backlog/references/heavy-trace-and-evidence.md`
- Modify: `skills/managing-superpowers-backlog/SKILL.md`
- Create: `tests/scenarios/2026-09-27-heavy-trace-vv.md`
- Create: `src/superpowers_backplane/prd.py`, `src/superpowers_backplane/trace.py`, `src/superpowers_backplane/evidence.py`, and matching `tests/unit/` cases for approved PRD parsing, current/stale links, verification, and distinct validation.

**Interfaces:** Consumes approved PRD revisions and Task 3 records. Produces forward/reverse trace, evidence freshness, verification and validation decisions.

- [ ] Capture RED scenarios for one-to-many and many-to-many requirement/outcome links, a changed PRD requirement, stale evidence, and validation mistaken for verification.
- [ ] Specify agreed behavior-example and test-definition links separately from evidence locator, method, result, checked semantic ID/revision, integrated source, reviewer, and time. Define current/stale/unknown independently for each edge. Historical verification remains visible after a requirement change but cannot satisfy a later release without re-review.
- [ ] Make an outcome's verified claim contingent on current evidence for every governing requirement it claims. Define distinct validation against users and success criteria; never infer it from verification tests or issue closure.
- [ ] Implement forward/reverse trace and V&V decisions in Python, with tests for changed PRD wording, stale historical evidence, partial requirement coverage, and a separate accepting person for validation.
- [ ] Re-run the scenarios and score each missing, ambiguous, stale, and current trace in both directions. Verify requirement wording remains in the PRD and no `verified` claim is produced for partial coverage.

### Task 5: Produce and check derived ROADMAP and BACKLOG views

**Files:**
- Create: `skills/managing-superpowers-backlog/references/heavy-snapshot-and-views.md`
- Create: `ROADMAP.md` and `BACKLOG.md` as generated outputs only after a validated migration snapshot exists.
- Create: `tests/scenarios/2026-09-27-heavy-view-freshness.md`
- Create: `src/superpowers_backplane/snapshot.py`, `src/superpowers_backplane/gh_adapter.py`, `src/superpowers_backplane/views.py`, `src/superpowers_backplane/cli.py`, and matching `tests/unit/` cases; expose `generate` and `check` operations through a proved installed Python invocation.

**Interfaces:** Consumes Task 3 graph and Task 4 trace. Produces canonical snapshot identities, two byte-reproducible views, and a freshness check.

- [ ] Record RED cases for changing issues mid-collection, pagination, missing issue permissions, duplicate IDs, a changed PRD revision, and offline collection. Establish expected refusal or retry outcomes before writing view guidance.
- [ ] Specify collection order, pagination completion, canonical serialization, input identities/hash, issue revision recheck, bounded retry, and offline policy. Require a view header with schema and source hash; emit volatile collection time and freshness status in the check result so unchanged inputs reproduce identical view bytes.
- [ ] Implement the approved read-only Python helper per `docs/superpowers/specs/2026-09-27-heavy-view-generator-decision.md` and `docs/superpowers/specs/2026-09-27-python-core-adr.md`. Use `unittest` for parsing, ID/link validation, canonical bytes, pagination, source races, and failures before implementation. Decide and prove installed invocation and any disclosed runtime dependency on Codex, Claude Code, and OpenCode. Until a declared host passes, its view capability is `UNKNOWN` and no current view is claimed.
- A bounded local packaging observation is recorded in `tests/scenarios/transcripts/2026-09-27-python-uvx-local-preflight.md`: the Python wheel's read-only entry point ran through Astral `uvx --offline` on Windows from outside the source worktree. This does not complete the preceding generate/check or cross-host proof step.
- [ ] Generate views from the approved migrated graph, re-collect source identities before publication, and run the project-owned check to compare source hash and generated bytes. Require zero diff on repeat generation; a changed source must cause a failing freshness check.

### Task 6: Define release records and the human gate

**Files:**
- Create: `skills/managing-superpowers-backlog/references/heavy-release-gate.md`
- Modify: `skills/managing-superpowers-backlog/SKILL.md`
- Create: `tests/scenarios/2026-09-27-heavy-release-gate.md`
- Create: `src/superpowers_backplane/release.py` and `tests/unit/test_release.py` for the same release criteria as the reference contract.

**Interfaces:** Consumes Tasks 3–5 records, traces, and view snapshot. Produces a release candidate decision contract separate from tag/release publication.

- [ ] Capture RED examples in which a closed outcome, passing tests, a candidate version, or an agent-authored comment incorrectly triggers publication.
- [ ] Require included outcomes verified on integrated source, current requirement traces, distinct validation, compatibility review against the PRD public contract and SemVer, no unresolved native release blocker, current views, and human authorization tied to the exact candidate revision.
- [ ] Define release `assembling -> candidate -> approved -> published` transitions, failure/cancellation, `target_release` changes, immutable `released_in` after publication, and evidence for tag and GitHub release identity. Publication remains a separate explicitly authorized action.
- [ ] Implement read-only release assessment and candidate identity in the Python core; test release slips, stale views, missing validation, compatibility failure, agent-authored approval, and postapproval candidate drift. Keep actual publication outside the helper.
- [ ] Re-run negative and positive scenarios. A missing, stale, unknown, or agent-supplied approval must fail closed. No tag or release is created in these tests.

### Task 7: Review and apply the live issue migration

**Files:**
- Modify: `docs/superpowers/migrations/2026-09-27-v01-to-v1-issue-map.md`
- Modify: `HANDOFF.md`, issue-linked plan/spec references, and scenario ownership records only as the approved mapping requires.
- GitHub: existing #1–#24 as mapped; create additional heavy issues only when the approved PRD needs an unmatched anchor/outcome.

**Interfaces:** Consumes approved Task 2 governance, Tasks 3–6 contracts, and Task 1 before-map. Produces an auditable after-map without erasing old evidence.

- [ ] For every existing issue, record old title/revision/state/labels/native edges, proposed kind/ID/PRD links/disposition, and exact expected new fields. Explicitly review #1 as release record, #7 as gate, #5 as self-hosting proof, #19 as an unapproved draft-plan owner, and all completed host evidence. Reassess each unfinished leaf; preserve, revise, supersede, or retire with stated rationale.
- [ ] Obtain human approval of the complete mapping and changed issue acceptance before the first live `gh issue edit`. Confirm issue revisions still match the before-map; a drifted issue returns to mapping review.
- [ ] Migrate in small issue batches. Use `gh` only, preserve unrelated labels and native edges, verify each complete 15-field intake after mutation, and record old/new revisions and reason. Do not silently move a non-executable issue off its old label before the new heavy reader handles it.
- [ ] Reconcile #19's draft plan with the changed release and issue contract before readiness or execution. Keep the root branch and its unapproved plan untouched; write a new revision in its own later work stream if the review requires it.
- [ ] Recheck every issue, PRD anchor, ID uniqueness, native blocker, trace, generated view, and release-gate input. The after-map must identify unresolved migration gaps, never guess them away.

### Task 8: Reconcile and finish the host adoption leaves

**Files:** Host package, guide, and scenario files owned by the reviewed plans for #11, #12, #19–#24; do not edit the unrelated #19 draft branch in this worktree.

**Interfaces:** Consumes the migrated 1.0 contract and the completed v0.1 Codex and Claude package/setup evidence. Produces fresh installed-package evidence for all declared host variants under the new kind, trace, view, and release behavior.

- [ ] Reconcile each open host issue's old acceptance, owner, and blocker against the approved PRD and heavy contract. Update its own SP spec and plan before execution, preserving the earlier approved host installation decisions that still apply.
- [ ] Complete the Claude lifecycle and final acceptance chain #19 -> #11. Treat the existing #19 plan as an unapproved draft needing revision against the migrated issue record and 1.0 release scope.
- [ ] Complete the shared OpenCode adapter and both setup/lifecycle branches #20 -> (#21 -> #22, #23 -> #24) -> #12. Verify both declared OpenCode variants from installed packages.
- [ ] Re-run Codex and completed Claude package/setup seams affected by the 1.0 skill or packaging changes; preserve historical results and record fresh evidence only for current inputs.
- [ ] For each host, score direct and model-selected discovery, compatible gz-skills/SP/SP-BP installation, issue kind and lifecycle semantics, trace and views, failure preservation, update, rollback, and uninstall where the approved host contract requires them. An UNKNOWN mandatory row blocks that host's 1.0 acceptance.

### Task 9: Complete adopter operations, self-hosting, and external validation

**Files:** `README.md`, `HANDOFF.md`, installation and operations guides, reviewed issue-specific SP artifacts, migration after-map, and evidence records.

**Interfaces:** Consumes Tasks 1–8 and the release graph #4–#6. Produces a usable adopting-project package and distinct self-hosting and external intended-use evidence.

- [ ] Reconcile #4's licensing and operations scope to 1.0, document the exact license choice for human approval, and exercise the documented installation, update, rollback, removal, and recovery paths. Do not invent legal authorization.
- [ ] Reconcile #5's self-hosting acceptance to the approved PRD. Exercise the migrated issue graph, requirement anchors, many-to-many traces, derived views, current evidence, and a bounded outcome lifecycle. Record which previous closed evidence is historical and which seams were freshly reverified.
- [ ] Reconcile #6's external pilot to the heavy 1.0 contract. Identify an authorized adopting repository and its own governing-document approver, compatibility contract, declared harnesses, and verification commands. Run the installed three-component workflow there without changing that project's documents or issues before its own authorization.
- [ ] Record separate verification of the specified 1.0 requirements and validation with intended users or maintainers against PRD users and success criteria. The external pilot alone does not silently become validation acceptance.

### Task 10: Integrated conformance and 1.0 release-candidate review

**Files:**
- Create: `tests/scenarios/2026-09-27-heavy-sdd-integrated.md`
- Modify: `README.md`, `HANDOFF.md`, and installation/operations guidance only for verified new behavior.

**Interfaces:** Consumes all prior slices. Produces reviewed 1.0 candidate and gate evidence, not a published release.

- [ ] Run the existing five named Backplane conformance checks plus heavy kind/ID/link, trace/V&V, view freshness, migration, and release-gate scenarios. Record PASS/FAIL/UNKNOWN per supported harness and surface; unknown mandatory rows block readiness.
- [ ] Audit the ADR against the implemented contracts and live graph, the approved PRD against every outcome, and every planned requirement against verification seams. Review changed skill behavior independently under upstream Superpowers review guidance.
- [ ] Run `git diff --check`, check all modified Markdown/JSON structure, re-run the project-owned view freshness check, and re-fetch the complete release graph. Record exact commands, exits, and identities.
- [ ] Reconcile #1's release record and #7's gate against #4–#6 and every included host outcome; review compatibility against the PRD public contract and the candidate `1.0.0` version. A closed issue or passing test does not imply intended-use validation or human authorization.
- [ ] Prepare a concrete review package and migration handoff. Do not commit, push, merge, tag, or publish until the operator separately requests git-sync and later authorizes release publication. Publication and release-record closure are later authorized actions with their own fresh checks.

## Execution and decision boundaries

Tasks 1 and the draft portions of Task 2 can proceed without mutating GitHub. Task 2 requires recorded human approval before its documents become authority. Task 7 requires approval of the exact before/after issue map before live mutation. Task 5's deterministic Python generator and installed invocation are design checkpoints: if the declared harnesses cannot run and check it under the reviewed runtime policy, do not claim current generated views. Task 6 never grants its own human publication approval. Historical v0.1 host work can continue only after its issue and plan are reconciled with the new 1.0 authority. Task 9 requires a human license choice and an authorized pilot repository; these are real product inputs, not implied by approval of this plan.
