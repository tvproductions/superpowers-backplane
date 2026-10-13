# GitHub governance bridge behavioral evidence

Issue: https://github.com/tvproductions/superpowers-backplane/issues/31,
consumed revision `2026-10-12T01:29:48Z`. Native inline execution in the recorded
Mac worktree. Baseline starts from `33068051537dccfaeb6a6dbb82f5b293e9489203`.

## Fixed inputs and test method

The original seven-case contract is
`docs/superpowers-backplane/plans/2026-10-11-governance-probe-contract.md`,
`governance-probes/v1`, SHA-256
`fc23cbae20160535f0836eff9920649c0dc78fe50b17ac3082904f2b38710f81`.
The separately added freshness contract is
`docs/superpowers-backplane/plans/2026-10-12-governance-freshness-probe-contract.md`,
`governance-freshness/v1`, SHA-256
`20349682b83f272925c245eb38a25530ced755ab70e94f8d08d83b0ba3592508`.
Neither contract is edited after its first baseline.

Each original common instruction block, fixture-record convention, and case
prompt is submitted unchanged. A common locator line designates the native
worktree's backlog SKILL.md in both arms. Each case uses its own fresh ephemeral
read-only Codex CLI 0.162.1 session, no model override, and process-only
`features.hooks=false`, `features.multi_agent=false`. The effective model ID is
not exposed by the captured CLI events; results are scoped to this harness
configuration. No real GitHub queries/mutations or agent dispatch are allowed
inside a probe. Full final responses are retained; command events are inspected
for unauthorized operations. A zero exit is not a rubric pass.

Baseline bundle hashes: SKILL `739a16fcdf2ee5adab0514f5a44db0629dcce558985fe5a31d71dd2606ac1e81`;
issue contract `d6dd8b8c2d1ea5836848fdac90aecf7002ab865dae612e94a560ebe7800d3121`;
binding `703435e24308513482da2ca7148de383b14305e3063abff08372b0e36ef7e6d6`;
installation `50d82ccacbf71d368e983984157abe91d1fafd977f1f4d654c0fd58b5393329d`.
Upstream is stable v7.0.0 at `bb92a77741419a4ab5f06e711a283343f1ada0c3`.
Probe-run metadata records exact prompt/response digests and later candidate
bundle identities. Verdicts below are manual evaluations of every numbered
original rubric statement and every supplied variant.

## Criterion and case map

| Case | Variants included | Design criteria |
| --- | --- | --- |
| 1 decomposition-adequacy | A–E | D1, D2, D5 |
| 2 coverage-revision | Changed C and independent editorial S2e/B | D1, D3, D6 |
| 3 design-authority-paths | Bounded issue, cross-cutting spec, broader product result | D1, D5 |
| 4 project-reconciliation | Integrated, denied capture, explicit Issues-only, absent custom types | D2, D3, D4 |
| 5 pr-contributions | A–F | D3, D6 |
| 6 checkpoint-preservation | A–I, including all B/D alternatives | D7, D8 |
| 7 namespace-boundary | Helper chain, proposed isolation, native override, resume | D5, D8 |
| Freshness | SP7/BP2 local scope, historical pin, bundle/adopter claims | Approved freshness clarification, D5/D8 |

## Baseline rubric scores

P = PASS; F = FAIL; U = UNKNOWN because required evidence is missing.
Order matches the numbered rubric in the immutable source. Baseline U/F are
coverage gaps to resolve, not passing candidate evidence. Existing P stays P;
no test is rewritten to manufacture RED.

| Case | Rubric scores | Response |
| --- | --- | --- |
| 1 | P P P P P P P | [capture](transcripts/2026-10-11-governance-baseline-case-1.md) |
| 2 | P P P P U P P | [capture](transcripts/2026-10-11-governance-baseline-case-2.md) |
| 3 | P P P P P P | [capture](transcripts/2026-10-11-governance-baseline-case-3.md) |
| 4 | P P P P P P P | [capture](transcripts/2026-10-11-governance-baseline-case-4.md) |
| 5 | P P P P P P P F U | [capture](transcripts/2026-10-11-governance-baseline-case-5.md) |
| 6 | F P P U P P P P P F P | [capture](transcripts/2026-10-11-governance-baseline-case-6.md) |
| 7 | P P P P P P U P P | [capture](transcripts/2026-10-11-governance-baseline-case-7.md) |
| Freshness | P P P P P P U P | [capture](transcripts/2026-10-12-governance-freshness-baseline.md) |

Specific missing/failed evidence:

- Case 2/R5 permits durable issue records as evaluations without establishing
  immutable accepted evidence distinct from the current issue-owned index.
- Case 5/R8 describes execution handoff bookkeeping instead of distinguishing
  verified feature identity from later product checkpoint/evidence storage.
  R9 supplies no pending-review workspace-cleanup disposition.
- Case 6/R1 uses publication/acceptance without the separately verified remote
  integration gate. R4 proposes restoration but does not bind exact K0 pair
  blobs/index entries and applicable recovery authority. R10 omits distinct
  verified-source and checkpoint storage identities.
- Case 7/R7 describes general handoff reconciliation without explicitly rejecting
  another plan/stale task inputs and selecting the first unsupported task.
- Freshness/R7 requires durable accessible publication identity but does not
  explicitly verify transport/arrival before consumption of the published cue.

## Candidate and regression results

Final candidate behavioral and existing conformance results are below.
Native JSON/file/Git exercises and whole-change review are recorded separately
from the simulated decisions above. Existing five-check conformance remains
required against the final candidate hashes. Missing mandatory captures or
unscored expectations prevent a completion claim.

