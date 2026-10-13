Using the designated candidate, I read its native issue contract, Superpowers binding, PR completion, governance, and installation references. This is hypothetical; none of the commands below were executed.

**Intake and selection**

Use authenticated `gh` and an operational, independently installed Superpowers. Fetch all 15 native fields:

```sh
gh issue view 12 --repo example/widgets --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

Inspect `gh label list --repo example/widgets` before first use to confirm the six lifecycle labels and their meanings. Do not silently create missing labels.

Confirm #12 is open, has exactly one lifecycle label (`backplane:ready`), has parent #3, and has no sub-issues or unresolved blockers. Its body must contain Objective, Bounded Scope with Allowed/Out of Scope, Acceptance Criteria, Verification Seams, and Superpowers Artifacts. Confirm plan approval: a committed plan alone does not establish approval.

The maintainer has selected #12; selection itself changes no label. Parent #3 supplies continuity, not an execution prerequisite or an automatic completion target.

**Start and Superpowers handoff**

Re-read the complete intake immediately before starting. Compare `updatedAt` with the revision consumed by the plan. Timestamp drift requires semantic reconciliation: record covered editorial changes, obtain approval for necessary plan changes, return to brainstorming for changed design, or record a concrete blocker.

The approved bounded issue body remains design authority. Do not repeat approved brainstorming or replace the existing current plan. Confirm the plan records the issue URL/revision, design authority, acceptance criteria, verification seams, and exact command.

Follow Superpowers isolation under project rules, then execution of the approved plan with appropriate TDD, review, verification, and branch finishing. When the first execution task actually begins:

```sh
gh issue edit 12 --repo example/widgets \
  --remove-label backplane:ready --add-label backplane:active
```

For every authorized transition, re-read first, preserve unrelated labels, replace the lifecycle label in one invocation, and re-fetch afterward to verify the result.

**Submission and lifecycle**

| Transition | Gate |
|---|---|
| `ready → active` | Eligible, selected, re-read; execution actually begins |
| `active → review` | Implementation, required review, and worktree verification support submission |
| `review → active` | Review requests implementation changes |
| Any open state → `blocked` | Concrete blocker; record `Resume target: backplane:<state>` and release condition |
| `blocked → recorded target` | Blocker resolved and target entry gates revalidated |
| `review → closed/completed` | Accepted integrated delivery satisfies every applicable criterion with fresh verification |

Submit the PR with design/plan revisions, criterion contributions, review evidence, and verification results. Use a neutral `Refs #12` while integrated evidence is pending. Move `active` to `review`, and retain the workspace for review fixes.

**Verification and closure**

The sole project verification command is:

```sh
cargo test --workspace
```

Run it and inspect its results in the implementation worktree before submission, then freshly at the accepted integration target before claiming completion. Add no Python runtime or test framework requirement.

At closeout, re-read the issue and inspect actual PR state:

```sh
gh pr view <pr-number> --repo example/widgets \
  --json number,url,state,baseRefName,headRefName,mergedAt,mergeCommit,reviewDecision,closingIssuesReferences
```

PR creation, merge, checked plan tasks, and automatic closure do not establish satisfaction. Require accepted review, integration, passing fresh checks, and acceptance evidence tied to exact requirement and delivery revisions.

Only then, with applicable closeout authorization, close #12 with reason `completed` and verify its actual state and relationships. Add no done label. Completion of #12 does not complete epic #3; every parent obligation needs accounting. Missing checks remain `UNKNOWN`; failed applicable checks remain `UNSATISFIED`, even if GitHub has already closed the issue.