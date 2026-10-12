# FDAU-Informed GitHub Governance Design Plan

> **For agentic workers:** This is an approved design-work brief, not a Superpowers implementation plan. The resulting specification is now approved; use `superpowers:writing-plans` for subsequent issue-bound implementation planning. The task lists below organize design research and validation; they do not authorize skill implementation or GitHub mutations.
> **Current operator direction:** The operator approved the design-work plan, challenged the reversed spec/plan ordering, and subsequently approved the written specification on 2026-10-11. Preserve the approved scope and continue with implementation planning, not execution.

**Status:** Approved for design work on 2026-10-11. The resulting [specification](../specs/2026-10-11-fdau-github-governance-design.md) was written, builder-checked, reviewed with the operator, and explicitly approved on 2026-10-11. A subsequent issue-bound implementation plan remains unwritten; this brief is not that implementation plan.

**Goal:** Establish Backplane's documented doctrine and policy for aligning a coded, deliverable-oriented product hierarchy, bounded execution, and evidence with GitHub's native facilities, informed by FDAU and fitted to upstream Superpowers.

**Architecture:** GitHub owns work identity, hierarchy, dependencies, ownership metadata, lifecycle, and delivery relationships. Approved design authority defines behavior and constraints: a complete, human-approved issue body for bounded work, or a reviewed Superpowers specification where warranted by the existing authority model. Plans authorize bounded execution; verification and review records support satisfaction claims. FDAU supplies design precedent, not a runtime dependency or a copied state engine.

**Tech Stack:** Markdown skills and references, Git, GitHub CLI (`gh`), native GitHub Issues and Projects, and independently installed Superpowers.

**Spec:** Governing background: `docs/superpowers/specs/2026-08-16-superpowers-backplane-bootstrap-design.md` and `docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md`. The new hybrid design is an output of this plan, not an existing approved specification. The operator accepted the first-pass mapping as a basis for planning on 2026-10-11.

## Operator Direction and Design Doctrine

On 2026-10-11 the operator clarified that Backplane is the place to cement these understandings in documentation and doctrine/policy. The goal is the greatest useful alignment with GitHub Issues and GitHub's other facilities, rather than designing a parallel local management system and attaching issue links afterward.

- Start with GitHub's native representations and use each where its semantics fit. Document remaining gaps explicitly before proposing additional records or conventions.
- Preserve the distinction between product organization and execution: a coded capability or outcome says what is being delivered; an issue provides durable tracker identity; a specification defines approved behavior; evidence supports satisfaction; a release records publication.
- Evaluate a coded, deliverable-oriented hierarchy as the organizing model. FDAU resembles a work breakdown structure augmented with dependencies, workflow, verification, and external boundaries. This is a structural comparison, not a claim that FDAU formally adopted PMI, NASA, Kanban, or a complete requirements-engineering standard.
- Native issue parentage expresses decomposition. Blocking relationships express prerequisites. Requirement coverage and satisfaction may be many-to-many and must not be inferred from parentage alone.
- Evaluate Projects as a useful product and execution interface, including hierarchy, codes, feature views, and release views. Optional means the underlying doctrine remains operable without Projects; it does not mean Projects should be ignored or reduced to an incidental board.
- Keep stable codes inspectable on underlying issues if adopted. A Project field may display the code, but must not become the sole required identity source. Define the owner and reconciliation rule for any mirrored value.
- Backplane supplies portable conventions and evidence gates; consuming projects choose their capability families and domain mnemonics. Do not prescribe FDAU's alphabet globally.
- Distinguish doctrine, normative policy, operational skill guidance, and worked examples. Each rule needs one authoritative home, with references from other surfaces rather than competing copies.

This direction is established by the operator. Specific fields, code syntax, taxonomy, lifecycle amendments, and implementation remain proposals requiring design resolution.

### Superpowers–Backplane–GitHub Bridges and Repository Preservation

The operator further clarified that any skills created here should bridge Superpowers, Backplane, and GitHub. Implementers must expect `gh` to be installed and use Backplane to understand the product-continuity work surrounding Superpowers. Additional portable tools and skills are optional complements, not prerequisites for those bridges.

