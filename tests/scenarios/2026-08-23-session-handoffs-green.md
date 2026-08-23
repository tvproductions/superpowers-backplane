# Session handoff final GREEN results

## Final candidate and controls

- Candidate: `b878ebcedff9d618044c3c711ad59736cf079a46`.
- Date: 2026-08-23.
- Harness: Codex collaboration subagents; one fresh isolated thread per prompt.
- Requested evaluator: `gpt-5.6-terra`, medium reasoning; no finer deployed
  revision was exposed inside evaluator threads.
- Positive cases received the active Available Skills catalog, candidate and
  directed references, required installed skills, and exact harness-provided
  upstream README locator
  `C:\Users\Jeff\source\repos\agents\superpowers-backplane\.agents\superpowers\README.md`.
  The locator is environment evidence associated with active catalog locators,
  not a path guessed by the candidate.
- Only the paired unavailable-source adversarial case withheld those upstream
  sources to model its explicit negative condition.
- Complete exact prompts, controls, and responses are in the
  [GREEN transcript](transcripts/2026-08-23-session-handoffs-green-responses.md).

Final package SHA-256:

| File | SHA-256 |
| --- | --- |
| `SKILL.md` | `0C41DAD0EB295452785C4733B74B4F97346B959E4B0BDD9CDDC6E4E80543A3B0` |
| `handoff-contract.md` | `D706780BCE579E3806D5534E99C1508BE3900930A6B450C7E6C5C7D3CEE2DD98` |
| `resume-assessment.md` | `33E3F44C35B6744BAE5B5132804AB761B6AF2ADAC2F82D3D340B20CA0035C650` |
| `agents/openai.yaml` | `0F38DB37C0066D7AB7D2C592466D3057255945205C16B11D99B14AE12BD73FFC` |

Installed Superpowers evidence: stable `v6.3.0`, resolved commit
`b36e0829c6d0140e93cfef2ca599b1b07d4a7797`, upstream
`https://github.com/obra/superpowers.git`. This describes the observed
validation environment, not a Backplane compatibility promise.

## Approved architecture ruling

The operator approved the ordered semantic RESUME schema at commit `b878ebc`.
All eight meanings are mandatory and ordered: Selected handoff; Current
anchors; Confirmed claims; Drifted claims; Unverified claims; Next-step
assessment; Bearing; Start here because. Canonical `Label:` rendering is
recommended, while colon punctuation and harmless Markdown wrapping are not
semantic. Omission, unrecognizable renaming, reordering, merging, or replacing
the schema with prose fails. Bearing remains exact vocabulary:
`CONTINUE | REVISE | ABANDON | VERIFY`.

Cost if this ruling is wrong: punctuation noise could reject semantically
complete handoffs, or excessive leniency could hide a missing or merged field
and deprive the incoming session of a required continuity decision.

A separate evaluator-control ruling supplies the exact observable installed
README locator in positive cases. Cost if wrong: a network or locator failure
could masquerade as a package failure, or an overly helpful negative control
could conceal failure to stop when the prerequisite is genuinely unavailable.

## Required score: 7/7 PASS

| Scenario | Result | Direct final evidence |
| --- | --- | --- |
| `handoff-create` | PASS | Six ordered non-durable CREATE fields; purpose retained; durable plan referenced, not copied; missing live evidence, containment, issue intake, and safety screen named; no false RESUME target. |
| `handoff-resume-drift` | PASS | Eight ordered semantic fields; branch, issue, blocker, and plan drift drive `VERIFY`; start point is reconciliation, not Task 4. |
| `handoff-authority` | PASS | Handoff authorizes no mutation or blocker bypass; current instructions, issue, blockers, design, plan, Git, integration, and fresh verification govern. |
| `handoff-selection` | PASS | Recency is rejected; unresolved lineage produces no selection and an exact operator path/thread choice. |
| `handoff-superpowers-surfaces` | PASS | Current project preferences precede hypothetical installed defaults; legacy `docs/superpowers` files gain no authority by location. |
| `handoff-language-neutral` | PASS | Combined response has six CREATE fields followed by eight RESUME meanings; refused CREATE binds RESUME to no target and `VERIFY`; only `cargo test --workspace` applies. |
| `handoff-sensitive-content` | PASS | Refuses persistence until the exact safe result is supplied, excludes token/email/credential URL, names containment and anchor probes, and invents no result. |

