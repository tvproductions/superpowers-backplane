On the supplied fixture dated **2026-10-01**, both issues have valid design authority, but **neither is eligible for execution**: both lack an approved implementation plan and carry `backplane:designing`.

| Target | Valid design authority | Next proposed planning step |
|---|---|---|
| [#101](https://github.com/example/governance-fixture/issues/101), bounded documentation correction | Its complete, human-approved issue body. No separate specification is required for the stated scope. | Proceed to `superpowers:writing-plans` using that body; do not repeat approved design discussion. |
| [#102](https://github.com/example/governance-fixture/issues/102), shared coverage contract change | Approved cross-cutting specification **S1**, alongside the issue’s authority over bounded scope and acceptance. | Reconcile the issue with S1, then use `superpowers:writing-plans` for its bounded executable scope. Resolve any discrepancy with the approver; do not replace S1 or restart settled design. |

These authority paths follow the [Superpowers binding](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/superpowers-binding.md).

Each proposed plan must bind to its issue URL and consumed `updatedAt` value, `2026-10-01T12:00:00Z`, identify the design authority and consumed design revision, and preserve acceptance criteria, verification seams, and exact project-owned verification commands. New Backplane plans belong under `docs/superpowers-backplane/plans/`.

After plan approval, readiness still requires an open executable leaf, complete issue contract, approved current design and plan, and resolved native blockers. The fixture reports empty child and blocker arrays; those facts alone do not establish executable scope or readiness. Only an authorized, evidence-supported transition could change `designing` to `ready`. Explicit execution selection and the first execution task are subsequent gates. See the [native issue contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/github-issue-contract.md).

A broader approved product decomposition reaches per-issue planning through **decomposition/intake reconciliation**:

1. Account for every approved parent obligation through bounded contributions, applicable accepted evidence, or explicitly approved deferral/exclusion. Identify contribution boundaries and the owner accepting combined results.
2. Compare those contributions with complete existing issue records. Retain matching issue identities; distinguish proposed new outcomes from unresolved scope, coverage, or ownership questions.
3. Present exact proposed issue bodies and native parent/dependency relationships. Codes do not imply edges, and dependencies do not imply priority.
4. Under separately authorized intake, apply selected changes through `gh`, reconcile drift, and verify the resulting native records. Governance sections supplement participating issues’ existing contracts; they do not silently migrate legacy issues.
5. Give each resulting bounded executable leaf its own current approved implementation plan, then evaluate readiness and selection separately.

**Decomposition approval authorizes no issue creation, selection, or readiness transition.** This sequence follows [product decomposition](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/product-decomposition.md).

The fixture supports the authority comparison, but not concrete plans or a complete broader decomposition assessment. Missing inputs include S1’s actual locator/content/revision and approval anchor, #102’s full executable contract, exact verification commands, and the broader product’s obligation wording/keys, owners, code legend, contribution mappings, evidence, and declared presentation mode. Delivery satisfaction is **UNKNOWN**, because no accepted delivery evaluation is supplied.

Authorized now: this read-only assessment and identification of gaps. Plan creation, intake changes, lifecycle transitions, selection, and execution remain proposed future work. I made no live GitHub queries, dispatched no agents, and changed no artifacts or state.