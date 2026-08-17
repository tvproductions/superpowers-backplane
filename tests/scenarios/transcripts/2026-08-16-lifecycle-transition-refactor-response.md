# Lifecycle REFACTOR Response Record

The fresh agent chose this sequence:

1. Repair the invalid initial state, keeping `backplane:review`.
2. Transition `review -> active` when review requests implementation changes.
3. Transition `active -> blocked` when the external blocker appears, recording
   `active` as the resume target.
4. Revalidate and transition `blocked -> active` after resolution.
5. Preserve `security` by editing only lifecycle labels.

It required the full native issue intake before each mutation and `gh label
list` before first lifecycle use. It refused to process the requested-changes
transition until the multiple lifecycle labels were repaired and verified.

The repair removed only `backplane:active`, retained the evidence-supported
`backplane:review`, and verified that `security` remained. It then used one
`gh issue edit` invocation to remove review and add active.

For blocking, it used one transition from active to blocked and required this
comment shape:

```text
Blocked: <concrete external blocker>. Resume target: backplane:active. Release
condition: <objective condition proving the blocker is resolved>.
```

It re-fetched the issue, reconciled revision drift, checked native blockers,
and revalidated active-entry gates before resuming. It explicitly failed closed
for zero or multiple lifecycle labels, unresolved revision drift, missing
native fields, ambiguous repair state, incomplete blocker evidence, failed
authentication, missing labels, or post-mutation verification failure.

This response record preserves every scored decision and command shape. The
harness did not expose a durable verbatim-message URI.
