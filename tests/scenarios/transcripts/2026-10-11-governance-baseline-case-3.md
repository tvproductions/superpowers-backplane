Both issues have approved design authority, but neither is eligible for execution: both lack an implementation plan and carry `backplane:designing`. These conclusions apply only to the fixture dated `2026-10-01T12:00:00Z`.

| Target | Valid design authority | Next planning steps |
|---|---|---|
| [#101](https://github.com/example/governance-fixture/issues/101) | Its complete, human-approved issue body is sufficient for this bounded documentation correction. A separate specification is unnecessary. | Proceed to Superpowers implementation planning using the approved issue body. Do not reopen approved design discussion. |
| [#102](https://github.com/example/governance-fixture/issues/102) | Approved specification **S1** governs the shared coverage-contract change. The cross-cutting decision warrants a separate specification. | Confirm that S1 covers the issue’s current scope and acceptance criteria, then proceed to implementation planning. Brainstorm only missing or newly changed design. |

Each executable issue needs one current, approved Superpowers plan recording its issue URL, consumed revision `2026-10-01T12:00:00Z`, design authority, acceptance criteria, verification seams, and exact project-owned verification commands. New Backplane plans belong under `docs/superpowers-backplane/plans/`, following the active project namespace rule.

The supplied empty native child and blocker arrays establish leaf status and no recorded blockers within this fixture. Before a future transition to `backplane:ready`, confirm the complete issue contract, approved current plan, executable scope, and resolved dependencies. Design approval alone does not satisfy that gate. Selection and execution remain separate subsequent steps. This follows the [design and plan binding]( /Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/superpowers-binding.md) and [eligibility contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/github-issue-contract.md).

A broader approved product decomposition first becomes a proposed mapping to issue work:

- Identify the product continuity parent and bounded executable leaves.
- Match each approved slice to an existing issue where appropriate; propose new issues for uncovered slices.
- Give each leaf its objective, allowed and excluded scope, observable acceptance criteria, verification seams, and design-authority linkage.
- Propose native parent/sub-issue relationships, dependency edges, and issue types where available. Decomposition and execution ordering are distinct relationships.

Only after authorized creation or reconciliation establishes those issue identities and revisions should per-issue implementation planning bind to them. Approval of decomposition does not itself authorize tracker mutations or make the leaves ready.

The remaining evidence gaps are S1’s contents and revision, #102’s actual body, exact verification commands, and any broader decomposition and existing-issue inventory. Those gaps prevent checking design alignment, drafting concrete executable plans, or mapping the broader result without duplication.

The authorized work here is this read-only assessment. Plan creation, issue reconciliation or creation, relationship changes, and lifecycle transitions are proposed future operations; none were performed. No live GitHub queries, mutations, helper execution, or agent dispatch occurred.