The sequence is **repair to review → active rework → blocked → active after revalidation**. The deadline, maintainer’s urgency, and preparation already spent do not waive any gate. These are hypothetical commands only; none were executed.

Before an authorized real operation, require authenticated, compatible `gh`, operational independent Superpowers, and all six lifecycle labels with correct descriptions:

```sh
gh auth status
gh label list --repo example/widgets --json name,description
```

Fully enumerate labels if necessary. Missing labels require separately authorized creation.

Before interpreting the issue, before each mutation, and after each label edit, use the complete intake:

```sh
gh issue view 24 --repo example/widgets \
  --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

Read comments when needed for review requests, approvals, blocker records, or evidence:

```sh
gh issue view 24 --repo example/widgets --comments
```

Compare `updatedAt` with the consumed revision and reconcile semantic changes before proceeding.

1. **Repair the invalid initial state first.** Two lifecycle labels are invalid. The supplied facts identify `backplane:active` as accidental and review as the valid state. Remove only the accidental label:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:active
   ```

   Re-fetch and verify the labels are `security` and exactly one lifecycle label, `backplane:review`. This repair is separate from returning to rework.

2. **Return review to active for requested implementation changes.** After the repair and a fresh intake, the documented review request supports `review → active`:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:review \
     --add-label backplane:active
   ```

   Remove and add in one invocation. Preserve the implementation workspace and continue the approved plan with applicable Superpowers execution, TDD, review, and verification. Record the review-request evidence in a comment only if it is not already represented by the review or another durable artifact. If the requested changes invalidate design or plan authority, reconcile that authority before implementation.

3. **Enter blocked when the external condition stops rework.** Record the concrete blocker, release evidence, and prior valid state:

   ```sh
   gh issue comment 24 --repo example/widgets --body \
   'Blocker: <specific external condition and owner/reference>.
   Resume target: backplane:active
   Release condition: <concrete evidence required to establish resolution>.'
   ```

   Re-read after the comment, reconcile its revision change, then:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:active \
     --add-label backplane:blocked
   ```

   Preserve native dependency relationships; the comment does not replace an available native blocking edge.

4. **Resume only after resolution and revalidation.** Verify the recorded release condition and every entry gate for `active`: open executable leaf, complete contract, approved design, current approved issue-bound plan, reconciled revisions, resolved native blockers, selection, and actual execution resumption. Record resolution/revalidation evidence if it is not already durable, re-read, then:

   ```sh
   gh issue edit 24 --repo example/widgets \
     --remove-label backplane:blocked \
     --add-label backplane:active
   ```

   If `active` is no longer valid, use an evidence-supported transition to `designing` or `backlog`. Never guess a missing resume target.

Every edit targets named lifecycle labels, preserving `security` and all other unrelated labels. Re-fetch after each edit to verify exactly one expected lifecycle label and unchanged unrelated labels.

**Fail closed** on zero or multiple lifecycle labels until a justified repair is established; missing required intake fields, references, authority, approvals, or evidence; incompatible tooling or unknown Superpowers provenance; unreconciled revision drift; unresolved blockers; or failed resume gates. This probe authorizes no real mutations. “Merge-ready,” urgency, and sunk effort establish neither satisfaction nor completion; completed closure requires accepted integration and fresh project-owned verification.