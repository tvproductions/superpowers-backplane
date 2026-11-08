# Release doctrine and lite/heavy alignment

Date: November 7, 2026. Revision: discussion 3. Status: design for reappraisal; implementation
and publication have not begun. The user agreed to Backplane owning portable
release-impact doctrine, the starter enforcing its adoption, and lite/heavy
remaining consistent while using different management approaches.

## Purpose and scope

Consolidate the existing outlines across Superpowers, Backplane, gz-skills and
gz-skills-first-starter. Establish one release-classification and evidence
contract, two management approaches, and explicit consumer bindings. Preserve
independent components and project-owned authority. Do not introduce another
backlog, an ensemble orchestrator, or an automatic release schedule.

This is a separate capability from the approved
[first-release scope review](2026-11-07-release-scope-review.md). That proposal
was approved by the user's subsequent “looks good”; its implementation and
publication remain separate. This alignment must receive its own backlog/scope
disposition rather than silently expanding the first-release bundle.

## What the existing outlines already establish

| Source | Existing intent or behavior | Consolidation needed |
| --- | --- | --- |
| Installed SP 7.0.1 README and feature skills | Feature design, approved spec/plan, execution, verification and review | Consume public-contract change evidence; no upstream modification or release-policy ownership transfer to SP |
| Backplane modes/governance | Owns product continuity, lite/heavy definitions and release monitoring; intent is separate from delivered capability | Supply portable release doctrine, clear light participation and impact accounting; retain current native issue authority |
| gz-skills candidate ecosystem proposal | Lite standalone skills; heavy combines SP, Backplane and portable disciplines; Backplane owns release records | Keep candidate history explicit; reconcile active lite wording and references, without importing unimplemented proposal machinery |
| Released gzs-release 0.1.0 | Recommend/prepare/publish, project-policy precedence, evidence-backed version advice and verified publication | Already usable in lite; add discovery of the adopted doctrine and common accounting without making Backplane installation mandatory |
| gzs-project-setup and README | Explicit lite/heavy selection; two-field settings; lite described as lacking release preference | Explain absence of ongoing central management, rather than absence of release discipline |
| Starter versioning/baseline/instructions | Same SemVer/major-PRD requirements in both modes; starter currently claims shared policy ownership | Reference Backplane's release doctrine, retain starter engineering/adoption ownership, and enforce adopted evidence requirements |
| Starter helper/tests | Preserve profile, validate catalogs/configuration, defer Backplane | Do not call these release enforcement; implement and test a separate explicit release acceptance check |

Reviewed gz-skills source is immutable main
`9a7970208207d68cc4a04eff7c3d39bcea664463`. Its source checkout is absent on
this machine; an old consuming-project plugin directory and installed caches
are not editing targets. The initial starter capture was main
`8d090f88bf45b9a755808a62c1445beeb005daff` plus uncommitted maintenance.
During reappraisal that independent work was committed as
`f0f5428c3f9146c4caaab209822b1f5d5fd57daa`; the observed tree was clean,
one commit ahead of its then-local tracking ref. No remote arrival is inferred.
The later read-only check observed clean main at
`e918dbbd02353258b697de5f63739a2431d65327`; that follow-up changes only
Dependabot configuration commentary and its compatibility evidence. Seventeen
of the original 18 sampled source hashes still match; only the session handoff
changed. These are source observations, not this task's edits or CI acceptance.
Preserve that maintenance and revalidate source identities before implementation.
Backplane base is
`0aa0cc007db63449455a1c4f9b6d92cb60c5d29a` plus this session's release review.
See the [source/evidence record](../../../tests/scenarios/2026-11-07-release-doctrine-alignment.json).

## Ownership and dependency direction

