# GitHub-Aligned Product Governance and Superpowers Bridges

**Status:** Approved by the operator on 2026-10-11 with the instruction "spec approved." The proposed defaults and policy in this document are approved as the design for subsequent implementation planning. This approval does not execute implementation, mutate GitHub, authorize publication, or waive the execution-workspace compatibility gate.

**Design-work brief:** [FDAU-informed governance](../plans/2026-10-11-fdau-github-governance-design.md).

**Builder check:** A fresh read-only reviewer on 2026-10-11 asked where current decomposition dispositions, coverage mappings, and accepted satisfaction records are maintained before capture. The author clarified the issue-owned sections and immutable evidence roles below, marked that convention as a proposal, and requested a focused recheck. The reviewer then reported "nothing important left." This is a design-completeness check, not operator approval, behavioral verification, or resolution of the execution-workspace compatibility gate.

## Intent

Superpowers Backplane connects the development discipline of upstream Superpowers to durable product organization and delivery evidence in GitHub. A reader should be able to follow a capability through its coded outcomes, approved behavior, bounded work, PR contributions, and satisfaction evidence without reconstructing a conversation or consulting a competing backlog.

Use GitHub's native structures where their semantics fit. Preserve a useful account in the repository so loss of GitHub access or Project membership does not erase the decomposition or the basis of satisfaction claims. Keep the companion skills-only and language-neutral.

## Decisions and Author Proposals

The operator established these boundaries: FDAU-style deliverable decomposition; native GitHub alignment; required `gh`; Backplane ownership of decomposition and satisfaction coordination; reuse of Superpowers planning, execution, review, and PR workflows; optional complementary tools without reverse dependencies; no new session-state handoff work; `.sp-bp/` for Backplane working state; and no writes whatsoever to `.superpowers/` or shipped Superpowers contents.

The author proposed the following concrete defaults; the operator approved them with this specification:

| Choice | Proposed default | Reason |
| --- | --- | --- |
| Projects | Normal integrated workspace, with an explicit Issues-only compatibility mode | Use native linkage without excluding installations governed by the existing optional-Projects policy. |
| Product codes | Project-owned mnemonic family/outcome codes, recorded on issues | Recognizable product identity survives release retargeting and Project removal. |
| Requirement authority | Existing approved issue-body/specification paths | Avoid a new mandatory PRD or a second acceptance authority. |
| Coverage/disposition ownership | Issue-owned sections linking to approved design and immutable evidence | Keep the checkpoint from becoming the only live traceability ledger. |
| Repository checkpoint | Two tracked files: `.sp-bp/state.md` and `.sp-bp/github-state.json` | Combine a readable record with captured source data instead of three manual mirrors. |
| Local ephemeral state | `.sp-bp/work/`, excluded from source control before use | Separate temporary execution support from tracked product checkpoints. |
| Doctrine home | `docs/superpowers-backplane/governance.md`, referenced by bridge guidance | One policy home rather than repeated normative copies. |
| Release placement | A separately scoped enhancement; no implicit expansion of the current v0.1 arc | Existing host acceptance and publication gates retain their scope. |

These originated as author choices and were accepted in the operator's specification approval. Later implementation planning must bind to an explicitly selected work item and its current revision.

## Goals and Exclusions

The design must support a coded product hierarchy, adequate decomposition, explicit many-to-many coverage, issue-bound implementation, PR contribution tracking, evidence-based satisfaction, and portable repository checkpoints. It must expose useful Project views while retaining an Issues-only path.

Do not introduce a runtime, service, database, dependency manager, IssueOps system, custom Git workflow, or copied local backlog engine. Do not copy gzkit or prescribe FDAU's domain letters. Do not create a general interviewer, session-handoff system, or alternate Superpowers lifecycle. Complementary tools may provide decisions, findings, or evidence, but do not become dependencies or approval authorities.

This document authorizes no installation, issue/Project mutation, commit, push, merge, tag, or release. Operational authority comes from the applicable request or standing project workflow and must be established before those actions.

## Superpowers Alignment and Freshness Ownership

The operator subsequently established that Backplane leads the stack's Superpowers alignment: Backplane must endeavor to remain current with upstream Superpowers, and the bundle and adopters should use Backplane's published freshness/compatibility evidence as their cue. This is a direct companion dependency, not interchangeable supporting tooling.

