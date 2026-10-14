# Superpowers Backplane governance

Backplane connects approved product obligations to native GitHub work,
Superpowers execution, and inspectable delivery evidence. Read the issue for
current intent and lifecycle, the approved design for behavior, the plan for
execution, and accepted evidence for satisfaction. A Project or repository
checkpoint presents those sources; it does not replace them.

## Ownership and authority

| Concern | Owner/source | Consequence |
| --- | --- | --- |
| Product purpose and constraints | Project instructions and approved product/architecture material | Keep the project's existing PRD-equivalent authority; no universal new document. |
| Work identity, scope, acceptance, hierarchy, dependencies, lifecycle | Native GitHub issue and relationships | Use repository plus issue URL/number; preserve full native intake. |
| Design | Human-approved complete issue body for bounded work, or approved specification for a cross-cutting decision | Both paths are valid. Resolve conflicts with the approver. |
| Execution | Current approved issue-bound Superpowers plan | Record consumed issue/design revisions and project verification seams. |
| Criterion satisfaction | Accepted immutable project-owned evaluation evidence | Bind the verdict to exact approved criteria and delivery inputs. |
| Presentation | Issue-backed Project items, optional views/mirrors | Refresh from canonical sources; display state is not execution authority. |
| Portable account | Dated committed repository checkpoint | Explain captured state and limitations; reconcile before live action. |

Approval identifies the approver, artifact/revision, accepted scope, and source
of the decision. A specification refines behavior without silently amending an
issue's scope. A discrepancy requires explicit reconciliation. Changed timestamps
trigger semantic comparison; they prove neither a behavioral change nor freshness.

An existing bounded approved issue may proceed to planning without repeating
brainstorming. Cross-cutting behavior uses a reviewed specification. Backplane
surrounds upstream Superpowers; it adds no alternate development lifecycle.

## Product identity and decomposition

A project supplies its code legend. For example, `INSTALL1` is a capability and
`INSTALL1.1` is an outcome; these are invented mnemonic examples, not prescribed
syntax, ordering, dates, or versions. Codes are unique within their declared
namespace and remain stable when release targets or parentage change. Preserve
issue identities and an approved alias history when migration is necessary.
Do not derive live parentage from the spelling of a code.

Use record kinds `capability`, `outcome`, `gate`, and `external-boundary`.
A grouping capability is not an implementation leaf. A small feature may itself
be the bounded outcome; do not create redundant layers. Native issue types are
used where available; the Backplane kind does not require custom organization
types. An external boundary names its actual owner and prerequisite. Link that
owner's issue when available; otherwise keep the boundary explicitly unresolved.

Participating issues maintain three issue-owned sections:

| Section | Contents |
| --- | --- |
| `Backplane Record` | Code, kind, code namespace, design/plan/approval and coverage references. |
| `Obligation Dispositions` | Parent obligation and governing revision, bounded child contributions or accepted evidence, owner, approved deferral/exclusion, unresolved gaps. |
| `Coverage and Satisfaction` | Current criterion-to-requirement mappings and pointers to accepted evaluations, including changed-input and outstanding-contribution findings. |

Native parent and dependency relationships stay native. The body references
those relationships without maintaining a separately editable duplicate graph.
These sections support declared governance participation; they do not silently
migrate every legacy issue or invalidate the existing bounded-issue contract.

Account for every approved parent obligation through bounded child outcomes,
eligible existing satisfaction evidence, or an explicitly approved disposition.
Reject omissions, unrelated additions, and ambiguous duplicated ownership.
Shared coverage is valid when contribution boundaries and the owner accepting
the combined result are explicit. Preserve the existing issue when it matches;
classify proposed new work and unresolved questions separately. Decomposition
approval alone authorizes no issue creation, selection, or readiness transition.

Deferral/exclusion records identify their approver, governing revision, rationale,
and revisit condition where applicable. They remain visible and do not count
as delivered. A child closed as not planned does not satisfy its obligation;
its parent needs approved alternative coverage or a scope disposition.
Dependencies establish readiness, not priority. Parentage describes decomposition,
not execution order. No priority is inferred from list order or codes.

## Coverage and satisfaction

A requirement reference includes its governing issue/document identity, stable
criterion/statement key, approved revision, and wording. Retain a project's
existing identifiers. Line numbers and checkbox positions are not durable keys.
Many requirements may map to one outcome, and several issues/PRs may contribute
to one criterion. State each contribution's scope and combined-result owner.

The outcome issue owns the current mappings and latest accepted evaluation
pointers. The evaluation is immutable evidence with exact inputs, method,
observed result, delivery/integration identity, review/acceptance disposition,
evidence identity/availability, and remaining obligations. Preserve historical
evaluations against their original revisions. Parent summaries reference child
results rather than maintaining independent verdict copies.

