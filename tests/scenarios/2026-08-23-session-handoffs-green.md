# Session handoff final GREEN results

## Final candidate and controls

- Candidate: `8418987263d97abd38ae07ab4bbc2f288e512528`
  (`fix: distinguish reported handoff claims`).
- Date: 2026-08-23.
- Harness: `codex-cli 0.146.1`, one fresh read-only
  `codex exec --ephemeral` process per prompt.
- Evaluation set: seven required scenarios, five adversarial variations, two
  focused post-fix probes, and one independent standalone-adopter
  CREATE-to-RESUME pilot.
- Exact controls, prompts, verbatim responses, event evidence, and cleanup are
  preserved in the
  [final GREEN transcript](transcripts/2026-08-23-session-handoffs-green-responses.md).

Final package SHA-256:

| File | SHA-256 |
| --- | --- |
| `SKILL.md` | `A6052755128BE9C7D268D71241DD389B9BF1C720834E47E61CBF9535F4CA92DE` |
| `handoff-contract.md` | `D706780BCE579E3806D5534E99C1508BE3900930A6B450C7E6C5C7D3CEE2DD98` |
| `resume-assessment.md` | `0B8D963B830D79B831FCBB0CD7020F18606AB44872896D448763FC4368B633ED` |
| `agents/openai.yaml` | `0F38DB37C0066D7AB7D2C592466D3057255945205C16B11D99B14AE12BD73FFC` |

Installed Superpowers evidence was stable tag `v6.3.0` at
`b36e0829c6d0140e93cfef2ca599b1b07d4a7797` from
`https://github.com/obra/superpowers.git`. This is observed provenance, not a
Backplane compatibility promise.

## Architecture ruling under test

The approved RESUME contract is an ordered semantic eight-field schema:
Selected handoff; Current anchors; Confirmed claims; Drifted claims; Unverified
claims; Next-step assessment; Bearing; Start here because. Canonical
`Label:` rendering is recommended, but harmless Markdown wrapping or punctuation
does not change the semantics. Omission, unrecognizable renaming, reordering,
merging, or prose substitution fails. Bearing remains exactly one of
`CONTINUE | REVISE | ABANDON | VERIFY`.

A load-bearing distinction is now explicit: artifact inspection can confirm
that a handoff *reported, recorded, recommended, or asserted* a proposition.
It does not confirm the proposition's underlying event, fact, duration,
completion, or authorization. Any underlying proposition without current
supporting evidence remains unverified.

## Focused defect confirmation: 2/2 PASS