- Superpowers owns its released workflow and interfaces. Backplane owns the SP-to-Backplane contract, follows the stable upstream channel by default, reviews workflow/interface changes, and verifies its bridges against immutable upstream revisions. Edge-channel selection remains explicit.
- Backplane's freshness record distinguishes latest stable upstream at the checked time, the exact SP revision evaluated, the exact Backplane revision and relevant project overrides evaluated, the harness/capability scope, verification results, and unresolved incompatibilities. Classify the newest stable target as verified compatible, untested, or incompatible with evidence and a reason; do not equate an installed version or an older passing baseline with currentness.
- Publish the record with the Backplane revision it describes. Local/uncommitted evidence may guide this development session but is not a published cue for the bundle or adopters. Evidence for one harness or an unmodified workflow does not establish another harness or the no-write execution override.
- The bundle follows that published contract when selecting Superpowers and Backplane, and owns end-to-end integration of its complete selected stack. It must not silently turn its older bundle pin into Backplane's own support policy. A retained older tuple needs a recorded integration reason and revisit condition.
- Adopters verify the chosen tuple and their project overrides. A Backplane freshness cue identifies the evaluated target; it does not authorize an automatic installation change or replace adopter acceptance.
- Resolve and retain immutable source identities through review, integration testing, and adoption. Freshness is a dated statement about those identities, not a continuously true moving alias. Bundle records cite the precise published Backplane evidence rather than racing independent declarations of its SP support.

This policy defines evidence ownership and consumption, not a new updater, scheduler, runtime, or mandatory supplementary plugin. The existing Superpowers update/preflight contract remains the operational mechanism until an approved bounded change replaces it.

## Doctrine and Authority

| Concern | Authority | Interpretation |
| --- | --- | --- |
| Product purpose, enduring constraints, approvers | Approved project instructions and product/architecture documents | Existing PRD-equivalent material is valid; no universal new document requirement. |
| Work identity, current scope, acceptance criteria, relationships, lifecycle | GitHub issue and native relationships | Repository plus issue number/URL is the tracker identity. |
| Approved design | Complete approved issue body for bounded work, or approved specification for cross-cutting work | Preserve the current Backplane design-authority decision. |
| Execution | Current approved Superpowers implementation plan | Bound to one executable issue and its consumed revision. |
| Verification and satisfaction | Project-owned evidence and acceptance authority | A label, checkbox, closure, or merge is not independent proof. |
| Product/delivery presentation | GitHub Project views | Project status is not a second mandatory lifecycle. |
| Portable record | Dated repository checkpoint | A historical account of captured authority and evidence, not a mutable offline backlog. |

Approved specifications refine behavior without silently replacing issue-owned scope or acceptance. If governing statements disagree, report the exact conflict and reconcile with the project approver before execution; do not choose the convenient source. Approval evidence must identify the approver, accepted artifact/revision, and scope of approval.

FDAU's organization resembles a deliverable-oriented work breakdown structure augmented with dependencies, workflow, verification, and external boundaries. Its documentation does not establish formal PMI/NASA/Kanban adoption or a complete requirements verification matrix. Borrow the distinctions, not its machinery or provenance claims.

## Product Records and Codes

Use issues for capability groups, deliverable outcomes, reconciliation gates, and tracked external work where an actual owner exists. A small feature may itself be the executable outcome; do not require another issue merely to represent a layer. Grouping issues are not executable implementation leaves.

Each participating issue exposes a `Backplane Record` section with its project-owned code, record kind, and governing authority/coverage references. Code and kind are canonical on the issue; title prefixes and Project fields may display them. Native parentage and blocking relationships remain canonical and are not duplicated as independently editable body fields.

The project supplies its code legend. An illustrative family `INSTALL1` and outcome `INSTALL1.1` are mnemonic identifiers, not mandated syntax, priority, dates, or release versions. Codes must be unique within the declared project namespace, retain issue URLs, and remain stable on release retargeting. On reclassification or reparenting, retain existing identity or make an explicitly approved alias migration; never infer live parentage solely from the code's spelling.

