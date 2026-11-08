# Release-scope review — November 7, 2026

Status: proposal for operator approval. The operator requested this assessment;
neither release rescoping nor publication has been approved. This dated review
does not replace native issue authority or the approved specifications/plans.

## Recommendation and purpose

Establish a first published **0.1.0** contract for Codex and Claude Code. Target
OpenCode V1/V2 supported adoption as a coherent **0.2.0** addition after its five
remaining acceptance issues pass. Finish release accounting before resuming
OpenCode testing. Preserve the existing quality and external-pilot gates.

The smaller first bundle makes accepted work available while keeping unverified
operations outside supported claims. It is not ready to publish today. #4 still
needs Codex/Claude operation evidence, #6 needs an external pilot, and #7 needs
an approved release plan, exact-candidate verification and publication authority.

This review proposes scope dispositions and a manual review cadence. It creates
no monitoring service, automation, milestone, issue transition or scheduled task.

## Authority and observed baseline

- Standalone repository: `/Users/jbabb/Documents/Devel/superpowers-backplane`,
  expected origin `https://github.com/tvproductions/superpowers-backplane.git`.
  Reviewed main: `0aa0cc007db63449455a1c4f9b6d92cb60c5d29a`; clean on entry.
- [Latest handoff](../handoffs/20261101T233052Z-opencode-preflight-and-release-accounting.md)
  preserves interrupted #21 work and the unresolved release-accounting concern.
- Full native intake on November 7 confirms #1 has 17 children, nine completed.
  Open release children: #4, #6, #7, #12, #21, #22, #23, #24. All remain backlog.
  No native milestones, remote tags or GitHub releases were observed.
- [Approval receipt](../plans/2026-11-01-opencode-wrap-approval.json) records
  approval of five OpenCode plans and their shared probe contract. Their native
  issue bodies still say no plan exists. Approval does not establish acceptance.
- [Review receipt](../../../tests/scenarios/2026-11-07-release-scope-review.json)
  retains full issue snapshots, source-policy blob identities and limitations.
  Current issue fields must be re-read before an authorized change.

## Policy reconciliation and version significance

The canonical starter's current reviewed main is
`8d090f88bf45b9a755808a62c1445beeb005daff`. Its published v0.8.0 tag resolves to
`e0b752fcc13b87ec7868fe0b0f85badefdb6bf52`; main is one commit later.
Reviewed inputs: versioning, changelog, baseline policy, architecture and Python
engineering guidance. The applicable comparison starts at the last recorded
review, `fc9cdd2b671f7af7e45fddaa1ac2739c75bb2281`.

