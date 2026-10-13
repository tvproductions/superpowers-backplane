The maintainer’s two claims are unsupported: **the bundle’s older pin does not define Backplane’s support policy, and the local BP2 report is not a universally published compatibility cue.** This follows the [freshness governance contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/docs/superpowers-backplane/governance.md).

Ownership is explicit:

- **Backplane** owns direct Superpowers alignment and dated compatibility/freshness evidence.
- **The bundle maintainer** consumes that evidence and owns complete-stack integration and acceptance.
- **Adopters** verify their actual component tuple, harness capabilities, and project overrides.

The fixture supports these conclusions as of **2026-10-13**:

| Claim | Assessment |
|---|---|
| SP7/U7 is the latest stable observed today | Supported by the supplied fixture; not independently verified. |
| Published evidence evaluated BP1 with SP6/U6 on Codex | Supported historical evaluation scope. It does not establish alignment with today’s latest stable. |
| The bundle pins BP1 + SP6/U6 | Supported configuration fact. Complete-stack acceptance evidence is not supplied. |
| BP2 with SP7/U7 was evaluated locally | Supported only for one Codex host using the specified no-write bookkeeping override. |
| BP2 + SP7/U7 is verified compatible even within that scope | Not established: the fixture says “evaluated” but supplies no results, scoring, or acceptance disposition. |
| BP2 + SP7/U7 works across other harnesses or the combined bundle | Untested in the supplied records; universal compatibility is unsupported. |
| SP7/U7 is incompatible | Unsupported: no failing compatibility evidence is supplied. |

Compatibility therefore remains **UNKNOWN where passing, accepted evidence is unavailable**. Missing evidence is not an incompatibility finding. Historical results cannot be transferred from BP1 to BP2, or from SP6/U6 to SP7/U7, without reconciliation and relevant revalidation.

A published cue must travel with immutable, inspectable evidence identifying:

- The checked time and latest stable observed.
- Exact evaluated Backplane and Superpowers revisions, relevant artifact hashes, harness/version/capability scope, and project overrides.
- Methods, captured outputs, scored results, review/acceptance disposition, and unresolved limitations.
- The bookkeeping override’s explicit authorization, scope, and demonstrated behavior.
- Authorized transport and verified arrival at the advertised publication target: exact identities must be reachable and supporting evidence inspectable by consumers.

An uncommitted report, a local commit, or a URL alone does not establish publication or arrival. Even a passing local result would remain limited to its tested host and override.

The next permissible action under this probe is **read-only refinement using supplied records**: inspect the actual reports, outcomes, acceptance records, artifact identities, and override evidence if provided. Proposed future work is to validate the intended harness/workflow matrix, obtain bundle-owned integration acceptance, and publish a scoped immutable cue with verified arrival. Those activities are **not authorized operations here**; installation updates and publication require their separate authority.

I read the designated skill and its directly linked references. No live GitHub queries, session-answer inspection, agent dispatch, helpers, or mutations were performed.