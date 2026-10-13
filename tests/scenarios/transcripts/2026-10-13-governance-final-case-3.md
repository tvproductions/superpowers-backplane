Both issues have valid design-authority paths on the supplied fixture facts, but **neither is eligible for execution**: each lacks an approved implementation plan and carries `backplane:designing`.

| Target | Valid design authority | Proposed next steps |
|---|---|---|
| [#101](https://github.com/example/governance-fixture/issues/101) — bounded documentation correction | Its complete, human-approved issue body. No separate specification or renewed design discussion is required. | Proceed to `superpowers:writing-plans`, binding one bounded plan to the approved issue body, acceptance criteria, and verification seams. Obtain plan approval. |
| [#102](https://github.com/example/governance-fixture/issues/102) — shared coverage-contract change | Approved cross-cutting specification **S1**, together with the issue’s authoritative scope and acceptance criteria. S1 does not silently amend the issue. | Reconcile the issue with S1, then prepare and approve one issue-bound implementation plan. Revisit design only if a conflict or missing decision emerges. |

Each plan must record the issue URL, consumed issue revision `2026-10-01T12:00:00Z`, design authority and its revision, acceptance criteria, verification seams, and exact project-owned verification commands.

The fixture’s empty child and blocker arrays support leaf status and no recorded native blockers. Readiness still requires the complete executable issue contract, approved design, a current approved plan, and resolved blockers. An authorized, verified transition to `backplane:ready` would then establish eligibility. Explicit selection and the start of execution are separate steps; selection alone changes no label.

A broader approved product decomposition enters native work through **decompose/intake reconciliation before per-issue implementation planning**:

1. Account for every approved parent obligation using bounded contributions, applicable accepted evidence, or explicitly approved deferral/exclusion. Keep omissions and ambiguous ownership unresolved.
2. Match contributions to existing issues and retain their identities. Classify unmatched contributions as proposed new bounded outcomes or gates; identify unresolved scope and ownership questions separately.
3. Present exact proposed issue-body and native relationship changes. Parentage expresses decomposition; dependencies express execution order. Neither codes nor list order establishes priority.
4. For declared governance participation, prepare issue-owned `Backplane Record`, `Obligation Dispositions`, and `Coverage and Satisfaction` sections alongside the executable issue contract. Specify shared contribution boundaries and who accepts the combined result.
5. Only an explicitly authorized intake operation may create or edit issues and relationships through `gh`, followed by verification. Each resulting bounded leaf then receives its own current approved implementation plan.

Decomposition approval authorizes no issue creation, readiness transition, selection, or execution. Proposed children are not existing native children. Deferral/exclusion is not delivery, and satisfaction remains `UNKNOWN` without applicable accepted evidence.

The fixture establishes the comparison, but does not supply inspectable issue-body bytes, S1’s exact locator/revision/content, detailed approval records, verification commands, or the broader obligation/decomposition records. Those omissions prevent drafting concrete plans, reconciling S1 against #102, or producing a complete obligation-accounting and graph proposal. Presentation mode is also unspecified; ordinary issue planning has no Project prerequisite.

**Currently authorized:** this read-only assessment. All planning artifacts, intake writes, lifecycle changes, and execution described above are proposed future work. No live queries, other-session inspection, agent dispatch, or mutations were performed.

These conclusions follow the [Superpowers binding](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/superpowers-binding.md), [native issue contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/github-issue-contract.md), and [product decomposition contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/product-decomposition.md).