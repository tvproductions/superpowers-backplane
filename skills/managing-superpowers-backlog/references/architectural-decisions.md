# Architectural decisions at Backplane checkpoints

Use this reference when a requested operation introduces a consequential choice
or consumes applicable architectural constraints. Read the project's actual ADR
policy/workflow, decision collection, approved records and retrievable approval
content. The project governs its language, conventions and tools; neither the
starter nor gz-skills is a required consumer dependency. Backplane preserves
references through its existing issue/spec/plan and evidence records.

## Reconcile the decision at the requested boundary

| Boundary | Required decision and action |
| --- | --- |
| Design/plan | Identify applicable ownership, dependency, interface, persistence, recovery, trust or operational choices. Cite and reuse covered approved decisions. Surface new/conflicting choices, alternatives, consequences and uncertainty through the project's ADR workflow; obtain separate explicit approval of its identified edition before dependent implementation. |
| Eligibility/start/transition | Re-read the complete native issue and reconcile its consumed design/plan revisions with the actual decision, edition, reviewed bytes and approval scope. A ready label or approved spec/plan supplies no missing ADR approval. Preserve every native eligibility, selection, blocker and mutation-authority gate. |
| Active execution | Recheck affected constraints when inputs or choices change. Pause only dependent work while a required choice/approval is unresolved; continue independent already-authorized tasks. Use existing blocked/resume semantics when the actual work-item condition warrants them, without inventing another lifecycle. |
| Review/closeout | Compare delivered behavior with applicable approved constraints despite green checks. Correct drift or obtain a separately approved replacement through the project workflow. Keep acceptance, integration, issue closure and publication at their existing separately authorized gates. |
| Checkpoint capture | Preserve exact decision/edition/content, applicability and actual approval using the mapping below. Check reference ownership and availability; retain partial/stale/UNKNOWN results where required. Capture acceptance or indexing does not approve architecture. |

For covered routine work, reuse the applicable decision without another ADR,
architectural approval request or restart of an already approved workflow.
Check the actual human response and recoverable reviewed edition/content; a
filename, hash, Current metadata, plan/release assent or lifecycle state alone
cannot establish approval. Preserve the original reviewed bytes and the source
context of any honestly transcribed interaction. Report missing or conflicting
content rather than inventing approval, history, URLs or empty successful results.

Requirements, plans, evaluations, decision editions and releases evolve
independently. Reconcile affected relationships after input changes; regrouping
unchanged work does not automatically revise a decision. Apply the project's
editorial, replacement and retirement rules. Preserve suitable existing naming
through an explicit semantic mapping. A new collection uses stable identity
ADR-[0-9]{4,} and edition filename ADR-[0-9]{4,}-[0-9]{3,}-<slug>.md, with
slug [a-z0-9-]+; widths are minimum padding, not overflow limits. These names
confer no authority and introduce no parser or bulk historical migration.

## Preserve references in the existing records

Use actual participating issue Superpowers Artifacts/Backplane Record sections,
plan constraints and the existing checkpoint/v1 collections. The consuming
issue/spec/plan remains its existing kind; the ADR remains decision authority.

| Meaning | Required existing representation |
| --- | --- |
| Decision and applicability | Consuming issue-body/specification/plan Authority.content names decision ID, edition, immutable locator/revision, applicable constraint and supporting evidence IDs. Preserve the same decision reference in its issue/plan context. |
| Reviewed ADR content | Evidence(kind=other) retains the reviewed content or available immutable reference, revision and SHA-256. Its content/limitations distinguish the reviewed proposal from any later administrative approval capture. |
| Actual architectural approval | Authority(kind=approval) identifies the human approver, exact reviewed decision/edition, accepted scope and retrievable interaction context. Reference that authority through the consuming authority's supported approval_ids. Evidence(kind=approval) preserves the actual response and reviewed-edition/content identity; name its evidence ID in the authority content. |
| Alignment evaluation | Evaluation.evidence_ids points to the appropriate available ADR, approval, verification and review Evidence records. Keep review_approval_ids for actual review-approval Authority records, independently of architectural approval. |
| Missing/conflicting/stale inputs | Existing availability, limitations, rechecks, result and applicability fields retain the observed gap. Preserve historical evaluations and actual source/delivery/storage identities; refresh affected claims before treating them as current. |

Every ID resolves in its proper typed collection. An authority ID belongs in
approval_ids; an evidence ID belongs in evidence_ids. Content explains the
reference and its meaning; a bare string pointer proves neither readability nor
approval. Keep Authority.kind exactly issue-body|specification|plan|approval|
project-instructions: no adr kind and no ADR relabelled as specification.
This mapping adds no schema field, enum, universal reference syntax, resolver,
approval store or service. Preserve all checkpoint/v1 pair, pagination, byte-digest,
semantic-validation, acceptance, user-edit and recovery requirements unchanged.
An absent approval can be captured honestly without becoming an approved choice;
a diagnostic cannot replace the last accepted pair as complete/current.

## Completion account

Record the policy/workflow source, actual decision/edition, reviewed content and
human approval context, applicable constraints, observed authorized continuation
and alignment result in the operation's existing evidence. Distinguish unavailable
content, local work, capture/storage acceptance, integrated satisfaction and
publication. Source/configuration presence proves neither native discovery nor
model behavior; preserve exact tested sources and limits when qualifying them.