Kinds distinguish capability grouping, outcome, reconciliation gate, and external boundary. Native issue types classify available work categories; they do not need to encode every Backplane kind. Use the record kind when an organization lacks custom types. Existing `backplane:*` lifecycle rules remain unchanged unless a separately approved amendment specifies otherwise.

An external boundary states another owner's prerequisite or acceptance condition. It does not create authority to execute their work. If the owner has an issue, link it and use native dependencies where available; otherwise retain an explicit unresolved boundary with source and owner, rather than inventing a resolved issue.

## Decomposition Adequacy

For each approved parent obligation, record one or more bounded child outcomes, existing eligible satisfaction evidence, or an explicitly approved exclusion/deferral. A disposition identifies the obligation, governing revision, responsible owner, and approval/evidence reference.

Reject unsupported omissions, unrelated additions, and ambiguous duplicated responsibility. Shared coverage is allowed when each contribution and the owner of the combined result are explicit. Excluded/deferred work remains inspectable and does not count as delivered or satisfied. A changed parent scope triggers reconciliation of affected children and prior evidence.

Maintain the current parent-obligation mapping and scope dispositions in the parent issue's `Obligation Dispositions` section. Each entry identifies its governing obligation/revision, linked child contributions or existing evidence, and any exclusion/deferral approval. Child relationships themselves remain native. A parent summary references child evaluation records rather than maintaining a competing copy of their verdicts.

Dependencies establish readiness, not priority. Parentage establishes decomposition, not execution order or satisfaction. An issue closed as not planned does not establish its intended outcome; downstream work needs an approved alternative, removal of the obligation, or other acceptable evidence under project policy.

## Requirements, Criteria, and Satisfaction

A requirement reference identifies approved behavior using an artifact/issue identity, stable statement or criterion key, and consumed revision. Use project-owned requirement IDs where they exist. Otherwise introduce stable criterion keys within the approved design authority; do not use changing line numbers or checkbox positions as durable identity.

Coverage records connect requirement references to outcome issues and acceptance criteria. They may be many-to-many and must say what each contribution covers. Do not use a tree edge as evidence that every requirement is covered.

Maintain each outcome's current criterion-to-requirement coverage in its issue's `Coverage and Satisfaction` section. This section also points to the latest accepted evaluation for each criterion and records unresolved contributions or stale-input findings. The accepted evaluation itself is immutable project-owned verification/review evidence, preferably committed at the project's existing evidence location, identifying the inputs and acceptance authority. An issue is the current index and claim surface, not a replacement for that evidence. Historical evaluations remain at their original identities.

The parent and outcome sections are authoritative for current mappings and dispositions; governing documents authorize the obligations and amendments; accepted evidence establishes the evaluated result. Project satisfaction displays and checkpoint records derive from these sources. If the current issue claim conflicts with its evidence or governing revision, report the discrepancy and evaluate the current satisfaction as unsupported until reconciled. A checkpoint must not become the only authoritative live coverage/satisfaction record. This ownership convention was proposed by the author and accepted in the specification approval.

A satisfaction record includes:

- Requirement/criterion reference and approved revision.
- Outcome and contribution issue/PR identities.
- Verification method, observed result, and scope/limitations.
- Verified integration commit or other project-owned delivery identity.
- Evidence artifact identity and availability, including an immutable revision or digest where appropriate.
- Required review/acceptance disposition and its source.
- Remaining contributions, failures, exclusions/deferrals, or changed inputs.

Report `SATISFIED`, `UNSATISFIED`, or `UNKNOWN` for an evaluated obligation. Scope dispositions such as deferred/excluded are separate annotations, not success states. An unexecuted or unverifiable check is `UNKNOWN`, not a pass. Feature satisfaction requires every applicable obligation to be satisfied, with exclusions/deferrals separately approved and disclosed.

Changed governing behavior or relevant implementation invalidates a current satisfaction claim until affected evidence is reconciled. Preserve the historical record against its original inputs. Editorial changes may retain evidence only after an explicit semantic reconciliation; timestamp changes alone do not prove a semantic change.

## GitHub Projects and Other Facilities

