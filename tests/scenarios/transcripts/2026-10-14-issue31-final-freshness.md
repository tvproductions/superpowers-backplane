Backplane owns direct Superpowers alignment evidence; the bundle maintainer owns complete-stack acceptance. The older bundle pin does **not** define Backplane’s support policy, and the local BP2 report does **not** establish universal published compatibility. These conclusions follow the [governing doctrine](/Users/jeff/Documents/Code/superpowers-backplane/docs/superpowers-backplane/governance.md).

This assessment uses only the dated fixture, without independent live verification.

| Claim | Assessment |
|---|---|
| SP7/U7 is the latest stable observed today, 2026-10-14 | Supported by the fixture. The precise observation time is unavailable. |
| BP1 was evaluated with SP6/U6 for Codex, with published evidence | Supported as a historical, scoped evaluation. The fixture does not supply its actual results, so a passing verdict cannot be inferred. |
| The bundle’s SP6/U6 pin is current | Unsupported: it trails the observed latest stable. That alone does not establish incompatibility. |
| BP2 was locally evaluated with SP7/U7 | Supported for one Codex host using the no-write bookkeeping override. Results are unspecified; verified compatibility remains **UNKNOWN**. |
| BP2/SP7 works without that override, across other harnesses, or in the combined bundle | Untested; compatibility is **UNKNOWN**. |
| The local report is universally published compatibility evidence | Unsupported: it is uncommitted, local, and narrowly scoped. |
| SP7/U7 is incompatible | Unsupported: no failed compatibility check is supplied. |

Backplane follows the latest **compatible stable** upstream release by default. No edge-channel selection is supplied. Backplane must evaluate and publish its direct alignment; the bundle maintainer must test and accept the combined stack. Adopters must verify their actual component revisions, harness capabilities, and project overrides. Neither a compatibility cue nor a bundle preference authorizes installation changes.

A published cue must carry:

- The latest stable observed and its checked time.
- Exact evaluated SP and Backplane revisions, relevant artifact/skill hashes, and the advertised Backplane revision.
- Tested harness versions, capabilities, workflows, and the exact override scope.
- Methods, observed results, review/acceptance disposition, inspectable immutable supporting evidence, and unresolved limitations.
- Verified authorized transport and arrival at the advertised publication target: exact commits/artifacts must be reachable and supporting evidence available to consumers.

The fixture lacks detailed results, hashes, host/capability identities, acceptance records, and BP2 publication/arrival evidence. Even a later local commit would not by itself establish publication. The [installation/preflight contract](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/installing-superpowers.md) requires candidate-specific checks and fresh discovery; older evidence cannot establish the changed tuple’s compatibility.

The next permissible action **here** is read-only refinement of the assessment or a proposed evidence checklist. Proposed future work is to validate BP2/SP7’s scoped results, test the claimed harness/workflow coverage, obtain separate complete-stack acceptance, and publish immutable evidence with verified arrival. Those tests, writes, publication, and any upstream revision change are **not authorized by this probe**.

No live queries, helpers, writes, Git mutations, or agent dispatch were performed.