| Owner | Canonical responsibility |
| --- | --- |
| Superpowers | Feature development methodology and its approved artifacts; independently owned upstream |
| Backplane | Portable release-impact classification, bundle accounting, readiness/evidence semantics and lite/heavy management definitions; heavy native work tracking |
| gz-skills | Optional portable procedures and profile selection; gzs-release executes the consumer's authorized workflow |
| Starter | Opinionated adoption and engineering requirements, versioned binding to the release doctrine, and enforcement for its own repositories/adopters |
| Consuming project / maintainer | Public contract, adopted policy/revision and deviations, scope and approvers, runtime/tools/channels, release decisions and publication authority |

Backplane requires Superpowers as its companion. It does not require gz-skills,
the starter, their settings, their Python baseline or their release command.
Its own maintainer engineering binding may reference the starter; the portable
release contract must not require fetching starter policy to operate.

The starter references Backplane's portable doctrine as policy data. That does
not activate the plugin or claim heavy readiness. gz-skills discovers the
consumer's adoption of that policy; it remains useful under a different project
policy. Neither portable component imposes starter requirements on unrelated
consumers. Cross-references express distinct responsibilities, not mutually
required runtime installations.

This intentionally amends the current arrangement: Backplane's release-policy
binding and starter versioning currently assign shared release policy to the
starter and prohibit a reverse policy dependency. Until this design is approved
and the affected authorities are reconciled, those current bindings remain in
force. Publish the approved Backplane authority when authorized, then let each
companion record adoption against that exact revision. Each new binding takes
effect at its own accepted reconciliation revision; unfinished consumers remain
explicitly unaligned. Preserve dated prior decisions as history. Do not claim a
completed transfer from this design file alone.

## One doctrine, two management approaches

| Concern | Lite | Heavy |
| --- | --- | --- |
| Policy | Explicit project adoption; same selected classification and evidence rules | Same |
| Feature/release accounting | Existing project release notes, issues, approved documents or handoff records; human/agent maintains links | Native Backplane issues, dependencies, criterion/evaluation links and release targets |
| Execution | Project release procedure, optionally gzs-release | Project release procedure, optionally gzs-release beneath the Backplane workflow |
| Monitoring | Explicit reviews at the project's selected cadence | Ongoing product/release readiness monitoring when implemented and explicitly adopted |
| State | Existing project authority; no mandatory Backplane lifecycle/settings | Backplane's existing native authority; no duplicate gzs lifecycle |
| Readiness | Actual evidence and authorization | Same evidence plus required current graph/coverage reconciliation |

Lite permits bounded releases, version advice, selected bundles and deliberate
release accounting. It does not require heavy product management, GitHub issue
hierarchies or a running Backplane plugin. Heavy adds management participation,
not weaker or stronger compatibility rules. An unavailable heavy integration
remains unready; no silent downgrade to lite. A project may explicitly retain
its existing management while integration is deferred, with that limitation
visible. Neither mode implies a fixed calendar or automatic agent wake-up.

Keep `.gz-skills/settings.json` exactly `schema_version` plus `profile`.
Selection is explicit; do not migrate settings or infer profile from installed
plugins. Release policy adoption belongs in existing project instructions and
release authority, not another settings key.

## Portable release doctrine

Backplane should own a concise `docs/superpowers-backplane/releases.md` defining
these semantics. Project adoption makes its selected rules binding; mere plugin
installation does not.

1. Identify the independently versioned public contract: API, CLI, formats,
   configuration, workflow, authorization/preservation behavior and any declared
   support requirements. An upstream version does not dictate a consumer bump.
2. Compare the whole selected candidate with its actual last published baseline.
   Distinguish absent first release, pending metadata, stable/prerelease status
   and unrelated component tags. Never invent historical releases.
3. Use major for incompatible stable public contracts, minor for compatible
   additions/deprecations, patch for compatible fixes. For projects adopting
   this opinionated 0.x policy, additions and changes requiring reconciliation
   advance minor; compatible fixes advance patch. First substantive release is
   0.1.0; 0.0.0 is only an unpublished bare-scaffold placeholder.
4. Select coherent bundles. Completion prompts release accounting; it does not
   automatically create a release or require one minor per feature. The highest
   applicable included impact sets the proposed bump for each component.