Projects are the proposed normal working interface. Use issue-backed items for approved product/delivery records; Project-only drafts may capture preliminary ideas but are not approved executable work. A Project item references its issue rather than creating a second product identity.

Provide product/decomposition, execution, satisfaction, and release-target views. Use native Title, issue type where available, labels, assignees, parent issue, sub-issue progress, milestones, and linked PR context. Optional mirrored columns are `Code`, `Kind`, and `Satisfaction`. Code/kind mirror issue records; satisfaction mirrors evaluated evidence. Define their refresh source and checkpoint rather than implying automatic semantic synchronization.

The current lifecycle is represented by issue labels and native state. A Project Status field is optional presentation, with an explicit mapping; do not require its value to decide execution eligibility. Closed-sub-issue progress counts closures, not verified obligations. A milestone expresses a target grouping, not publication approval.

An Issues-only compatibility mode retains the same code, coverage, evidence, and lifecycle contract. Declare the mode in the checkpoint. If the integrated mode cannot capture a Project, report that capture as incomplete; do not silently claim Issues-only mode was selected or a complete Project backup exists.

Use issue forms/templates for intake structure where useful, Discussions for nonbinding deliberation, repository review/rules controls for integration policy, and Releases for separately approved publication. Adopt each only where it serves a defined role; do not require all GitHub features for every project. Use `gh` and capability/permission checks appropriate to the target scope.

## Superpowers–Backplane–GitHub Workflow

1. Read existing project authority and GitHub context. Reuse existing issues; do not infer selection from list order.
2. Product/design planning clarifies behavior and produces adequate decomposition. Optional questioning/audit tools may contribute inspectable results.
3. Present the decomposition against its approved authority. An authorized intake operation reconciles it with existing issues and creates/updates missing records and native relationships within the allowed scope.
4. Identify a bounded executable leaf for planning and prepare/approve its Superpowers implementation plan, recording issue URL, consumed revision, design authority, acceptance criteria, and project verification seams. Then validate every execution-eligibility gate, including the approved plan and resolved blockers, and select eligible work for execution. Choosing a planning target does not change its lifecycle or make it execution-ready.
5. Follow Superpowers isolation, execution, test discipline, review, verification, and finishing, subject to project rules and the namespace boundary below.
6. Use PRs as the normal integration path under project policy. Reconcile contributions and outstanding obligations throughout review.
7. After integration, establish fresh project-owned evidence, reconcile satisfaction and native issue/Project state, and refresh the portable checkpoint.
8. Consider release inclusion/publication separately under the project's release authority.

Already captured bounded work may start with its approved issue body; it does not need a fresh product-planning exercise. The numbered sequence describes bridge boundaries, not a demand to repeat approved design. Planning, intake, selection, submission, merge, and closure are different operations; authorization for one does not automatically authorize all later operations.

## PR Contributions and Completion

Each delivery PR identifies its affected issues, approved design/plan references, criterion contributions, verification result, review disposition, and intended closure behavior. Design/policy PRs identify the decisions they establish without implying that future implementation is delivered. Multiple PRs may contribute to one outcome; one coherent PR may contribute to several outcomes with explicit coverage.

Use native issue/PR links where their semantics fit. Distinguish ordinary contribution references from links that trigger automatic closure. The proposed default is contribution references during partial delivery or when integrated evidence is pending, followed by authorized issue closure after integrated verification. If a project deliberately uses automatic closure, retain the native relationship but reconcile any premature close or failed post-merge result through its authorized workflow. Do not equate observed closed state with satisfaction.

PR readiness, accepted review, merge, integrated verification, requirement satisfaction, issue completion, parent/feature satisfaction, and release authorization remain distinct. Final integration evidence names the verified commit. A subsequent checkpoint-only PR references that result; it does not claim its own future merge was already verified. If a later change affects delivered behavior, revalidate the affected obligations.

Keep the implementation workspace for review fixes under Superpowers/host ownership rules. Backplane does not independently remove branches/worktrees or bypass integration policy. Project-owned checks determine the verification commands; no runtime or test framework is assumed.

## Repository Checkpoint and Preservation

Retain approved product intent in the project's existing PRD, architecture, or equivalent documents. Do not add a mandatory new PRD or three manually maintained mirrors. The proposed backup pair is tracked in Git:

