# GitHub Governance Bridges Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans after execution approval and the namespace compatibility gate below. Steps use checkbox (`- [ ]`) syntax. Do not invoke upstream workspace/ledger helpers that write to `.superpowers/`.

**Status:** Approved by the operator on 2026-10-11 with "approve": native inline execution, a fresh whole-change reviewer, and both explicit worktree and bookkeeping exceptions below. The design is approved and the plan is bound to issue #31. Verify the remaining live entry guards before implementation.

**Goal:** Deliver the approved GitHub-aligned governance doctrine and three bridge operations through the existing backlog skill, with portable checkpoint templates and meaningful behavioral evidence.

**Architecture:** One doctrine home defines ownership and completion policy. The backlog skill routes product decomposition/intake, PR closeout, and repository checkpoint capture into focused references, preserving native GitHub authority and upstream Superpowers sequencing. Project-specific verification and approval remain external inputs.

**Tech Stack:** Markdown skills/references, JSON checkpoint examples, Git, authenticated `gh`, native GitHub Issues/Projects/PRs, and native harness skill discovery. No project runtime or package manager.

**Spec:** `docs/superpowers-backplane/specs/2026-10-11-fdau-github-governance-design.md`, approved 2026-10-11; criteria D1–D8.

**Work-item binding:** [Issue #31](https://github.com/tvproductions/superpowers-backplane/issues/31), consumed `updatedAt` **`2026-10-12T00:53:44Z`**. Created through `gh` after the operator explicitly authorized creation. Full 15-field native intake confirmed OPEN, native type Feature, exactly one `backplane:designing` label, no parent, no children, no native blockers/blocking edges, and no closing PRs. Its body matches the prepared scope and explicitly identifies the spec/plan as local artifacts pending publication. #1/#5 exclude Projects; #9 evaluates deterministic helpers; #19 covers Claude lifecycle, so this is a separate leaf without an invented release assignment. Re-fetch and reconcile before readiness/execution; creation and plan binding do not establish execution selection.

## Global Constraints

- Follow approved D1–D8 and current project rules. Existing issue/body and separate specification design-authority paths both remain valid.
- Remain language-neutral and skills-only. Do not add a runtime, helper engine, package manager, IssueOps, copied upstream files, or a second lifecycle/backlog authority.
- Required dependencies are Git, operational Superpowers, and authenticated `gh` with the needed capabilities. Other tools/skills are optional; no named supplementary bundle is required.
- Backplane owns staying aligned with upstream SP and publishing dated, revision-bound freshness/compatibility evidence that the bundle/adopters consume. The bundle owns complete-stack integration. Local or harness-limited evidence must not be presented as a published universal readiness cue; an older bundle pin is not Backplane's support policy.
- Use `.sp-bp/` for Backplane state. Never write to `.superpowers/`, shipped upstream checkouts/caches, or links into them, including writes through invoked helpers.
- New documentation belongs in `docs/superpowers-backplane/`. Preserve historical paths and the existing handoff skill.
- Preserve unrelated local changes: dependency/handoff records and evidence, the issue #19 draft, and the approved design-work/spec artifacts. Do not absorb them into implementation commits without separate reviewed scope.
- Before each Git mutation, establish the exact authorized repository/worktree boundary. The current root is `U:/repos/agents/superpowers-backplane`; current instructions require that exact root. Do not create/mutate a nested feature worktree until that rule and Superpowers isolation are reconciled by an explicit project override or supported native approach.
- The approved normal interface is Projects with explicit Issues-only compatibility; issue labels/native state remain lifecycle authority. No live Project rollout or issue migration occurs in this implementation slice.
- Read-only probes use invented supplied data and must not touch production issues. Native issue/Project mutation, publication, merge, and release require their own applicable authority.
- Use `superpowers:writing-skills` before changing the skill. Use meaningful RED/GREEN behavioral scenarios; do not add prose-presence tests or temporary-state snapshots.

## Preconditions and Execution Compatibility

1. Re-fetch issue #31's full native contract and reconcile it against the consumed revision above before readiness or execution. Work-item ownership is established; the issue remains designing, not execution-ready.
2. Approve this implementation plan and choose execution approach. For this coupled documentation/skill slice, recommend native execution with a fresh whole-change reviewer, because the three references share one authority contract.
3. Use the native-first linked-worktree procedure below, preserving the current dirty root and the unrelated existing `design/sdd-ecosystem-v1` worktree. No root branch switch, stash, reset, cleanup, or unrelated-file transport is part of this procedure.
4. Use the native file-operation bookkeeping procedure below under an explicit project override of upstream helper invocation. The inspected v7.0.0 `sdd-workspace` hardcodes `.superpowers/sdd`; helpers that call it without a safe explicit output are prohibited. This is a project exception, not an upstream redirection feature.
5. Verify the bookkeeping and checkpoint recovery behavior in disposable filesystem fixtures outside `.superpowers/`, then recheck the actual isolation/path guards at execution entry. A fixture demonstration is not proof that a live worktree has been created, protected, or authorized. If any guard fails, stop that operation and report the exact condition.

These are entry gates, not implementation tasks that may be bypassed to start editing skills. Planning and review themselves require no execution ledger.

### Exact Isolation Procedure and Required Project Override

Use the harness's native `list_worktrees`/`create_worktree` operations when available, as upstream using-git-worktrees requires. On 2026-10-12 UTC the native attachment inventory was empty, while Git registered the dirty root and unrelated `design/sdd-ecosystem-v1`; neither is a reusable issue-31 isolation attachment. Recheck both inventories before execution. A native creation takes the exact recorded source commit as `ref`; its returned path and branch/detached state are recorded rather than forced into a manually chosen path.

Only if native worktree creation is unavailable, the Git fallback branch is `feat/issue-31-governance-bridges` and fallback workspace is `U:/repos/agents/superpowers-backplane/.worktrees/issue-31-governance-bridges`. Require unused names and create from the recorded root with `git worktree add -b feat/issue-31-governance-bridges .worktrees/issue-31-governance-bridges <recorded-source-commit>`. Do not silently substitute the fallback after a pending native operation or an attachment-registration failure; inspect and use the returned workspace or report the precise failure.

The current exact-root Git rule must be explicitly amended for this worktree before Git mutations there. The proposed exception is:

> Before a Git mutation, either `git rev-parse --show-toplevel` resolves exactly to `U:/repos/agents/superpowers-backplane`, or it resolves to the exact issue-31 workspace recorded from the authorized native operation (or named Git fallback), the root's worktree registry contains that exact workspace, its resolved shared Git directory is the root's Git directory, and its branch/detached state matches the recorded execution identity. Otherwise stop. This exception does not authorize another checkout or another worktree. Any branch-state change requires its own authorized finishing operation and identity-record update.

Approval of the implementation plan must expressly include this scoped exception and the bookkeeping exception below; merely authorizing a review or a documentation correction does not enact them. Record the accepted exceptions in project instructions before execution. Do not broaden the rule to arbitrary paths sharing a directory name.

Execution steps:

1. From the root, record HEAD, branch, `git status --porcelain -uall`, all registered worktrees, and SHA-256 of every currently modified/untracked project file. Keep this preservation manifest outside the protected namespaces. Resolve the absolute root Git directory and record the exact source commit.
2. Re-fetch issue #31 and validate its owner/revision. Bind the execution baseline to the recorded root HEAD after inspecting any required upstream divergence; do not pull or merge automatically.
3. Reinspect native attachments and reuse only an attachment already proven to belong to issue #31 at the correct source. Otherwise, after creation is authorized and the root boundary confirmed, invoke native `create_worktree` with `allowAsync=true` and `ref=<recorded-source-commit>`, retain its operation ID, and use `get_worktree_creation_status` to obtain completion before using its returned `workspaceRoot`. Obtain filesystem access if that path is outside the current writable roots. Record the actual canonical path, shared Git directory, source HEAD, and branch/detached state. Do not create a second worktree while the native operation is pending. For the fallback only, verify `.worktrees/` is ignored and the explicit destination/branch are unused before the command above. All later worktree mutations require the exception's exact identity checks; unprovable aliases or ownership stop execution.
4. Copy only the reviewed issue-31 planning artifacts and the explicitly accepted project-rule delta into the new worktree. The allowlist is the approved spec, this implementation plan, the issue-creation record, the frozen probe contract, and the plan-correction verification receipt, all under `docs/superpowers-backplane/`. Preserve their byte hashes. Never copy root `.superpowers/`, root ephemeral `.sp-bp/`, issue #19 files, dependency records, handoffs, or unrelated evidence. Apply the accepted AGENTS delta as a scoped patch, not a wholesale copy of unrelated edits.
5. Ensure the active harness discovers the unchanged upstream skills from their existing authoritative source and the candidate Backplane skills from the isolated checkout. Do not create an upstream installation or write to existing discovery junction targets. If discovery cannot be isolated, stop before behavioral probes and report the exact source conflict.
6. Before any `.sp-bp/work/` write in the isolated checkout, add only `.sp-bp/work/` to its `.gitignore` and confirm `.sp-bp/state.md` and `.sp-bp/github-state.json` are not ignored. Include this narrow configuration change in the reviewed implementation scope.
7. Recompare the original root's preservation manifest and the unrelated worktree identities. The root must remain on its original branch with original artifact bytes; only the new registered worktree/branch is expected to appear. Keep both original and feature worktrees until the applicable finishing policy permits cleanup.

### Exact Native Bookkeeping Override

Within the verified feature worktree, the only execution workspace for this plan is `.sp-bp/work/2026-10-11-github-governance-bridges-implementation/`. Verify it and its parents are normal directories inside that worktree, not links into `.superpowers/`, upstream, or another workspace. Record baseline digests of the protected contents; use read-only inspection with optional Git locks disabled.

Replace only upstream workspace/brief/report/ledger-helper invocation with native file operations under this path. Preserve Superpowers task ordering, TDD, conflict rulings, fresh verification, review, and finishing semantics. Do not copy or patch upstream scripts. Default execution is native inline with one fresh whole-change reviewer; subagent execution needs a separately reviewed equivalent dispatch/review-package procedure.

`progress.md` starts with the repo-relative implementation-plan path, followed by its SHA-256, the approved spec path/digest, issue URL/consumed revision, branch, and starting HEAD. Each task gets an append-only entry containing task number, state (`started`, `verified`, or `needs-revalidation`), recorded inputs, verification command/probe IDs and results, evidence paths/digests, implementation commit when available, and unresolved review findings. A task becomes verified only after its full completion contract passes; an absent commit stays explicitly absent rather than fabricated. Rulings are separate attributed entries. Task briefs and review packets reference exact artifacts/diffs and live in this same plan workspace.

On resume, compare plan/spec identity and hashes, issue semantics, branch/HEAD, and evidence inputs. Reject a ledger belonging to another plan. Select the first task lacking a currently supported verified record; a mismatched/stale verification reopens that task for revalidation. Never infer completion from a checkbox or a remembered conversation. No `sdd-workspace`, default-output `task-brief`/`review-package`, or helper caller may run under this override.

The disposable verification must show: verified Task 1 plus started Task 2 resumes Task 2; a different plan identity is rejected; changed task input invalidates its recorded verification; and protected namespace digests are unchanged. This demonstrates the local bookkeeping contract, not upstream-native support for another ledger directory.

## Frozen Behavioral Probe Contract

The exact initial prompts, fixture inputs, and criterion-level rubrics are in `2026-10-11-governance-probe-contract.md`, alongside this plan. They are fixed before the first baseline. Record that file's SHA-256, candidate skill/reference hashes, host/session setup, and probe version with each captured response. The scenario report references that immutable contract; it does not silently rewrite it.

Run baseline and candidate arms in separate fresh read-only sessions with identical prompts, fixture data, tool-access constraints, and scoring. Only the skill/reference candidate may differ. Every case includes the supplied issue record shapes, modes, PR variants, checkpoint failures, and namespace constraints needed by later tasks. Current passing behavior remains passing; RED requires an observed failing expectation.

Any added or changed prompt, fixture, or rubric becomes a new explicit probe version. Obtain a fresh baseline against the pre-change skill for that version before comparing with the candidate; do not rescore an old response as if it saw new input. Retain both original records. Tasks 2–4 may implement or score frozen cases, but may not extend the initial comparison in place.

## Checkpoint Acceptance, Publication, and Recovery

This procedure distinguishes an accepted Git checkpoint from provisional worktree files. It makes no claim that two filesystem replacements or a remote GitHub capture are atomic.

1. Resolve the authorized repository/worktree boundary. Require the live output paths to be absent or equal to the last accepted pair; require no staged/unstaged/untracked user changes at those paths. Never overwrite a dirty user-owned pair. Record `prior_checkpoint_commit` and exact prior blobs for both paths, or record that no accepted pair exists.
2. Create a unique candidate directory under the validated `.sp-bp/work/` workspace, containing proposed `state.md`, `github-state.json`, and a transaction receipt. Both accepted output files remain untouched while source capture, revision checks, rendering, and validation run.
3. Validate JSON structure/reference constraints, full declared capture scope/pagination, current input reconciliation, evidence availability, shared capture ID, SHA-256 of the exact JSON bytes named in Markdown, and semantic equality of the readable graph/claims/dispositions with the structured records. Incomplete data may be retained as an explicitly partial diagnostic; it is not accepted as a complete replacement.
4. Record candidate hashes and exact prior state in the receipt, set `phase=prepared`, and recheck both live outputs still match the recorded prior state. On prepublication failure, leave the accepted pair untouched and keep the failed candidate/result for diagnosis.
5. Under separately established commit authority, install the two validated candidate files with native literal-path operations, setting `phase=installing`. Immediately verify both bytes against candidate hashes. Stage exactly the pair, verify the index contains the validated blobs, and commit the pair together as an isolated checkpoint/evidence commit. No unrelated staged files may enter that commit. A hook failure or interruption leaves the transaction unaccepted.
6. The acceptance point is the successfully created Git commit whose tree contains both validated blobs; record its SHA in the external transaction receipt and set `phase=accepted`. Do not hash that storage commit into its own files. Before claiming repository publication, verify the approved integration target contains that commit/pair; local acceptance is not proof of remote integration.
7. Before any new checkpoint operation, inspect unfinished receipts and the index/worktree. If the accepted pair commit exists, verify it and finish the receipt. If publication stopped before acceptance, compare any existing live output and staged blob against the union of recorded prior and candidate hashes. A differing user edit or an unexplained HEAD/index change stops automatic recovery and preserves the files for reconciliation.
8. With verified ownership and applicable recovery authority, restore both output paths and their index entries from `prior_checkpoint_commit`; if there was no prior pair, remove only the two provably transaction-created output paths. Use checked literal paths within the intended repository and do not reset unrelated files/index entries. Verify restored hashes/absence and mark `phase=rolled-back`. After a successfully accepted commit, do not silently roll it back; any reversal is a separately authorized Git operation.

A partial/uncommitted worktree pair is never presented as the accepted portable record. Readers use the validated pair in the recorded accepted commit, or report the missing/mismatched state. The required interruption test stops after installing the JSON file, demonstrates mismatch rejection, and recovers the exact prior pair without touching an unrelated sentinel. Repeat with no prior pair, and with an intervening user edit that must stop automatic recovery. Fixture tests prove file/receipt/reconciliation behavior; actual Git publication still requires its execution-time index/tree verification.

### Correction Verification Evidence

`2026-10-11-governance-plan-corrections-verification.json` records the disposable native-file fixture run at `2026-10-12T01:08:14.5074707Z`: 15/15 assertions passed for ledger resume/wrong-plan/stale-input behavior, candidate pair validation, interrupted replacement rejection, exact prior-byte recovery, preservation of intervening edits, no-prior cleanup, unrelated sentinel preservation, and unchanged protected/upstream file digests. The fixture used no Git mutation or upstream helper. This verifies the local contract examples, not installed-skill conformance, live worktree creation, or Git index/commit publication. Required scoped exceptions and execution approval remain pending.

The initial frozen probe contract digest is `FC23CBAE20160535F0836EFF9920649C0DC78FE50B17AC3082904F2B38710F81`. Reverify it at baseline entry; a changed digest requires version reconciliation before comparing arms.

## File Responsibilities

| File | Responsibility |
| --- | --- |
| `docs/superpowers-backplane/governance.md` | Canonical doctrine, authority, decomposition adequacy, satisfaction, and bridge boundaries. |
| `skills/managing-superpowers-backlog/references/product-decomposition.md` | Planning-result intake, issue-owned sections, native graph reconciliation, and Projects/Issues-only operation. |
| `skills/managing-superpowers-backlog/references/pr-completion.md` | PR contribution and closure intent, integrated evidence, parent coverage, and closeout checkpoints. |
| `skills/managing-superpowers-backlog/references/repository-checkpoint.md` | Concrete versioned format, scope/capture/reconciliation/publication procedure, and offline interpretation. |
| `skills/managing-superpowers-backlog/references/checkpoint-format.md` | Exact `sp-bp-checkpoint/v1` fields/types, reference/coverage constraints, and complete/partial example data. |
| `skills/managing-superpowers-backlog/references/checkpoint-state-template.md` | Readable `.sp-bp/state.md` sections and shared capture-ID/digest relationship. |
| Existing backlog `SKILL.md` and relevant references | Route the new operations and reconcile existing guidance, without copied policy or unrelated installation changes. |
| `tests/scenarios/2026-10-11-github-governance-bridges.md` | Fixed prompts, observable rubrics, D1–D8 mapping, RED/GREEN scores, and limitations. |
| `tests/scenarios/transcripts/2026-10-11-governance-*.md` | Verbatim fresh probe records, identified by case and candidate hashes. |

Runtime checkpoint outputs are `.sp-bp/state.md` and `.sp-bp/github-state.json`; this slice supplies their contract/templates, not a fabricated live repository checkpoint. `.sp-bp/work/` is ephemeral; any approved use must first exclude that subdirectory while keeping the output pair trackable.

## Review Focus

1. Omissions or unsupported children pass a structurally valid decomposition: require every parent obligation's explicit disposition and clear shared responsibility.
2. Evidence names old requirements or a different integration commit: preserve historical results and reject the current satisfaction claim until reconciled.
3. Native issue closure or Project status outruns verification: report the observed state and outstanding obligations; do not manufacture a pass or mutate without authority.
4. Graph pagination/drift, missing evidence, or partial publication yields an apparently complete backup: preserve the accepted pair and disclose capture scope/limitations.
5. A helper, link, test probe, or scratch path writes to `.superpowers/` or shipped upstream: fail the boundary check and stop that path.

---

### Task 1: Establish Negative Controls and Publish the Doctrine

**Files:** Create `docs/superpowers-backplane/governance.md`; create `tests/scenarios/2026-10-11-github-governance-bridges.md`; create baseline transcripts under `tests/scenarios/transcripts/`.

**Interfaces:** Consumes approved D1–D8 and the existing issue/lifecycle/authority contract. Produces the canonical policy and fixed behavioral acceptance cases used by Tasks 2–4.

- [ ] Load writing-skills and its artifact-appropriate test-first workflow; verify all preconditions before any skill implementation. Record candidate file hashes and actual work-item binding.
- [ ] Load the frozen probe contract, record its digest, and map each case/rubric to D1–D8 in the scenario report without modifying prompts, fixtures, or expected outcomes. Include every declared variant in both comparison arms.
- [ ] Run fresh read-only baseline probes using the current backlog skill and supplied fixtures, with no new bridge references. Capture complete responses. Score observed gaps; retain existing passing behavior. If a case already passes, do not fabricate a failure or rewrite its expectation to create RED.
- [ ] Write the doctrine from approved decisions: source ownership, codes/kinds, parent dispositions, current coverage/evidence pointers, satisfaction vocabulary, approval/revision safety, optional complements, and distinct execution/release claims. Use a worked example with both issue-body and cross-cutting-spec design authority.
- [ ] Include the operator's subsequent SP-freshness ownership clarification: Backplane leads SP alignment and publishes immutable scoped compatibility evidence; the bundle consumes that cue and verifies the combined stack; adopters validate their tuple/overrides. Reconcile this clarification against issue #31 before readiness. If it adds a behavioral probe, create a separately versioned freshness case and obtain its own baseline; do not edit the frozen initial seven-case contract or reuse old responses under new expectations.
- [ ] Review each doctrine rule against a spec criterion and a scenario outcome. Check local authority links and `git diff --check`. Record the checkpoint as doctrine delivery, not a claim that installed skill behavior is green. Commit only the reviewed task scope if execution/commit authority permits it.

### Task 2: Bridge Product Planning and Native GitHub Intake

**Files:** Create `references/product-decomposition.md`; modify backlog `SKILL.md`, `references/github-issue-contract.md`, and `references/superpowers-binding.md`; update case scores/transcripts.

**Interfaces:** Consumes Task 1 policy/cases. Produces a routed planning-to-intake operation with canonical `Backplane Record`, `Obligation Dispositions`, and `Coverage and Satisfaction` sections and native relationship reconciliation.

- [ ] Use the frozen decomposition/authority/coverage/Project prompts and their already supplied record shapes/modes. Score existing-match/new/unresolved classification, parent accounting, and the prohibition on implicit creation/selection/readiness; do not extend baseline inputs in place.
- [ ] Write the product reference: consume approved artifact/revision, record bounded outcomes/codes/kinds/owners/criterion references, classify native parent/dependency operations, preserve existing issues, and identify scope/approval conflicts. Require the existing full 15-field intake before interpreting an existing candidate.
- [ ] Describe four Project views and native fields, mirrored Code/Kind/Satisfaction sources, optional status mapping, and explicit Issues-only mode. A failed Project capture in integrated mode is incomplete, not a silent mode switch. Do not require custom organization types.
- [ ] Add named operation routes in the existing skill: `decompose/intake`, `PR closeout`, and `capture checkpoint`. Route to focused references only when requested; keep existing status/selection/transition semantics and authoritative doctrine links. Reconcile examples showing old document paths without relocating historical artifacts.
- [ ] Re-run fresh adequacy, authority-path, coverage-revision, and Project-reconciliation probes with candidate references. Require complete rubric scoring, unchanged native-state expectations for read-only requests, and no invented priority. Record RED-to-GREEN evidence for actual baseline gaps.

### Task 3: Bridge PR Contributions to Satisfaction and Closeout

**Files:** Create `references/pr-completion.md`; modify binding/issue references where they currently describe submission/closure; update `pr-contributions` and `coverage-revision` evidence.

**Interfaces:** Consumes policy, issue coverage/source ownership, and routed closeout operation. Produces a PR contribution/closeout checklist that references exact verification inputs and refreshes downstream projections without inferring success from merge.

- [ ] Use all PR input variants and assertions already fixed in the probe contract: design-only, partial multi-PR delivery, review pending, merge with failed integrated checks, automatic close, fully verified delivery, and a nondefault target. Preserve their baseline identity and score every expected/forbidden claim.
- [ ] Write PR guidance with affected issue/design/plan revisions, contribution criteria, review disposition, verification identity, and explicit closure intent. Use ordinary contribution references while integrated evidence is pending; do not confuse native closing links with neutral references.
- [ ] Define evaluation-index updates in outcome issues, parent-obligation references, Project projection refresh, and backup refresh checkpoints. Preserve historical evidence, separate approved deferral from satisfaction, and distinguish publication of a later checkpoint-only PR from the verified feature commit.
- [ ] Keep fresh project-owned integrated verification and authorized closure under the existing lifecycle; project integration and workspace cleanup rules remain authoritative. Specify reporting/recovery when native closure already occurred, without unrequested reopen or label mutation.
- [ ] Run fresh PR and changed-evidence probes; score every expected/forbidden claim. Inspect final reference consistency with the existing lifecycle, preserving unsupported/unknown results rather than weakening criteria.

### Task 4: Define and Prove the Portable Checkpoint Contract

**Files:** Create checkpoint operation/format/template references; score the frozen `checkpoint-preservation` fixtures and capture candidate transcripts. The narrow `.sp-bp/work/` ignore rule is established at execution entry before any workspace writes, not deferred to this task.

**Interfaces:** Consumes current issue-owned mapping/disposition indices, accepted evidence, native graph, Project mode, and approved closeout policy. Produces the concrete structured/readable contract and capture procedure for the two output files.

- [ ] Define exact field names/types for the sections named in the approved spec: format/capture identity and times/mode/status; repository/Project identities; source commit; graph scope/pagination/completeness; native source records/revisions; design/plan/approval references; dispositions; coverage; satisfaction/evidence; and limitations. Use string tracker identities, arrays for many-to-many relationships, explicit null/unknown values where unavailable, and the approved result vocabulary. Document references and uniqueness constraints rather than leaving arbitrary untyped objects.
- [ ] Supply a complete invented JSON example and limited/partial variants. Supply the readable template with capture identity, structured-file digest, hierarchy, obligations, evidence, release targets, and limitations. Keep immutable source evidence separate from the checkpoint's eventual storage commit.
- [ ] Specify `gh` source queries and full pagination, required-input revision rechecks, semantic reconciliation, and evidence availability checks. Use the active host's native JSON/file tools; do not introduce a mandatory language, copy source-manager caches, or execute an unaudited helper. A permission/network/schema failure is incomplete capture.
- [ ] Implement the exact staging/validation/receipt/index/commit/recovery procedure in the Checkpoint Acceptance section as operational guidance. Preserve its acceptance point, dirty-output guards, prior blob recovery, no-prior case, and user-edit stop rule. Require actual equality between readable claims and structured data, not merely matching filenames.
- [ ] Exercise complete capture, omitted page, changed source revision, missing remote evidence, contradictory Project projection, wrong capture ID/digest, interruption between file writes, and offline resume/reconciliation. Validate example JSON using available native tooling and inspect reference/semantic constraints. Capture expected failures and valid cases without production queries/mutations being fabricated.
- [ ] Run fresh checkpoint/namespace behavioral probes, with and without supplementary tools and Project access. Require no writes to forbidden paths, preservation of unavailable-evidence limitations, and no stale-state replay. Record exactly which behavior was simulated versus executed.

### Task 5: Review, Regression Verification, and PR Handoff

**Files:** Modify only this slice's doctrine, references, skill routes, allowed configuration, and scenario/transcript evidence; update README with a concise governance entry link.

**Interfaces:** Consumes Task 1–4 artifacts and evidence. Produces reviewed delivery scope, verification summary, and PR-ready issue/criterion mapping; live submission/merge/closure remains authorized separately.

- [ ] Run structural checks on both existing skills: valid YAML frontmatter, exact names, descriptions beginning with `Use when`, and existing direct references. Scan changed published artifacts for unresolved placeholders and verify no copied upstream content or mandatory runtime/tool bundle was introduced. Use `git diff --check` for formatting, not as behavioral proof.
- [ ] Re-run all seven new fixed behavioral cases in fresh read-only sessions against the same candidate hashes, then all five existing backlog conformance checks with their exact mapped prompts/rubrics. Reuse unchanged results only when their input identities are proven; missing captures or unscored required expectations remain UNKNOWN.
- [ ] Inspect D1–D8 coverage and actual checkpoint examples; retain only meaningful tests. Compare source-of-truth records, lifecycle semantics, Projects mode, existing handoff behavior, `.superpowers/` snapshot, and upstream status before/after. Report proof limitations explicitly.
- [ ] Obtain the chosen independent review at the approved checkpoint, address substantive findings, and rerun the first affected verification. Do not use passing prose-presence checks as satisfaction evidence.
- [ ] Inspect final changes for unrelated dependency/handoff/issue #19 work. Prepare a PR description linking the actual selected issue, approved spec, criterion contributions, and verification, with neutral contribution references until integrated checks justify closure.
- [ ] Follow Superpowers finishing with the approved isolation/bookkeeping override. Preserve the workspace during PR feedback. After authorized integration, establish fresh evidence at the integrated commit, then reconcile satisfaction/issue/Project/checkpoint closeout under the approved scope. No release is part of this plan.

## Self-Review and Handoff

Coverage: Tasks 1–2 own D1/D2/D4/D5; Tasks 2–3 own D3/D6; Task 4 owns D7; entry gates and Tasks 4–5 own D8. Every Review Focus failure class has an explicit probe in its owning task. New references have one purpose and share the canonical doctrine; no new workflow skill or runtime is assumed.

The operator approved this implementation plan, native inline execution with fresh whole-change review, and the two explicit exceptions on 2026-10-11. Live identity, preservation, and source-reconciliation guards still apply. Issue #31 was created through `gh` only after explicit operator authorization and its full native state/revision verified before binding this plan. No implementation, branch/worktree mutation, commit, publication, or prohibited-directory write occurred during planning or issue intake.