5. Include rationale, consumer impact/migration, supported tuple, current
   verification/validation and accepted deviations. Missing or stale mandatory
   evidence is UNKNOWN; observed unmet obligations are UNSATISFIED.
6. Preserve distinct facts: implemented, accepted, included/deferred, ready,
   authorized, published and remotely verified. Deferral needs explicit scope
   disposition; it is not satisfaction. Immutable published identity never moves.

The user's release premises are part of this opinionated doctrine: majors are
PRD-driven; minors are driven by coherent feature/outcome bundles; patches are
driven by compatible defect/repair outcomes. Every major, including 1.0.0 and
independently versioned skill majors, requires newly written accepted requirements
for that major. The starter adopts and enforces that rule rather than owning a
competing version. Unrelated consumers retain their own explicitly adopted
policy. Issue type alone never determines the bump; compatibility still governs.

The ownership transfer covers version classification, public-contract impact,
bundle accounting, major-PRD requirements and evidence semantics. The starter retains its supplementary
engineering and adoption requirements. A binding names the exact
Backplane policy revision, applicable supplement revisions and approver; no
implicit selection of arbitrary clauses or substitution of a moving main URL.
Updating either source requires a semantic diff and explicit project adoption,
not a plugin-pin update or retroactive change to historical acceptance.

When declared adopted sources conflict, report the conflict and stop the
affected release check until the project's authorized amendment resolves it.
Project policy remains the authority for unrelated consumers; it does not let
a starter-governed project silently waive that starter's adopted requirements.

## Release-impact accounting contract

Use the existing feature/outcome record; avoid a second mutable registry. A
release-impact disposition references:

- Governing feature/requirement revision and delivered contribution.
- Affected independently versioned public contract and baseline identity.
- Proposed impact: none, compatible fix, addition/deprecation or incompatible
  change; selected bump under the adopted policy, with rationale.
- Consumer/support/migration consequences, including requirement changes versus
  tested-pin refreshes.
- Proposed bundle or explicit deferral, authority and revisit condition.
- Acceptance/evidence references and unresolved compatibility questions.

Record a provisional impact during design, reconcile against implementation at
review/closeout, then recompute at bundle selection. A no-impact result needs a
reason. UNKNOWN does not silently become patch. Classification and scope can
change before publication with recorded approval; published membership and
identity are historical facts. Skill and bundle versions remain independent.

Bundle selection must reconcile the entire distributed candidate delta against
the last published baseline, including uncommitted intended changes and packaged
resources at preparation time. Every changed path and independently versioned
component must map to a reviewed contribution or a justified non-public/no-impact
disposition. Include removals, default/configuration changes, support obligations,
dependency-mediated public effects and features absent from the tracker. Missing
inventory coverage blocks the decision. A component path map supplies traceable
coverage; changed-path counting alone does not establish semantic completeness.

A deferred work item does not remove its shipped behavior from compatibility
analysis. If the bytes remain distributed, account for their actual exposed
contract and experimental/support boundary. Excluding behavior requires an
observed packaging or activation boundary and its verification, or its removal
from the candidate through separately scoped work. Approval to defer acceptance
cannot relabel an exposed incompatible change as no-impact.

Lite records those meanings in existing documents. Heavy binds them to native
outcome/release issue fields and immutable evaluations. Views are derived.
No mandatory universal local file path, new lifecycle ladder or runtime schema
is needed in Backplane for this first increment.

### Feature/outcome unit and patch recommendations

Backplane's bounded delivery unit is the **outcome**, anchored by an executable
leaf GitHub issue and its acceptance criteria. A capability may group outcomes;
a small feature may be a single outcome. The native issue URL is the stable
tracker identity. A project-declared semantic code remains stable across release
retargeting; it is not an issue number or a mandatory new coding scheme.
An outcome has approved design authority, an issue-bound execution plan and
accepted criterion-level evidence. Plan tasks, commits and PRs contribute to
that outcome; they are not automatically separate feature/release units.