| Path | Role |
| --- | --- |
| `.sp-bp/state.md` | Readable product hierarchy, coverage/satisfaction tables, release-target summary, dispositions, unresolved work, and capture limitations. |
| `.sp-bp/github-state.json` | Structured capture and evaluated-claim records supporting the readable account. |

The structured document has a versioned format identity `sp-bp-checkpoint/v1`. Its sections record capture identity/time/mode/status; repository and Project identities; source Git commit; selected scope and capture completeness; issue bodies/revisions/labels/types/owners/milestones; native parent/dependency/PR relationships; Project item identities and relevant field values; approved design/plan references; parent-obligation dispositions; criterion coverage; satisfaction records; and evidence/approval content or explicit availability limitations.

Enumerate the selected graph to completion, including pagination and excluded/external scope. Record observation start/end times and recheck source revisions used to assemble the capture. A changed relevant input makes the candidate stale until recaptured/reconciled; `updatedAt` alone is not a transaction guarantee. Do not claim an atomic GitHub snapshot.

The capture must preserve human-readable outcomes, criterion wording and governing revisions, not just URLs. Retain repo-relative evidence references where the evidence is committed. When supporting approval/evidence exists only remotely, preserve the claim-relevant content through an authorized capture or mark it unavailable. Partial/private/redacted material must retain its limitation; never claim full reconstructability from missing evidence.

Both files share a capture identifier; the readable file names the structured file's content digest. Compare the readable obligations, graph, satisfaction results, and limitations against the structured capture before accepting the pair. Retain the last valid pair if capture/reconciliation fails; report the failed candidate without partially replacing one accepted file. A later implementation plan must define the concrete capture/publication procedure and its meaningful verification scenarios; no helper runtime is mandated here.

The implementer refreshes the pair after approved decomposition intake, material scope/coverage changes, verified outcome closeout, and release review. Per-task edits and ordinary discussion do not require refresh. Existing records are historical until refreshed; Git history preserves earlier checkpoints. A checkpoint written for a design PR records proposed scope as proposed, not as approved intake.

Record the verified source commit separately from the eventual commit storing the pair; avoid self-referential hashes. A checkpoint/evidence-only follow-up PR may preserve post-merge evidence. Until that follow-up is integrated, report the local capture and committed source evidence separately rather than claiming the repository's published backup is current.

Offline, the pair explains captured state and supporting claims; live eligibility and mutation remain unverified. Project removal does not erase issue identity or local captured relationships. After access returns, reconcile source revisions, graph, and claims before replaying any intended update. Never blindly restore stale local state into GitHub.

## Filesystem and Upstream Compatibility

New Backplane documentation belongs under `docs/superpowers-backplane/`; tracked product checkpoints and optional local work state belong under `.sp-bp/`. Ephemeral `.sp-bp/work/` must be excluded before use; the two checkpoint files remain trackable. Preserve historical `docs/superpowers/` authority links.

No writes whatsoever to `.superpowers/`, including writes caused by invoked scripts. Shipped Superpowers checkouts/plugin caches and discovery links into them are read-only for this work. Do not patch, relocate, or copy upstream implementation to bypass the boundary.

The inspected Superpowers v7.0.0 helper `skills/subagent-driven-development/scripts/sdd-workspace` hardcodes `<repo>/.superpowers/sdd`. This is an observed compatibility gap, not a resolved execution path. Do not invoke that helper or its callers when they would write there. Before implementation, demonstrate a supported alternative that preserves required execution bookkeeping outside the reserved directory. If none exists, return the precise incompatibility to the operator; do not weaken the boundary or claim standard execution is ready. Drafting/reviewing this specification requires no execution ledger.

## Worked Example

The following codes and tracker identifiers are invented, not proposed changes to live Backplane issues.

`INSTALL1` groups installation capability. `INSTALL1.1` is an independently deliverable setup outcome with two approved obligations: adopt authoritative upstream without replacing an existing valid installation, and verify required host discovery. A third platform is explicitly deferred by the project approver and does not count as delivered.

One design PR establishes the setup contract. A package PR contributes implementation for authoritative adoption; a verification PR contributes discovery evidence. Neither partial contribution closes the outcome. The outcome issue links both criteria to their governing revisions, PRs, integrated commit, and accepted review. The Project displays the coded hierarchy and native parent relationship.

