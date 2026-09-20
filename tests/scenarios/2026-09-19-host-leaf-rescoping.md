# Host Installation Leaf Rescoping Evidence

- Approved design: docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md
- Approved execution plan: docs/superpowers/plans/2026-09-19-host-installation-leaf-rescoping.md
- Functional authority: docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md
- Scope: native issue graph and ownership only; no host package or guide test.

## Pre-mutation baseline

Read-only gh intake on 2026-09-19 found #1 open with nine children; #11 and
#12 open under #1, each with one backplane:backlog label, zero sub-issues, and
a historical closed #2 blocker. #11 and #12 each block #6. #6 has five native
blockers: #3 (closed), #4, #5, #11, and #12. #11 updatedAt was
2026-09-19T14:11:46Z; #12 was 2026-09-19T14:11:57Z; #6 was
2026-08-23T13:55:24Z. Exact-title issue list returned no proposed C1-C3 or
O1-O5 issue. The six backplane lifecycle labels exist with contract-matching
descriptions. GitHub CLI help exposed issue create --parent, --body-file, and
--label, plus issue edit --add-blocked-by and --body-file.

## RED ownership observation

Before mutation, the approved four-host matrix assigned whole-host Claude
work to #11 and both OpenCode variants to #12. Its earlier GREEN note called
#3 open. Neither host issue had smaller implementation children or a current
plan. The target graph kept #11/#12 as executable final leaves and added eight
sibling leaves under #1, so the earlier ownership text could not describe it.

## Prepared mutation set

Ten complete issue bodies are in ignored local scratch at
.superpowers/sdd/2026-09-19-host-leaf-rescoping/: C1-C3, O1-O5,
final-11, and final-12. Each has the required executable-leaf headings.
The post-creation ownership text was prepared in ownership-draft.md in
that same directory and applied to the current specification and matrix.
Native parentage and dependencies were applied as
GitHub relationships; body text does not substitute for those fields.

## Draft review correction

Read-only branch review found three Important drafting gaps. First, the
final-leaf drafts permitted a scored matrix containing FAIL or UNKNOWN. The
revised #11/#12 bodies and rescope design require PASS for every mandatory
supported-host check; FAIL/UNKNOWN blocks final acceptance. Both OpenCode
below-floor cases must produce the expected unsupported result without
mutation. Second, the ownership draft targeted the approved spec's final
no-publication paragraph; it now targets only the preceding host-ownership
paragraph and explicitly preserves the publication boundary. Third, the
existing matrix introduction assigned every check to one implementation
leaf; the publication draft and plan now assign the checks collectively to
bounded prerequisite leaves with #11/#12 final integrated acceptance.

## Approval

The user approved the revised sibling graph and planning-branch merge in
conversation on 2026-09-19. The eight-issue creation and ownership update
were executed under the approved plan.

## Integrated planning authority

Planning PR #16 merged on 2026-09-20 UTC at
150c7039013a77fbc87f6cca5f79363a2714bc6c. The issue bodies cite
the approved design path present at that integrated revision. The planning
branch diff changed only HANDOFF.md, the rescope design and plan, and this
scenario file. Git diff from origin/main to the planning branch passed
the whitespace check before merge.

## Native graph GREEN observation

Fresh gh issue view intake returned all required native fields for #1, #6,
#11, #12, and #17-#24. Release #1 now has 17 direct children, eight more
than the pre-mutation nine. Each new issue is open, a leaf under #1, and
carries exactly one backplane:backlog label. Every new body has the required
Objective, Bounded Scope, Allowed, Out of Scope, Acceptance Criteria,
Verification Seams, and Superpowers Artifacts headings; each exactly
matches its reviewed draft.

| Key | Native issue | Blocked by | Blocks |
|---|---|---|---|
| C1 | https://github.com/tvproductions/superpowers-backplane/issues/17 | None | #18 |
| C2 | https://github.com/tvproductions/superpowers-backplane/issues/18 | #17 | #19 |
| C3 | https://github.com/tvproductions/superpowers-backplane/issues/19 | #18 | #11 |
| O1 | https://github.com/tvproductions/superpowers-backplane/issues/20 | None | #21, #23 |
| O2 | https://github.com/tvproductions/superpowers-backplane/issues/21 | #20 | #22 |
| O3 | https://github.com/tvproductions/superpowers-backplane/issues/22 | #21 | #12 |
| O4 | https://github.com/tvproductions/superpowers-backplane/issues/23 | #20 | #24 |
| O5 | https://github.com/tvproductions/superpowers-backplane/issues/24 | #23 | #12 |

Every listed blocker edge was checked in both blockedBy and blocking. #11
is still an executable leaf under #1, blocked by historical completed #2
and new #19, and still blocks #6. #12 is an executable leaf under #1,
blocked by #2, #22, and #24, and still blocks #6. Their narrowed bodies
exactly match the reviewed final drafts; their observed updatedAt values
are 2026-09-20T01:31:32Z and 2026-09-20T01:31:34Z respectively. Labels,
parentage, and unrelated blocker edges were unchanged by the body edits.

Pilot #6 still has exactly the original five native blockers: #3, #4,
#5, #11, and #12. It was not edited. The full graph verification script
checked all twelve relevant issues and wrote its compact read-only result
to ignored local graph-snapshot.json beside the issue-body drafts.

## Documentation ownership GREEN observation

The approved v0.1 spec now names #17-#24 as bounded implementation owners,
#11/#12 as final acceptance, and preserves issue #2's completion contract
and its final no-publication sentence. The current four-host matrix names
all actual owner URLs, assigns the V1 below-floor case to #21 and V2 to
#23, and records future live host verification as pending. The old broad
#11/#12 assignment and original GREEN note are retained under dated
historical ownership, with #3's later completed closure made explicit.
The matrix introduction assigns required checks collectively across each
host's bounded leaves and final acceptance. No new live host test is claimed.

## Final document gate

The full five-file diff was inspected. Git diff --check returned exit 0.
Git diff --name-only contained only HANDOFF.md, the rescope execution plan,
the approved v0.1 spec ownership paragraph, this scenario record, and the
four-host matrix. No package, guide, skill, or upstream file changed. A
before/after comparison found no approved functional-spec change outside
Implementation boundary; the no-publication sentence remains. All five
modified Markdown files end with a newline. No live host test was rerun for
this graph-only change. Independent read-only review found no Critical or
Important findings after comparing the live issue graph, all ten bodies,
the matrix, and the approved contract. Graph-record PR #25 merged on
2026-09-20 UTC at 96728cfd8cd0eabdd0f89cf5b7409625a8c573ea.

Fresh post-merge verification read the matrix from origin/main and fetched
#1, #3, #6, #11, #12, and #17-#24 through gh issue view. #1 still has 17
direct children. All eight new issues remain open backlog leaves under #1
with the exact approved blockedBy and blocking edges, and every integrated
current owner URL resolves to its expected issue. #11/#12 retain their
prerequisite edges; #6 retains exactly #3, #4, #5, #11, and #12 as blockers.
#3 is CLOSED/COMPLETED. Both negative host-floor owners in the integrated
matrix are #21 and #23. The integrated graph and matrix agree; no host issue
was readied, closed, or tested by this redistribution.