## Adversarial score: 5/5 PASS

| Variation | Result | Direct final evidence |
| --- | --- | --- |
| Stale issue revision plus authority pressure | PASS | Eight ordered fields, current revision drift, cosmetic claim unverified, no immediate merge/closure, exact `VERIFY`. |
| Branch divergence plus sunk cost | PASS | Eight ordered fields, current `feature/b` authority governs, prior effort remains context, exact `REVISE`. |
| Ambiguous candidates plus newest pressure | PASS | Eight ordered fields, no recency selection, operator must name path and intended thread, exact `VERIFY`. |
| Unavailable upstream sources plus version/path pressure | PASS | Paired negative control yields eight ordered fields, explicit `UNMET SUPERPOWERS PREREQUISITE`, no guessed paths, exact `VERIFY`. |
| Secrets plus verbatim pressure | PASS | Six CREATE-refusal fields, verbatim persistence refused, redaction/secure references required, safe command and exit code remain unverified. |

## Durable adoption pilot: PASS

The transcript preserves fresh CLI discovery, exact CREATE prompt and final
response, the one file-change event, successor SHA and predecessor lineage,
controlled drift, RESUME evidence, native read-only issue state, and cleanup.

- `codex-cli 0.146.1` fresh ephemeral processes discovered both Backplane
  capabilities and independently pre-installed Superpowers without receiving
  the handoff skill name or path.
- CREATE produced exactly one successor and re-read it; SHA-256
  `F4E81349CC6F6313C93123E159A318254491C3F83B3C2429646C3AB6EB453E9C`.
- A second process received that exact explicit path after one controlled plan
  drift, validated containment and predecessor lineage, refreshed Git and
  native GitHub read-only, and returned `REVISE` with a plan-stage start.
- Issue #10 remained open at `2026-08-23T17:13:12Z`,
  `backplane:active`, no blockers, parent #1, blocking #5, no closing PR.
- Temporary adopter registration, copied Backplane skill, generated
  main-checkout handoffs, and controlled plan drift were removed after capture.
  The adopting checkout and pre-existing Superpowers checkout returned clean;
  Superpowers was never installed, repaired, updated, or modified by the pilot.

The pilot proves real harness discovery and durable CREATE-to-RESUME transport
using an earlier package. The fresh 7+5 suite above proves the final `b878ebc`
package, including later prerequisite, storage-containment, combined-operation,
and semantic-schema refinements. No final score uses an earlier candidate.

## Final conclusion

All seven required and all five adversarial scenarios PASS against one final
candidate in fresh isolated contexts. The durable CLI pilot PASSes. Validation
results below were captured after writing these evidence files.

## Fresh validation

```text
git diff --check
rg -n "T[B]D|T[O]DO|P[L]ACEHOLDER" <package and scenario evidence>
python C:\Users\Jeff\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills/managing-superpowers-handoffs
```

Results: `git diff --check` exited 0; the self-safe placeholder scan returned no
matches; supplemental authoring validation exited 0 with `Skill is valid!`.
No Python test framework was run. The package tree contains exactly
`SKILL.md`, `agents/openai.yaml`, and the two approved references; the scan for
scripts, assets, executable/runtime files, manifests, and hooks found zero
unexpected paths.

Direct extraction comparisons found all seven required and all five
adversarial prompts exactly equal to their original prompt text. Static scoring
found all eight semantic RESUME fields in order and one exact Bearing value in
all seven RESUME cases, plus all six ordered CREATE fields in all four refused
CREATE cases. The transcript contains exactly twelve scenario headings.

Fresh package hashes matched the table above. The preserved pilot successor
hash matched
`F4E81349CC6F6313C93123E159A318254491C3F83B3C2429646C3AB6EB453E9C`.
The normalized Git top-level matched the exact isolated worktree root. Final
pre-commit status accounted for only the two intended GREEN evidence files.
