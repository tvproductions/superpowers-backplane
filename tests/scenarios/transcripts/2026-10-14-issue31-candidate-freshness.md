The bundle maintainer’s two claims are unsupported: their older pin does not define Backplane’s support policy, and the local BP2 report is neither a published cue nor evidence of universal compatibility.

Under [Backplane governance](/Users/jeff/Documents/Code/superpowers-backplane/docs/superpowers-backplane/governance.md):

- **Backplane owns direct Superpowers alignment evidence**, including dated freshness and compatibility claims.
- **The bundle maintainer owns complete-stack integration and acceptance**, consuming Backplane’s scoped cue and evaluating the actual bundle.
- **Adopters verify their actual installed tuple and project overrides.**

| Fixture claim | Assessment |
|---|---|
| SP7/U7 is the latest stable observed today | Supported as a supplied fixture fact; no independent live verification occurred. |
| Published evidence evaluated BP1 with SP6/U6 on Codex | Supported historical evaluation scope. It establishes neither SP7 currentness nor BP2 compatibility. |
| The bundle pins BP1 + SP6/U6 | Supported configuration fact. Its SP pin is older than the latest observed stable; a pin alone proves no compatibility. |
| Local evidence evaluated BP2 with SP7/U7 | Supported only for the stated single Codex host and no-write bookkeeping override. |
| BP2 + SP7/U7 is verified compatible | **UNKNOWN:** “evaluated” does not supply passing results, acceptance, or complete preflight evidence. |
| The combined bundle or other harnesses are compatible with SP7 | Untested; acceptance remains **UNKNOWN**. |
| The local report is a universally published cue | Unsupported: it is uncommitted, unpublished, and restricted to one host/override. |

No supplied result establishes incompatibility either. Missing evidence cannot be converted into a pass or failure.

A published cue must carry:

- The latest stable observed and its checked time.
- Exact evaluated Superpowers and Backplane revisions, relevant artifact hashes, and project overrides.
- Harness and capability/workflow scope, evaluation methods, observed results, acceptance disposition, and unresolved limitations.
- Immutable supporting evidence published with the advertised Backplane revision.
- Verified authorized transport and arrival at the advertised target: exact identities must be reachable and evidence inspectable by consumers. A URL, local commit, or publication proposal is insufficient.

The [installation/preflight contract](/Users/jeff/Documents/Code/superpowers-backplane/skills/managing-superpowers-backlog/references/installing-superpowers.md) also requires provenance, operational discovery, the required GitHub CLI capability surface, and all five named conformance checks. The fixture does not provide those results, report hashes, acceptance records, override authorization/demonstration, or publication-arrival evidence. Even a passing local report would retain its single-host, override-specific scope.

The authorized operation now is this read-only assessment. Proposed future work is for Backplane to obtain and preserve scoped passing evidence for BP2/SP7/U7, for the bundle owner to evaluate the complete stack, and for adopters to validate their actual configurations. Broader claims require corresponding broader evidence. Publication, upstream revision changes, installation changes, and repository or tracker mutations require separate applicable authorization; neither the cue nor the maintainer’s preference supplies it.

Only permitted local guidance was read. No live queries, helpers, writes, Git mutations, installation changes, or agent dispatch occurred.