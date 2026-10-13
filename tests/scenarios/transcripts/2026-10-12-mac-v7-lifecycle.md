The hypothetical sequence is **invalid labels → repaired review → active rework → blocked → active**, with `security` preserved throughout.

I read the inventory-listed `using-superpowers`, its Codex reference, `managing-superpowers-backlog`, and all three backlog references: `github-issue-contract.md`, `superpowers-binding.md`, and `installing-superpowers.md`, plus required governing instructions. Live authentication, installation provenance, and full compatibility remain **unknown**; they were not probed. All commands below are hypothetical.

Before operating, check prerequisites:

```bash
gh auth status
gh label list --repo example/widgets --json name,description
gh issue edit --help
gh issue close --help
```

Require all six lifecycle labels with correct meanings and supported CLI capabilities. Missing labels require separately authorized creation.

Immediately before **every mutation**, and afterward to verify its result, use complete intake:

```bash
gh issue view 24 --repo example/widgets \
  --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

Read discussion evidence where needed:

```bash
gh issue view 24 --repo example/widgets --comments
```

Reconcile changed `updatedAt` against the plan’s consumed revision before proceeding.

1. **Repair the invalid initial state first.** Multiple lifecycle labels require failing closed on ordinary transitions. Because the scenario explicitly identifies `active` as accidental, retain `review`:

   ```bash
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:active
   ```

   Re-fetch and require exactly `{security, backplane:review}`. This is a repair, separate from the rework transition. If evidence does not establish which label is accidental, stop instead of choosing one.

2. **Return review to implementation rework.** The changes-requested review supplies the transition evidence. After fresh intake and revision reconciliation, swap labels in one invocation:

   ```bash
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:review \
     --add-label backplane:active
   ```

   Require `{security, backplane:active}` afterward. Continue the applicable Superpowers execution, TDD, review, and verification workflow. Changed scope or design requires corresponding plan/specification reconciliation first.

3. **Enter blocked when the external impediment stops progress.** Record the concrete reason, release evidence, and prior valid state:

   ```bash
   gh issue comment 24 --repo example/widgets --body \
   'Blocked: <concrete external impediment>.
   Resume target: backplane:active
   Release condition: <specific observable evidence required to unblock>.'
   ```

   The placeholders must be replaced with actual hypothetical facts; the prompt does not supply them. Re-read before the label mutation:

   ```bash
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:active \
     --add-label backplane:blocked
   ```

   Require `{security, backplane:blocked}`. Use native blocking relationships when the blocker is another issue; prose cannot replace that relationship.

4. **Resume only after resolution and gate revalidation.** Verify the recorded release condition, native blockers, current issue semantics, approved design/current plan, and authority to resume execution. Record evidence if not already available:

   ```bash
   gh issue comment 24 --repo example/widgets --body \
   'Resolution evidence: <evidence satisfying the recorded release condition>.
   Revalidated entry gates for Resume target: backplane:active: <evidence>.'
   ```

   Re-read, then:

   ```bash
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:blocked \
     --add-label backplane:active
   ```

   Require `{security, backplane:active}`. If the recorded target is no longer valid, move to `designing` or `backlog` according to established facts. Never guess a former state.

**Fail closed** on missing or unknown required discovery/provenance/compatibility, unavailable authentication or intake fields, invalid lifecycle cardinality, unreconciled revision drift, missing approval or transition evidence, unresolved blockers, or failed post-mutation verification. An unresolved blocker prevents execution/resumption; it supports entering `blocked`.

The deadline, maintainer pressure, and day already spent preparing the PR waive no gates. “Merged-ready” does not prove integration or completion. Completion requires integrated delivery satisfying acceptance criteria and fresh project-owned verification. Every label command above touches only lifecycle labels, preserving `security`.