For participating governance records, use the existing `Backplane Record`,
`Obligation Dispositions` where applicable, and `Coverage and Satisfaction`
sections. Do not silently migrate legacy issues. Minor bundles select accepted
outcomes and account for their combined public-contract effect. Lite can express
equivalent bounded outcomes in existing project records without requiring
Backplane issue hierarchy or installing its runtime.

The user prefers a patch consideration threshold of **10–12 accepted unreleased
repairs**, replacing the earlier suggestion of three. Proposed default: recommend
considering a patch when the count reaches **12**; projects may explicitly set
their threshold within the preferred range. The threshold is a decision prompt,
not a mandatory publication count, maximum wait, or fixed calendar. A consequential
regression or user-blocking repair can justify an earlier recommendation.

Count distinct accepted repair outcomes available for the candidate since the
component's last published release. Do not count commits, PRs, raw closures,
duplicate issues or multiple slices of the same repair as separate fixes.
Reconcile actual shipped deltas and acceptance so issue splitting cannot inflate
the count. Recompute at repair closeout and release review; record release/defer
decision, rationale and revisit in existing authority. A deferral does not reset
the count. A published patch or larger bundle consumes only repairs actually
included; accepted repairs left out remain visible for the next recommendation.
This is agent/manual behavior at those workflow events, not an unimplemented
background scheduler. The threshold never overrides compatibility or acceptance.

### Strict Python/Astral alignment for Backplane development

The user explicitly requires Backplane-owned Python implementation and tooling
to meet the strict Astral/Python alignment and acceptance contracts reviewed in
the starter's `docs/engineering/astral-alignment.md` and
`docs/engineering/astral-acceptance.md`. This is a Backplane-owned engineering
decision, not adoption of the starter bundle or a consumer runtime requirement.
Apply every applicable requirement; absence of a feature needs a reasoned N/A,
and a departure needs evidence, approval, owner and dated revisit.

Confirmed requirement: the user explicitly reaffirmed that the same strict
Astral project compliance applied elsewhere must exist here, including resolving
the absent pyproject/uv lock and the current no-project execution model. This is
mandatory reconciliation of Backplane's existing development tooling, not an
optional improvement deferred until a Python feature happens to need it. The
overall design remains under review; this confirmation accepts this requirement
without implying release publication or approval of every proposed interface.

Use the approved uv-managed Python 3.14 family/exact verified pin, uv-managed
project/environment/dependencies and lock, centralized effective configuration,
Ruff lint/format, ty and unittest, with the declared routine hook/CI contract.
Use applicable `src/` packaging, uv_build for pure Python distributions and
source-independent builds plus clean installed-artifact checks. Keep deeper
engineering checks and current-version idiom/freshness assessment in their
prescribed on-demand acceptance scope. No pytest. Do not invent a runtime
package where the scoped product has none; justify package/build applicability.
Minimal JavaScript required by native host adapters remains a tested adapter
boundary, not permission for a parallel non-Python Backplane core.

At initial review, this repository had no tracked pyproject/uv lock or Python
package, and its agent instructions prescribed `uv run --no-project`. Before new Python implementation, inventory
A01–A18 applicability/gaps and plan the necessary Backplane tooling migration,
including explicit command/instruction reconciliation. Until that change is
approved and verified, obey existing execution commands; do not silently claim
locked project acceptance from the current local environment. Preserve historical
runtime evidence and separately assess host/plugin acceptance.

Treat tooling migration and its full applicable acceptance as the first
implementation prerequisite. No new Backplane Python feature work proceeds on
the unreconciled baseline. Creating pyproject/lock files alone cannot close the
gap: effective configuration, reproducible locked execution, required checks,
hooks/CI and applicable artifact proof need actual evidence. Missing required
results remain incomplete; convenience, pre-existing layout and a passing local
script are not exceptions. The migration plan must amend conflicting current
instructions explicitly and verify the replacement commands before declaring
the new baseline operational.

