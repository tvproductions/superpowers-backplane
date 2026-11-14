# Lite records and structured Git commits: paired design

Date: November 14, 2026. Status: proposed for joint review; not approved or
implemented. The maintainer explicitly authorized designing this simultaneously
with the starter in the local Backplane checkout. This document grants no
implementation, issue mutation, installation, commit/push or publication authority.
Architectural choices need separate approval of their identified ADR edition.

## Purpose and owning boundaries

Keep the starter's lite records aligned with Backplane management meanings while
preserving a small file-based implementation. Lite may remain permanent; heavy
means explicit adoption of verified Backplane management. Retain Superpowers as
the feature inner loop. Maintain philosophical alignment only with gzkit; add
no integration, permanent ledger, SQLite or Dolt dependency.

Backplane owns native work/lifecycle, requirement/criterion coverage, evidence
semantics, handoffs and mode definitions. The starter owns its JSON sidecar and
Markdown representation, opinionated engineering rules, commit wire format and
enforcement. The starter follows reviewed Backplane design, records mappings and
reconciles evolution; it does not define Backplane law from a private fork.
Backplane may improve its shared structure through this owning design process.
Do not impose starter-specific file names, Python tools or commit policy on
unrelated Backplane consumers.

The starter remains the current shared release-policy alignment source under
docs/release-policy.md. The November 7 release-doctrine transfer remains proposed;
this draft neither activates it nor replaces earlier approved contracts.

## Paired candidate and provenance

Paired starter repository: tvproductions/gz-skills-first-starter, draft path
`docs/superpowers/specs/2026-11-14-lite-record-and-commit-contract-draft.md`.
Both documents are working-tree candidates, not published source guarantees.
The starter base is 8c8ff4b plus separately identified local changes; Backplane
base is 05505f8009989eb7514ec62750e33c78bc40abf9. Source hashes and verification
observations belong in the HANDOFF continuation, outside the paired documents
to avoid circular content identity. Recheck final committed sources before
published alignment claims.

Reviewed authorities: governance.md, modes.md, the native GitHub issue contract,
repository-checkpoint.md, checkpoint-format.md, handoff-contract.md and the
November 7 release-doctrine discussion. Existing published v0.2.0 engineering
acceptance remains historical at its own exact inputs.

## Alternatives and selected direction

The maintainer selected current-state JSON sidecars, Markdown narrative/views,
a hand-written changelog, Git history and bounded local recovery. A permanent
JSONL event store would add replay/projection responsibilities; SQLite/Dolt would
introduce a different persistence authority. Those alternatives are excluded.

Recommend a shared semantic contract with two representations: lite local files
and heavy native GitHub plus approved project artifacts. Reusing checkpoint/v1
unchanged as a mutable lite store would confuse captured observations with live
authority. Maintaining separate unrelated meanings would defeat safe promotion.

## Minimum semantic correspondence

| Meaning | Lite owner | Heavy owner/correspondent |
| --- | --- | --- |
| Governing obligations, statement keys and revisions | Requirements records, with actual authority/approval references | Approved project docs/issues; Requirement/Authority semantics |
| Outcome identity/kind, bounded scope and work criteria | Backlog records | Native issue plus Backplane Record and executable body |
| Parentage, blockers, priority and lifecycle | Backlog records; each meaning explicit | Native hierarchy/dependencies, project priority and existing lifecycle contract |
| Capability progression and forecasts | Roadmap records | Capability/outcome decomposition and target groupings/views |
| Selected execution and task progress | Work records and approved plans | Issue-bound Superpowers plan, PR contributions and handoff context |
| Coverage, satisfaction and scope dispositions | Typed references to exact criteria/evaluations; governed current pointers | Coverage and Satisfaction / Obligation Dispositions plus immutable evaluations |
| Bounded release selection, classification and publication | Releases records under adopted project policy | Project release authority and native targets/actual releases; expanded portable release schema remains pending |
| Human-facing change history | Hand-written CHANGELOG.md | Same repository document |

The minimum invariants are stable identities, explicit governing revisions,
many-to-many coverage, exact evaluated inputs and one owner per mutable fact.
Reuse capability/outcome/gate/external-boundary kinds; the six open lifecycle
meanings and completed/not-planned closure reasons; and SATISFIED/UNSATISFIED/
UNKNOWN satisfaction. Deferred/excluded/unresolved scope is a separate dimension.
Keep parentage, execution dependency and priority distinct. No task checkbox,
commit, closure or milestone establishes satisfaction or publication authority.