- Treat GitHub as a first-class dependency and Projects as an intended working interface for the proposed design, taking advantage of its links to issues and other native structures. Resolve the exact Projects requirement and migration from the existing optional-Projects policy explicitly; do not silently change current policy.
- Design bridge operations around approved planning/decomposition intake, issue-bound execution context, and reconciliation of verification/satisfaction evidence. Do not recreate Superpowers' interviewing, planning, execution, or review skills here.
- Evaluate repository-local PRD, roadmap, and backlog material for preservation and implementer usability. The operator proposed these documents but raised their maintenance cost; three separate manually maintained mirrors are not an approved requirement.
- Assign each retained document a distinct role and authority. The proposed distinction is approved product intent in a PRD or existing equivalent, and dated roadmap/backlog projections of GitHub-owned work state. Define how decomposition, coverage, satisfaction evidence, and source revisions survive loss of access or Project membership; URLs alone are insufficient preservation.
- Define the implementer's reconciliation obligations at meaningful workflow checkpoints. Specify the responsible actor, source records, refresh method, checkpoint triggers, and stale/offline behavior for every retained projection. Keep live GitHub state distinct from a historical repository snapshot.
- Do not make an optional skill bundle or interviewing technique a prerequisite for creating or refreshing these records. No reverse dependency from a supporting tool is required.
- Session-state handoffs are outside this design. The operator instructed that existing supporting capabilities already cover them and no additional handoff work is needed. Portable product/decomposition/satisfaction records are distinct from session-state handoffs; their preservation remains in scope.

### Optional Complementary Capabilities

Describe capabilities and their interfaces rather than prescribing a named skill bundle. Useful complements include intent clarification, intent-to-plan audits, delivered-behavior audits, independent change review, project-owned quality-gate execution, root-cause debugging, dependency/hygiene maintenance, architecture analysis, and instruction-context maintenance. Existing session-state handoff tools remain outside this design's work scope.

Each complement must yield an inspectable result, such as settled decisions, findings, or verification evidence. It must respect the project's authority and the active Superpowers/Backplane workflow. It cannot independently change lifecycle, declare satisfaction, override approval, or establish release authority. Do not import another framework's ledger, taxonomy, lifecycle, or required toolchain as a consequence of using one supporting capability.

### Agreed Decomposition and Workflow Distinctions

During the plan review on 2026-10-11, the operator affirmed the FDAU-style decomposition and GitHub alignment and accepted the following distinctions and adequacy rule:

- Product/design planning defines the intended outcomes and produces decomposition. Backplane reconciles that decomposition into existing or proposed GitHub work items. Each selected executable issue then receives its own implementation plan bound to that issue and consumed revision.
- Every obligation in the approved parent scope must map to bounded child work, existing satisfaction evidence, or an explicitly approved exclusion or deferral. Unsupported omissions and additional work outside the parent scope are findings.
- Shared coverage is permitted. Overlap requires explicit responsibility and coverage links; ambiguous duplicate ownership is a finding.
- Approved exclusion or deferral is a scope disposition, not satisfaction evidence. Preserve its rationale and approval; do not count deferred or excluded obligations as delivered.
- An approved issue body and a separate approved specification remain valid design-authority paths under the existing Backplane policy. Requirements' exact representation remains open.

### Superpowers PR Integration and Feature Completion

The operator directed Backplane to make maximum useful use of Superpowers' PR workflow for its own workflow and feature-completion management. Superpowers already supports isolated workspaces, review, branch finishing, and PR creation; Backplane supplies the product-continuity connections around those operations.

