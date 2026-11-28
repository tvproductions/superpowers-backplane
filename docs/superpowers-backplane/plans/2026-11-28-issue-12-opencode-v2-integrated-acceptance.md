# Issue #12 OpenCode V2 Integrated Acceptance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement the plan inline after approval. Steps use checkboxes for tracking.

**Status** — Draft for operator review.

**Goal** — Verify and accept the integrated Backplane installation and lifecycle for OpenCode V2 2.0.4+.

**Architecture** — Reconcile the accepted shared adapter, setup, and lifecycle results against the integrated source. Retain evidence for matching inputs, rerun affected operations, and verify the exact hosted package in a fresh V2 session.

**Tech stack** — OpenCode V2, Git, `gh`, the existing Node adapter checks, and Backplane's locked Astral/Python tooling.

**Spec** — [Adoption and installation design](../../superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md) (`a790d953691d178f711757e9164afb60932eb65a`) and [host leaf rescope](../../superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md) (`e1e42d0b89bf950b988b05097dd011c6490aefe6`). [Issue #12](https://github.com/tvproductions/superpowers-backplane/issues/12) at `2026-11-27T08:47:30Z` narrows OpenCode acceptance to V2.

## Global Constraints

- Keep the canonical Backplane skill tree, the shared adapter and V2 `plugins` configuration, and independently installed Superpowers. Exclude V1 qualification, Codex and Claude Code metadata, consumer runtime requirements, Projects, and IssueOps.
- Preserve the [November 1 plan](2026-11-01-issue-12-opencode-final-acceptance.md) and its [approval receipt](2026-11-01-opencode-wrap-approval.json). Reuse the V2 cases and evidence interfaces from the [shared probe contract](2026-11-01-opencode-remaining-acceptance-probe-contract.md). Use the current locked repository commands for Python and the current issue revision for scope.
- Protect user files, unrelated plugins, upstream installations, repository history, and GitHub issue state. Follow [repository rules](../../../AGENTS.md) for registered worktrees, owned `.sp-bp/work/issue-12/` fixtures, canonical containment, and child-scoped configuration and authentication. Reuse authentication through the native host's authorized mechanism. Keep credentials and raw captures outside tracked evidence.
- Apply [ADR-0001 edition 1](../../decisions/ADR-0001-001-reference-decisions-through-existing-checkpoints.md) and its [explicit approval](../../decisions/approvals/ADR-0001-001-approval.md) when recording authority and evidence. Keep existing record formats and distinguish reviewed inputs, delivery, verification, and approval.
- Issue #12 acceptance gates the [selected 0.4.0 bundle](../releases/2026-11-28-v0.4.0.md). Maintain #4, #6, and #1's own acceptance gates. Obtain applicable authorization for remote fixture mutations, publication, integration, and completed closure.

## Review Focus

- The setup guide changed between accepted #23 and #24 deliveries. Compare the commands and assertions used by each row, including the capability checks in the new maintenance section.
- The package includes `docs/` and `README.md`. The README still describes V1/V2 smoke coverage and pending lifecycle verification. Check the shipped support statements against the V2-only issue and the current guide. Include any corrections and newly tracked planning or release documents in the manifest for the exact source tested.
- A successful V2 2.4.2 inventory proves package and skill file identity only. Require three completed native Skill calls for any fresh supported-host result. Preserve the actual 2.0.3 refusal and its original binary identity.
- Check the ordering of #39's real integration and verified completion, and retain the unrelated `documentation` label and zero-mutation status and selection evidence.
- Keep the source tested by the integrated assessment distinct from a later evidence commit and from the 0.4.0 candidate. Reassess affected inputs whenever the target changes.

### Task 1 — Reconcile current authority and freeze the V2 matrix

**Files** — Create `tests/scenarios/2026-11-28-issue-12-opencode-v2-acceptance.md` and `.json`. Start an append-only execution ledger under `.sp-bp/work/issue-12/`.

**Consumes** — Current #12 and #1/#2/#6/#20/#23/#24/#39 native records, the approved designs, the owning receipts below, and the verified hosted `main` baseline `9bf8cba0cf21a7e86b4979f1f6b416dd9e328b5c`.

**Produces** — A fixed 41-row matrix with 17 setup and failure cases, eight lifecycle operations, five conformance checks, and 11 native issue-state scenarios. Each row carries accepted evidence pointers and exact inputs or identifies a seam to rerun. Task 3 records the fresh hosted delivery separately.

- [ ] Re-read the complete native issue fields and relationship counts. Reconcile #12's revision and lifecycle with this plan. Verify completed closure of #2, #20, #23, and #24 and the accepted V2 [adapter](../../../tests/scenarios/2026-11-01-issue-20-satisfaction.md), [setup](../../../tests/scenarios/2026-11-27-issue-23-satisfaction.md), and [lifecycle](../../../tests/scenarios/2026-11-28-issue-24-satisfaction.md) deliveries and review evidence. Confirm #39's completed closure after PR #40 and refresh #12's effect on #6. Record the approved plan and the native issue revision before starting execution.
- [ ] Fix the setup rows to `S-native`, `S-sibling`, and `S-absent`. Fix the failure and preservation rows to `F-lookalike`, `F-versionless`, `F-duplicate`, `F-dirty-adopt`, `F-dirty-update`, `F-collision`, `F-gh-auth`, `F-gh-intake`, `F-gh-label`, `F-gh-close`, `F-missing-skill`, `F-incompatible`, `F-below-floor`, and `F-unauthenticated`. Use the [17-row setup receipt](../../../tests/scenarios/2026-11-01-issue-23-opencode-acceptance.json) for original case definitions and outcomes. A verified refusal with unknown upstream provenance can satisfy `F-versionless` while the provenance remains UNKNOWN. `F-below-floor` requires actual V2 2.0.3 and unchanged configuration before package loading.
- [ ] Fix lifecycle rows to `L-install`, `L-repeat`, `L-update`, `L-rollback`, `L-unavailable-source`, `L-failed-verification-recovery`, `L-uninstall`, and `L-test-restore`. Include the unavailable-candidate preflight control and both after-apply recovery controls. Use the [lifecycle receipt](../../../tests/scenarios/2026-11-01-issue-24-opencode-acceptance.json) and [corrected update/rollback replay](../../../tests/scenarios/2026-11-28-issue-24-capability-replay.json).
- [ ] Include `skill-structure`, `native-issue-intake`, `language-neutral-verification`, `lifecycle-transitions`, and `superpowers-installation` from the [conformance receipt](../../../tests/scenarios/2026-11-01-issue-24-opencode-conformance.json). Include `status`, `design`, `ready`, `selection`, `start`, `block`, `resume`, `submit`, `rework`, `resubmit`, and `close` from the [native fixture receipt](../../../tests/scenarios/2026-11-01-issue-24-opencode-native-fixture.json). Check zero mutation for status and selection, one correct lifecycle label on each open fixture state, preservation of unrelated labels, and actual completed closure after verified integration.
- [ ] Compare exact package manifest, adapter, guide sections, installed skill blobs, host executable/version/hash, upstream origin/revision, and `gh` version/capabilities applicable to each row. The guide changes from `08a6348ecb3a83eaa91ce65d07e02b0032fd683d` at #23 delivery to `4d3e5597e5961c417c34666e5eff43a53995b1b4` at #24 delivery and the handoff baseline. The adapter (`c96a668ce427f1f8017894f58e291882c82e171a`) and skill tree (`a20788fd467af8c6fb22a7cc00fe9c396e3c1154`) match at all three revisions. Cite each retained run at its original revision and show why the changed inputs do or do not affect its assertion. Record missing comparisons as UNKNOWN.
- [ ] Record for each row its ID, criterion, scored result, applicable input identities, evidence locator and digest, expected outcome, actual observations, and preservation result. Mark inapplicable fields with a reason, such as skills not loaded during an expected prior refusal. Confirm all 41 unique row IDs and identify every unresolved or changed seam before Task 2.

### Task 2 — Rerun affected operations and verify the integrated candidate

**Files** — Complete the Task 1 assessment pair. Correct the OpenCode support statements in `README.md` and `docs/installing-opencode.md` where the V2 contract or evidence requires it. If replay demonstrates an adapter defect, correct `index.js` and add a focused control to `tests/opencode-adapter.test.mjs`. Retain any new verification helper source with the supporting evidence under `tests/scenarios/transcripts/`.

**Consumes** — Fixed matrix, verified isolated V2 inputs, and a clean registered execution workspace.

**Produces** — Complete passing matrix, full quality-gate results, and a reviewed candidate.

- [ ] Read the active OpenCode V2 guide and help for the verified executable. Establish owned child config/cache/state and authenticated model availability. Use Windows V2 2.1.4 and independent native Superpowers v7.0.1 as the proposed replay baseline because #23 and #24 already qualified that combination. Verify absolute binary path, version and hash, upstream origin/resolved SHA, `gh` full native intake and label/close-reason capabilities, and the effective sources before reuse. Reconcile any changed input before scoring affected rows. Use the real retained V2 2.0.3 binary in an isolated profile if its negative seam requires replay.
- [ ] Rerun every affected row with the applicable #23 or #24 native procedure using its archived source and exact assertions. For guide changes, check the setup prompt, fresh discovery, pre-apply candidate lookup, post-update and rollback compatibility checks, and before/after protected state where applicable. Use an authorized fresh fixture if changed inputs require native mutation scenarios to run again. Record outcomes and recovery before repair. Require PASS for every mandatory row including the expected refusal outcomes.
- [ ] Reuse the owning scorers where they cover the required assertions. If new validation is needed, demonstrate a failing `unittest` control before adding the minimum logic. Cover omitted or duplicate rows, supported results claimed for the below-floor binary, wrong source or missing Skill results, altered protected state, missing authority, and completion before integration. Preserve original receipts and require the valid matrix to pass.
- [ ] If replay exposes an integration defect, reproduce it with an assertion-level failure in the verified worktree, apply the bounded correction, and rerun the affected checks. Recompute the target manifest and reopen any row whose inputs changed. Keep this task within the issue's adapter, guide, and integration verification scope.
- [ ] Reconcile the README and guide with the V2-only scope and 2.0.4 floor. Tie statements about setup and lifecycle to their accepted evidence. Keep integrated-acceptance claims tied to the verified target and retain any V1 example as historical context. Recompute the manifest for the candidate containing the corrected docs before whole-candidate review.
- [ ] From the verified root, run the full [Python/Astral acceptance gate](../../engineering/python.md#canonical-commands) with the applicable A01–A18 evidence: `uv sync --locked --all-groups`, `uv lock --check`, `uv run --locked ruff check .`, `uv run --locked ruff format --check .`, `uv run --locked ty check`, `uv run --locked python -m unittest discover -s tests -p test_*.py -v`, `uv run --locked pre-commit run --all-files`, `node --test tests/opencode-adapter.test.mjs`, and `git diff --check`. Compile and parse guide examples as required by the established probe, validate links and receipt identities, and obtain fresh review of the whole candidate and all acceptance claims. Record the exact reviewed commit and resolve material findings.

### Task 3 — Prove exact hosted delivery and record acceptance

**Files** — Finalize the Task 1 assessment pair. Conditionally create `tests/scenarios/2026-11-28-issue-12-opencode-v2-integrated-delivery.json` and `tests/scenarios/2026-11-28-issue-12-closeout.json` once the corresponding observations exist.

**Consumes** — Reviewed candidate, passing fixed matrix, and applicable authority for integration and closeout.

**Produces** — Exact-source V2 installation evidence and a criterion-by-criterion acceptance record for #12.

- [ ] Verify the approved integration target and remote arrival. Require exact-delivery CI on Windows, macOS, and Ubuntu. Reconcile the integrated source against the reviewed candidate and replay affected rows if integration changed any relevant inputs.
- [ ] Install the exact hosted delivery SHA through the native V2 resolver in a fresh owned profile. Using the [#24 hosted verification driver](../../../tests/scenarios/transcripts/2026-11-28-issue-24-verify_hosted24.py.txt) as the reference, compare every installed package file against the resolved Git tree, including shipped docs. Require one effective Backplane entry, independent upstream, three successful native Skill results with their sources, full `gh` capability results, and preserved user/plugin/upstream/repository/issue state. Confirm success from the fresh native results and keep the installed delivery distinct from the assessment storage commit.
- [ ] Map all current #12 criteria and verification seams to the final matrix and delivery receipt. Require PASS for every supported-host row and prove the actual below-floor refusal. If applicable authority is present, publish the reviewed assessment, verify its remote blob IDs, re-read the full issue immediately before completed closure, remove only the Backplane lifecycle label, and verify native readback. Record the observed closure and #1/#6 relationship effects separately.
- [ ] Feed the accepted #12 evidence into #4's existing adopter-operations plan when that work resumes. Before 0.4.0 publication, bind #12 acceptance to the actual release candidate and verify its affected inputs and exact installed package under the release plan.
