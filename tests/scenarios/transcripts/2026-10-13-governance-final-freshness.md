The bundle’s older pin does **not** define Backplane’s support policy, and the local BP2 report is **not** a universally published compatibility cue. These conclusions follow the [freshness governance](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/docs/superpowers-backplane/governance.md).

Ownership is divided:

- **Backplane** owns direct Superpowers alignment and dated published compatibility/freshness evidence.
- **The bundle maintainer** consumes that evidence and owns acceptance of the complete integrated stack. Its pin describes the bundle’s chosen tuple.
- **Adopters** verify their actual revisions, harness capabilities, installation provenance, and project overrides.

The fixture supports these distinctions:

| Claim | Assessment |
|---|---|
| SP7/U7 is the latest stable observed today | Supported as a dated fixture fact; not independently verified live. |
| Published evidence evaluated BP1 with SP6/U6 on Codex | Supported historical evaluation scope. It does not establish alignment with today’s stable release. |
| BP1/SP6 is compatible | A passing verdict is not supplied. “Evaluated” alone does not prove compatibility. |
| BP1 works with SP7/U7 | Untested by the supplied records. |
| BP2 was evaluated with SP7/U7 | Supported only for one Codex host with the stated bookkeeping override. Results are unspecified, so verified compatibility remains unknown. |
| BP2/SP7 works across harnesses or without that override | Untested; a universal compatibility claim is unsupported. |
| The combined bundle is accepted | Unknown: complete-stack testing and acceptance are absent. Direct component evidence cannot substitute for them. |
| The uncommitted report is published evidence | Unsupported. Local evaluation and publication are separate facts. |

No supplied failure establishes incompatibility. Missing tests or results mean **UNKNOWN**, rather than an invented pass or failure.

A published cue must travel with:

- The latest stable observed and the actual check time.
- Exact evaluated SP and Backplane revisions, relevant artifact hashes, and project overrides.
- Harness/capability scope, methods, observed results, and unresolved limitations.
- Immutable, inspectable supporting evidence published with the advertised Backplane revision.
- Verified authorized transport and arrival at the advertised target: exact commits/artifacts must be reachable by consumers. A local commit or URL alone is insufficient.

The missing inputs include passing/scored results, exact BP artifact identities and hashes, override authorization and demonstrated scope, preflight and all five conformance-check evidence, fresh-session discovery, review/acceptance records, other-harness coverage, bundle integration results, and consumer-visible publication/arrival evidence. The [installation contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/installing-superpowers.md) defines those compatibility checks.

The next permissible work **within this probe** is read-only examination of any additionally supplied evidence and refinement of scoped conclusions. Proposed future work is to fill the direct-alignment gaps, have the bundle owner evaluate its exact complete stack, and prepare an immutable scoped cue. Testing that requires writes, installation changes, committing, transport, and publication need their applicable authorization; this assessment authorizes none of them. The stable-channel preference also supplies no automatic update authority.