November7 implementation checkpoint: the mandatory engineering contract,
non-package pyproject/uv lock, locked commands, routine checks and CI configuration
are now prepared locally, and the normal local pre-commit hook is installed.
See [the scoped acceptance matrix](../../../tests/scenarios/2026-11-07-strict-astral-acceptance.md).
This does not establish full conformance: hosted CI and remaining wider
engineering/guide-quality evidence are still UNKNOWN. The feature gate remains
in force. This status note does not approve the rest of the release design.

## Starter enforcement boundary

Instructions alone establish obligations but cannot honestly be called automatic
enforcement. Add a separate on-demand **release acceptance check** to the starter
helper, provisionally `skills-first-starter release-check --project <root>
--record <existing-project-evidence.json>`. This is starter-owned validation of
its adopted policy, not Backplane's release manager or a publishing command.
Do not couple ordinary configure/status/validate to release readiness.

The execution plan must define and test the adapter's JSON encoding/schema
before implementation. Its required semantic groups are fixed by this design:

| Group | Required meaning |
| --- | --- |
| Context | Project identity, adopter versus starter-repository context, selected management approach and its authority |
| Policy | Exact adopted doctrine/supplement identities, binding approval, mandatory check identity and tested helper compatibility |
| Baseline | Component's last published version and immutable source, or explicit first-release evidence |
| Candidate | Source commit, distributed payload/path inventory, component map and owning-tool generated-artifact identities |
| Contributions | Complete delta-to-impact mapping, included/deferred obligations, consumer effect and accepted classification rationale |
| Gates | Applicable criterion/seam results, exact evaluated inputs, available evidence hashes, semantic acceptance and unresolved gaps |
| Decisions | Scope approval, current major PRD and acceptance where required, eligible exceptions and requested publication boundary |

The check validates coverage, declared-rule consistency, identities and evidence
availability. It cannot infer API compatibility, consumer impact or PRD adequacy
from source text, a hash or a JSON assertion. Those judgments require a named
project-authorized reviewer, exact inputs, rationale and an accessible acceptance
record. A PRD must identify the affected component and major and be accepted as
newly written requirements; a file path alone is insufficient. The check reports
which facts it verified mechanically and which judgments it consumed. It does
not rerun model/host operations or execute commands embedded in evidence.

### Candidate identity without an evidence cycle

Prepare-time advice may inspect dirty intended changes, but strict readiness
requires a committed candidate. Record the tested delivery commit and exact
distributed payload manifest. Later review/evidence storage has its own commit;
it never asserts that its own future SHA was tested. Documentation or metadata
that enters the shipped payload belongs in that manifest and must receive the
owning applicable checks. There is no blanket evidence-directory exclusion.

Before publication, reconcile the actual final release commit and package
inventory with the tested manifest. Reuse evidence only for unchanged applicable
inputs with recorded equivalence; rerun affected gates for any relevant delta.
The final receipt binds the final commit, payload hashes and gate inputs.
Publication still requires fresh immutable-tag/channel verification. This
prevents both perpetual self-invalidating evidence commits and stale passes
being reused after a source or package change.

### Profiles and starter self-release

For adopters, read the existing two-field profile settings, reject missing,
pending or conflicting selection, and verify the project identity. Do not create
settings in the checker. Starter development explicitly has no self-adoption
lock or inferred profile. For the starter's own release, accept a separately
documented repository management declaration in its release authority; identify
the validated canonical starter source/package so an adopter cannot claim this
exception by setting a JSON flag. No synthetic self-adoption is introduced.
Projects using Backplane independently of the starter need no gz-skills profile.

### Results, exceptions and mandatory checks