After the integrated target passes both project-owned checks, the authorized closeout records the two satisfaction results, closes the outcome under existing lifecycle rules, reconciles Project display, and refreshes the backup pair. The capability summary discloses the deferred platform. Another repository may plan against the approved contract earlier, but adoption of delivered artifacts and its own acceptance remain separate conditions.

If discovery subsequently fails or the criterion changes, preserve the old evidence against its old inputs and mark the current claim unsupported until reconciled. If GitHub is unavailable, the last committed checkpoint still explains what was recorded without asserting current live eligibility.

## Acceptance and Design Validation

| Criterion | Required demonstration |
| --- | --- |
| D1: Authority and identity | Both approved design-authority paths work; code and issue identity survive release retargeting and Project removal. |
| D2: Adequate decomposition | Omitted obligations, unrelated child scope, and ambiguous ownership fail; explicit shared coverage, eligible existing evidence, and approved dispositions remain distinguishable. |
| D3: Coverage and satisfaction | Many-to-many contributions are explicit; changed requirements, unavailable evidence, and failed checks cannot become satisfied through labels or closure. |
| D4: GitHub alignment | Native hierarchy/dependencies/PR links and useful Project views express the model; Issues-only mode preserves the same contract with honest capture limitations. |
| D5: Superpowers bridge | Product planning yields decomposition; intake reconciles issues; one selected leaf binds to its implementation plan; upstream sequencing remains intact. |
| D6: PR completion | Design-only and partial PRs do not establish delivery; integration-pending and premature automatic closure report outstanding evidence; verified closeout preserves exact input identities. |
| D7: Portable record | The two files reconstruct captured outcomes/coverage/claims offline; pagination, drift, missing evidence, mismatched pair, and failed capture prevent a complete/current backup claim. |
| D8: Boundaries | Optional tools may be absent; no foreign lifecycle/runtime is imported; no operation writes to `.superpowers/` or shipped upstream; execution incompatibility is explicit. |

Use invented paper scenarios first, plus a read-only mapping of an existing Backplane capability. Record inputs, expected actions, actual design interpretation, evidence, and PASS/FAIL/UNKNOWN for each criterion. Paper walkthroughs establish design consistency, not installed-skill conformance. Later skill implementation requires fresh behavioral evidence under the repository's writing-skills workflow.

## Scope of Later Implementation

After approval, create a bounded, issue-linked implementation plan for the doctrine/reference and necessary Superpowers–Backplane–GitHub bridges. Prefer extending current backlog guidance where responsibility is coherent; create a separate skill only when a distinct operation warrants it. The approved specification, selected work item, exact artifact/schema decisions, verification scenarios, and filesystem compatibility constrain that plan.

This approval does not amend the current release arc, complete any host leaf, remove the existing handoff skill, change live Projects or issues, or claim the execution compatibility gap is solved.

## Evidence and References

- Backplane bootstrap authority: `docs/superpowers/specs/2026-08-16-superpowers-backplane-bootstrap-design.md` and current backlog references.
- FDAU sources: `docs/project/backlog-method.md`, `docs/project/backlog-governance-model.md`, `ROADMAP.md`, and `BACKLOG.md` in the read-only `xplane-fdau` checkout at `94109c1373953898ce780bc7a94c659d3c6bdc08`, observed on 2026-10-11. Described policy is not independent certification of that implementation.
- Superpowers sources: active-discovered brainstorming, writing-plans, worktree, branch-finishing, and execution guidance at v7.0.0 / `bb92a77741419a4ab5f06e711a283343f1ada0c3`; the workspace helper was inspected, not invoked.
- [Projects and linked work](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects).
- [Parent issue and sub-issue progress](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-parent-issue-and-sub-issue-progress-fields).
- [Issue dependencies](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies).
- [Issue types](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/managing-issue-types-in-an-organization).
- [PR links and automatic closure](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue).
- [Milestones](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones).

Recheck host/API capabilities and permissions before implementation. GitHub observations and this draft are dated design evidence, not an assurance that an adopter's environment is operational.
