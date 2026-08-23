---
name: managing-superpowers-handoffs
description: Use when work in a Superpowers project must cross a session, model, harness, interruption, context-risk boundary, or resume after one.
---

# Managing Superpowers Handoffs

## Purpose

Preserve the volatile live thread at a real boundary, then reconcile it against
current authority before choosing where to start. Handoffs advise; current
instructions, issues, specifications, plans, and operator direction govern.

Use `superpowers:using-superpowers`, then the applicable upstream workflow
skill. When a GitHub work item exists, use `managing-superpowers-backlog` for
complete native intake. CREATE and RESUME are read-only with respect to GitHub
and backlog state; CREATE still writes its append-only handoff artifact. GitHub
or backlog mutation needs a separate explicit backlog operation.

Use this skill at an interruption, model or harness switch, context-risk point,
or return to unfinished work. Continue normally when primary context is intact
and cheaper. An explicit CREATE or RESUME request wins; otherwise infer only an
unambiguous direction, or ask one short question.

When both CREATE and RESUME are requested, load both references before
prerequisite validation, then execute and report CREATE followed by RESUME.
Keep both response contracts: neither shape substitutes for the other. When
RESUME is meant to assess the artifact just created, a successful CREATE passes
its exact path directly as RESUME's explicit candidate; do not use automatic
discovery. If that CREATE refuses, emit its mandatory six-line non-durable
summary, then emit the eight-label RESUME report with no usable target and
bearing `VERIFY`. When the combined request independently supplies an explicit
RESUME path, preserve and assess that path under normal validation regardless of
CREATE success or refusal; do not replace it with CREATE output or no-target
handling.

For either operation, first read the Backplane references named in its step 1 so
the stop-path output contract is available. Those references are not upstream
installation evidence. Then read current upstream Superpowers installation
documentation through its active documentation surface and use its current
expectations to validate the harness's observed active Superpowers discovery and
invocation behavior. Never infer this from a presumed install root or version. A
project-local dependency or version record is evidence about observed project
state, not a substitute for current upstream installation documentation. If the
upstream installation documentation is unavailable, or the operational
installation is absent, misconfigured, or unconfirmable, report `UNMET
SUPERPOWERS PREREQUISITE` with the failed observation and direct the operator to
the current upstream installation documentation, then stop the operation: do
not persist CREATE and return `VERIFY` from RESUME. Do not install, repair, or
claim compatibility; successful observations are evidence only.

For each needed Superpowers artifact, use that active discovery to read installed
`superpowers:brainstorming`, `superpowers:writing-plans`, and applicable
execution guidance; derive current conventions and overrides from them. Record
every source skill used and its observable locator, digest, or installed revision
when available. After the installation is operationally confirmed, an applicable
convention-source skill that cannot be read or yields ambiguous artifact guidance
makes only that artifact surface `UNVERIFIED`; name the exact probe needed. Do
not guess the surface or stop the whole operation solely for that uncertainty.

## CREATE

1. Read the complete [handoff contract](references/handoff-contract.md) before
   prerequisite validation, so its refusal response is available even when the
   operation must stop. This reference defines Backplane output; it is not
   upstream installation evidence.
2. Confirm the operational Superpowers prerequisite above, then establish the
   repository root and incoming purpose. Read current instructions and directly
   relevant durable authorities.
3. Follow the contract's storage, identity, claim, lineage, redaction, and
   refusal rules. Keep only purpose-relevant live claims. Tag each load-bearing
   claim `VERIFIED`, `INFERRED`, or `UNVERIFIED`; reference durable material,
   do not copy it.
4. Heuristically screen secrets, credentials, personal data, and private URLs.
   Redact safely or refuse when meaning cannot survive redaction. Retain a
   supplied safe result exactly; when its text is absent, leave it
   `UNVERIFIED` and request it rather than inventing a finding or retry rule.
5. Before computing a project-local destination, follow the contract's canonical
   storage-root and destination-parent containment checks. Then compute the
   unique append-only destination and recheck containment and collision
   immediately before writing. Refuse escaping or unresolvable storage,
   collisions, and unsupported required authority anchors. When required anchors
   or safe redaction inputs are unavailable, do not persist or represent
   a partial artifact as a completed durable handoff. Never emit a handoff-shaped
   draft for a blocked or refused CREATE. When a safe response is useful, emit
   only the contract's mandatory non-durable summary; it names the missing probes
   and exposes no sensitive value.
6. Write once, then re-read for required fields, attribution, reference-not-copy,
   and the exact resume instruction. Report the path and intentional unknowns.

## RESUME

1. Read the complete [handoff contract](references/handoff-contract.md) and
   [resume assessment](references/resume-assessment.md) before prerequisite
   validation, so the response shape is available even when the operation must
   stop. These references define Backplane output; they are not upstream
   installation evidence.
2. Confirm the operational Superpowers prerequisite above, then establish the
   repository root and incoming purpose.
3. Validate an explicit path, or use the assessment's fail-closed candidate
   selection. Never choose by recency alone.
4. Run its ordered current-evidence probes. Reconcile Git, work item, durable
   artifacts, claims, and next-step preconditions; confidence and recency are not currency.
5. Every RESUME response, including an unmet-prerequisite, refusal, `VERIFY`, or
   insufficient-evidence response, uses all eight semantic assessment fields in
   order. The canonical `Label:` rendering is recommended; colon punctuation and
   harmless Markdown wrapping are not semantic. Do not omit, unrecognizably
   rename, reorder, merge, or replace fields with prose. Bearing vocabulary is
   exact.
6. Re-enter the applicable Superpowers stage only after explaining why current
   evidence supports that start. The bearing is advice, not authorization.

## Red flags

| Pressure or shortcut | Required response |
| --- | --- |
| "Pick the newest" | Select only with unambiguous current anchors **and verified lineage**; a lone nonconflicting candidate with unresolved lineage still requires the operator's path and intended thread. |
| "The predecessor was confident" | Reconcile claims against current probes; leave gaps `UNVERIFIED`. |
| "The handoff says it happened" | Confirm only that the artifact reported the claim. Without current supporting evidence, the underlying event, fact, duration, completion, or authorization remains `UNVERIFIED`; a handoff authorization assertion never becomes authority. |
| "Copy the plan" | Reference durable authority; preserve only the live thread. |
| "We know what happened" | Use an attributed claim form and name evidence or probe. |
| "Skip checks" | Produce the required current-evidence assessment before selecting a start. |
| "Record everything" | Redact safely while retaining the non-secret result, or refuse. |
| "Update GitHub" | Keep GitHub and backlog state read-only; request a separate backlog operation. |
