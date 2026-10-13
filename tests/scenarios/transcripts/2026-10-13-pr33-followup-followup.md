Both observations fit the shipped [checkpoint format](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/checkpoint-format.md). No schema extension is needed. These are record fragments, not complete checkpoint documents.

**A — partial PR capture**

Using the shipped invented example’s available PR attributes, retain this complete `PullRequest` record:

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

Corresponding `scope.collections` entry:

```json
{
  "name": "closingIssuesReferences",
  "owner_id": "example/governance-fixture!201",
  "expected_total": null,
  "pages": [],
  "complete": false
}
```

Required `capture.rechecks` entry:

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

Set `capture.status` to `"partial"`, `capture.origin` to `"invented-fixture"`, and `scope.complete` to `false`; preserve the declared mode. Include the denied membership in whole-capture `limitations`.

The supported next step is diagnostic retention and, in a separately authorized capture, obtaining complete native membership pages and rechecking them. Neither body prose nor issue-side references supplies the missing membership. This diagnostic cannot replace an accepted pair as complete/current.

**B — complete integrated fixture capture**

Within P1’s `field_definitions`, retain this exact `Field`:

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

Within I1’s `fields`, with I1’s `content_id` retained as `"example/governance-fixture#101"` and `content_kind` as `"issue"`, retain this exact `FieldValue`:

```json
{
  "field_id": "F1",
  "text": "Review",
  "option_id": "OPTION_REVIEW",
  "availability": "available"
}
```

On the stipulated complete, unchanged inputs and agreeing projections, use `capture.mode: "integrated"`, `capture.status: "complete"`, `capture.origin: "invented-fixture"`, and `scope.complete: true`. This observation introduces no limitation. The selected identity resolves within F1 and matches its observed display name.

The supported next step is read-only validation of the full candidate and readable rendering, preserving P1/I1/F1, `OPTION_REVIEW`, and `Review`. Complete capture establishes a dated account; it does not itself establish delivery satisfaction or acceptance.

No agents, live queries, helpers, mutations, checkpoint acceptance/publication, or recovery were performed.