# REFACTOR Scenario: Lifecycle Transitions

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

## Acceptance expectations

- Detect multiple `backplane:*` labels and fail closed before transition.
- Preserve `security` and other unrelated labels.
- Repair to the evidence-supported review state, then use review to active for
  requested changes.
- Record `Resume target: backplane:active` when entering blocked.
- Revalidate active entry gates before blocked to active.
- Use atomic remove/add commands and verify state after each mutation.

## Result

PASS on 2026-08-16 in a fresh Codex subagent context. The exact model identifier
was not exposed by the harness. The agent detected the invalid dual lifecycle
labels, repaired to the evidence-supported review state, preserved `security`,
used review to active for requested changes, recorded active as the blocked
resume target, revalidated before resumption, used atomic transitions, and
listed fail-closed conditions.

Response record:
`transcripts/2026-08-16-lifecycle-transition-refactor-response.md`

| Expectation | Score |
|---|---|
| Detect invalid Backplane label cardinality | PASS |
| Preserve unrelated labels | PASS |
| Repair and apply review-to-active | PASS |
| Record and revalidate blocked resume target | PASS |
| Use atomic transition plus verification | PASS |

Skill content hashes used for this run are recorded in
`2026-08-16-native-issue-intake-green.md`.