- Adopt PR-based integration as the proposed normal delivery path, subject to consuming-project integration policy and authorization. Reuse Superpowers' workspace, execution, review, and branch-finishing guidance rather than implementing a competing Git workflow.
- Connect each delivery PR to its bounded work-item scope, approved design authority and consumed revision, implementation plan, acceptance obligations, verification results, and review disposition. Preserve native GitHub issue/PR relationships where available.
- Distinguish PRs that approve design or policy from PRs that deliver implementation. A design PR may advance planning or decomposition without satisfying future delivery obligations; references to an issue must not imply intended closure.
- Permit one outcome to require multiple PRs and one coherent PR to contribute to multiple outcomes. Require explicit coverage and closure intent rather than a rigid one-issue/one-PR rule. Explain how contributions accumulate into complete satisfaction without relying on a PR count.
- Keep PR readiness, accepted review, merge/integration, integrated verification, requirement satisfaction, issue completion, feature completion, and release authorization distinct. PR creation or merge alone is not a satisfaction decision.
- Define the bridge between native automatic closure and Backplane's evidence-gated completion rules. If GitHub closes a linked issue before required integrated verification has been established, report and reconcile that state under the authorized workflow rather than treating closure as proof or claiming the issue remained open.
- Retain the implementation workspace while review changes are pending, following Superpowers and host ownership rules. Cleanup follows verified integration and the applicable finishing workflow; Backplane does not independently delete workspaces or branches.
- Define the implementer's PR closeout duties: reconcile acceptance/evidence links, native issue and Project records, parent coverage, and the portable repository checkpoint at a named stage. Avoid claiming that a pre-merge checkpoint already proves the eventual integrated result.

## Planning-to-Backplane Boundary

The operator established this ownership direction on 2026-10-11: planning must produce decomposition that can enter Backplane. Backplane may use a reviewed, attributed adaptation of Matt Pocock's grilling technique as a supporting planning tool; that tool does not need to know about this project or implement its workflow.

- Superpowers remains the required design/execution workflow. Grilling supports intent clarification and decision exploration within that workflow; it does not create a second approval lifecycle.
- Backplane owns the decomposition and satisfaction contract, the mapping to native GitHub records, and reconciliation with approved design authority.
- The supporting tool's publisher owns its portable interviewing implementation. It need not know Backplane's taxonomy, labels, GitHub schema, state transitions, or release policy. No reverse dependency or coordinated release requirement is introduced.
- Backplane consumes an inspectable planning result rather than another plugin's internal state. The proposed result contains settled decisions and their authority, unresolved questions, bounded outcomes, ownership boundaries, explicit prerequisites, proposed acceptance criteria, and coverage links. Task 2 must resolve the minimum contract and record format.
- Product/design planning closeout must either produce a reconciled decomposition ready for an authorized Backplane intake operation or identify the exact unresolved decisions that prevent it. A design document alone is not evidence that the work has been decomposed or entered into the backlog. A per-issue implementation plan follows issue identity and approved design authority; it must not stand in for product decomposition or create its own backlog.
- Intake must preserve existing issues where they already represent the outcomes. Record which proposed outcomes match existing work, need new records, or remain unresolved; retain traceability to the consumed planning revision.
- Requirement satisfaction still requires project-owned verification evidence and acceptance authority. A completed interview, approved decomposition, created issue, or closed parent does not establish satisfaction.
- GitHub mutation remains a separately authorized operation. Preparing decomposition does not implicitly create issues, change labels or dependencies, or select work.
- The workflow must remain usable when no grilling skill is installed. Backplane specifies the expected planning/decomposition result, not a mandatory external skill invocation.

Availability rule: a proposed interviewing adaptation is not a shipped capability. Verify the selected tool's actual availability and review exact source, attribution, license, and behavior before any later reuse. A personal installation in one environment does not establish adopter availability or create a Backplane dependency.

## Global Constraints

