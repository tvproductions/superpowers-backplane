# Issue31 integrated verification and bounded review corrections

## Identities and current result

Verification began on clean integrated `main` at
`a1eb10bbc174cfe7b0a80aed9411ef06fab3fcee`, matching live remote `main`.
PR33 is MERGED at `1cbe39323da7480e9d41657b757088a774972eac`.
Full native intake observes issue31 OPEN/Feature with exactly `backplane:review`,
revision `2026-10-13T07:27:56Z`, and empty parent/children/dependency/closing-PR
relationships. Current scope and acceptance match the approved authorities.

The operator requested integrated verification and R1 reconciliation, then
explicitly selected fixing the four confirmed PR33 findings. The corrections
are locally committed on `fix/issue-31-integrated-review` at
`24a073438ffcb6832219ae4f4083eb5b17604573`. This report's later storage commit
does not replace that source identity. The correction branch is not yet
integrated or published; issue31 remains open. No tracker mutation or release
was performed.

Latest scoped freshness application passes **8/8**, including explicit
stable-channel policy, and the focused correction application passes **5/5**.
The fresh full candidate run supplies **56/56 governance**, **23/23 existing
behavioral expectations**, and **6/6 representation assertions**. The latest
native fixture replay passes **38/38**. Retained results have the source
identities and semantic reconciliation described below; they are not falsely
presented as fresh executions against every final byte.

## Fixed inputs and captured method

The [run manifest](2026-10-14-issue-31-integrated-runs.json) preserves all **30
complete responses**, actual prompts and hashes, response paths/hashes, each
observed source bundle, per-assertion grades, process exits, completed commands,
and transient transport errors. No model override was supplied; the effective
model was not exposed. Codex CLI was `0.162.1`; sessions were ephemeral/read-only
with hooks and agent dispatch disabled per invocation. Global configuration and
installations were unchanged.

One installation response contains indentation-only blank lines rejected by
the Git whitespace gate. Its Markdown view normalizes only those blank lines;
the manifest preserves the exact original text and captured hash in
`response_verbatim`/`captured_response_sha256`, separately from the view hash.
No captured content or score was discarded to pass formatting.

The original `governance-probes/v1`, `governance-freshness/v1`, existing
conformance fixtures/rubrics, and checkpoint representation fixtures remain
unchanged. The designated source locator was relocated from the removed d181
workspace to the standalone root. Candidate/final sessions additionally restrict
reads to source, required instructions, and governing authorities, excluding
tests, transcripts, other sessions, review comments and ignored work. That
harness boundary is recorded separately from the unchanged fixture data.

The [focused contract](2026-10-14-review-consistency-contract.md) adds
`issue31-review-consistency/v1`; it does not rewrite earlier comparisons. Its
baseline correctly identified source gaps: mixed-kind rechecks were rejected
by the written rule, generic mutation guards existed but the numbered pre-close
checkpoint was missing, and two explanations contradicted their observations.
Those source-application scores are **1 PASS / 3 FAIL / 1 UNKNOWN**, not a claim
that the diagnosing agent acted unsafely.

One original-source representation response is excluded from acceptance scoring:
its broad `rg` read included historical test responses/manifests. The full
response and command observations remain preserved with six UNKNOWN grades.
The strict source-only candidate replay passes all six assertions independently.
Completed sessions exit zero; exit codes alone are not grades. The manifest
contains 453 completed read commands; neither probe arm performed live queries,
mutations, helper calls or agent dispatch.

## R1 reconciliation

R1 requires both Backplane ownership of direct SP alignment and a stable default.
The earlier October13 UNKNOWN responses remain unchanged. The initial October14
integrated response explicitly supplies both clauses and passes 8/8, but the
full correction-candidate response again omits the default and retains R1 UNKNOWN.

That repeat demonstrates an output omission despite an existing correct policy.
The bounded correction gives the existing freshness route three required
assessment fields: ownership/channel policy, evaluation, and publication/next
action. The latest response explicitly states compatible stable by default,
keeps edge selection explicit, and passes all eight original assertions. No
policy, updater, runtime, automatic installation, bundle authority, or new
compatibility promise was added. These samples establish their observed scoped
outcomes, not a model-wide consistency guarantee.

