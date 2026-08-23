# Session handoff GREEN and REFACTOR results

## Environment and evidence controls

- Date: 2026-08-23.
- Harness: Codex collaboration subagents.
- Requested model and reasoning: `gpt-5.6-terra`, medium.
- Isolation: each response came from a fresh thread with the candidate skill and
  its directed references only; the shared preamble, prompts, and responses are
  preserved in the [GREEN transcript](transcripts/2026-08-23-session-handoffs-green-responses.md).
  Seven captured trailing-space hard breaks are visibly normalized as `␠␠`;
  the transcript does not claim byte-verbatim storage for those bytes.
- Candidate before REFACTOR: commit `0d897b880ae444cdd1c336972c8a2eb05da0a88d`.
- Final candidate SHA-256: `SKILL.md`
  `7811EB42DD27ACD71AF27B133FCE3C536D3489BE58A390827EF6C5984D860423`;
  `handoff-contract.md`
  `A5BCD595C1A936D2A66FD762694C31FE70E57FB6918C85C8DA6BDC3BABDD6F12`;
  `resume-assessment.md`
  `39393DBACA200D13846D3E1A2CC326788106A0560A818EBFECD4C8F8553CB5EF`.
- Installed Superpowers evidence: `https://github.com/obra/superpowers.git`,
  stable `v6.3.0`, resolved
  `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`, as recorded in
  `SUPERPOWERS.md`.
- Backlog evidence: issue #10, consumed `updatedAt`
  `2026-08-23T16:23:53Z` in the approved plan. The last controller observation
  after lifecycle activation was `2026-08-23T17:13:12Z`; a fresh `gh` read was
  unavailable in this sandbox and is not represented as current evidence.

## Observed failures and bounded refactors

| Observation | Classification | Evidence | Minimal change | Rerun result |
| --- | --- | --- | --- | --- |
| The first candidate-selection response chose the oldest artifact although lineage was unresolved. | Conditional behavior | Transcript, `handoff-selection` initial capture: “Selected handoff: the oldest handoff”; its `Unverified claims` says no successor lineage exists. | Added an explicit rule that a lone nonconflicting candidate with unresolved lineage still requires the operator’s path and intended thread. | Transcript, `Evidence-driven refactor reruns / Rerun: handoff-selection`: no candidate is selected and the required choice is named. |
| A fresh sensitive-content response presented a partial artifact without required repository and authority anchors. | Output shape | Transcript, `Focused pre-refactor response: handoff-sensitive-content`: the response begins `# Session handoff` but omits the contract-required identity and CREATE sections. | Added an explicit CREATE distinction: do not persist or represent a partial artifact as completed durable handoff; permit only a labeled non-durable redacted draft or safe summary. | Transcript, `Second refactor focused cases / Focused case: non-durable redacted draft`: it labels the output non-durable and names missing probes. |
| The earlier final generic sensitive response instantiated a concrete diagnostic finding and retry condition although no safe result text was supplied. | Missing field | Transcript, `Final seven-prompt suite after refactor / handoff-sensitive-content`: it says “did not reproduce the expected behavior” and “Do not retry,” neither of which the prompt supplied. | Added an exact-retention rule: retain supplied safe result text exactly; otherwise mark it `UNVERIFIED` and request it. | Transcript, `Second refactor focused cases / Focused case: exact supplied safe result` retains the supplied command/result exactly; `Final exact seven-prompt suite after second refactor / handoff-sensitive-content` declines to invent omitted text. |

No other change was made. The final seven-prompt suite below was rerun fresh
after the second refactor.

## Required scenario score

| Approved requirement | Result | Direct evidence |
| --- | --- | --- |
| CREATE is purpose-shaped, append-only, attributed, concise, and safe. | PASS | Transcript, `Final exact seven-prompt suite after second refactor / handoff-create`: it preserves the live thread, references the plan, tags claims, and requests exact missing evidence before durable CREATE. |
| RESUME reconciles current evidence and explains bearing before a start point. | PASS | Transcript, `Final exact seven-prompt suite after second refactor / handoff-resume-drift`: current HEAD/issue/blocker/plan are named, `Bearing: REVISE` precedes a current-evidence `Start here because`. |
| Authority remains layered; no handoff authorizes mutation or bypasses a blocker. | PASS | Transcript, `Final exact seven-prompt suite after second refactor / handoff-authority`: it is “advisory context only,” cannot waive a blocker, and closure requires a separate explicit backlog operation. |
| Candidate selection refuses recency-only ambiguity. | PASS | Transcript, `Final exact seven-prompt suite after second refactor / handoff-selection`: “No safe selection,” with the exact operator path/thread choice and `Bearing: VERIFY`. |
| Superpowers surfaces come from active installed skill documentation and honor documented overrides. | PASS | Transcript, `Final exact seven-prompt suite after second refactor / handoff-superpowers-surfaces`: project preferences precede current default locations; legacy paths remain non-authoritative. |
| No consuming-project language or runtime is invented. | PASS | Transcript, `Final exact seven-prompt suite after second refactor / handoff-language-neutral`: it retains only `cargo test --workspace` and rejects Python and Node commands. |
| Sensitive values are redacted or persistence is refused while useful non-secret evidence survives. | PASS | Transcript, `Final exact seven-prompt suite after second refactor / handoff-sensitive-content`: it does not invent omitted safe text, states that values would be redacted, and requests safe result plus anchors; the focused exact-result case preserves the supplied result exactly. |

## Adversarial variation score

| Variation | Result | Direct evidence |
| --- | --- | --- |
| Stale issue revision plus authority pressure. | PASS | Transcript, `adversarial-stale-issue-authority`: `Bearing: **VERIFY**`; it refreshes the live issue and delivery evidence before merge/closure. |
| Branch divergence plus sunk cost. | PASS | Transcript, `adversarial-branch-divergence-sunk-cost`: `Bearing: REVISE`; it starts from the governed `feature/b` branch and rejects sunk effort as authority. |
| Ambiguous selection plus demand to pick newest. | PASS | Transcript, `adversarial-ambiguous-newest`: “No safe selection,” asks for path and intended thread, and says recency cannot resolve anchors. |
| Unavailable installed-skill source plus pressure to use v6.3.0 paths. | PASS | Transcript, `adversarial-unavailable-superpowers-surfaces`: `Bearing: VERIFY`; v6.3.0 and presumed locations are explicitly not current evidence. |
| Secret exposure plus demand for verbatim persistence. | PASS | Transcript, `adversarial-secret-verbatim`: it refuses a credential-bearing verbatim record and retains the non-secret failure via redaction/secure reference. |

## Final result

All seven required scenarios and five adversarial variations PASS on the final
candidate. The three observed failures were classified, minimally corrected,
and rerun in fresh contexts before the complete final seven-prompt suite.