| Result | Meaning |
| --- | --- |
| `SATISFIED` | Applicable obligations have accepted passing evidence against the exact reconciled current inputs. |
| `UNSATISFIED` | Accepted evidence establishes an unmet applicable obligation. |
| `UNKNOWN` | Execution, input matching, evidence, or acceptance is unavailable or unverified. |

Deferral and exclusion are scope dispositions, separate from this result
vocabulary. Missing evidence is UNKNOWN, not success or a fabricated failure.
Feature satisfaction requires every applicable obligation to be satisfied,
with approved excluded/deferred scope separately disclosed.

A behavior-changing requirement or implementation delta makes affected current
claims unsupported until evidence is reconciled/revalidated. A prior pass at
commit B does not prove commit C. An editorial revision may retain matching
evidence only with explicit semantic equivalence and unchanged relevant delivery
inputs. A timestamp alone cannot supply that equivalence. Project/checkpoint
satisfaction displays derive from the reconciled evidence and disclose gaps.

## GitHub presentation

Integrated Projects are the normal proposed presentation for these bridges.
An explicitly declared `issues-only` compatibility mode preserves the same
identity, coverage, evidence, and lifecycle rules. Ordinary existing backlog
status/selection operations continue to use native issues without a Project
prerequisite. Before a checkpoint capture, declare its scope and mode.

Use issue-backed items and four views: product/decomposition, execution,
satisfaction, and release targets. Native Title, issue type where available,
labels, assignees, parent issue, sub-issue progress, milestones, and PR context
present their source records. Optional `Code`, `Kind`, and `Satisfaction` mirrors
refresh from issue sections and accepted evidence. Define who refreshes them
and when; mirrors are not automatic semantic synchronization.

An optional Project Status field has an explicit project-owned mapping to issue
labels/native state. It is presentation, never a second readiness gate. Done
cannot override an issue in review or UNKNOWN integrated checks. Closed-child
counts count closures, not satisfied obligations. A milestone groups targets;
it does not authorize publication.

Denied Project capture in declared integrated mode is incomplete capture. Retain
that mode and the limitation; do not silently switch to issues-only or invent
inaccessible values. Missing custom issue types need no new organization types.
Project drafts and Discussions may support preliminary deliberation; they are
not approved executable work. Forms/templates, review rules, and Releases have
project-specific roles rather than becoming universal dependencies.

## Bridge operations and Superpowers sequence

1. Read current project authority and complete native issue context.
2. Consume an approved product/design result and assess complete decomposition.
3. Reconcile proposed/existing records and native relationships through an
   explicitly authorized intake operation.
4. Plan one bounded selected issue against current issue/design revisions,
   approved acceptance criteria, and project-owned verification seams.
5. Validate eligibility, then follow Superpowers isolation, execution, TDD,
   review, verification, and branch finishing under project rules.
6. Track PR contributions and remaining obligations through review/integration.
7. After accepted integration, run fresh project checks, reconcile satisfaction
   and authorized issue/Project closeout, then refresh the portable checkpoint.
8. Evaluate release inclusion/publication under separate release authority.

Use the existing six Backplane lifecycle labels and open/closed state as defined
in the native issue contract. Keep exactly one lifecycle label on open tracked
issues and preserve unrelated labels. A prepared worktree, checked task, commit,
PR, or merge alone does not prove the next lifecycle gate.

The named operations are `decompose/intake`, `PR closeout`, and `capture
checkpoint`. Focused references define their input/output contracts. Supporting
tools may contribute inspectable findings or decisions; none becomes a required
skill bundle, approval authority, helper engine, or language runtime.

## PR contributions and completion

A PR records affected issue/design/plan revisions, criterion contributions,
review disposition, verification inputs/results, and closure intent. A design
PR establishes design, a partial PR contributes scoped delivery, and accepted
review/branch checks still await integration. Use neutral contribution references
while integrated evidence is pending. A closing keyword is closure intent,
not proof of a native closure relationship or satisfied outcome; nondefault
integration targets require observed native behavior rather than assumption.

Review acceptance, merge, integrated verification, satisfaction, issue/parent
completion, and release are distinct. If automatic closure outruns verification,
report the actual closed state and unmet obligations. Propose the appropriate
recovery under project authority; do not reopen or edit labels unrequested.

Verified closeout names the accepted integration commit and approved requirement
revision, updates issue-owned evaluation pointers, refreshes parent references
and Project projections, and captures a dated repository checkpoint. Preserve
old evidence. A later checkpoint/evidence storage commit refers to the verified
feature commit; it cannot claim its own future merge was already checked.
Keep the implementation workspace for pending review fixes; cleanup follows
upstream/project ownership and authorized branch finishing.

## Portable repository record and working state

The product checkpoint pair is `.sp-bp/state.md` plus
`.sp-bp/github-state.json`, format `sp-bp-checkpoint/v1`. It records captured
outcome/criterion wording, source graph and revisions, design/plan/approval
anchors, dispositions, many-to-many coverage, evidence-backed claims and
availability limitations. It is a dated account, not an offline mutable backlog.

