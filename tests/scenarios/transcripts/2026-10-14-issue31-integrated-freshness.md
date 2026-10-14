The maintainer’s two claims are unsupported: an older bundle pin does not define Backplane’s support policy, and a local report cannot serve as a universally published compatibility cue. This follows the [Backplane governance contract](/Users/jeff/Documents/Code/superpowers-backplane/docs/superpowers-backplane/governance.md).

**Ownership**

- **Backplane** owns direct Superpowers alignment and dated, scoped compatibility/freshness evidence, following the stable channel by default.
- **The bundle maintainer** consumes Backplane’s cue and owns acceptance of the complete integrated stack, including its exact pinned tuple.
- **Adopters** verify their actual installed tuple, harness capabilities, and project overrides. Neither a cue nor a bundle preference authorizes installation changes.

**Assessment of the dated fixture**

| Claim | Assessment |
|---|---|
| SP7/U7 is the latest stable observed today | Supported as a supplied fixture fact, not independently verified live state. |
| Published BP1–SP6/U6 evidence applies to Codex | Supported only within its recorded evaluation scope and results. It establishes no SP7 currentness. |
| The bundle follows the latest stable SP | Unsupported: it still pins SP6/U6 while SP7/U7 is the observed latest stable. |
| BP2–SP7/U7 was evaluated on one Codex host with the override | Supported as a reported local evaluation only. “Evaluated” does not supply a passing or accepted verdict. |
| BP2–SP7/U7 is verified compatible | **UNKNOWN from the supplied inputs**: results, captures, and acceptance are unavailable. Even a demonstrated pass would cover only that host and override. |
| The complete bundle works with BP2–SP7/U7 | Untested. Component evidence cannot establish complete-stack acceptance. |
| Other harnesses or workflows without the override are compatible | Untested; a universal compatibility claim is unsupported. |
| The local report is a published compatibility cue | Unsupported: it is uncommitted and local, with no verified publication or arrival. |

No supplied result establishes incompatibility. Missing tests or evidence mean **UNKNOWN**, rather than a fabricated failure.

**Evidence required with a published cue**

The cue must carry the checked time and latest stable observed; exact evaluated SP and Backplane revisions; relevant artifact hashes; project overrides and their scope; harness and capability boundaries; inspectable methods, captures, scored results, and acceptance; and unresolved limitations. It must classify the latest stable target as verified compatible, untested, or incompatible, with reasons.

Publish immutable evidence with the advertised Backplane revision. Before consumers rely on it, verify authorized transport and arrival at the advertised target: exact commits/artifacts must be reachable and supporting evidence inspectable. A local commit or URL alone is insufficient. These requirements include the [installation and preflight contract](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/installing-superpowers.md).

Here, missing inputs include actual evaluation verdicts, immutable report identities and hashes, host/capability details, override authorization and demonstration, required preflight/conformance captures, review acceptance, and publication reachability.

Only this read-only assessment is authorized. Permissible next steps are read-only examination of supplied evidence and clarification of those gaps. Proposed future work is scoped fresh verification, complete-stack testing by the bundle owner, separate harness testing, and authorized immutable publication with arrival verification. None authorizes an upstream update, commit, publication, or tracker mutation. No live queries, agent dispatch, or mutations were performed.