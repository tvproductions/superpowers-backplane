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
complete native intake. CREATE and RESUME are read-only; mutation needs a
separate explicit backlog operation.

Use this skill at an interruption, model or harness switch, context-risk point,
or return to unfinished work. Continue normally when primary context is intact
and cheaper. An explicit CREATE or RESUME request wins; otherwise infer only an
unambiguous direction, or ask one short question.

For each needed Superpowers artifact, use active skill discovery; read installed
`superpowers:brainstorming`, `superpowers:writing-plans`, and applicable
execution guidance; then derive current conventions and overrides. If unavailable
or ambiguous, record `UNVERIFIED` and ask for evidence. Never guess a root or path.

## CREATE

1. Establish repository root and incoming purpose. Read current instructions and
   directly relevant durable authorities.
2. Read the complete [handoff contract](references/handoff-contract.md). Follow
   its storage, identity, claim, lineage, redaction, and refusal rules.
3. Keep only purpose-relevant live claims. Tag each load-bearing claim
   `VERIFIED`, `INFERRED`, or `UNVERIFIED`; reference durable material, do not copy it.
4. Heuristically screen secrets, credentials, personal data, and private URLs.
   Redact safely or refuse when meaning cannot survive redaction. Retain a
   supplied safe result exactly; when its text is absent, leave it
   `UNVERIFIED` and request it rather than inventing a finding or retry rule.
5. Compute the unique append-only destination; check immediately before writing;
   refuse collisions and unsupported required authority anchors. When required
   anchors or safe redaction inputs are unavailable, do not persist or represent
   a partial artifact as a completed durable handoff. Any handoff-shaped output
   in that state must prominently say `NON-DURABLE DRAFT — not persisted` and
   must not imply a durable artifact or usable RESUME target. A safe summary is
   permitted when useful, names the missing probes, and exposes no sensitive
   value.
6. Write once, then re-read for required fields, attribution, reference-not-copy,
   and the exact resume instruction. Report the path and intentional unknowns.

## RESUME

1. Establish repository root and incoming purpose. Read the complete
   [handoff contract](references/handoff-contract.md) and
   [resume assessment](references/resume-assessment.md).
2. Validate an explicit path, or use the assessment's fail-closed candidate
   selection. Never choose by recency alone.
3. Run its ordered current-evidence probes. Reconcile Git, work item, durable
   artifacts, claims, and next-step preconditions; confidence and recency are not currency.
4. Emit its exact assessment shape, one bearing, and evidence-backed `Start here because`.
5. Re-enter the applicable Superpowers stage only after explaining why current
   evidence supports that start. The bearing is advice, not authorization.

## Red flags

| Pressure or shortcut | Required response |
| --- | --- |
| "Pick the newest" | Select only with unambiguous current anchors **and verified lineage**; a lone nonconflicting candidate with unresolved lineage still requires the operator's path and intended thread. |
| "The predecessor was confident" | Reconcile claims against current probes; leave gaps `UNVERIFIED`. |
| "Copy the plan" | Reference durable authority; preserve only the live thread. |
| "We know what happened" | Use an attributed claim form and name evidence or probe. |
| "Skip checks" | Produce the required current-evidence assessment before selecting a start. |
| "Record everything" | Redact safely while retaining the non-secret result, or refuse. |
| "Update GitHub" | Keep handoff work read-only; request a separate backlog operation. |