- Remain a companion fitted to upstream Superpowers, language-neutral and skills-only. Add no Python baseline, runtime, package manager, or deterministic helper in this design slice.
- Never write anything to `.superpowers/`, directly or through invoked scripts/helpers. Never write Backplane artifacts into shipped Superpowers checkouts, plugin caches, or links resolving into them. Use `docs/superpowers-backplane/` for new documents and the operator-selected `.sp-bp/` for any later approved local working state. Existing `docs/superpowers/` documents are historical project-owned authorities, not installation contents. If an upstream operation requires writing to `.superpowers/`, reconcile a supported alternative before invoking it; do not patch shipped upstream files.
- Use `gh` for GitHub operations. Native issue hierarchy, dependencies, types where available, labels, linked PRs, and closure relationships remain the work-management surfaces.
- Do not require GitHub Projects or introduce IssueOps. Projects and saved Views may present authoritative records; they must not hold required workflow state.
- Do not copy gzkit. Do not copy FDAU's Markdown backlog engine, domain IDs, lifecycle vocabulary, parser, or Python tooling.
- Preserve project rules above portable workflow guidance. Use Superpowers directly; additional portable tooling is optional. Do not onboard an external starter bundle into Backplane.
- Keep dependency direction one-way: Backplane may consume portable planning/interview results; supporting tools need not depend on or understand Backplane. Do not require a proposed grilling adaptation to operate Backplane.
- Do not create a second mutable local roadmap/backlog authority for GitHub-owned fields.
- Preserve existing issue identities and separate outcome identity from target release.
- Preserve existing lifecycle labels until an approved design explicitly changes their contract. Readiness, selection, satisfaction, integration, and release are distinct claims.
- This discussion is separate from issue #19. Do not execute its draft plan or absorb its scope into this work.
- Do not design, implement, or review a general session-state handoff system in this slice. Do not remove or redesign the existing `managing-superpowers-handoffs` skill or its approved contract here; that is not needed to establish the product/workflow bridges. External handoff tools do not become core dependencies.
- Preserve pre-existing dependency records, evidence, and handoffs. Write only the new design artifacts within the authorized scope.
- GitHub changes, commits, pushes, and release publication are not authorized by this draft. Before any later Git mutation, verify `git rev-parse --show-toplevel` resolves exactly to `U:/repos/agents/superpowers-backplane`.

## First-Pass Mapping

These are proposals for evaluation, not approved schema or lifecycle changes.

| Concern | Proposed home | Constraint |
| --- | --- | --- |
| Capability or feature family | Coded parent GitHub issue | Grouping does not authorize execution of every child; codes are independent of release targets. |
| Independently deliverable outcome | Coded child issue with scope and acceptance criteria | One bounded execution plan per selected outcome; a simple feature may itself be the execution leaf. |
| Prerequisite | Native blocking relationship | A closed predecessor is not automatically evidence of successful completion. |
| Owner | Repository boundary and assignee | Assignment does not confer another project's decision authority. |
| Execution state | Existing Backplane lifecycle labels | Label transitions remain evidence-gated. |
| Target release | GitHub milestone | Retargeting must not change outcome identity or establish release approval. |
| Approved behavior and constraints | Approved issue body or reviewed Superpowers specification, as appropriate | Preserve both existing design-authority paths; requirement placement and reference format remain undecided. |
| Satisfaction evidence | Linked verification, accepted review, and integrated PR | An issue checkbox or PR merge alone does not prove every criterion. |
| Views and Projects | Product, hierarchy, execution, and release views over authoritative records | Evaluate their useful affordances explicitly; the workflow must also operate without them. |

## Open Decisions

1. **Product structure and requirement authority:** First distinguish capability families, features/outcomes, specified requirements, and delivery work. Evaluate which share an issue and which need separate records, using concrete examples rather than forcing an early choice between all requirements in specifications and all requirements in issues. Specifications owning approved statements remains an author recommendation, not an operator decision.
2. **Requirement references and change control:** Decide stable identifiers or anchors, consumed revisions, and what changes invalidate prior satisfaction evidence. Do not invent an ID scheme before the authority decision.
3. **Coverage and satisfaction:** Decide the minimum relationship from requirement to outcome to criterion to evidence, including one requirement delivered by multiple issues and one issue satisfying multiple requirements.
4. **Cross-project and release boundaries:** Decide how planning handoffs, delivered-artifact adoption, external acceptance, cross-child reconciliation, and publication approval are represented separately.
5. **Adoption scope and doctrine home:** Propose a reusable Backplane contract with a bounded self-hosting example, and identify the authoritative documentation/reference home for its policy. Decide whether it belongs in the current release arc or later work; do not silently expand v0.1.
6. **Projects and portable repository records:** Resolve Projects' intended requirement versus the existing optional policy, which PRD/roadmap/backlog documents add distinct value, and how implementers preserve and refresh decomposition/satisfaction records without maintaining competing mutable backlogs.
7. **PR closeout and integration evidence:** Define contribution/closure links, accumulated satisfaction across PRs, the integrated-verification checkpoint, automatic-closure reconciliation, and how the portable record receives final results. Preserve project integration policy and the Superpowers finishing boundary.

## Review Focus