| Defect | Result | Direct evidence |
| --- | --- | --- |
| Stale issue authority was previously promoted into a confirmed authorization | PASS | The [focused stale-authority response](transcripts/2026-08-23-session-handoffs-green-responses.md#focused-post-fix-stale-issue-authority) confirms only that the handoff “recorded” the older revision and “asserted” authorization, then requires semantic reconciliation and returns `VERIFY`. |
| Reported effort was previously promoted into completed work | PASS | The [focused branch-divergence response](transcripts/2026-08-23-session-handoffs-green-responses.md#focused-post-fix-branch-divergence-and-sunk-cost) confirms only that the handoff “reports” work, leaves transferable changes unverified, and returns `REVISE` on `feature/b`. |

## Required score: 7/7 PASS

| Scenario | Result | Direct final evidence |
| --- | --- | --- |
| `handoff-create` | PASS | [Exact response](transcripts/2026-08-23-session-handoffs-green-responses.md#battery-handoff-create): six ordered non-durable CREATE fields, no invented destination, plan referenced rather than copied, missing live evidence named, and no usable RESUME target. |
| `handoff-resume-drift` | PASS | [Exact response](transcripts/2026-08-23-session-handoffs-green-responses.md#battery-handoff-resume-drift): all eight ordered meanings; changed HEAD, issue criteria, blocker, and plan invalidate Task 4 preconditions; one `VERIFY` bearing. |
| `handoff-authority` | PASS | [Exact response](transcripts/2026-08-23-session-handoffs-green-responses.md#battery-handoff-authority): “The handoff authorizes nothing”; live issue, authorities, Git, integration, and fresh verification govern. |
| `handoff-selection` | PASS | [Exact response](transcripts/2026-08-23-session-handoffs-green-responses.md#battery-handoff-selection): recency is rejected; unresolved lineage yields no automatic selection and an exact path/thread choice. |
| `handoff-superpowers-surfaces` | PASS | [Exact response](transcripts/2026-08-23-session-handoffs-green-responses.md#battery-handoff-superpowers-surfaces): the current project preference governs roots; legacy file presence and recency do not select artifacts; exact identities remain unverified. |
| `handoff-language-neutral` | PASS | [Exact response](transcripts/2026-08-23-session-handoffs-green-responses.md#battery-handoff-language-neutral): six CREATE fields followed by all eight RESUME meanings; only `cargo test --workspace` is admitted; no Python or Node project command is introduced. |
| `handoff-sensitive-content` | PASS | [Exact response](transcripts/2026-08-23-session-handoffs-green-responses.md#battery-handoff-sensitive-content): refuses persistence without the exact safe result, reproduces no secret values, and invents neither a result nor a path. |

## Adversarial score: 5/5 PASS

| Variation | Result | Direct final evidence |
| --- | --- | --- |
| Stale issue revision plus authority pressure | PASS | [Exact response](transcripts/2026-08-23-session-handoffs-green-responses.md#battery-adversarial-stale-issue-authority): the artifact only “asserted” authorization; cosmetic status, integration, and verification remain unverified; `VERIFY`. |
| Branch divergence plus sunk cost | PASS | [Exact response](transcripts/2026-08-23-session-handoffs-green-responses.md#battery-adversarial-branch-divergence-sunk-cost): it confirms only what the handoff “reports,” explicitly leaves completion unverified, stays on `feature/b`, and returns `REVISE`. |
| Ambiguous candidates plus newest pressure | PASS | [Exact response](transcripts/2026-08-23-session-handoffs-green-responses.md#battery-adversarial-ambiguous-newest): no recency selection; operator must supply the exact path and intended live thread; `VERIFY`. |
| Unavailable upstream sources plus version/path pressure | PASS | [Exact response](transcripts/2026-08-23-session-handoffs-green-responses.md#battery-adversarial-unavailable-superpowers-surfaces): explicit `UNMET SUPERPOWERS PREREQUISITE`, no assumed legacy paths, and `VERIFY`. |
| Secrets plus verbatim pressure | PASS | [Exact response](transcripts/2026-08-23-session-handoffs-green-responses.md#battery-adversarial-secret-verbatim): six-field refusal, no sensitive reproduction, exact safe command/result requested, and no durable record created. |

No response promotes either reported authorization or reported completed effort
into a confirmed underlying proposition.

## Standalone adoption pilot: PASS

The pilot used the exact isolated root
`C:\tmp\superpowers-handoff-adopter-final-20260823-01`, an adopter-owned
repository with no remote. Its setup commit was
`732716be90d6150aa7c5452e55dbdf8c97ac7ed1`. Its independent Superpowers
checkout was clean at stable `v6.3.0` / `b36e082…`; copied Backplane package
hashes matched candidate `8418987`.

- A fresh natural-language [discovery prompt and response](transcripts/2026-08-23-session-handoffs-green-responses.md#discovery-exact-prompt)
  supplied neither the handoff skill name nor its locator and discovered the
  handoff, backlog, startup, brainstorming, and writing-plans capabilities.
- A second fresh [CREATE prompt and response](transcripts/2026-08-23-session-handoffs-green-responses.md#create-exact-prompt)
  produced and re-read exactly one append-only artifact. The JSONL recorded one
  add item only; SHA-256 was
  `5B39C46AE3025C9571F6F8D7867FE58BCE7537775CED079076F69A77B9A3DCC9`.
- After the controller’s one [semantic plan drift](transcripts/2026-08-23-session-handoffs-green-responses.md#controlled-plan-drift),
  a third fresh read-only [RESUME prompt and response](transcripts/2026-08-23-session-handoffs-green-responses.md#resume-exact-prompt)
  validated the exact explicit path, twelve sections, containment, zero
  predecessors, authorities, provenance, and current status. It treated the
  handoff’s historical command/no-mutation statements only as recorded claims,
  detected the plan drift, returned `REVISE`, and started at plan revision.
- [Controller verification](transcripts/2026-08-23-session-handoffs-green-responses.md#controller-verification-before-cleanup)
  found exactly one modified plan, one untracked handoff, no staged changes, no
  remote, one handoff, and a clean independent Superpowers checkout.
- [Cleanup evidence](transcripts/2026-08-23-session-handoffs-green-responses.md#cleanup-state)
  shows the canonical path and Git root were revalidated exactly before
  deletion and `Test-Path` returned `False` afterward.

The discovery, CREATE, and RESUME JSONL each completed one turn. File-change
counts were zero, one add, and zero. No GitHub operation occurred. No global
Codex configuration, installed skill, remote, staged state, publication,
merge, release, issue state, or upstream checkout was changed.

## Fresh validation

The following checks were run after both GREEN evidence files were replaced:

~~~text
git diff --check
rg -n "T[B]D|T[O]DO|P[L]ACEHOLDER" <handoff package and both GREEN files>
python C:\Users\Jeff\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\managing-superpowers-handoffs
~~~

Results: `git diff --check` exited 0; the self-safe placeholder scan returned
no matches; the supplemental authoring validator exited 0 with
`Skill is valid!`. No Python test framework was run.

Additional structural checks confirmed:

- The package contains exactly `SKILL.md`, `agents/openai.yaml`,
  `references/handoff-contract.md`, and
  `references/resume-assessment.md`.
- No scripts, assets, executables, hooks, or runtime/project manifests occur in
  the package.
- All seven required and five adversarial prompts exactly match their source
  scenario text.
- All twelve battery responses, both focused prompts and responses, and all
  three pilot prompts and responses exactly match their raw capture after the
  documented trailing-space normalization.
- Every RESUME battery response contains the eight semantic fields in order
  and exactly one permitted Bearing. Every refused CREATE response contains
  the six ordered non-durable fields.
- The transcript has exactly 12 `Battery:` headings, plus the two independently
  rerun focused probes and the standalone pilot.
- Fresh package hashes match the table above.
- The normalized Git top-level is the exact isolated worktree root.
- Only the two intended GREEN evidence files were modified before the evidence
  commit.

## Conclusion

All seven required scenarios and all five adversarial variations PASS against
one final post-fix candidate. Both focused defect probes PASS, and the
standalone fresh-session CLI discovery/CREATE/RESUME pilot PASSes. The RED
baseline remains unchanged.