BACKLOG owns outcome lifecycle; WORK references it and owns selected plan-task
progress. A roadmap target is not selected release membership. Current pointers
do not overwrite immutable historical evaluations. Generated views never become
another mutable master. No requirement hierarchy or redundant work layer is
mandatory merely to resemble a diagram.

## Proposed reference contract

RecordRef has exactly namespace and id, both nonempty strings. Stable IDs are
unique across a project's namespace; existing IDs/aliases must be preserved or
mapped explicitly. A reference identifies the record, not an approval/version.

SourceRef has exactly locator (nonempty string), revision (string or null),
record_id (string or null), and availability (available/unavailable/redacted).
Known revisions use git-commit:<full-lowercase-oid>, git-blob:<full-lowercase-oid>
or sha256:<64-lowercase-hex>. Git OIDs use their actual 40/64-character object
format. Locators identify the source repository/path or other actual source;
record_id selects an internal named record where applicable. Retain known IDs
when access fails, but missing readable approval/evidence cannot support an
accepted dependent claim. Hashes identify content; actual human action approves it.

These are proposed semantic interfaces for the paired design, not a silent edit
to the exact existing checkpoint/v1 field set. Adapters must map into existing
published contracts, or version/amend those contracts through reviewed owning
changes. Reject unknown schemas/fields and invalid references rather than
silently dropping information. No Pydantic runtime or model package is selected
for consumers by this document.

## Commit record correspondence

The maintainer requested a small typed JSON record in every governed new commit.
The starter's proposed transport is one Starter-Record Git trailer containing
one compact JSON object. Its proposed five keys are format, kind, records,
evidence and reason; format is skills-first-commit/v1, records use RecordRef and
evidence uses SourceRef. Kind describes change category, not SemVer. Its exact
enum, serialization and 8,192-byte payload limit belong to the starter binding.

Backplane can consume such change/evidence references as contributions without
making them issue lifecycle authority or requiring that binding from unrelated
consumers. Own-project adoption remains prospective and explicit after schema/
ADR review. No retrospective message rewrite or commit-policy activation occurs
here. Git supplies commit/tree/parent identity; do not insert a commit's future
SHA into its own record. Post-commit CI and publication results arrive later.

Preserve the existing four routine checks: Ruff check/format, ty and unittest.
Do not install another hook. Determine prospective adoption, CLI preparation and
actual-commit integration acceptance explicitly. A typed message is neither
semantic approval nor proof of evidence truth. Merge/squash/revert/automation
behavior and copied metadata need explicit conformance cases.

## Recovery and promotion

Use the starter's proposed bounded local recovery for lite writes: prepare and
validate a candidate, preserve exact starting/proposed bytes before replacement,
guard input changes, verify final state and inspect interruptions before further
mutations. All-proposed outputs may finalize after revalidation; all-starting
outputs may discard; a verified mixed state may restore exact starting bytes.
Independent edits or unexplained input changes stop automatic recovery. Never
reset the workspace over pre-existing uncommitted work. Keep successful recovery
scratch disposable and durable continuation/evidence in tracked authorities.

This resembles Backplane's existing guarded checkpoint acceptance but does not
claim multi-file filesystem or remote API atomicity. Existing checkpoint
acceptance still uses its verified pair commit; ordinary lite field edits do
not require a new commit/full suite each time. Git history records coherent
committed snapshots, not every uncommitted operation or authenticated approval.

Promotion is an explicit reviewed transfer: inventory local requirements/work,
map stable keys to observed native IDs, preserve criteria/revisions/approvals/
evidence and unresolved scope, verify actual arrival, then switch field owners.
GitHub-owned fields become projections in retained local views. Do not maintain
dual mutable masters or replay an offline checkpoint into GitHub. No converter
or fully qualified shared roadmap/release schema currently exists for these files.

## Completion and next review

Before implementation, reconcile the exact starter models and this semantic
contract, assign narrative/field ownership, define schema upgrades and prospective
commit-policy adoption, and obtain separately identified ADR approvals. Preserve
existing native IDs, contracts and user work. Shared conformance must cover both
positive transfer and rejected missing/stale/ambiguous evidence, unknown IDs,
criteria revision changes, lifecycle/satisfaction separation, interrupted writes,
independent edits and actual resulting commit metadata.

Published baseline remains v0.2.0. This local design-only change leaves all
version mirrors unchanged. Future new workflow capability is minor scope under
the existing policy, with its own bounded work/release accounting before an
implementation plan is accepted. It does not silently join a historical release.
No issues/labels, models, hooks, dependencies, native installs, commits, pushes,
tags or releases change through this draft. Current Backplane requires
GitHub/gh. No additional hosting target is defined.