1. A requirement changes after linked work closes: preserve historical evidence but do not claim that evidence satisfies the changed requirement without reconciliation.
2. A predecessor closes as not planned: do not treat its acceptance criteria as delivered or release downstream execution automatically.
3. A parent or milestone reaches full closure while evidence is missing: report unmet satisfaction or release gates rather than declaring completion.
4. A downstream project may plan against an approved design before runtime delivery: distinguish planning readiness from artifact adoption and external acceptance.
5. Multiple issues share requirements, or a view disagrees with native issue state: preserve explicit coverage and one authoritative source without forcing a misleading tree or duplicate status.
6. Structurally valid children omit a parent obligation, duplicate responsibility ambiguously, or introduce unrelated work: report decomposition findings; distinguish approved exclusions/deferrals from satisfied obligations.
7. A PR merges or automatically closes an issue before integrated verification is available, or delivers only part of a feature: preserve the observed native state, identify outstanding obligations, and reconcile through the authorized workflow without claiming satisfaction from closure alone.

---

### Task 1: Establish the Source and Authority Inventory

**Files:**
- Create: `docs/superpowers-backplane/specs/2026-10-11-fdau-github-governance-design.md` as an explicitly unapproved source/authority draft with alternatives and unresolved choices recorded. Task 2 resolves those choices and revises this draft.

**Interfaces:**
- Consumes: current Backplane rules, bootstrap/adoption specifications, FDAU's actual model, and official GitHub documentation.
- Produces: attributed source inventory and ownership matrix separating observed behavior from proposed additions.

- [ ] Read FDAU's `docs/project/backlog-method.md`, `docs/project/backlog-governance-model.md`, and relevant roadmap/backlog examples from a read-only reference checkout. Record its inspected revision and distinguish declared rules from behavior independently verified in this work.
- [ ] Recheck official documentation and available `gh` capabilities for issue types, hierarchy, dependencies, assignees, labels, milestones, saved Views, Projects, and PR closure relationships. Also assess issue forms/templates, Discussions, repository rules/review controls, and Releases where they could own intake, deliberation, integration, or publication. For each facility, record useful role, semantic limits, availability/scope, and adopt/defer reason; do not require every facility merely because it exists.
- [ ] Check the complete Backplane issue inventory for an existing owner of this design scope. Before interpreting a candidate work item, retrieve the full native intake contract. Leave work-item ownership unresolved if no current issue covers it; create nothing during discovery.
- [ ] Write the authority matrix and distinguish portable FDAU principles from project-specific implementation choices. Verify that each mutable field has one owner and every proposed relationship has a defined meaning. Explain the WBS resemblance and its limits, without inventing formal-method provenance.

### Task 2: Define Requirements, Coverage, and Evidence Semantics

**Files:**
- Modify: `docs/superpowers-backplane/specs/2026-10-11-fdau-github-governance-design.md`.

**Interfaces:**
- Consumes: Task 1's authority inventory, draft alternatives, existing approved authority model, and the operator's agreed decomposition/workflow distinctions. Requirement-placement decisions are resolved within this task.
- Produces: proposed record/reference contract and explicit satisfaction/change-control rules.