Fail closed for incomplete delta coverage, ambiguous policy, unavailable required
helper/profile evidence, inconsistent bump, unauthorized deferral, required
FAIL/UNKNOWN, stale identities or missing major-PRD acceptance. Emit distinct
structural validity, evidence-match and accepted-judgment results plus gaps.
Strictly ready is the only success exit. Incomplete/conditional/not-ready results
are non-success, distinguishable from malformed input or tool failure; the plan
sets exact codes consistent with the helper CLI.

An exception must name the requirement, governing policy permission, candidate,
evidence, authorized approver, owner and dated revisit. Conditional acceptance
is never strict success. Missing exception authority cannot become a waiver;
neither an exception nor this checker authorizes publication or mutable release
identity. The owning release procedure decides whether expressly permitted
conditional publication is authorized and records that decision separately.

Both modes use the same classification and evidence rules. Heavy additionally
requires current issue/coverage reconciliation; unavailable heavy evidence cannot
be substituted with lite records. Each criterion remains SATISFIED, UNSATISFIED
or UNKNOWN; a bundle readiness result also accounts for explicit scope
dispositions. A successful check reports assessed readiness against a candidate,
not authorization, publication or verified installation.

Bind the check into the starter's own release instructions and generated adopter
instructions, identifying the minimum compatible helper and immutable policy
source. If the adopted binding requires this check, an absent/older/incompatible
helper blocks acceptance. gzs-release must not switch to manual fallback merely
because the required command is unavailable. Only a policy-permitted approved
substitution with equivalent evidence can support conditional handling.
Unrelated consumers without mandatory automation retain documented manual
release workflows. No portable dependency on this exact command is introduced.

The checker is read-only and does not install, mutate remote or source state,
fetch arbitrary evidence URLs, or execute record contents. Read project-approved
local artifacts or explicitly obtained immutable snapshots. Canonically resolve
paths and symlinks, reject unapproved escapes/unavailable inputs, bound parsing,
and redact sensitive diagnostics. These are evidence-read boundaries, not a
credential-copy or background-service mechanism.

### Shared conformance and offline policy access

Backplane owns language-neutral semantic examples with expected classifications,
readiness outcomes and explanations at the same revision as the doctrine.
Starter tests its adapter against those reviewed examples; gz-skills tests
equivalent lite and heavy scenarios. Data can be distributed as a pinned,
attributed documentation/fixture resource with source/hash provenance, without
copying skills or importing a Backplane runtime. Consumers must not privately
change the expected verdicts and still claim alignment.

At adoption, obtain the exact reviewed policy/fixture snapshot through authorized
source access and record its identities. Offline use can consume those verified
bytes; it does not prove live source currency. New adoption/update without the
required snapshot is UNKNOWN. Existing accepted bindings continue against their
recorded revision unless project policy requires a fresh-source review; when it
does, unavailable current-source evidence blocks that review. No always-online
or moving-main dependency is introduced.

## Consolidation map and order

1. **Backplane:** create portable release authority; reconcile `modes.md`,
   `governance.md`, backlog references and `docs/release-policy.md`/AGENTS so
   release-doctrine ownership and starter engineering/adoption ownership are
   explicit. Keep historical dated bindings unchanged. Changes to skills require
   writing-skills and behavior/scenario evidence. Preserve existing issue
   eligibility/closure rules; do not activate unimplemented proposal node kinds.
2. **gz-skills:** in a verified owned source checkout, reconcile README,
   `gzs-project-setup`, `gzs-release`, release binding and packaging ownership.
   Reference the consumer-adopted doctrine and correct lite wording. Preserve
   portable fallback, settings schema, project precedence and release authority
   modes. Treat the old ecosystem proposal as historical candidate context,
   with a reconciliation pointer rather than a competing active specification.
3. **Starter:** reconcile versioning, architecture, baseline/adoption guidance,
   AGENTS and generated instruction source; retain component-specific examples
   and enforcement obligations while replacing duplicated general rules with
   precise authority references. Regenerate checked wheel resources through the
   owning helper. Implement the release-check adapter and tests separately from
   the documentation migration. Preserve current November 7 maintenance.

