# RESUME reconciliation and bearing

RESUME is an evidence-first assessment of what an earlier handoff means now.
The handoff preserves useful context, but it is not current merely because it
parses, is recent, or confidently recommends an action. Reconstruct current
state from the authorities and probes available to the incoming session before
recommending where to start.

## Inputs and authority

Read `handoff-contract.md` before using this procedure. The contract defines
the artifact format, the project-owned storage location, claim forms, and
containment expectations.

The selected handoff is advisory context. It is not design authority, execution
authority, backlog authority, or an authorization gate. Current project
instructions, operator direction, the active issue, specification, plan, and
applicable Superpowers workflow guidance govern their own layers. The verdict
is advice and neither grants nor removes authorization to mutate Git, GitHub,
or the project.

## Candidate validation and selection

An explicitly supplied handoff path is the candidate to assess; it is not a
waiver of validation. Record that the selection reason was the explicit path,
then validate it under the first reconciliation probe. Require containment for
an explicitly supplied project-local candidate. An explicitly supplied external
candidate is eligible only when its contract-required external and ephemeral
status, exact location, and operator request are established from the artifact
together with its associated outgoing report and/or a current explicit operator
request. Preserve that external/ephemeral status visibly in `Selected handoff`
and `Current anchors`; verify provenance, repository identity, and accessibility
before relying on it. If its status, provenance, identity, or accessibility is
unestablished, keep that failure visible and normally return `VERIFY` rather
than substituting another file. External location alone is not a validation
failure.

Without an explicit path:

1. Derive the project-owned handoff location from `handoff-contract.md`; do
   not guess another root or search arbitrary repository files. Discover only
   candidate artifacts under that derived location; never discover an external
   or ephemeral candidate automatically.
2. For every candidate that can be inspected, compare its repository identity,
   branch, work item and consumed revision, specification identity, plan
   identity, and predecessor lineage with current evidence. Mark each anchor
   `VERIFIED`, `INFERRED`, or `UNVERIFIED` using the claim form from the
   contract.
3. Select a candidate only if the available repository, branch, work-item,
   plan, and lineage anchors establish one continuing thread and clearly
   exclude all other candidates. A missing, dangling, or unresolved lineage
   link is not evidence that a candidate is the current successor.
4. Treat creation time and recency as drift signals only. They can help explain
   a choice already supported by the anchors; they never make a candidate
   authoritative and must never select the newest file by themselves.

If zero candidates qualify, or two or more remain plausibly compatible, report
the candidate paths, matching and conflicting anchors, and unresolved lineage.
Ask the operator to choose the handoff path and, when needed, identify the
intended live thread or successor. Do not silently discard unsafe candidates or
choose the newest candidate. An ambiguous selection normally produces
`VERIFY`.

## Ordered reconciliation probes

Run these probes in this order. Do not use a later conclusion to bypass an
earlier unavailable or contradictory probe.

1. **Validate the artifact.** Check the format identifier, required sections,
   timestamps, repository identity, and every predecessor path that can be
   inspected. Require project-local path containment for a project-local
   candidate. For an explicitly supplied external/ephemeral candidate, verify
   external status, exact location, and operator request from the artifact
   together with its associated outgoing report and/or a current explicit
   operator request; then verify provenance, repository identity, and
   accessibility. Report malformed timestamps, missing sections, containment
   failures for project-local candidates, unestablished external status,
   provenance, identity, or accessibility, repository mismatch, and dangling
   predecessors as current evidence.
2. **Refresh guidance.** Re-read current project instructions and the
   applicable installed Backplane and Superpowers skills. A prior handoff's
   description of a rule or skill is historical context, not a replacement for
   the active source.
3. **Reconcile Git state.** Establish the repository root, branch, HEAD
   relationship, relevant commits, dirty state, and changed relevant files.
   Compare that observed state to every corresponding artifact anchor and live
   claim.
4. **Reconcile the work item when present.** Invoke
   `managing-superpowers-backlog` for complete native, read-only intake. Check
   lifecycle label, hierarchy, blockers, `updatedAt`, and linked pull-request
   delivery evidence. CREATE and RESUME do not mutate GitHub.
5. **Reconcile Superpowers artifacts.** Use the active skill-discovery
   surface to find and read the installed Superpowers skills. Derive design and
   plan conventions, including documented override behavior, from those skills
   before resolving the current specification and plan. Compare their current
   existence and Git identities with the handoff anchors. Do not guess an
   installation root or use an old default path merely because it is familiar.
6. **Reclassify claims.** Reclassify every load-bearing handoff claim as
   confirmed, drifted, or unverified. A current probe or authoritative source
   can confirm a claim; changed or contradictory current evidence makes it
   drifted; an unavailable, insufficient, or unresolved source leaves it
   unverified. A remembered result, digest, stale handoff, or elapsed time is
   not current proof.
7. **Test proposed next steps.** For every proposed step, check its stated and
   implied preconditions against current authority and observed evidence.
   Record whether each precondition is met, drifted, blocked, or unverified,
   and name the narrowest next probe or operator decision where one is needed.

Unavailable evidence remains `UNVERIFIED`. Unknown never means fresh.

## Bearing selection

Choose one bearing only after the ordered probes. Use these meanings verbatim:

- **CONTINUE** — the objective and next action remain supported by current
  authority and verified preconditions.
- **REVISE** — the objective remains live, but the plan or next action no longer
  fits current evidence.
- **ABANDON** — current operator or authoritative project state has rejected,
  superseded, or completed the handed-off objective. The agent does not invent
  abandonment authority.
- **VERIFY** — an unresolved contradiction or unknown load-bearing claim makes
  the correct starting action additional verification.

Use `VERIFY` for a malformed timestamp, missing required section, dangling
predecessor, repository mismatch, ambiguous candidate selection, or unavailable
load-bearing probe unless current authority supplies a stronger, evidenced
bearing. These conditions remain visible in the report; do not turn uncertainty
into a hard failure that suppresses the session-entry warning.

## Required incoming-session report

Report the assessment in exactly this order and preserve the vocabulary below.
Keep each item concise but evidence-backed; do not hide an unsafe candidate or
an unavailable probe behind a generic success statement.

```text
Selected handoff: <path and selection reason>
Current anchors: <repository, branch, HEAD, issue revision, spec, plan>
Confirmed claims: <claim plus current evidence>
Drifted claims: <old claim, current evidence, consequence>
Unverified claims: <claim plus required probe>
Next-step assessment: <preconditions and result>
Bearing: CONTINUE | REVISE | ABANDON | VERIFY
Start here because: <current-evidence explanation>
```

If no safe candidate was selected, say so in `Selected handoff`, list the
candidate evidence and the requested operator choice under `Unverified claims`,
and use `VERIFY` unless a different bearing is directly established by current
authority. The final sentence must state what current evidence makes the chosen
starting action appropriate; it must not repeat the handoff's recommendation as
its sole justification.