- [ ] Walk one capability family through its coded outcomes, specifications, and bounded delivery issues before resolving requirement authority with the operator. Record operator decisions separately from author recommendations.
- [ ] Define how the coded hierarchy appears in Issues and Projects: native parentage, code location, family/node-kind classification, linked specifications, views, and any mirrored fields. Specify uniqueness, stable identity under release retargeting, and reconciliation; do not claim GitHub enforces custom code rules automatically.
- [ ] Define stable requirement references, approved revisions, issue coverage links, acceptance criteria, and evidence references. Address many-to-many coverage without using issue parentage as a substitute for satisfaction.
- [ ] Define the planning-to-decomposition intake contract: approved source revision, bounded outcomes, parentage, ownership, prerequisites, acceptance obligations, coverage links, unresolved decisions, and mapping to existing or proposed GitHub issues. Specify what is required before an authorized intake can publish the decomposition and how changed planning inputs are reconciled.
- [ ] Define the decomposition adequacy check: account for every approved parent obligation through child work, existing satisfaction evidence, or an explicitly approved exclusion/deferral; reject unsupported omissions and unrelated additions. Define responsibility for shared coverage and preserve the distinction between scope disposition and satisfaction.
- [ ] Define the workflow boundaries explicitly: product/design planning produces decomposition; authorized Backplane intake establishes or reconciles issue identities; selected executable issues receive implementation plans bound to their design authority and consumed issue revisions. Preserve the existing issue-first path for already captured work and approved issue-body design authority for bounded changes.
- [ ] Document optional interviewing integration without a supporting-tool-to-Backplane dependency. Compare the expected planning result with any reviewed grilling adaptation; keep adapter knowledge and GitHub operations in Backplane. Record missing released support honestly and retain a Superpowers-only path. Describe complementary audit/review/verification capabilities through their results and authority limits rather than required skill names.
- [ ] Define when evidence supports a requirement, which input changes require revalidation, and how historical evidence remains inspectable after reopening or supersession.
- [ ] Map FDAU's design-ready versus delivery-ready distinction to Backplane without importing a second lifecycle. Specify what native closure reasons, external decisions, and missing evidence mean for eligibility.
- [ ] Define how release targets, reconciliation gates, and separately authorized publication differ. Confirm a milestone or parent closure cannot bypass review and evidence requirements.
- [ ] Allocate doctrine, normative policy, operational references, and examples to proposed Backplane document homes. Reconcile them with the existing bootstrap/adoption authority model and avoid adding a second lifecycle or backlog authority.
- [ ] Define the Superpowers–Backplane–GitHub bridge responsibilities and required `gh` preflight. Resolve Projects policy explicitly and evaluate a minimal set of portable repository records against separate PRD/roadmap/backlog documents. For each retained record, define authority, preserved content, source revisions, implementer responsibility, refresh checkpoint/method, maintenance cost, and stale/offline behavior; additional portable skill bundles remain optional.
- [ ] Define the PR integration/completion bridge using current Superpowers worktree, review, verification, and branch-finishing guidance. Specify design-only versus delivery contributions, native issue links and closure intent, multiple-PR coverage, integrated-result evidence, automatic-closure reconciliation, parent satisfaction, Project reconciliation, and the repository-checkpoint closeout stage. Keep the consuming project's integration rules authoritative.
- [ ] Reconcile upstream execution-ledger helpers with the operator's absolute no-write rule for `.superpowers/`. Determine whether supported configuration or a project-owned execution approach can keep working state in `.sp-bp/`; record incompatibility if no supported alternative exists. Do not invoke a helper that writes to the reserved directory or modify shipped upstream code. This design slice itself creates no execution ledger.

### Task 3: Exercise the Proposed Model With Paper Scenarios

**Files:**
- Modify: `docs/superpowers-backplane/specs/2026-10-11-fdau-github-governance-design.md`.
- Create: `tests/scenarios/2026-10-11-fdau-github-governance-design.md`.

**Interfaces:**
- Consumes: Task 2's proposed contract.
- Produces: scored design walkthroughs and identified gaps; no claim of installed-skill behavioral conformance.

- [ ] Build invented fixtures for all seven Review Focus cases. For each, record inputs, the expected next action, supporting evidence, and the completion claims that remain unsupported.
- [ ] Add a normal end-to-end example: approved requirement, bounded child issue, consumed design revision, approved plan, delivery, accepted review, integrated verification, and separately considered release inclusion.
- [ ] Add one self-hosting example using read-only current Backplane issue data. Demonstrate continuity of existing issue IDs; make no issue edits or inferred approvals.
- [ ] Present the same invented coded hierarchy as an issue structure and as proposed Project columns/views. Trace each displayed value to its authoritative source and demonstrate recovery when a mirrored code or Project status disagrees with that source.
- [ ] Walk a planning result through decomposition intake with and without an optional grilling skill. Include one unresolved ownership decision and one existing issue matching a proposed outcome; require the same Backplane contract, no duplicate issue, no implicit approval, and no unrequested GitHub mutation in both paths.
- [ ] Exercise decomposition adequacy with separate cases for omitted parent scope, ambiguous overlapping ownership, and a child outside parent scope. Add passing cases for explicit shared coverage, existing satisfaction evidence, and an approved exclusion/deferral. Require exclusions/deferrals to retain their approval and remain distinguishable from delivered scope.
- [ ] Walk both approved design-authority paths through the workflow. For already captured bounded work, use the approved issue body and a revision-bound implementation plan; for a broader product design, produce decomposition first and reconcile it into proposed or existing issues before per-issue implementation planning. Demonstrate that neither path changes GitHub state without authorization.
- [ ] Walk loss of GitHub access, removal of an issue from a Project, and a stale local projection. Show that a repository checkout still explains the recorded decomposition and satisfaction claims, does not imply current live state, and can be reconciled after access returns. Record which proposed documents duplicate maintenance without adding preservation value.
- [ ] Walk a design-only PR, partial delivery across multiple PRs, accepted review with integration still pending, and automatic issue closure followed by missing or failed integrated verification. Include a passing delivery closeout that reconciles native issue/PR links, complete acceptance evidence, parent coverage, Project representation, and the portable checkpoint. Treat these as paper scenarios, not authorization to create, merge, or reopen live records.
- [ ] Walk every case through the proposed rules and mark PASS, FAIL, or UNKNOWN with reasons. Revise contradictory design rules instead of changing expected outcomes to make the table pass.
- [ ] Verify that all examples remain interpretable without Projects, custom organization issue types, FDAU tooling, or a local mutable backlog mirror.