Publish portable authority first when publication is authorized, then bind
consumers to its exact reviewed revision. Local drafts must be labelled as such;
never point at a nonexistent hosted authority and claim completed integration.
Do not update plugin pins, caches, adopter projects or activation merely because
policy references change. Validate each component independently; end-to-end
ensemble acceptance is an additional claim requiring its own evidence.

## Alternatives and decisions

Keeping duplicate doctrine in the starter/gz-skills would preserve current
locations but require recurring semantic reconciliation and leave Backplane's
release role unclear. Making every mode require full Backplane runtime would
centralize execution but contradict portable lite and Backplane independence.
The user selected the third approach in this conversation: Backplane owns the
portable canon, lite/heavy use consistent semantics, and the starter binds and
enforces its adoption. The exact release-check command and JSON adapter are
reviewer-proposed implementation details, not an already approved interface.

## Verification and release implications

Prove equal version decisions for equivalent lite/heavy fixtures: first release,
compatible patch, coherent addition, stable breaking change, independent bundle
and skill impact, policy change versus pin refresh, missing compatibility and
explicit deferral. Include consumers with no gz-skills/starter and gz-skills lite
with no Backplane plugin. An unrelated consumer's policy must prevail.

Demonstrate negative controls for feature completion without release accounting,
missing/stale evidence, deferred work called satisfied, missing major PRD,
unavailable heavy reconciliation and unauthorized publication. Test preserved
two-field settings, unsupported schemas and explicit profile choice. Prove the
starter check and generated installed instructions agree, and that configure or
manifest validation does not claim release readiness. Run each repository's
own full gate for behavior changes; no new tests are needed for prose alone.

Required additional boundary controls are: an unlisted shipped addition; an
unlisted removal/default change; experimental shipped bytes marked deferred;
an adopted mandatory check with no compatible helper; starter self-release
without self-adoption settings and an adopter falsely claiming that context;
later evidence-only storage with unchanged payload versus altered release
metadata or payload; unsupported human judgments represented as mechanical
proof; approved conditional evidence versus strict success; path escapes and
embedded commands; old accepted offline policy versus an unavailable mandatory
fresh-source review; and a consumer privately changing conformance verdicts.
Each refusal must identify the exact gap and preserve project state.

Discussion-3 additions require boundary scenarios for patch counts below/at the
adopted threshold, duplicate repair records, count persistence after deferral,
partial release membership and earlier consequential-repair recommendation.
Prove major/new-PRD, minor/outcome-bundle and compatible patch/repair decisions
under both management approaches. For Backplane Python work, require its own
A01–A18 applicability/evidence record; borrowed starter results cannot certify it.

Before implementation planning, resolve the next work's issue identity and
scope in each owning repository through authorized intake. This design does not
invent issue numbers or silently select a release target. The approved initial
Codex/Claude scope stays intact; any inclusion of this new behavior requires its
own explicit bundle decision. If only documentation is selected first, keep
enforcement status visibly unimplemented until its separate behavior gate passes.

Evaluate versions against each last release. Added release behavior/enforcement
is a minor capability during 0.x; changed released skill trees need their own
classification and a bundle advance. Pending changes may share one coherent
minor where justified. Documentation-only scope must not be mislabeled as
implemented enforcement. No version/tag/release is changed by this design.

## Acceptance for the consolidation

The implementation is complete only when each active authority names the same
owners, both modes reach equivalent semantic decisions, standalone boundaries
pass, starter enforcement rejects demonstrated missing-evidence controls,
generated/distributed instructions match, and current evidence distinguishes
implemented behavior from candidate doctrine. Preserve existing approvals and
historical evidence. Integration, publication, installation and host acceptance
remain separately observed results.

After approval, write issue-bound implementation plans in the appropriate owning
repositories and follow Superpowers isolation, TDD appropriate to each artifact,
fresh review and verification. Start with Backplane's portable contract; do not
resume OpenCode tests as an incidental part of this consolidation.