The [canonical version policy](https://github.com/tvproductions/gz-skills-first-starter/blob/8d090f88bf45b9a755808a62c1445beeb005daff/docs/versioning.md)
now explicitly identifies 0.1.0 as the first substantive versioned public
commitment. Multiple untagged development commits do not constitute previous
releases. Retain 0.1.0 for the first bundle; explain the accumulated additions
in its release notes. Do not invent historical releases or bump solely because
many issues closed. Compatible fixes after publication use patches; supported
OpenCode adoption is a minor addition, proposed as 0.2.0. A newly written PRD
remains required for every major, including 1.0.0.

The relevant source delta adds initial-version clarification and stronger
adopter configuration/activation-scope discipline. Apply the initial-version
rule here. During #4 acceptance, inspect native install/update activation scope
and preservation on the selected host tuple; reconcile a demonstrated conflict
through a bounded guide fix. Do not assume historical installation proves scope
preservation. Starter helper changes, its cognitive-engine exception and its
Python-only adopter baseline are not adopted into this companion. The existing
Backplane Python/Astral and consumer language-neutral policies remain in force.
No runtime/plugin update, policy exception or formal starter conformance is
claimed. Broader engineering/freshness qualification remains a release-preparation
gate under the existing binding, not a completed result of this scope review.

| Delivered capability | Evidence and current limit | Proposed version treatment |
| --- | --- | --- |
| Native issue intake, lifecycle and independent Superpowers adoption | #2 completed; canonical backlog skill and contract | Initial 0.1.0 public baseline |
| Cross-session handoff continuity | #10 completed; canonical handoff skill | Initial 0.1.0 public baseline |
| Codex native installation | #3 completed; historical Windows tuple and later captures require candidate reconciliation | Supported 0.1.0 surface within verified tuple |
| Claude native installation/lifecycle | #17–19 and #11 completed; exact delivery and host limits retained | Supported 0.1.0 surface within verified tuple |
| Native governance, coverage/satisfaction and PR/checkpoint bridges | #31 completed outside #1; preserve its accepted scope/evidence | Describe delivered workflows in initial 0.1.0; no claim of automatic release management |
| MIT and adopter operations | License published and currently recognized; #4 operation acceptance incomplete | Mandatory 0.1.0 completion for selected supported surfaces |
| Self-hosting | #5 completed against its four criteria/eight seams | Evidence supporting 0.1.0; not release-monitoring acceptance |
| OpenCode shared adapter | #20 completed; initial smokes do not prove setup/lifecycle coverage | Existing source may ship explicitly experimental; supported V1/V2 contract targeted at 0.2.0 |

## Approaches assessed

| Approach | Benefit | Remaining cost and risk |
| --- | --- | --- |
| Retain four-host 0.1.0 | Preserves approved release scope and graph | #21/#23 setup and failures, #22/#24 lifecycle/conformance, #12 integrated acceptance, #4 operations, pilot and release remain. No defensible publication window until native setup evidence exists. |
| Codex/Claude 0.1.0, supported OpenCode 0.2.0 — recommended | Publishes a coherent accepted core sooner; keeps host acceptance explicit | Requires approved scope transfer, #4 evidence completion, current tuple reconciliation and pilot. Smaller scope does not waive any included gate. |

Recommendation is the reviewer's proposal, not an operator-selected release
contract. The user's request authorized assessment of this option. The current
four-host specification and native graph continue to govern until reconciled.

## Proposed bundle and obligation accounting

0.1.0 includes the two canonical skills, their delivered governance bridges,
independent stable Superpowers integration, MIT, and verified Codex/Claude
installation, setup, update, rollback, removal and recovery guidance. Publish
exact tested host/upstream/Backplane/gh tuples and platform limits. Historical
Windows acceptance does not certify current Mac or every newer host version.

Existing OpenCode source/docs can remain in the repository and package as an
experimental preview with explicit unverified operations. Removing them would
be new product work. Review the package contents and entry points so inclusion
cannot be read as supported acceptance. Automatic backlog/release monitoring,
additional harnesses (#8) and deterministic helpers (#9) are not part of this
first supported contract. Preserve #31's delivered workflow scope.

| Existing #1 obligation | Proposed 0.1.0 disposition | Required evidence / owner |
| --- | --- | --- |
| Every release child completed with integration/verification evidence | Retain for the explicitly selected bundle; transfer unfinished OpenCode outcomes visibly to 0.2.0 | Operator-approved scope/graph reconciliation, then accepted evidence for every retained child; maintainer |
| Four host variants pass fresh-host leaf verification | Amend supported host scope to Codex and Claude; defer V1/V2 obligation to 0.2.0, never mark it satisfied | #3/#11 acceptance reconciled to candidate; mandatory affected reruns; #4/#7 |
| Fresh adopting-project pilot passes compatibility/conformance | Retain unchanged | Authorized external repository, installed candidate, fresh discovery and all five named checks; #6 |
| Licensed, documented release published from verified source | Retain unchanged | #4 satisfaction, clean reviewed exact candidate, tag/release arrival evidence; #7 |

For 0.2.0, retain every OpenCode setup/failure, lifecycle, conformance, native
issue-state and below-floor requirement. Existing sequence remains #21 → #22
and #23 → #24, then #12. #20 stays accepted for its bounded initial adapter work.
The Windows #21 preflight is historical evidence; retained authentication and
profiles are not transported to this Mac.

## Proposed native reconciliation after approval

1. Amend #1's supported host criteria to the selected initial bundle. Keep its
   identity as the first-release outcome; record each deferred obligation,
   approval, rationale and revisit condition. Preserve historical approved bytes.
2. Create one 0.2.0 OpenCode release outcome and move #12/#21–24 beneath it,
   preserving their numbers, criteria and dependency chains. Keep completed #20
   under #1 as shipped experimental-source contribution, with its limit explicit.
   This would leave #1 with 12 children, nine completed; it is a proposed count,
   not today's native state or a readiness percentage.
3. Narrow #4's accepted-operation contract explicitly to supported Codex/Claude
   and accurate experimental OpenCode disclosure. Create a bounded 0.2.0
   operations-guidance outcome owning the transferred OpenCode obligation,
   consuming #21–24 evidence without duplicating those host tests. Make that
   outcome depend on #22/#24 and block #12 final acceptance. It remains open
   until guidance and exact installed operations agree.
4. Remove only #12's blocker edge into #6 after scope approval; preserve #6's
   #3/#4/#5/#11 edges. Keep #7 blocked by #6. Preserve the Codex pilot contract;
   Claude release acceptance remains mandatory through #4/#7, without silently
   inventing a second external pilot.
5. Reconcile #7's scope/verification with the revised bundle. Link the approved
   release design and create its execution plan. Add immutable approved-plan
   links to #12/#21–24 and reconcile their labels when their actual stage gates
   are met. Do not manufacture historical transitions.
6. Use native 0.1.0 and 0.2.0 milestones for selected release targets if approved;
   the issue graph and accepted evaluations retain authority. Record material
   scope changes through the existing checkpoint workflow under its own scope.

The approved adoption design and #4/OpenCode plans remain unchanged historical
authorities. An approved amendment must identify their affected clauses and
provide new issue-bound execution authority before the changed work begins.
No issue may close merely because an obligation moved.

## Acceptance gaps and publication evidence

| Gate | Current result | Evidence needed before publication |
| --- | --- | --- |
| Scope authority | Proposed | Explicit approval of selected bundle, transferred obligations, graph and affected design/plan amendments |
| Legal recognition | Currently observed MIT | Reconfirm hosted license and exact candidate LICENSE bytes |
| Codex operations | Incomplete #4 inventory/scoring | Score archived command/session/recovery rows individually; prove exact package revisions and nontrivial unrelated-plugin/user/upstream preservation for applicable stages; rerun missing or changed seams |
| Claude operations | Accepted host evidence plus incomplete #4 reconciliation | Reconcile guide/host/upstream/candidate tuple; verify operation inventories, fresh skill loads and preservation; rerun affected/missing seams |
| Activation scope and support claims | Candidate review pending | Preserve intended project/profile activation and unrelated state; disclose exact tested tuples, experimental source and unsupported scope; resolve applicable current policy conflicts |
| External pilot #6 | Not executed; no plan | Select/authorize external repository, approve issue-bound plan, install exact hosted candidate, fresh discovery and five scored checks; resolve release blockers |
| Release preparation #7 | No plan | Full scope-specific quality command matrix, current policy/tool/dependency applicability review, metadata agreement, unreleased notes, whole-change review and exact integrated-candidate results |
| Publication | Not authorized; no tags/releases | Explicit authority, annotated immutable v0.1.0 tag at verified full SHA, GitHub release and exact remote tag/notes/artifact verification |

Valid JSON, closed issues, a successful model process, a passed syntax check or
an old installation cannot substitute for these gates. Retain PASS/FAIL/UNKNOWN
per operation and criterion. Any included mandatory FAIL or UNKNOWN prevents
publication. Record historical acceptance at its original delivery and assess
applicability; repeat only changed or unsupported seams. Final checks must run
on the actual integrated candidate, with later evidence-storage SHAs distinct.

## Proposed window, ownership and review cadence

Planning assumption: maintainer approval and availability of isolated authenticated
hosts plus an external pilot owner. The dates below are reviewer estimates,
not resource commitments or release permission. They become the working cadence
only on approval.

| Target | Outcome | Accountable owner |
| --- | --- | --- |
| Monday November 9 | Approve or reject bundle; reconcile scope/graph and select exact host tuples | Maintainer, assisted by executing agent |
| November 10–13 | Complete #4 Codex/Claude inventory, scoring, preservation and affected reruns; approve #6/#7 plans | Executing agent; maintainer accepts evidence |
| November 16–20 | Run authorized external Codex pilot and resolve findings; freeze exact release candidate | Pilot repository owner plus executing agent; maintainer accepts |
| November 23–25 | Conditional 0.1.0 publication window after full gate and explicit authorization | Maintainer/release operator |
| November 30 | First post-release review, or explicit missed-window replanning | Maintainer |

Until publication, review readiness each Monday and Thursday and after any
material candidate/scope change. First proposed reviews: November 9 and 12.
Each review names bundle/version, candidate SHA, per-gate evidence and gaps,
owner/next action, changed inputs and the next decision date. Store dated
evidence in existing project records and reference it from native #7; do not
create a second mutable status ledger. This is a manual procedure, not a promise
that an agent will wake automatically.

If scope approval is absent November 9 or #4 cannot pass by November 13,
re-estimate the window at the next review. If pilot acceptance is unavailable
November 20, mark the November 23–25 window at risk and propose a revised date.
Never waive gates to hit the calendar. Any further scope reduction requires a
new explicit disposition. After publication, review the next coherent bundle
monthly and on material delivery, without requiring a release every month.

Set a 0.2.0 target window only after #21/#23 produce credible setup matrices and
the remaining lifecycle/final-acceptance effort is estimated. Revisit the
OpenCode deferral at the first post-0.1.0 review, or November 30 if still
unreleased. Preserve standing OpenCode plan approval, but sequence its execution
after this release decision; do not discard its captured work.

## Decision requested and permissible next work

Approve or amend: Codex/Claude 0.1.0 supported scope, experimental OpenCode
disclosure, OpenCode 0.2.0 obligation transfer, proposed native reconciliation,
and conditional window/manual cadence. Approval of this proposal would permit
preparing the corresponding reconciliation and execution plans; publication,
remote mutations and release execution retain their explicit authority gates.

The first implementation priority after reconciliation is **#4's remaining
Codex/Claude operation acceptance**, followed by #6 and #7. If four-host scope is
retained instead, resume the already approved #21 thread after current-host
revalidation, and estimate the first-release window from actual setup results.
This review has not started either execution path.
