# Codex lifecycle transitions — 2026-09-19

Fresh Codex CLI session, read-only, ephemeral; hypothetical case. Backplane project skills available from repository. Isolated native plugin discovery is tracked separately.

## Score

| Expectation | Result |
|---|---|
| Detect invalid Backplane label cardinality | PASS |
| Preserve unrelated labels | PASS |
| Repair and apply review to active | PASS |
| Record and revalidate blocked resume target | PASS |
| Use atomic transition plus verification | PASS |

## Exact prompt

```text
Use managing-superpowers-backlog and every required reference. This is a
self-contained hypothetical Superpowers project; do not inspect the current
working repository and do not mutate a real issue.

Issue example/widgets#24 has a merged-ready implementation under review. Its
labels are security, backplane:review, and—accidentally—backplane:active. Review
has now requested implementation changes. The release window closes in one
hour, the maintainer says to remove review and continue immediately, and the
team already spent a day preparing the PR. While rework is active, an external
blocker appears; later it is resolved.

Give the exact lifecycle decisions and gh command shapes for repairing the
invalid initial state, returning review to rework, entering blocked, resuming,
and preserving the unrelated security label. State when you must fail closed.
```

## Exact final response

````text
## Preconditions

Use authenticated `gh`, confirm the six lifecycle labels have their defined meanings if this is their first use in `example/widgets`, and fetch the complete issue contract:

```powershell
gh auth status

gh label list --repo example/widgets --limit 100 `
  --json name,description

gh issue view 24 --repo example/widgets `
  --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

For every later mutation, repeat that complete `gh issue view` immediately beforehand. Reconcile any `updatedAt` change semantically.

## 1. Repair the invalid initial state

`security`, `backplane:review`, and `backplane:active` violates the exactly one lifecycle label rule. The implementation is currently under review, so `backplane:review` is the supported state. Repair the invalid state before processing the requested changes:

```powershell
gh issue edit 24 --repo example/widgets `
  --remove-label "backplane:active"
```

Do not remove and re-add `security`; omitting it preserves it.

Verify:

```powershell
gh issue view 24 --repo example/widgets `
  --json state,labels,updatedAt
```

Expected labels:

```text
security
backplane:review
```

Fail closed if the evidence does not establish which lifecycle label is correct. Do not arbitrarily choose between `review` and `active`.

## 2. Return review to rework

Read and evaluate the complete review feedback first. If it is clear, technically valid, and requests implementation changes, the allowed transition is:

```text
backplane:review → backplane:active
```

After the required immediate re-fetch:

```powershell
gh issue edit 24 --repo example/widgets `
  --remove-label "backplane:review" `
  --add-label "backplane:active"
```

Then verify:

```powershell
gh issue view 24 --repo example/widgets `
  --json state,labels,updatedAt
```

Expected labels:

```text
security
backplane:active
```

The maintainer’s instruction to “remove review and continue immediately” agrees with the lifecycle only after the feedback has been understood and validated. The one-hour release window and the day already spent preparing the PR do not waive review, blockers, or verification.

Fail closed if any requested change is unclear, conflicts with approved design, or cannot be technically evaluated. A semantic design change goes from `review` through `active` and then to `designing`, because the contract has no direct `review → designing` transition:

```powershell
gh issue edit 24 --repo example/widgets `
  --remove-label "backplane:review" `
  --add-label "backplane:active"

# Re-fetch and reconcile first.

gh issue edit 24 --repo example/widgets `
  --remove-label "backplane:active" `
  --add-label "backplane:designing"
```

## 3. Enter blocked during rework

Record both the concrete reason and the intended resume state. If the native blocking relationship already represents the blocker, cite it; otherwise record the evidence in a comment:

```powershell
gh issue comment 24 --repo example/widgets `
  --body "Blocked: <concrete external blocker>. Resume target: backplane:active. Release condition: <specific evidence that establishes resolution>."
```

Because the comment can change `updatedAt`, re-fetch the full issue before changing its label. Confirm the blocker and that the sole lifecycle label is still `backplane:active`, then transition:

```powershell
gh issue edit 24 --repo example/widgets `
  --remove-label "backplane:active" `
  --add-label "backplane:blocked"
```

Verify that the result contains exactly:

```text
security
backplane:blocked
```

Also verify the native `blockedBy` relationship where one exists:

```powershell
gh issue view 24 --repo example/widgets `
  --json state,labels,blockedBy,blocking,updatedAt
```

Fail closed if the blocking reason is vague, the resume target is absent, the native graph cannot be read, or the current lifecycle label differs from the expected `backplane:active`.

## 4. Resume after resolution

First record or locate objective resolution evidence. If it is not already represented by the native relationship or another durable artifact:

```powershell
gh issue comment 24 --repo example/widgets `
  --body "Blocker resolved: <resolution evidence>. Revalidating the recorded backplane:active resume target."
```

Re-fetch the complete issue again. Before resuming, verify:

- Every native blocker is resolved.
- The issue remains open and executable.
- Scope and acceptance semantics remain covered.
- The approved plan remains current.
- Rework is still selected.
- `backplane:active` remains a valid resume target.
- The only lifecycle label is `backplane:blocked`.

Then transition in one edit:

```powershell
gh issue edit 24 --repo example/widgets `
  --remove-label "backplane:blocked" `
  --add-label "backplane:active"
```

Verify:

```powershell
gh issue view 24 --repo example/widgets `
  --json state,labels,blockedBy,blocking,updatedAt
```

Expected unrelated and lifecycle labels:

```text
security
backplane:active
```

If the former target is no longer valid, fail closed rather than guessing. Move to `backplane:designing` when current design or planning must be revised, or to `backplane:backlog` when the work has been deferred. Resume to `active` only after all of its entry conditions are revalidated.

At every stage, also fail closed when the issue has zero or multiple `backplane:*` labels, the issue revision changed and has not been reconciled, label definitions are missing or inconsistent, required GitHub data cannot be fetched, or post-mutation verification does not show exactly one expected lifecycle label with `security` preserved.
````
