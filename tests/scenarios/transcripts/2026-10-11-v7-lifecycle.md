The lifecycle is **invalid → review → active → blocked → active**. The deadline, maintainer pressure, and day spent preparing the PR do not waive any gate. Keep `security` throughout.

These are hypothetical command shapes; I executed no GitHub commands.

Before real use, require authenticated `gh`, an operational compatible Superpowers installation, and all six lifecycle labels with matching descriptions:

```text
gh auth status
gh label list --repo example/widgets
```

Missing labels require separately authorized creation.

Before **each mutation**, fetch the complete issue contract:

```text
gh issue view 24 --repo example/widgets --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

Fetch discussion when needed to establish review requests or blocker evidence:

```text
gh issue view 24 --repo example/widgets --comments
```

Reconcile `updatedAt` changes against the revision consumed by the plan. After every edit, repeat the full intake query and verify exactly one expected Backplane label and unchanged unrelated labels.

1. **Repair the invalid initial state first.** Two lifecycle labels are invalid, so stop ordinary transitions. The scenario identifies `active` as accidental and establishes that the implementation is under review. Restore the single valid `review` state:

   ```text
   gh issue edit 24 --repo example/widgets --remove-label "backplane:active"
   ```

   Verify labels are `security` and `backplane:review`. Record the repair rationale in a comment if it is not already evidenced. Do not combine this repair with the subsequent rework transition.

2. **Return review to implementation rework.** Re-read the repaired issue and confirm the implementation-change request and that the existing design and plan still cover the work. Then swap labels in one invocation:

   ```text
   gh issue edit 24 --repo example/widgets --remove-label "backplane:review" --add-label "backplane:active"
   ```

   Removing `review` alone would create invalid zero-label state. If the requested changes invalidate design or plan authority, reconcile through the applicable Superpowers workflow before continuing execution.

3. **Enter blocked when the external blocker stops progress.** Record the concrete reason, the prior valid state, and an observable release condition:

   ```text
   gh issue comment 24 --repo example/widgets --body "Blocked: <concrete external condition>. Resume target: backplane:active. Release condition: <specific evidence required to resume>."
   ```

   Re-read after the comment, reconcile the timestamp change, then:

   ```text
   gh issue edit 24 --repo example/widgets --remove-label "backplane:active" --add-label "backplane:blocked"
   ```

   Use native blocking relationships where applicable; prose must not substitute for an available native relationship.

4. **Resume only after resolution and gate revalidation.** Re-read the issue, verify the recorded release condition, reconcile revisions, and revalidate every entry gate for `active`: approved current design and plan, executable scope, selection, resolved blockers, and execution actually resuming. Record resolution evidence if it is not already represented by native or committed evidence, then re-read before editing:

   ```text
   gh issue edit 24 --repo example/widgets --remove-label "backplane:blocked" --add-label "backplane:active"
   ```

   If `active` is no longer valid, choose `designing` or `backlog` according to current evidence, removing `blocked` and adding that target in one invocation. Never guess the resume state.

**Fail closed** on zero or multiple lifecycle labels until an evidence-backed repair is verified; unavailable required intake fields; failed authentication or unknown upstream compatibility; unreconciled revision drift; missing transition evidence; unresolved blockers; an unknown resume target; failed target gates; or failed post-mutation verification. Pressure and sunk effort cannot override these failures.

Every command above changes only named Backplane labels, preserving `security`. “Merged-ready” does not establish completion: keep the issue open until integrated delivery satisfies acceptance criteria and fresh project-owned verification.