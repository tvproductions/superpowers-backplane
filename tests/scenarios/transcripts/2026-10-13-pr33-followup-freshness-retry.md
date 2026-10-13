The maintainer’s two claims are unsupported: **the bundle’s older pin does not define Backplane’s support policy**, and **the local report is not a universally published compatibility cue**. This follows the [freshness governance](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/docs/superpowers-backplane/governance.md:219).

Ownership is split:

- **Backplane** owns direct Superpowers alignment and dated, scoped compatibility/freshness evidence.
- **The bundle maintainer** owns complete-stack integration and acceptance.
- **Adopters** verify their actual installed tuple, harness capabilities, and project overrides.

| Fixture claim | Assessment |
| --- | --- |
| SP7/U7 is the latest stable observed today | Supported as a supplied fixture fact, without independent live verification. |
| Published evidence evaluated BP1 with SP6/U6 on Codex | Supported historical evaluation scope. It does not establish currentness against SP7. |
| The bundle pins BP1 + SP6/U6 | Supported configuration fact; neither currentness nor complete-stack acceptance follows from a pin. |
| Local evidence evaluated BP2 with SP7/U7 | Supported only for the stated Codex host and no-write bookkeeping override. |
| BP1 works with SP7/U7 | Untested in the supplied records. |
| BP2 + SP7/U7 works in the combined bundle or other harnesses | Explicitly untested. |
| Either evaluated tuple passed compatibility | UNKNOWN: the fixture supplies no observed results, scored checks, or acceptance disposition. No incompatibility is established either. |
| The local report proves universal, published support | Unsupported in publication status and scope. |

A published cue must carry the checked time and latest stable observation; exact SP and Backplane revisions; relevant artifact hashes; harness/capability scope and project overrides; methods, results, and unresolved limitations. It must classify the latest stable target as verified compatible, untested, or incompatible with supporting reasons. Publish immutable evidence alongside the advertised Backplane revision, then verify authorized transport and arrival: exact identities must be reachable at the advertised target and supporting evidence inspectable by consumers. A URL or local commit alone is insufficient.

The missing inputs are the actual reports and results, exact evidence identities/hashes, review or acceptance records, and publication-arrival evidence. The override’s authorization and demonstrated boundaries are also unavailable. The [preflight contract](/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog/references/installing-superpowers.md:127) requires all five named conformance checks and fresh discovery; an evaluation’s existence does not establish that these passed.

**Permissible now:** refine this assessment from additional supplied fixture records and draft a scoped cue or verification matrix in the response. **Proposed future work:** validate Backplane’s SP7 alignment, test the complete bundle and each advertised harness/workflow, and publish immutable scoped evidence with verified arrival under separate authorization. Neither a cue nor a bundle preference authorizes installation changes.

Only the read-only assessment was authorized and performed. No live GitHub queries, other-session inspection, agent dispatch, or mutations occurred.