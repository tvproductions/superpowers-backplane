# Heavy SDD Trace and V&V Evidence

SP-BP's Python core owns the implemented forward/reverse reconciliation and V&V decision rules. This reference is the workflow and schema contract; an agent or thin host adapter must not become a second trace engine. Until the Python trace/evidence modules and installed invocation are verified, report computed claims as provisional and do not claim the integrated heavy gate is ready.

Use this contract only after the heavy profile and approved governing documents have been established under [the heavy issue record contract](heavy-issue-record.md). The approved project PRD owns requirement IDs, wording, approval, users, and success criteria. GitHub issues anchor those requirements and planned outcomes. Superpowers owns feature specs and plans. Backplane reconciles their links and evidence; it does not change another owner's authority.

## Build both directions from one validated graph

Collect the approved PRD revision, complete native issue intake, all required `## Backplane Record` blocks, linked SP specs/plans and ADR revisions, agreed concrete behavior examples, test or demonstration definitions, evidence artifacts, and release records. Validate semantic ID uniqueness and typed-link endpoints first. Compute reverse links from the one directional record; do not maintain independent reverse text. Present at least these columns for each requirement/outcome relation: requirement ID and approved PRD revision, anchor issue URL, outcome ID and issue URL/revision, `satisfies` link, examples, test definitions, verification evidence, validation evidence if applicable, release selection, and current/stale/missing/ambiguous/unknown finding.

A requirement may govern several outcomes; an outcome may claim several requirements. Evaluate each edge independently. `satisfies` is a delivery claim, `exemplified_by` is an agreed behavior definition, and `tested_by` identifies a check. None is a passing result. A `verified_by` or `validated_by` link points to an evidence artifact; the link alone does not certify its content. For any absent or conflicting edge, show the gap in both forward and reverse views rather than choosing one convenient path.

## Evidence record

Evidence can be a committed project report or an immutable CI/test/demonstration artifact. An editable issue comment may explain a result but cannot stand alone as immutable evidence. The `verified_by` or `validated_by` link target contains the artifact `locator` and immutable `revision`. The artifact carries one `## Backplane Evidence` fenced JSON block. The project may include prose, logs, and links outside the block, but the block has the required decision fields:

````markdown
## Backplane Evidence

```json
{
  "schema": "backplane-evidence/v1",
  "kind": "verification",
  "method": "test",
  "result": "pass",
  "observed_at": "2026-09-27T00:00:00Z",
  "integrated_source": "0123456789abcdef0123456789abcdef01234567",
  "requirements": [{"semantic_id": "R-1", "prd_revision": "P1"}],
  "outcomes": [{"semantic_id": "C2.3", "issue": "https://github.com/OWNER/REPO/issues/32", "issue_revision": "2026-09-27T00:00:00Z"}],
  "success_criteria": [],
  "users": [],
  "accepted_by": "reviewed-human-or-project-authority"
}
```
````

`kind` is `verification`, `validation`, or `impact_review`. `method` is the project's named test, demonstration, analysis, inspection, stakeholder review, or measurement; a test framework is never mandated. `result` is `pass`, `fail`, or `unknown`. `observed_at` is an ISO-8601 UTC time. `integrated_source` is the exact reviewed Git commit or immutable deployed build identity, not a branch name. `requirements` and `outcomes` list every claim this artifact covers, not every relation in the product. Each requirement entry has its semantic ID and approved PRD revision; each outcome entry has its ID, issue URL, and issue revision consumed. `success_criteria` contains PRD criterion IDs or exact reviewed locators, and `users` contains the intended user groups used in a validation. `accepted_by` identifies the project's named person who accepted the result; it cannot be the agent's own self-approval. Unknown or unavailable identity is an `unknown` result for gate purposes.

Verification requires at least one requirement and one outcome entry, a method, the actual result, exact integrated source, artifact locator/revision, and acceptance identity. Validation requires at least one PRD user group and success criterion, the intended-use method and result, exact integrated source, locator/revision, and accepting person; it remains separate even if a test was also used. An `impact_review` names old and new PRD revisions in its `requirements` entries, the affected edges/evidence locators, whether each remains applicable, and its accepting person. A format extension needs a reviewed schema revision; never silently guess omitted fields.

## Currency and outcome decision

Classify each requirement-to-outcome edge and its evidence:

| Finding | Condition |
| --- | --- |
| `current` | Approved PRD identity/revision, outcome meaning and issue revision, link endpoints, evidence artifact revision, integrated source, result, and acceptance all match; a passing result covers this exact claim. |
| `missing` | A required link, example, check, or passing evidence is absent from an otherwise validated snapshot. |
| `stale` | A known source changed after the recorded evidence or link; impact review or re-verification has not established its applicability to the new approved revision. |
| `ambiguous` | Duplicate IDs, conflicting links, incompatible endpoint kinds, or multiple inconsistent source revisions prevent one interpretation. |
| `unknown` | The source, permission, artifact, revision, approval, or result cannot be checked. Lack of network access is `unknown`, not `current`. |

`updatedAt` is a change detector. A changed issue timestamp triggers comparison of its actual semantic fields and links; an editorial change already covered by the evidence may be reconciled and recorded without rerunning a test. A changed approved requirement always triggers impact analysis of every linked outcome, example, test definition, design, plan, evidence artifact, view, and later release. Old evidence remains historical. It can support a new revision only through a new reviewed impact record that explicitly concludes the evidence remains applicable, with old/new PRD revisions and rationale; otherwise gather new verification. A changed meaning needs a new semantic ID and cannot be cleared by editorial reconciliation.

An outcome is `verified` only when every governing requirement it claims has current passing verification for that outcome on integrated source **and** the outcome's own acceptance criteria have current evidence. A `fail`, `missing`, `stale`, `ambiguous`, or `unknown` edge prevents that claim. An issue closed as completed, an approved plan, a passing test for only one requirement, or a release candidate assignment does not substitute. A release is `validated` only when a separate current passing validation artifact checks intended use against the PRD's users and success criteria and names its accepting person. Verification does not imply validation, and validation does not repair missing verification.

## Read-only reconciliation and mutation

Status, trace, and release-candidate review are read-only. Fetch complete `gh` fields and approved documents, validate records, compute both directions, then report each edge and evidence finding with source revisions. Do not mutate an issue or PRD to make a trace pass. If a link or evidence change is authorized, re-read all affected sources, apply only the reviewed relation/evidence update, preserve history, then re-fetch and re-score. An issue edit never approves changed PRD wording. A derived trace or view may summarize this result but cannot become a second requirement or issue authority.
