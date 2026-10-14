Both observations fit the shipped [checkpoint format](./skills/managing-superpowers-backlog/references/checkpoint-format.md), `sp-bp-checkpoint/v1`. No schema extension is needed.

These are relevant JSON fragments, not complete checkpoint objects. Other required fields retain their observed values; A’s available title/body/state literals were not supplied, so they are not invented below.

**A — partial PR capture**

```json
{
  "capture": {
    "status": "partial",
    "origin": "invented-fixture",
    "rechecks": [
      {
        "kind": "graph",
        "id": "example/governance-fixture!201:closingIssuesReferences",
        "initial_revision": null,
        "final_revision": null,
        "result": "unavailable",
        "approval_ids": [],
        "details": "Native closingIssuesReferences query denied; membership unavailable."
      }
    ]
  },
  "scope": {
    "complete": false,
    "collections": [
      {
        "name": "closingIssuesReferences",
        "owner_id": "example/governance-fixture!201",
        "expected_total": null,
        "pages": [],
        "complete": false
      }
    ]
  },
  "pull_requests": [
    {
      "id": "example/governance-fixture!201",
      "number": 201,
      "url": "https://github.com/example/governance-fixture/pull/201",
      "closing_issue_ids": null,
      "limitations": [
        "closing_issue_ids unavailable: native closingIssuesReferences query denied; membership unknown."
      ]
    }
  ],
  "limitations": [
    "PR example/governance-fixture!201 closingIssuesReferences membership is unavailable; capture is partial."
  ]
}
```

Retain all available PR fields alongside this fragment. `pages: []` means no pages were observed; it does **not** establish empty membership. Neither issue-side references nor body keywords can fill the denied connection.

Supported next action: retain the partial diagnostic. A future authorized recapture must observe the connection’s membership, pagination and graph recheck before claiming completeness. It cannot replace an accepted pair as complete/current.

**B — complete integrated fixture capture**

```json
{
  "capture": {
    "mode": "integrated",
    "status": "complete",
    "origin": "invented-fixture"
  },
  "scope": {
    "complete": true
  },
  "project": {
    "id": "P1",
    "field_definitions": [
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
    ],
    "items": [
      {
        "id": "I1",
        "content_id": "example/governance-fixture#101",
        "content_kind": "issue",
        "fields": [
          {
            "field_id": "F1",
            "text": "Review",
            "option_id": "OPTION_REVIEW",
            "availability": "available"
          }
        ]
      }
    ],
    "limitations": []
  },
  "limitations": []
}
```

The selected identity is the observed `OPTION_REVIEW`, resolving within F1; `Review` preserves its observed display text. Given the stated complete, unchanged sources and agreeing projections, B supports `complete` capture status. That status does not establish satisfaction, eligibility or acceptance.

Supported next action: preserve both identity and display text in any readable rendering and assess pair consistency. No live acceptance, publication or recovery was performed or authorized.