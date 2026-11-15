---
id: ADR-0001
title: Reference architectural decisions through existing Backplane checkpoints
revision: 1
state: Current
decision_date: 2026-11-15
revision_date: 2026-11-15
approved_by: "project maintainer in this conversation"
approved_revision: 1
approval_ref: "#approval-evidence"
---

# ADR-0001 edition 1 — reference decisions through existing checkpoints

Current decision. Separate explicit architectural approval is preserved below;
implementation, integrated acceptance and publication remain separate.

## Scope and context

Backplane coordinates native GitHub work around Superpowers using approved issue
designs/specifications, issue-bound plans, evaluations, evidence and dated
checkpoint pairs. Relevant architecture decisions must constrain that workflow
without becoming another mutable backlog or an architectural approval service.

The starter's [approved component design](https://github.com/tvproductions/gz-starter/blob/f42e6f186f062493c09fc2c2dc935e9a64310e33/docs/superpowers/specs/2026-11-08-adr-practice-design.md)
requires an owning Backplane contribution using existing supported records.
Its [architectural policy](https://github.com/tvproductions/gz-starter/blob/f42e6f186f062493c09fc2c2dc935e9a64310e33/docs/engineering/architectural-decisions.md)
supplies the approval/edition semantics proposed for this repository's binding.
Those approvals do not approve this Backplane edition.

Inspected baseline: `c1b63d8f72fba9996f0857120f8c97e9e8d5700d`, published
version 0.2.0. The checkpoint/v1 Authority enum has no ADR kind; Evidence already
supports other and approval. Unknown fields/kinds are rejected. Backplane's
governance and delivery lifecycles are independent of a decision's edition/state.

## Alternatives

1. Add only project instructions. This is small but leaves the shipped backlog
   checkpoints without an explicit portable integration/evidence contract.
2. Add a focused integration reference at existing checkpoints and preserve ADR
   references with existing authority/evidence fields. This keeps the current
   lifecycle and wire contract, but requires explicit content mapping and actual
   agent qualification rather than claiming a typed resolver validates decisions.
3. Introduce typed ADR checkpoint records, a registry or approval-event store.
   This improves machine-addressable structure at the cost of new schema,
   migration, persistence and authority responsibilities outside this increment.

## Decision and rationale

Choose alternative 2. Keep each project ADR as decision authority, with actual
approval and edition history embedded or durably referenced there. Backplane
consumes that authority at its existing design, plan, eligibility/start,
execution, review/closeout and checkpoint-capture boundaries.

Represent decision ID/edition/applicability and immutable locator in existing
issue/spec/plan authority content. Preserve reviewed decision bytes through
Evidence(kind=other), actual approval through Authority(kind=approval) and
Evidence(kind=approval), and alignment through existing evaluation/review fields.
Use each existing typed reference only for its defined collection. Keep ADR
approval distinct from review approval. Do not invent Authority.kind=adr or
misclassify the ADR as a specification. The paired readable checkpoint must
preserve the same meaning, exact sources and limitations.

Do not add fields, resolver, ledger, approval service, transaction mechanism or
generic ADR procedure/template. gz-skills owns the portable procedure/template;
Backplane consumes the project's selected workflow without requiring gz-skills
or the starter from unrelated consumers. Do not adopt the starter bundle here.

Missing/conflicting load-bearing ADR approval stops dependent implementation,
while independent authorized work may proceed. Reuse applicable approved
decisions without duplicate ADRs or architectural approval requests. Indexing,
ready/active labels, a spec/plan, green checks, merge, capture acceptance and
release assent confer no architectural approval. Changed requirements, plans
and release grouping do not automatically amend a still-applicable decision.

## Consequences and uncertainty

The integration remains instruction/reference based. Native schema validation
can check structure, but cannot prove human approval or an agent's behavior.
Require exact-source stop/continue controls, alignment review, qualified record
mapping and stated supported-host scope. Unavailable policy/workflow/approval
content limits dependent claims; preserve historical evidence and disclose gaps.

Keep the existing six lifecycle labels, native relationships, checkpoint pair and
recovery semantics. No automatic conversion, bulk historical ADR backfill,
matching component versions or approval cascade follows. Future typed ADR
support would be separately designed/versioned work requiring its own decision.

## Confirmation

After separate approval, use this decision genuinely in the owner implementation
and review its alignment. Preserve the exact implementation/evaluation/release
sources in ordinary owner evidence; do not accumulate test logs inside the ADR.
The [integration design](../superpowers-backplane/specs/2026-11-15-architectural-decision-integration-design.md)
defines proposed checkpoints and acceptance. No verification or release result
is claimed by this draft.

## Approval evidence

See the [actual approval capture](approvals/ADR-0001-001-approval.md) and exact
[preserved reviewed proposal](approvals/ADR-0001-001-reviewed.txt), SHA-256
`5a39dcb0db8553af4a30d4acdbd57461c9a62d9a2f72da285caa57ceb0630d7b`. The separate explicit human response approves edition 1;
metadata and content hashes do not create approval.

## Edition history

Edition 1, November 15, 2026: original proposal separately approved by the
project maintainer in this conversation. Administrative capture creates this
Current record while preserving the reviewed bytes and actual interaction.
No material architectural replacement or retrospective approval is asserted.