### Task 2 candidate

Fresh cases 1–4 pass all 27 original rubric statements with every declared
variant. Case 2 now explicitly separates the mutable issue-owned mapping/index
from accepted immutable evaluation evidence, resolving baseline R5's UNKNOWN.
Existing passing decomposition/design/Project behavior remains passing. Capture
paths and exact phase bundle/prompt/response hashes are in the run manifest.
The forward PR/checkpoint routes are explicitly unavailable until Tasks 3/4;
these results establish only the Task 2 assessed operations, not those routes.

### Task 3 candidate

Fresh cases 5 and 2 pass all 16 original rubric statements. All PR A–F states
remain distinct, including actual auto-closure with failed verification and a
nondefault target with no observed closure. The response preserves the pending
review workspace and explicitly separates verified S1/B from later storage K,
resolving baseline Case5/R8 FAIL and R9 UNKNOWN. Coverage-revision behavior
remains passing. Required native PR CLI fields were also verified through a
read-only observation of existing PR #32, outside the invented probes.

### Task 4 candidate and native exercises

Fresh cases 6/7 pass 20/20 original rubric statements. They distinguish verified
source from storage, local acceptance from integration, exact pair/index recovery
under authority, first unsupported-task resume, and all failure variants. Captured
events show completed turns; process exit was not recovered across the context
boundary, so no invented exit code is used.

[Concrete JSON validation](2026-10-13-checkpoint-validation.json) records 18/18
expected outcomes with native JSON/JavaScript capabilities: complete and partial/
stale diagnostic records, missing pages, changed revisions, unavailable evidence,
wrong delivery/review, dangling references, and contradictory Project projection.
The disposable test validator initially keyed rechecks by id alone; corrected
(kind,id) uniqueness admits distinct issue/delivery observations of one identity.
No mandatory JSON language or production validator/helper is shipped.

[Actual file/Git exercise](2026-10-13-checkpoint-file-git-exercise.md),
[output](2026-10-13-checkpoint-file-git-results.txt), and
[external receipt](2026-10-13-checkpoint-fixture-receipt.json) record 12/12 checks:
ID/digest/semantic rejection, interrupted JSON-only installation, exact prior
pair/index recovery preserving an unrelated staged sentinel, blocked acceptance
with unrelated staged state, user-edit stop, no-prior filesystem/owned-index
absence, and an actual pair-only K1 parent/blob/tree acceptance and receipt
finalization. K0 is b32f6473161ff199234a4011bad4ac6b5c13e1dc; K1 is
32d9284af6c3188981c2883b91a9bc8400331f16. These pair commits contain invented
tests/scenarios/fixtures/issue-31-checkpoint/ data, not actual product state.
The readable fixture renderer covers its one-issue account; it is not a general
renderer or proof of live full-graph/Project capture. No remote publication,
new-host arrival, production recovery, or GitHub replay was performed.

### Final candidate verification (2026-10-13)

All original seven cases pass 56/56 statements, and the separate freshness
contract passes 8/8. All variants retain their unchanged fixture/rubric inputs.
Candidate1 passed the original 56 but left freshness R7 UNKNOWN: the response
required availability without explicit transport/arrival. It is retained with
its exact source hashes. Investigation found the explicit arrival rule scoped
to execution handoff, while freshness required only publication/availability.
One canonical freshness paragraph now binds consumer-visible transport, exact
reachable identities, and inspectable evidence to cue consumption. Fresh full
sessions at the corrected common bundle resolve R7; no prompt/rubric was edited.
Case1 experienced a transient CLI 503 reconnect, then completed with a full
response and zero exit. All final probe exits are zero; those exits alone were
not treated as rubric success.

[Existing conformance manifest](2026-10-13-governance-regression-runs.json)
records five named checks: parsed frontmatter/exact names/Use when descriptions,
all direct links and placeholder inspection on both skills, then four fresh
behavioral sessions scoring all 23 original acceptance expectations. They all
PASS. Candidate1 and final responses are retained; the final four were run after
the corrected seven-case suite. Available Ruby/Psych, Perl and native JSON tools
were authoring verification capabilities, not project runtime dependencies.
The handoff skill and installation reference remain byte-identical to their
implementation-entry identities.

The final doctrine hash is
176ef7f079762e3cde482952ba37315d2e1693f94d03f2090764e628aa461827;
all routed reference/example/skill hashes are recorded per final run. Source
hashes were checked after sessions; no skill/reference changes occurred during
probes. Captured executed-command events contain only permitted reads; no live
queries, mutations, helper invocations or agent dispatch occurred in probes.

[Native query validation](2026-10-13-governance-native-query-validation.json)
separately confirms current gh GraphQL subIssues/blockedBy/blocking/native closing
PR connections and terminal zero-member pages for real #31. Complete native
intake observes #31 still OPEN/Feature, only backplane:active, no relationships
or closing PRs, unchanged updatedAt 2026-10-12T01:29:48Z. This is CLI capability
validation, not a full repository/Project capture or authorized tracker write.

Root and upstream preservation manifests still pass; both .superpowers paths
remain absent, upstream is clean at the recorded revision, scratch is ignored,
and the actual product checkpoint paths remain trackable. Unrelated issue #19,
root dependency/handoff records and the unrelated worktree were not transported
into implementation commits or modified. The earlier Mac prerequisites are in
separate, explicitly authorized setup commits.

Independent whole-change review and final finishing disposition are recorded in
the portable execution checkpoint and review evidence. Local evidence does not
prove remote integration/arrival, integrated issue satisfaction, other harnesses,
bundle acceptance, live full-graph/Project capture, or release.
