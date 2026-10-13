Neither requested observation has a fully conforming representation in shipped `sp-bp-checkpoint/v1`. These are format gaps.

**A — denied PR closing relationships**

The conforming `Collection` record is:

```json
{
  "name": "closingIssuesReferences",
  "owner_id": "example/governance-fixture!201",
  "expected_total": null,
  "pages": [],
  "complete": false
}
```

Capture status is `partial`, origin is `invented-fixture`, and scope completeness is `false`. A suitable whole-capture limitation is:

```json
{
  "limitations": [
    "example/governance-fixture!201 closingIssuesReferences was denied; closing-issue membership is unknown."
  ]
}
```

**No conforming partial `PullRequest` record can retain this observation.** The exact format requires `closing_issue_ids: ID[]`, without allowing null. Therefore:

- `null` violates its type.
- `[]` falsely reports observed empty membership.
- Omitting the field violates the required-field rule.
- Omitting the scoped PR loses the known record.

The available PR identity, number, URL, title/body/state must remain in the raw diagnostic until a conforming representation is possible. The operation’s unavailable-collection guidance cannot override the nonnullable type. See the [PullRequest definition]( /Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/checkpoint-format.md:59).

**B — observed single-select identity**

Using explicit fixture namespaces (`field:F1` and `option:<native optionId>`), the conforming field definition is:

```json
{
  "id": "field:F1",
  "name": "Status",
  "type": "SINGLE_SELECT",
  "options": [
    {
      "id": "option:OPTION_REVIEW",
      "name": "Review"
    },
    {
      "id": "option:OPTION_DONE",
      "name": "Done"
    }
  ]
}
```

The conforming `FieldValue` for P1’s item I1, backed by `example/governance-fixture#101`, is:

```json
{
  "field_id": "field:F1",
  "text": "Review",
  "availability": "available"
}
```

This retains the display text, **but cannot retain the observed selected `optionId` as part of the field value**. The definition preserves available options; it does not encode which option identity I1 selected. Matching “Review” to a definition does not preserve the actual source observation.

`FieldValue` has exactly three fields, so adding `option_id`, embedding an object in `text`, or substituting the option ID for “Review” would violate the contract or change the projection. See the [FieldValue definition]( /Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/checkpoint-format.md:52).

B’s supplied source observations meet the complete/unchanged gates. The remaining problem is representational, not missing access or stale data. No conforming complete candidate satisfying the requested identity retention can be produced; an extended candidate would be `invalid`.

Supported next actions are to preserve these findings and raw fixture observations as diagnostics, and propose explicit contract reconciliation for both gaps. A future authorized recapture could also resolve A’s denied membership. Neither diagnostic replaces an accepted checkpoint. No live queries, mutations, helpers, acceptance, publication, or recovery were performed.