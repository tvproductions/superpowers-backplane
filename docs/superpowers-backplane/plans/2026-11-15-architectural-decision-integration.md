# Architectural Decision Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Preserve and enforce applicable architectural decision references at existing Backplane checkpoints, qualify the behavior and publish the independently scoped contribution.

**Architecture:** Add one focused backlog reference and calls from existing checkpoints. Project ADRs retain decision authority; existing Authority/Evidence/Evaluation records preserve references without extending checkpoint/v1 or adding a service.

**Tech Stack:** Markdown skills/references, Git/gh, native model sessions, existing locked Python 3.14 development checks and minimal Node adapter regressions. No new runtime, dependency or hook is introduced by ADR integration.

**Spec:** [Owning integration design](../specs/2026-11-15-architectural-decision-integration-design.md), including the remote GZKit H5 naming precedent at `8208381d149b8b8704bd012849332ed3a1f2fb38`.

**Plan status:** APPROVED for Native execution; actual main-conversation approval is captured below. Re-read the native issue/entry gates before starting. The maintainer said “proceed with that design” after design/naming review. The [actual approval capture](../../decisions/approvals/ADR-0001-001-approval.md) preserves that direction separately from the explicit “Approve Backplane ADR-0001 edition 1 as written”. The [Current ADR](../../decisions/ADR-0001-001-reference-decisions-through-existing-checkpoints.md) retains the approved original choice and links [exact reviewed bytes](../../decisions/approvals/ADR-0001-001-reviewed.txt) at `335bd2575eeaae92ce094582cd11dccf18f37b41`, SHA-256 `5a39dcb0db8553af4a30d4acdbd57461c9a62d9a2f72da285caa57ceb0630d7b`. Later naming commentary remains design context. Validate this capture and applicability without requesting duplicate architectural approval; this plan does not supply or broaden it.

