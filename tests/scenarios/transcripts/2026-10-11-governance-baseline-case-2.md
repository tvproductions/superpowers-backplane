Both current **SATISFIED** claims on [outcome #101](https://github.com/example/governance-fixture/issues/101) are unsupported by the fixture’s evidence. This means current satisfaction is **unverified**, not that either criterion has failed.

| Criterion | Assessment at implementation C |
|---|---|
| AC1 | E1 passed R1/S1 at A. The current mapping requires R1/S2, with no supplied equivalence between S1 and S2. C also changes behavior affecting AC1. |
| AC2 | E2 passed the mapped R1/S2 and R2/S1 at B. C changes behavior affecting AC2, so E2 does not establish satisfaction at C. |

PRs #201 and #202 describe implementation contributions. Their combined scope does not independently prove criterion satisfaction, integration, or fresh verification. Preserve E1 and E2 as historical accepted results; do not silently retarget them to newer revisions or commits.

Authority should remain distributed as follows:

- **Approved specifications:** requirement definitions and their approved semantic revisions.
- **Outcome issue:** acceptance criteria, current Coverage and Satisfaction mappings, current claims, and links to supporting evidence.
- **Durable evaluation records:** accepted results identifying the criteria, requirement revisions, implementation commit, verification evidence, and acceptance authority. These can be committed artifacts or durable issue records.
- **Project displays and checkpoints:** derived views or dated snapshots of those authorities, with source identities and revisions. Neither becomes a second mutable backlog master. Plan checkboxes record progress only.

The designated skill and its linked references establish these general authority and verification boundaries. They do **not** prescribe a detailed Coverage and Satisfaction schema or a normative replacement status vocabulary.

For the independent **S2e/B** case:

| Criterion | Assessment |
|---|---|
| AC1 | Still unsupported. Equivalence of S2e to S2 does not bridge E1’s R1/S1 evidence to S2, or establish its applicability at B. |
| AC2 | E2 remains applicable within the fixture: implementation remains B, and the approver explicitly recorded S2e as semantically equivalent to S2. Retain E2’s original revision identity and link the equivalence record. |

An editorial revision alone therefore need not force reevaluation, but it cannot repair an unrelated evidence gap.

Missing inputs include the actual criteria and requirement definitions, evaluation methods and acceptance records, exact implementation deltas, and any evidence bridging E1 from S1/A to S2/B. The supplied records support this assessment as a dated fixture; they provide no independent live verification or closure basis.

The proposed next work is to evaluate **both criteria at C** against their current approved mappings and obtain accepted results. For S2e/B, retain AC2’s evidence with its equivalence linkage and resolve AC1’s missing evidence.

Only read-only assessment is authorized here. Updating claims, recording evaluations, changing displays, transitioning lifecycle state, or closing #101 would require separately authorized operations and the applicable evidence gates. No live queries, mutations, helpers, or agent dispatches were performed.