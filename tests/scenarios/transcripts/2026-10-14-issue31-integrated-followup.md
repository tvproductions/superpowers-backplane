Both observations are representable in the shipped [`sp-bp-checkpoint/v1` format](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/checkpoint-format.md). No schema extension is needed. The fragments below are separate record objects, not whole checkpoints.

**A — partial capture**

Using the shipped invented example’s available PR scalar values, retain this exact `PullRequest` shape:

```json
{
  "id": "example/governance-fixture!201",
  "number": 201,
  "url": "https://github.com/example/governance-fixture/pull/201",
  "title": "Preservation contribution",
  "body": "Refs #101; contributes AC1 at S1.",
  "state": "MERGED",
  "base_ref": "main",
  "head_ref": "fixture-preservation",
  "merged_at": "2026-10-01T11:00:00Z",
  "merge_commit": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
  "review_status": "accepted",
  "closing_issue_ids": null,
  "closure_intent": "contribution",
  "updated_at": "2026-10-01T12:00:00Z",
  "limitations": [
    "closing_issue_ids unavailable: native closingIssuesReferences query denied; membership unknown."
  ]
}
```

The corresponding `scope.collections` entry is:

```json
{
  "name": "closingIssuesReferences",
  "owner_id": "example/governance-fixture!201",
  "expected_total": null,
  "pages": [],
  "complete": false
}
```

The required `capture.rechecks` entry is:

```json
{
  "kind": "graph",
  "id": "example/governance-fixture!201:closingIssuesReferences",
  "initial_revision": null,
  "final_revision": null,
  "result": "unavailable",
  "approval_ids": [],
  "details": "Native closingIssuesReferences query denied; membership and stability could not be checked."
}
```

Set `capture.status` to `"partial"`, `capture.origin` to `"invented-fixture"`, and `scope.complete` to `false`. Include the denied connection in whole-capture `limitations`:

```json
[
  "example/governance-fixture!201:closingIssuesReferences unavailable; closing-issue membership and graph recheck are unknown."
]
```

Preserve the declared capture mode. Neither body text nor issue-side references can supply the missing PR-side membership.

Supported next action: retain a clearly labeled diagnostic; under a later authorized capture, obtain native membership, enumerate its pages, and recheck it before reconsidering completeness. This partial candidate cannot replace an accepted pair as complete/current.

**B — complete invented integrated capture**

For Project P1, retain this `Field` object:

```json
{
  "id": "F1",
  "name": "Status",
  "type": "SINGLE_SELECT",
  "options": [
    {
      "id": "OPTION_REVIEW",
      "name": "Review"
    },
    {
      "id": "OPTION_DONE",
      "name": "Done"
    }
  ]
}
```

Within Item I1’s `fields` array, retain this exact `FieldValue`:

```json
{
  "field_id": "F1",
  "text": "Review",
  "option_id": "OPTION_REVIEW",
  "availability": "available"
}
```

Item I1’s `content_id` remains `"example/governance-fixture#101"`. The selected identity resolves within F1, and its observed display text agrees.

Under the supplied complete/unchanged conditions, use `capture.mode: "integrated"`, `capture.status: "complete"`, `capture.origin: "invented-fixture"`, `scope.complete: true`, and whole-capture `limitations: []`. The readable account must preserve P1/I1/F1, `OPTION_REVIEW`, and `Review`.

Supported next action: read-only validation of the full candidate and its readable counterpart, including exact fields, references, pagination, rechecks, and semantic agreement. Complete capture establishes a dated account; it does not establish delivery satisfaction or checkpoint acceptance.

No live queries, mutations, helpers, agent dispatch, acceptance, publication, or recovery were performed.