**Owner work binding:** [Backplane #37](https://github.com/tvproductions/superpowers-backplane/issues/37), intake revision
`2026-11-15T18:53:19Z`. All fifteen native fields were fetched and preserved;
state OPEN, exactly one `backplane:designing` label, no parent/children or native
blockers observed. Body/acceptance match the approved bounded intake payload.
Issue type is recorded as observed, not invented. Native work remains designing
until re-read/reconciliation and entry gates are satisfied; no active/complete
state follows from this capture alone. The proposed intake body remains at
`docs/superpowers-backplane/specs/2026-11-15-architectural-decision-integration-intake.md`.


## Global Constraints

- Consume project ADR policy/workflow; gz-skills owns its portable procedure/template. Do not require gz-skills or starter adoption from unrelated Backplane consumers.
- Preserve checkpoint/v1 exact fields/enums, six native lifecycle labels, independent record histories, consumer tools and existing `.superpowers/`/upstream write prohibitions.
- Use only verified registered worktrees and contained ignored `.sp-bp/work/adr-integration/` fixtures; do not change original dirty checkout work, installed caches or user profiles.
- Stable new-collection identity is `ADR-[0-9]{4,}`; edition filename is `ADR-[0-9]{4,}-[0-9]{3,}-<slug>.md`, slug `[a-z0-9-]+`. Preserve suitable existing conventions; do not introduce a stricter parser or bulk rename.
- Missing/conflicting approval stops dependent work only. Approved decision reuse and independent already-authorized work proceed without duplicate ADRs or redundant permission.
- Proposed finite release is published 0.2.0 -> 0.3.0, minor new behavior; reconcile any valid pending target. No new major PRD is required. Exclude sidecar/commit schemas, doctrine transfer and historical OpenCode/pilot completion.
- Use locked uv-managed exact Python 3.14, minimum-only uv executable compatibility, Ruff check/format, ty and unittest. Preserve thresholds and the four routine hooks. No pytest.
- Current/latest versions are not supplied by this plan: complete the official-source maintenance inventory/migration before owner release and freeze the actual qualified tuple afterward.

## Review Focus

- Ready/indexed work with an approved plan but no exact ADR approval must stop dependent actions; test at design/plan, start, active work and closeout (T1/T3/T4).
- Approval for a different edition or missing reviewed bytes must remain a gap; test alongside genuine approved-decision continuation (T3/T4).
- Checkpoint references must use correct existing typed collections without an `adr` enum or implied approval; demonstrate complete, unavailable and stale captures (T3/T4).
- Unrelated consumers and disabled Backplane must retain their own workflow/tool authority; test a language-neutral active consumer and preserve separate disabled-path responsibility (T3/T4).
- A released source label, installed cache or old transcript must not replace actual loaded-source/action evidence; test immutable hosted-source discovery and exact tuple applicability (T4/T6).

---

### T1: Establish owner authority and freeze the behavioral probe contract

**Files:** Modify this plan's owner binding after intake; preserve coordinator-owned approval evidence/approved decision under `docs/decisions/`; create `tests/scenarios/2026-11-15-adr-integration-probe-contract.md`, `tests/scenarios/2026-11-15-adr-integration-baseline.md` and supporting `tests/scenarios/transcripts/2026-11-15-adr-integration/` records after execution is authorized.

**Interfaces:** Consumes actual design/ADR approval interactions, reviewed proposal bytes and existing backlog contracts. Produces immutable authority anchors and frozen fixture/rubric/hash identities reused unchanged for baseline/candidate comparisons. Execute the baseline once after T2 fixes the tooling tuple and before T3 authors product instructions.

- [ ] Verify root/shared Git identity, HEAD, dirty/staged scope, current instructions and live remote main; preserve unrelated work. Read the design, Current ADR, actual approval capture and exact preserved bytes linked above; verify the reviewed hash and naming reconciliation. Reuse the actual approved choice without a duplicate approval request; surface any material discrepancy rather than silently approving changed text.
- [ ] Read the coordinator's actual owner leaf using `gh issue view <actual-url> --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url`. Require `Objective`, `Bounded Scope` with `Allowed`/`Out of Scope`, `Acceptance Criteria`, `Verification Seams`, `Superpowers Artifacts`; record all actual authority revisions in this plan.
- [ ] Reconcile plan approval/current issue semantics, native blockers, explicit selection and exactly-one lifecycle label before ready/start. Use existing guarded transitions, not a new ADR label or an assumed issue number. Missing readiness permits independent preparatory work only.
- [ ] Freeze a probe contract containing two paired action cases at each design/plan, start, active execution, review/closeout and checkpoint boundary: missing approval/wrong edition versus retrievable approved decision. Include green tests, ready/index claims, mid-work independent task, no implied publication and unchanged decision under release/requirement regrouping. Name each assertion and expected permitted/prohibited action.
- [ ] Prepare invented disposable repository inputs and staged human responses only inside contained ignored scratch; record canonical fixture root, origin, starting SHA and protected sentinel/source hashes. No real issue mutations are authorized by fixture instructions.
- [ ] Prepare the pre-authorship native baseline invocation against the existing unmodified skill/reference bundle; run it after T2 freezes the tooling tuple. Record help/version-supported child configuration, actual loaded sources, full prompts/actions/responses and each verdict. A baseline pass is a pass; report it honestly. Missing required reference is structural absence, not a fabricated behavioral failure. Preserve genuine observed failures without forcing a model to fail.
- [ ] Preserve baseline evidence and frozen contract in a reviewed normal-hook commit when commit authority applies; leave product reference files unchanged in this task.

### T2: Complete owner tooling/source maintenance and observe the baseline

**Files:** As required by verified maintenance: `.python-version`, `pyproject.toml`, `uv.lock`, `.github/workflows/check.yml`, `SUPERPOWERS.md`, native dependency declarations/catalogs and owning guidance; create `tests/scenarios/2026-11-15-adr-release-tooling.md` with dated receipt data.

**Interfaces:** Consumes current owner engineering/release policy and scoped migration authority. Produces a verified exact runtime/tool/SP tuple, rollback identities and explicit incompatibility exceptions/UNKNOWNs for T4/T6.

- [ ] Use the discovered owner-appropriate `gzs-update-dependencies` maintenance procedure; read official live releases for every declared dev/hygiene package, Python approved family patch, uv executable, pre-commit/CI execution and pinned Actions, plus independently installed SP/gz-skills and deferred SP-BP roles as applicable. Latest previously observed candidates include uv 0.13.8, Ruff 0.17.5, ty 0.0.104, Cosmic Ray 8.9.0 and Lizard 1.26.0; recheck them and all other inventory entries rather than treating these observations as current pins.
- [ ] Reconcile owner source-policy applicability. Migrate the authorized scope to current stable families using owning tools and compatibility verification, retaining Python-family/product decisions. Retained older versions need demonstrated incompatibility, owner and dated revisit; absence of proof is UNKNOWN. Do not weaken lint/complexity/coverage/mutation requirements to make migration pass.
- [ ] Update affected metadata/lock/CI/dependency records together, preserve current activation and user defaults, and use isolated profile scope for required native tests. A normal-profile plugin reinstall/update is not incidental maintenance authority; record unsupported scope instead of global fallback.
- [ ] Run the existing locked engineering gate and affected changed-tool compatibility/deeper checks on the actual pinned interpreter. Preserve structured Cosmic Ray worker/test outcomes rather than accepting exit zero alone. Record candidate/source provenance, failures, fixes and remaining gaps; commit only reviewed maintenance scope with normal hooks.
- [ ] With the maintained SP/workflow/host tuple frozen, execute the T1 baseline against unchanged product instructions and fixture/rubric bytes before T3 authorship. Preserve all actual actions/verdicts. Running after maintenance avoids replaying an obsolete tooling tuple; a later relevant input change invalidates only affected evidence.

### T3: Add the focused integration and own-project binding

**Files:** Create `skills/managing-superpowers-backlog/references/architectural-decisions.md` and `docs/engineering/architectural-decisions.md`; modify backlog `SKILL.md`, `references/superpowers-binding.md`, `references/github-issue-contract.md`, `references/pr-completion.md`, `references/repository-checkpoint.md`, `docs/superpowers-backplane/governance.md` and `AGENTS.md`. Preserve `checkpoint-format.md` unchanged.

**Interfaces:** Consumes approved T1 authorities and baseline plus T2 actual tuple. Produces discoverable focused instructions, exact reference mapping and Backplane's own policy/workflow binding for candidate tests.

- [ ] Read/use the skill-authoring workflow before modifying skills. From the frozen T1 assertions, implement only the missing checkpoint behavior in the focused reference; do not paste a generic portable procedure/template.
- [ ] Route consequential design/planning/start/transitions/review/closeout/capture through the reference. Preserve ordinary bounded approved work, existing native issue/plan revision reconciliation, blocked resume targets and independent tasks. Require actual edition/content/approval context; no label, spec/plan assent, capture/index, green checks, merge or release creates approval.
- [ ] Implement the exact mapping: consuming issue/spec/plan Authority `content` names decision ID/edition/immutable locator/applicable constraint; `Evidence(kind=other)` preserves reviewed ADR bytes; `Authority(kind=approval)` names approver/reviewed edition/accepted scope/source context through existing `approval_ids`; `Evidence(kind=approval)` preserves actual interaction. Evaluations reference appropriate evidence IDs; `review_approval_ids` remains actual review approval, distinct from ADR approval. Never introduce `Authority.kind=adr`, relabel an ADR specification, or use a cross-collection ID in the wrong field.
- [ ] Bind this repository to the immutable starter policy at `f42e6f186f062493c09fc2c2dc935e9a64310e33`, its actual approved decision collection and the selected readable portable workflow source/revision. Record any later policy reconciliation and exact final workflow tuple. Consumers remain governed by their project policies; an available policy copy proves neither installed skill discovery nor behavior.
- [ ] During the real work cite the captured actual ADR-0001 decision, approved edition and applicable constraints. Keep an attributable internal-use note for later alignment review; invented fixture approval must not replace it.
- [ ] Run shipped resource/reference/native metadata checks through `uv run --locked python -m unittest discover -s tests -p test_*.py -v` and `git diff --check`; rerun frozen candidate action controls. Expected: required references load, no broken links/schema changes, all asserted actions comply. Fix actual failures and repeat affected controls, preserving each result. Commit the reviewed focused source/binding scope with normal hooks.

### T4: Qualify active integration, record preservation and genuine internal use

**Files:** Create `tests/scenarios/2026-11-15-adr-integration.md`, `.json`, `tests/scenarios/fixtures/adr-integration/checkpoint-complete.json` and `checkpoint-state.md`; preserve candidate transcripts beneath the T1 transcript directory. Disposable execution/validation sources remain under `.sp-bp/work/adr-integration/`, with supporting used sources archived in tracked evidence when necessary.

**Interfaces:** Consumes unchanged T1 cases/rubrics, exact T2/T3 sources and actual approved ADR. Produces assertion-to-evidence mapping, source-linked internal-use alignment review and bounded host-scope acceptance.

- [ ] Inspect current native CLI help/version and supported profile isolation; use fresh native sessions loading actual Backplane plus independent SP and the selected policy/workflow. Record explicit expected versus observed sources and duplicate-source/activation scope. Do not substitute an evaluator prompt quoting the desired answers for skill discovery.
- [ ] Execute every frozen stop/continue pair through the actual checkpoints. Before staged approval assert dependent file/tool action count is zero while an authorized independent task produces its intended change. After exact fixture approval assert already-authorized dependent work proceeds and no duplicate ADR/redundant approval is demanded. Review controls must identify contradictory implementation despite green checks; lifecycle/index controls must not fabricate approval. Preserve before/after file hashes and tool actions.
- [ ] Derive a complete invented checkpoint pair from `skills/managing-superpowers-backlog/references/checkpoint-complete-example.json` and the current exact field contract, adding only supported mapped records. Assert exact field sets/enums/types, ID resolution, correct approval/evidence collection ownership, edition/content/source agreement, exact JSON digest and readable semantics. Follow `tests/scenarios/2026-10-13-checkpoint-file-git-exercise.md` and `tests/scenarios/2026-10-13-checkpoint-native-edge-contract.md` against this fixture in scratch, retaining actual current observations and source identities. `uv run --locked python -m json.tool tests/scenarios/fixtures/adr-integration/checkpoint-complete.json` proves syntax only; the listed semantic assertions and actual file/Git observations must also pass. No new generic shipped validator is required.
- [ ] Repeat with missing approval content, wrong edition, changed source revision and intervening output edit. Expected: required approval remains unavailable/unreconciled, capture partial/stale as appropriate, last accepted pair/user edits preserved, no approval inferred from capture acceptance. Demonstrate all existing pair/commit/source/delivery/storage distinctions; changes cannot extend checkpoint/v1 or its recovery semantics.
- [ ] Test a language-neutral consuming fixture without mandatory gz-skills/starter adoption. Record that disabled Backplane leaves project/portable workflow responsibility intact; coordinate the separately executed starter disabled lite/heavy checks without claiming they qualify active Backplane.
- [ ] Link the exact shared B01-B16 workflow/template evaluation and explain each reused result's applicable inputs. Expand affected cases after shared-behavior changes/discrepancies; preserve failures/reruns and require all applicable assertions PASS. No averaging away failures, inferred host scope or schema-only behavioral acceptance.
- [ ] Have a fresh reviewer inspect real implementation against actual approved ADR-0001 and cited constraints; preserve genuine internal use plus this alignment review separately from invented controls. Resolve material findings with affected verification and record actual tested host/model/version/settings or UNKNOWN.
- [ ] Commit reviewed qualification/internal-use evidence with normal hooks. Keep discovery, behavioral compliance, engineering checks and release readiness as separately stated results.

### T5: Reconcile finite release scope, versions and integration acceptance

**Files:** Modify `package.json`, `plugin.json`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `pyproject.toml`, owning-tool-generated `uv.lock`, `CHANGELOG.md`, `HANDOFF.md`; create `docs/superpowers-backplane/releases/2026-11-15-v0.3.0.md`. Update owner work/current evidence pointers only under applicable authority.

**Interfaces:** Consumes approved scope, current maintenance/qualification/internal-use results and fresh review. Produces an integrated accepted candidate and finite release-scope accounting; no tag is moved.

- [ ] Execute the source-policy version decision: published 0.2.0 -> 0.3.0 for this capability unless a valid pending target must be reused. Record governing owner work, completed/remaining/deferred scope, compatibility impact and acceptance evidence. Preserve unrelated draft doctrines and historical adoption obligations. No major PRD is required for this minor.
- [ ] Update all five version mirrors together and regenerate uv lock through uv; inspect the exact resolution delta and reject unrelated dependency churn. Reconcile metadata/resource/native catalog versions and changelog. No source-only metadata validation proves installed behavior.
- [ ] Run the full current gate below and applicable release/deeper evidence; obtain whole-change fresh review. Resolve findings, repeat affected checks and reconcile owner issue/plan `updatedAt` before submission/integration. Integrated satisfaction and any authorized closure follow existing closeout; publication and another outcome's acceptance stay separate.
- [ ] Commit reviewed scope with ordinary hooks; integrate/push through the owner-authorized branch strategy without overwriting remote work. Verify exact remote SHA and observe all configured Linux/macOS/Windows CI jobs for that SHA. Preserve tested delivery identity separately from later evidence storage; unknown CI is not full verification.

### T6: Verify immutable native source and publish the owner contribution

**Files:** Update T4/T5 existing evidence/release records with actual results; create bounded `tests/scenarios/2026-11-15-v0.3.0-publication.md` and `.json` after publication. Do not create an endless evidence-only commit chain.

**Interfaces:** Consumes accepted integrated SHA, release authority, exact CI and supported native channels. Produces an immutable published Backplane contribution and inspectable provenance for starter exact-combination qualification.

- [ ] Reconcile live official release/tool freshness, source policy and final tuple before publication. If changed relevant inputs invalidate acceptance, requalify affected behavior rather than reusing an older label/transcript. Recheck actual publication authority already given; do not invent new permissions or ask again solely because this stage is later.
- [ ] Confirm native channels actually support the reviewed immutable source in their current documented interfaces. Use isolated profiles for verified published commit installation/fresh discovery; preserve normal profile/user/cache state. Record actual installed source hashes and both Backplane skill plus independent SP discovery, then execute bounded active stop/continue controls. No npm/PyPI upload, global activation, or untested OpenCode/Claude/platform support is implied by a GitHub tag.
- [ ] After exact candidate gates/CI pass and tag absence is observed, create a new annotated `v0.3.0` at the accepted full SHA, push normally and publish the GitHub release through direct git/gh. Follow current owner release procedure; do not move historical tags or claim simultaneous component versions.
- [ ] Query tag/release/source archives and native tag-to-commit resolution, verify actual immutable arrival/non-draft/non-prerelease state and release notes' exact source/CI/limitations. Refresh the isolated installation to the released identity through its supported channel and verify matching loaded bytes; retain commit-tested scope when a host cannot consume tags directly. Unsupported channels remain UNKNOWN, not successful installation.
- [ ] Record actual source, delivery, evaluation/storage, release and native identities; reconcile final local/remote SHA and remaining worktree. Link this owner design/approval, actual ADR provenance/internal use, delivery/release and qualification evidence to the coordinating starter receipt. Starter 0.10.0 acceptance still needs the other publisher/lite/heavy/exact-stack evidence and its separate propagation decision.

## Commands and completion gate

Run from the verified owner repository/registered worktree with actual supported
uv provenance and pinned managed Python. Sync only the intended owned environment
when state requires it; do not replace tools merely for differing from CI.

```text
uv sync --locked --all-groups
uv lock --check
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked ty check
uv run --locked python -m unittest discover -s tests -p test_*.py -v
uv run --locked pre-commit run --all-files
node --test tests/opencode-adapter.test.mjs
git diff --check
```

Expected: applicable checks PASS, native adapter regressions PASS, unchanged
four-hook scope and complete separately evaluated behavioral/internal-use/native
evidence. No Python product package exists: build/install-package proof remains
reasoned N/A unless implementation introduces one, which this plan does not.
Missing mandatory release evidence blocks the corresponding claim/publication;
retain honest UNKNOWN/UNSATISFIED and evidenced exceptions without weakening rules.

## Self-review and execution handoff

Coverage: T1 binds real approvals/native work and captures the honest baseline;
T2 owns current compatible tooling; T3 implements each named checkpoint/mapping
and owner binding; T4 qualifies actions/capture/independence/internal use; T5 owns
finite version/integration accounting; T6 owns immutable source/publication.
Every Review Focus condition has a targeted T3/T4/T6 evidence seam.

Current gaps: approval-capture validation/alignment, actual owner issue/revision,
plan review/approval, current tool/portable workflow tuple and all
unperformed execution/qualification/release results. No gap is silently waived.

Recommend **Native** execution after main-conversation plan review: the cohesive
references share one existing record contract, so one implementer can preserve
their consistency, with fresh whole-change review and native behavioral sessions.
This recommendation neither selects execution nor marks the plan approved.

## Execution approval — November 15, 2026

The maintainer approved this plan in the main conversation, responding
“approve, are we sure "native" is the best term?” to the review of the immutable
plan at `18ee7b53b7e900aa31b687a1de098aec138a152e`. Subsequent discussion confirmed retaining Superpowers'
**Native** label rather than contradicting its owning skill; the maintainer
then directed “so, we'll just move on”. Native means the controller implements
in this session, with one fresh independent final review. No duplicate plan or
architectural approval is requested. Original reviewed plan bytes remain in
that immutable Git history; this section is administrative execution capture.
