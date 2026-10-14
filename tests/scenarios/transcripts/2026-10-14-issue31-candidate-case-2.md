Both current **SATISFIED** claims on [outcome #101](https://github.com/example/governance-fixture/issues/101) are unsupported. Under the [governance rules](docs/superpowers-backplane/governance.md), both assess as **UNKNOWN**, not UNSATISFIED: the fixture supplies no applicable failing result.

| Criterion | Current inputs | Accepted historical evidence | Assessment at C |
| --- | --- | --- | --- |
| AC1 | R1/S2 | E1 passed AC1 against R1/S1 at A | **UNKNOWN:** requirement revision mismatch, plus C changes affected behavior. |
| AC2 | R1/S2 and R2/S1 | E2 passed those inputs at B | **UNKNOWN:** matching requirement revisions, but B’s pass does not establish C’s behavior. |

Preserve E1 and E2 at their original inputs and commits. Neither should be retargeted to C.

PR #201 contributes part of R1; PR #202 contributes the remainder of R1 and R2. This supports explicit shared coverage: both PRs contribute to R1-related criteria, and #202 also contributes R2. Contribution coverage alone does not establish acceptance. The fixture does not establish these PRs’ review, merge, or integration state, or identify the owner accepting their combined result. No native hierarchy, dependency, or closure relationship should be inferred from their contribution descriptions.

For the **independent editorial case S2e, with implementation still B**:

| Criterion | Assessment |
| --- | --- |
| AC1 | **UNKNOWN.** Approved S2e↔S2 equivalence cannot bridge E1’s R1/S1↔R1/S2 mismatch. E1 also evaluated A; applicability to B remains unestablished. E2’s AC2 pass cannot substitute for an AC1 evaluation. |
| AC2 | **SATISFIED within the fixture’s stated scope.** E2 matches B and the requirement inputs, with the supplied semantic-equivalence approval bridging S2e to S2. This is fixture-supported reasoning, not independent verification. |

The [product decomposition contract](skills/managing-superpowers-backlog/references/product-decomposition.md) assigns records as follows:

- **Outcome #101’s `Coverage and Satisfaction`:** canonical current mappings, bounded PR contributions, latest accepted evaluation pointers, applicability, and gaps.
- **Immutable project-owned evaluation evidence:** exact criterion/requirement revisions, tested integration commit, method, result, review/acceptance, evidence identities and availability, and remaining obligations. The mutable issue verdict is an index to this evidence.
- **Parent records:** obligation accounting and references to child results, where applicable.
- **Projects:** derived displays refreshed from issue records and accepted evidence, with explicit refresh ownership. A display cannot resolve an evidence gap.
- **Checkpoint pair:** `.sp-bp/state.md` and `.sp-bp/github-state.json` preserve a dated account. They must distinguish the observed SATISFIED claims from the supported UNKNOWN assessments. Source, verified-delivery, and later storage commits remain separate identities.

The [checkpoint contract](skills/managing-superpowers-backlog/references/repository-checkpoint.md) also distinguishes capture completeness from delivery success: a complete capture can faithfully record UNKNOWN satisfaction. This fixture does not establish an accepted checkpoint.

The missing evidence includes full criterion/requirement wording and approval anchors; immutable evaluation records, methods and evidence availability; contribution boundaries and combined-result owner; actual PR review/integration facts; and accepted verification at C. Project identity, presentation mode, capture scope, and checkpoint acceptance evidence are also absent. The fixture’s `updatedAt` value supplies no semantic-equivalence or freshness proof.

**Authorized now:** this read-only assessment and refinement using the supplied records.

**Proposed, requiring separate applicable authorization:** revalidate AC1 and AC2 against current approved inputs at C, accept immutable results, then reconcile #101’s pointers and claims. Any issue, parent, Project, or checkpoint update has its own authorized scope. Closure additionally requires accepted integration, fresh project checks, and lifecycle reconciliation under the [PR closeout contract](skills/managing-superpowers-backlog/references/pr-completion.md).

No live queries, mutations, helper invocations, or agent dispatch were performed.