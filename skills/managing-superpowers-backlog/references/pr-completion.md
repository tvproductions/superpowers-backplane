# PR contributions, satisfaction, and closeout

Use for `PR closeout`. Read [governance](../../../docs/superpowers-backplane/governance.md),
the [native issue contract](github-issue-contract.md), and
[Superpowers binding](superpowers-binding.md). This bridges evidence into the
existing lifecycle; it does not create a second approval process or infer
completion from tracker state.

## Required inputs and closeout assessment

Read the full 15-field native issue contract for each affected issue, current
issue/design/plan semantic revisions and approvals, exact contribution scope,
project integration target, required review/acceptance, verification method and
observed results, immutable evidence and delivery identities, and actual closure
intent/relationships. For a fixture, use its supplied facts and explicitly
missing inputs instead of live queries.

Inspect actual PR state through gh, for example:

```sh
gh pr view "$sp_bp_pr_number" --repo "$sp_bp_repo" \
  --json number,url,state,baseRefName,headRefName,mergedAt,mergeCommit,reviewDecision,closingIssuesReferences
```

A truncated relationship collection needs complete pagination before a full
closeout claim. PR body prose is not proof of native graph or closure. Record
an unavailable field/permission as unknown rather than inferring it.

Return: (1) input/revision/authority anchors and observed tracker/PR facts;
(2) criterion contributions and outstanding obligations; (3) review, integration,
verification, and satisfaction separately; (4) proposed or authorized issue,
parent, Project and checkpoint closeout; (5) preserved historical evidence,
recovery needs, and release/workspace disposition. Missing evidence limits the
corresponding result; a read-only assessment performs no mutation.

## Contribution states

| State | Supported result | Next evidence/action |
| --- | --- | --- |
| Design-only PR | Establishes the accepted design/revision | Delivery, plan binding and verification are still required. |
| Partial merged contribution | Retain its scoped issue/criterion contribution | Remaining PRs/obligations and integrated checks stay outstanding. |
| Accepted review, unmerged PR, passing branch checks | Review accepted for the stated scope; integration pending | Project-approved integration then fresh checks at that target. |
| Merged/auto-closed issue, failed integrated check | Report actual CLOSED state and UNSATISFIED affected obligation | Authorized corrective/reopen/lifecycle reconciliation; no unrequested mutation. |
| Complete accepted integrated delivery with current passing evidence | SATISFIED for the evaluated current criterion/revision/commit | Authorized issue closeout, then parent/projection/checkpoint reconciliation. |
| Nondefault target with closing text, no observed closure | Closure intent only | Inspect native references/state and applicable target/automation behavior. |

Neutral `Refs #101` expresses a contribution without claiming all work is done.
A closing keyword expresses intent and may cause tracker closure under the
host/project policy; it is distinct from an observed relationship and actual
closed state. Do not presume default-branch keyword behavior for a nondefault
target, or that an observed automatic close establishes verification. A project
may deliberately use automatic closure, but must reconcile premature closure
through its authorized workflow. No generic integration/closure rule overrides
current project policy.

A PR can contribute to several outcomes and several PRs can contribute to one.
Identify the issue/criterion and approved requirement revision for each bounded
contribution; state the combined-result owner. Merge is contribution evidence,
not an independent acceptance result. Keep outstanding review findings visible.

## Evidence, changed inputs, and evaluated results

A current satisfaction claim needs the exact approved criterion/requirement
inputs, accepted review/verification results, applicable integration/delivery
commit, evidence identities/availability, and remaining obligations. Preserve
historical passes against their original inputs. A behavior-changing requirement
or delivery delta requires revalidation of affected claims. Explicit editorial
semantic equivalence can retain matching evidence with unchanged relevant delivery
inputs; it cannot repair an unrelated old gap.

Use SATISFIED, UNSATISFIED, or UNKNOWN as defined in governance. A known failed
applicable check is UNSATISFIED; an unperformed or unavailable check is UNKNOWN.
Neither merge, native closure, Project Done, code coverage, nor a checked plan
supplies missing acceptance evidence. Scope deferrals/exclusions require their
own approval and remain distinct from success.

## Authorized closeout sequence

1. Re-read the issue and native relationships. Reconcile changed issue/design,
   plan, integration target, and evidence inputs before a write. Validate the
   exactly-one open lifecycle label and preserve unrelated labels.
2. Confirm accepted review and integration at the project's actual target.
   Execute the exact project-owned verification commands there; inspect current
   outputs and acceptance criteria. Record immutable scope and limitations.
3. Update the outcome's `Coverage and Satisfaction` current mappings/evaluation
   pointers under the authorized body-edit scope. Keep accepted evaluation
   evidence immutable and preserve prior identities. Do not make the issue's
   mutable verdict the only accepted result.
4. Immediately before closure, re-fetch the full native issue contract and
   relationships after any body/evaluation-pointer edits. Reconcile the current
   `updatedAt`, exactly one lifecycle label, scope, criteria, blockers, and
   evidence applicability against the evaluated inputs. Record an editorial
   pointer edit as semantic reconciliation; do not infer equivalence from the
   timestamp alone. If another edit changes an acceptance or delivery input,
   stop the closing write and refresh the affected approved inputs, review,
   and verification before rechecking closure eligibility.
   Close completed only under the existing lifecycle and explicit applicable
   authority once all obligations pass. Preserve unrelated labels; remove
   lifecycle labels as required by project closed-state policy, without a done
   label. Re-fetch actual state/reason, labels and native closing relationships.
   Simulation-only closeout authority is never used on a real issue.
5. Reconcile parent `Obligation Dispositions` and references to child evaluations.
   A child close does not establish parent completion: account for every
   applicable parent obligation, remaining contribution, and approved disposition.
   Not-planned children supply no delivery evidence.
6. Refresh derived Project Code/Kind/Satisfaction and optional lifecycle display
   under authorized scope, from canonical issue records and evaluations. Denied
   access remains a limitation in the declared mode; repairs are proposed when
   not authorized. A milestone is a target, not release permission.
7. Request the checkpoint operation for the reconciled closeout scope, preserving
   mode and evidence availability. Validate/accept its pair under its own
   transaction and commit authority. No checkpoint completeness claim arises
   merely from having closed an issue.
8. Preserve the implementation workspace for pending review fixes and follow
   Superpowers/project finishing and cleanup ownership. Release publication,
   branch deletion/worktree removal, and unrequested reopening are separate
   operations with their applicable authority.

If native closure already occurred and checks fail or remain UNKNOWN, report
both facts and the outstanding obligation. Propose the project's corrective
operation, including recovery to an evidence-supported lifecycle where authorized.
Do not silently reopen, repair labels, or claim satisfaction just to match closure.

## Verified source and checkpoint storage

Keep these identities separate:

- Design/input revision identifies the approved behavior evaluated.
- Verified delivery/integration commit identifies the actual tested outcome.
- Checkpoint/evidence storage commit identifies the later record preserving
  those results. It does not replace the verified delivery commit.

A checkpoint-only follow-up PR names the exact accepted delivery and input
identities. Until that PR is integrated, distinguish local capture/accepted
commit from remotely integrated backup. Do not claim its future merge already
passed checks. A later behavior-changing contribution triggers affected
revalidation; pure storage of dated evidence preserves the original evaluation
scope, with limitations disclosed. Publication and release remain separately
authorized claims.
