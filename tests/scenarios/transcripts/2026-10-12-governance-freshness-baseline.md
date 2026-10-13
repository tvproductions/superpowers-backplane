The bundle’s older pin does **not** define Backplane’s support policy, and the local BP2 report does **not** establish universal published compatibility.

Under the [installation contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/installing-superpowers.md), Backplane follows the latest **compatible stable** Superpowers release by default. Recorded revisions identify tested baselines; they are not permanent pins. A newer stable release alone does not prove compatibility or authorize an update.

Ownership follows that boundary:

- **Backplane maintainers own Backplane–Superpowers alignment evidence:** the tested revisions, compatibility checks, harness coverage, limitations, and scope of Backplane’s published claims.
- **The bundle maintainer owns complete-stack acceptance:** validating the actual combined package, pinned components, discovery, configuration, and supported harnesses. Backplane’s component evidence can inform that acceptance but cannot replace it.
- **Adopters own validation of their actual installation** against project rules and the applicable evidence. Neither maintainer’s assurance establishes every adopter’s environment.

| Fixture claim | Assessment |
|---|---|
| SP7/U7 is today’s latest stable release | Supported as a supplied fixture fact; not independently verified. |
| Published evidence evaluated BP1 with SP6/U6 on Codex | Supported historical evaluation scope. Passing compatibility requires the underlying results. |
| The bundle still pins BP1/SP6/U6 | Supported fixture fact. Its upstream revision trails the observed stable release; that does not itself prove incompatibility. |
| BP2 was evaluated with SP7/U7 locally | Supported only for the reported Codex host and no-write bookkeeping override. |
| BP2/SP7/U7 is compatible under ordinary workflows | Unestablished: the override’s effect and underlying results are unavailable. |
| The combined bundle or other harnesses are compatible | Untested on the supplied evidence. |
| The old bundle pin defines Backplane-wide support | Unsupported. It defines the bundle’s selected tuple. |
| The local report is a universally published compatibility cue | Unsupported: it is uncommitted, local, and narrowly scoped. |

A published compatibility cue must travel with durable, accessible evidence identifying the exact Backplane source revision and skill hashes; Superpowers source, channel, and immutable revision; harness/version and installation mode; evaluation date; `gh` capability results; fresh-session discovery; and results for all five named conformance checks. Behavioral evidence needs the exact prompts, response captures, rubric scores, and explicit failures or unknowns. The bookkeeping override must be disclosed, including what it changed and which ordinary execution paths remain untested. Publication and integration identities must make the evidence traceable to the advertised package. Complete-stack claims additionally require tests of that actual bundle. These requirements follow the [compatibility preflight](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/installing-superpowers.md) and [four-harness verification contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md).

The principal gaps are the underlying reports and scores, BP1/BP2 immutable source identities, exact override behavior, host/tool versions, publication provenance, and combined-bundle and other-harness results. Evaluation is not automatically a passing result; missing evidence remains unknown.

**Authorized now:** this read-only fixture assessment. **Proposed future work:** review the missing evidence, validate the candidate under the intended workflows, test the combined bundle and each claimed harness, and prepare a narrowly scoped publication package. Those operations have not been performed or authorized. No upstream update, publication, live GitHub query, agent dispatch, or mutation was performed.