Declare capture scope/mode and start/end observations. Enumerate every required
page, preserve excluded/external scope, and recheck the source revisions used.
A missing page, denied capture, changed relevant source, unavailable required
evidence, mismatched capture IDs/digest, or contradictory readable claims prevents
a complete/current replacement. Retain the last accepted pair. A partial
candidate may be kept as a clearly labelled diagnostic.

Stage candidates and a transaction receipt under ignored `.sp-bp/work/`.
Validate exact JSON bytes, shared capture ID, readable/structured semantic equality,
scope, references, and evidence before installing outputs. Check prior outputs
and index ownership; user edits stop automatic overwrite/recovery. The local
acceptance point is one verified Git commit containing both validated blobs.
Remote integration is separately observed. Filesystem copies and GitHub capture
are not atomic. Store the acceptance commit in the external receipt, avoiding
self-referential content hashes. Recovery verifies prior/candidate ownership and
restores only the pair and its index entries under applicable authority.

Refresh after approved decomposition intake, material coverage/scope changes,
verified closeout, and release review. Routine task edits need no product
capture. Offline records explain their captured state but cannot establish live
eligibility or authorize replay into GitHub. Reconcile after access returns.

Scratch is disposable. For this repository's issue-31 execution, the separately
tracked execution summary and supporting evidence preserve progress across
machine/harness boundaries under the existing handoff approach. Verify transport
and arrival before claiming another host can resume. This does not introduce a
new general session-handoff system or make scratch the sole authority.

## Superpowers freshness evidence

Backplane owns its direct SP alignment and publishes dated compatibility/freshness
evidence. Follow the stable upstream channel by default; edge and revision
changes need their applicable explicit authorization. The bundle consumes that
cue and owns complete-stack integration. Adopters verify their actual tuple and
project overrides. An older bundle pin is not Backplane's support policy.

Return these fields for a freshness assessment:

- **Ownership and channel policy:** Backplane owns direct SP alignment and
  follows stable by default; identify any explicitly selected edge exception.
  Name the bundle's complete-stack owner and the adopter's tuple/override role.
- **Evaluation:** exact SP/Backplane revisions, tested host/capabilities and
  overrides, supported results, and unavailable or untested scope.
- **Publication and next action:** local versus published evidence, verified
  transport/arrival or its absence, and proposed versus authorized operations.

A cue identifies latest stable observed at a checked time, exact evaluated SP
and Backplane revisions, relevant artifact hashes and project overrides,
harness/capability scope, results, and unresolved limitations. Classify the latest
stable target as verified compatible, untested, or incompatible with the evidence
and reason. An older pass does not establish currentness; an installed version
alone does not establish compatibility. Local/uncommitted evidence is not a
published cue, and one host/override does not establish all harnesses/workflows.
Publish immutable scoped evidence with the advertised Backplane revision. Before
consuming it as a published cue, verify authorized transport to the advertised
target and arrival there: the exact commit/artifact identities must be reachable
and their supporting evidence inspectable by the consumer. A local accepted
commit, proposed publication, or URL alone does not demonstrate that arrival.
Neither cue nor bundle preference
authorizes automatic installation changes.

## Boundaries and worked example

Backplane documents use `docs/superpowers-backplane/`; optional local state uses
`.sp-bp/`. Ignore only `.sp-bp/work/` before use and keep the product pair trackable.
Never write to `.superpowers/`, shipped upstream, or discovery targets within
upstream. A helper whose default writes there is prohibited even when its visible
output is redirected. Preserve upstream independently. A supported native
bookkeeping exception must be explicitly scoped and demonstrated; it is not an
upstream redirection feature. Git, authenticated gh, and operational Superpowers
are required; project language/runtime and verification remain project-owned.

Invented example: `INSTALL1` owns O1 source adoption, O2 discovery, and O3
preservation. Existing outcome `INSTALL1.1` covers O1. Two proposed outcomes split
O2 into enumeration and invocation with an explicit combined-result owner; accepted
E3 covers O3 at S1. An approved O2 deferral is a separate valid disposition,
not delivery. The parent issue maintains those dispositions and native child links.
A bounded documentation correction can use its approved issue body as design;
a shared coverage change uses an approved specification. Each executable leaf
still needs its own current approved plan and clear dependencies.

A design PR establishes S1, a package PR contributes O1, and a verification PR
contributes discovery. Partial delivery or accepted review alone cannot close
the outcome. Fresh accepted checks at integrated commit B justify applicable
criterion satisfaction and authorized closeout. A later checkpoint commit K
captures that result as evidence for B, with its own capture limitations; K is
not substituted for B. Release remains separate. If S2 or commit C changes
relevant behavior, preserve B's history and revalidate the affected current claims.

Authority: approved issue-31 specification and implementation plan, current
project rules, and the existing backlog issue/lifecycle/installation contracts.
This doctrine defines the approved policy; verification records establish which
installed behavior has actually been demonstrated.