### Task 4: Review the Design and Bound Later Implementation

**Files:**
- Modify: this plan and the proposed design/scenario files only as review requires.

**Interfaces:**
- Consumes: operator decisions, proposed design, and scored paper scenarios.
- Produces: reviewed design candidate and a bounded recommendation for later implementation ownership.

- [ ] Self-review the source-to-design and design-to-scenario coverage. Confirm unanswered operator decisions remain explicit and no proposal is labeled approved.
- [x] At the operator's request, obtain a fresh independent plan review. The 2026-10-11 read-only review identified three Important findings: preserve both approved design-authority paths, add decomposition adequacy proof, and remove the draft/decision ordering dependency. It also recommended separating product/design planning from per-issue implementation planning. The operator accepted these distinctions; the draft has been corrected. This completed plan review is not a review or approval of the future design output.
- [ ] Reconcile review findings and present any choices affecting authority or scope to the operator. Obtain approval of the completed design before implementation planning.
- [ ] Identify the smallest implementation slice and its work-item owner. A later implementation plan must name exact skill/reference changes, use `superpowers:writing-skills`, and define meaningful fresh-session behavioral scenarios appropriate to a skills-only artifact.
- [ ] Inspect the final artifact diff and report remaining unknowns. Do not execute the later implementation, create backlog records, or publish as part of this design-work plan.

## Source References

- FDAU reference: `xplane-fdau/docs/project/backlog-method.md` and `docs/project/backlog-governance-model.md`; these describe an evidence-backed delivery model and explicitly do not establish a formal requirements verification matrix.
- GitHub sub-issues: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues
- GitHub dependencies: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies
- GitHub issue types: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/managing-issue-types-in-an-organization
- GitHub milestones: https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones
- GitHub PR relationships: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue

Initial read-only discovery on 2026-10-11 observed enabled organization issue types Task, Bug, and Feature, and no open Backplane milestones. These are dated observations, not a portable availability guarantee or an adopted taxonomy. Recheck before designing a concrete migration.

## Validation and Handoff

This plan is documentation for design work. Validate internal links and paths, authority consistency, all seven failure cases, decomposition adequacy, both design-authority paths, the PR completion bridge, and scope preservation. Do not add phrase-presence tests or temporary-state snapshots. Later implementation requires the repository's skill scenario workflow and fresh conformance appropriate to the approved change.

The operator requested saving the first pass, subsequently requested review, and then explicitly approved the design-work plan on 2026-10-11. A fresh agent completed the read-only review, and the operator accepted the decomposition/workflow distinctions and corrections recorded above. The original strict audit verdict was FAIL pending those corrections; do not portray it as a passing audit of the revised bytes. The discussion exposed a workflow error: this design-work document was written before the new specification and labeled too much like an implementation plan. The subsequent specification was written, builder-checked, reviewed with the operator, and explicitly approved on 2026-10-11. The next stage is issue-bound implementation planning. No implementation execution method has been selected, work item selected, or GitHub state changed by these approval records.