## PR33 source corrections and review

- Recheck record identity is explicitly `(kind, id)`: distinct observations of
  the same tracker ID are allowed; an identical pair is rejected. Other
  collections with an `id` field use that field; exact schemas remain unchanged.
- Closeout step4 re-fetches the full issue/native graph after body/pointer edits
  immediately before closure, reconciles revision/evidence applicability, and
  stops the write when acceptance/delivery changes require approved revalidation.
  This does not invent an atomic GitHub compare-and-swap operation.
- Partial E1 explains its unavailable final revision. The related partial graph
  no longer claims full enumeration despite omitted page2: its final observation
  is unavailable and explicitly limited.
- The stale issue explanation records revision drift and required reconciliation
  without claiming unchanged body/relationships or inventing a semantic delta.

The [fresh source review](2026-10-14-issue-31-corrections-review.md) initially
identified one Minor qualification, which was corrected. The final six-file
review reports no Critical, Important or Minor findings. It independently accepts
the bounded evidence reconciliation below, with source-inspection proof limits.
Review does not substitute for the captured verification or authorize integration.

## Evidence freshness and semantic reconciliation

The full candidate run has 97 PASS / 1 UNKNOWN across 98 assertions: freshness
R1 is the sole UNKNOWN. After that run, only conditional freshness output fields
and qualification of the existing exact-schema identity sentence changed.
Non-freshness requirements, fixtures, methods and applicable semantics are
unchanged. The independent reviewer confirmed this bounded reconciliation.

Retain the **85 passing non-freshness statements** at their original tested
hashes. Replace neither those records nor the intermediate freshness UNKNOWN.
Fresh final executions establish **8 freshness + 5 focused assertions** at the
final source bundle. Together these support the current 98 scoped expectations
through explicit reconciliation; they do not constitute 98 new final-byte
executions. Final source hashes match the source commit above.

The [native replay record](2026-10-14-issue-31-native-replay.json) preserves the
driver source and all 38 typed/semantic fixture outcomes, using the existing
recorded validator and native macOS JavaScript. It adds no required runtime or
production helper. The existing validator's Project-paging/unavailable-body
coverage limits still apply. An initial driver attempt used raw pre-field edge
fixtures and rejected two positives; switching to the already retained candidate
projections corrected that harness error without changing fixtures, expectations
or shipped source. Initial JXA read/evaluation errors were harness failures, not
product RED evidence.

The historical K0/K1 file/Git exercise is retained at its original identities.
Both commits are reachable from integrated main; K1's parent, pair-only diff and
both fixture blobs match the integrated tree. This is a fresh identity check,
not a new interrupted-recovery exercise or production checkpoint acceptance.

## Preservation, upstream, and limitations

Both skill frontmatters and ten direct references pass current structural checks;
current example JSON parses and `git diff --check` passes. Approved spec/plan and
both frozen governance contracts retain their bytes. All 238 upstream file hashes
match the starting manifest, upstream is clean, and both reserved `.superpowers/`
paths remain absent. No unrelated host-leaf work was changed.

Current upstream installation documentation was read through `gh`; active
repository discovery and fresh source invocation were observed. Latest published
stable is v7.0.0, published `2026-10-10T00:28:58Z`, resolving authoritatively to
`bb92a77741419a4ab5f06e711a283343f1ada0c3`, matching the independent checkout.
This is dated evidence for the recorded Codex/read-only probe and native fixture
scope. It does not verify the entire bundle, other harnesses, all upstream
workflow helpers, or live Project/full-graph capture and production recovery.
Windows predecessor completion remains unknown.

Next: choose the follow-up branch's integration disposition, then verify the
actual accepted integration target and assess issue31 satisfaction before any
completed closure. Local source/evidence commits, remote branch arrival, main
integration, issue closure and release remain distinct.
