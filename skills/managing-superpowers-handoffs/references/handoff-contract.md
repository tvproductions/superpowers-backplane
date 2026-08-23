# Handoff Artifact Contract

## Format and storage

Every durable artifact conforming to this contract identifies itself as `superpowers-backplane-handoff/v1`.

Unless an operator explicitly requests an ephemeral external location, CREATE writes the artifact to:

```text
docs/superpowers/handoffs/<UTC-basic-timestamp>-<safe-kebab-slug>.md
```

Use a UTC basic timestamp in the form `YYYYMMDDTHHMMSSZ`. Derive the slug from the incoming purpose, using lowercase letters, digits, and single hyphens; remove or replace unsafe characters. The name is append-only: check that the complete destination does not exist immediately before writing, and refuse to write on a collision. Never overwrite an existing handoff and never maintain a mutable `latest` pointer.

Project-local storage is the default because it can move across sessions, models, and machines when the project chooses to commit or otherwise transport the file. CREATE does not commit, push, archive, copy, or otherwise transport the artifact automatically.

An external location is permitted only after an explicit operator request for that location. Record that it is external and ephemeral, its exact location, and the operator's request in the artifact or outgoing report as applicable. Do not imply that an external artifact is project-local, durable, committed, or available to a future session. If the external location cannot safely preserve the required content, refuse CREATE and ask for a safe location.

## Document shape

Use Markdown. Start with an identity block that supplies the following fields. An unknown value is not invented: record it as `UNVERIFIED` with its required probe, or omit the optional creator identity.

| Field | Requirement |
| --- | --- |
| Format | Exactly `superpowers-backplane-handoff/v1`. |
| Creation time | UTC timestamp recorded at creation. |
| Repository identity | Observable repository identity, sufficient to detect a later mismatch. |
| Branch | Observed branch or explicit detached/unverified state. |
| HEAD | Observed Git HEAD identity or explicit unverified state. |
| Incoming purpose | The purpose the incoming session is expected to pursue. |
| Work item | URL and observed `updatedAt` when work is backlog-tracked; otherwise state that no work item was identified. |
| Specification | Path and observed Git identity when a specification is present; otherwise state its absence or uncertainty. |
| Plan | Path and observed Git identity when a plan is present; otherwise state its absence or uncertainty. |
| Superpowers derivation provenance | Every installed Superpowers skill used to derive artifact conventions, with its observable locator and digest or installed revision when available. |
| Predecessors | Zero or more predecessor handoff paths; preserve every known path without fabricating a successor. |
| Creator | Identity only when known; do not invent a session identifier. |
| Storage location | The project-local destination or explicitly requested external location. |

For every specification and plan identity, use the tracked blob object ID when the artifact is tracked in Git. If it is untracked, say that explicitly and record a content digest only as evidence of the observed contents. A digest is never proof of commit identity. Apply the same distinction to any other artifact whose Git identity is claimed.

## Claim attribution

Every load-bearing statement uses exactly one of these forms:

```text
VERIFIED — <claim>. Evidence: <source>
INFERRED — <claim>. Evidence and reasoning: <sources and inference>
UNVERIFIED — <claim>. Required probe: <check>
```

Treat a command and its observed output, a current authoritative document, or an inspected Git/GitHub result as evidence only when it actually supports the claim. Do not upgrade a remembered result, a stale handoff statement, a content digest, or elapsed time into verified current state.

## Required CREATE sections

After the identity block, write these headings in this exact order. Keep each section limited to the incoming purpose and use the claim forms above for its load-bearing content.

1. `## Incoming purpose`
2. `## Authority anchors`
3. `## Verified current state`
4. `## Live implementation thread`
5. `## Corrections to durable artifacts`
6. `## Decisions and provenance`
7. `## Negative results`
8. `## Deferred obligations`
9. `## Risks and unknowns`
10. `## Proposed next steps`
11. `## Suggested skills`
12. `## Resume instruction`

Use this skeleton; fill every identity field with the applicable claim form and
do not insert a CREATE section between the required headings:

```markdown
# Session handoff

- Format: `superpowers-backplane-handoff/v1`
- Creation time: VERIFIED — <UTC timestamp>. Evidence: <creation observation>
- Repository identity: VERIFIED — <identity>. Evidence: <source>
- Branch: VERIFIED — <branch or detached state>. Evidence: <source>
- HEAD: VERIFIED — <commit or unresolved state>. Evidence: <source>
- Incoming purpose: VERIFIED — <expected incoming-session outcome>. Evidence: <source>
- Work item: VERIFIED — <URL and observed updatedAt>, or UNVERIFIED — <no work item identified>. Required probe: <check>
- Specification: VERIFIED — <path and blob ID>, or UNVERIFIED — <absence or unresolved identity>. Required probe: <check>
- Plan: VERIFIED — <path and blob ID>, or UNVERIFIED — <absence or unresolved identity>. Required probe: <check>
- Superpowers derivation provenance: VERIFIED — <each source skill, locator, and observed digest or revision when available>. Evidence: <active-discovery observation>
- Predecessors: VERIFIED — <zero or more explicit paths, including none>. Evidence: <source>
- Creator (omit when unknown): VERIFIED — <known identity>. Evidence: <source>
- Storage location: VERIFIED — <destination>. Evidence: <source>

## Incoming purpose

## Authority anchors

## Verified current state

## Live implementation thread

## Corrections to durable artifacts

## Decisions and provenance

## Negative results

## Deferred obligations

## Risks and unknowns

## Proposed next steps

## Suggested skills

## Resume instruction
```

### Section requirements

**Incoming purpose** states the expected incoming-session outcome, not a generic instruction to continue.

**Authority anchors** references the issue, specification, plan, repository, branch, and revisions that govern the work. A handoff is advisory context: it does not become design, execution, backlog, or authorization authority.

**Verified current state** records commands actually run and their observed results, including worktree and verification state. Preserve an observed verification failure as the command, relevant environment, failure result, and the next probe; never claim an unobserved replacement command succeeded.

**Live implementation thread** contains only volatile, purpose-relevant context that would be expensive or impossible to reconstruct: observations, unfinished reasoning, and the exact reason a next action remains plausible.

**Corrections to durable artifacts** records evidence-supported corrections to a plan, specification, assumption, or precondition. Name the artifact and the specific correction; do not silently rewrite its authority in the handoff.

**Decisions and provenance** separates an operator ruling from an agent choice. For each decision, identify the source, evidence, and whether it remains only a recommendation.

For every Superpowers convention used to locate or identify an artifact, record
the exact installed source skill and its observable locator. Include a digest or
installed revision when the harness makes one observable; otherwise say it is
unavailable. This provenance is evidence of the observed source, not a
compatibility guarantee.

**Negative results** preserves each attempted approach, concrete observed failure, and the condition under which it should not be retried without new evidence. Do not replace this with a vague statement that an approach failed.

**Deferred obligations** preserves discovered work that must survive the handoff but is not silently added to the current scope. Reference the proper authority or ask the operator to create or amend one; do not mutate backlog state.

**Risks and unknowns** marks every load-bearing gap as `UNVERIFIED` and gives the exact probe needed to resolve it, including branch-specific risks.

**Proposed next steps** lists ordered actions. Each action names its preconditions and verification seam; a next step is advice, not permission to mutate Git, GitHub, or project state.

**Suggested skills** lists the exact applicable upstream Superpowers and Backplane skill names. It does not assert a skill is installed unless observed.

**Resume instruction** gives the exact artifact path and directs the incoming session to invoke RESUME against that path before selecting a next action.

## Mandatory non-durable safe summary

When CREATE refuses persistence but a safe summary is useful, the response is
not a handoff-shaped draft. It uses these labels in this order:

```text
NON-DURABLE SUMMARY: not persisted; no usable RESUME target
Incoming purpose: <purpose in claim form, or UNVERIFIED with required probe>
Intended destination rule: <project-local default or explicitly requested external/ephemeral location>; establish eligibility and derive or verify the destination only after prerequisites; append-only and collision checked immediately before writing; no path invented here
Attribution state: <load-bearing claims in VERIFIED, INFERRED, or UNVERIFIED form, with evidence or required probes>
Missing probes: <every probe required before durable CREATE>
CREATE result: no handoff created
```

Every safe summary includes all six lines. Do not add the format identifier,
identity block, required CREATE headings, or resume instruction: those would
make the response masquerade as a full handoff.

## Reference-not-copy discipline

Reference durable material rather than reproducing it. Omit issue objective, acceptance criteria, settled specification, plan task list, commit content, and diff content when a stable path, URL, or Git identity lets the incoming session reconstruct them cheaply. Preserve only the live thread relevant to the incoming purpose, including observed failures, corrections, rejected approaches, deferred obligations, and uncertainty. A request to copy the plan does not change this rule.

## Lineage and locations

Record every known predecessor as a path, preserving the order needed to understand the live thread. A missing, dangling, or uninspectable predecessor remains visible as `UNVERIFIED`; do not invent a link, delete the reference, or declare the newest file authoritative. CREATE does not select a predecessor automatically merely because it is recent.

Paths in a project-local artifact must be explicit and suitable for later
containment checks. Before treating a candidate or predecessor as project-local,
canonically resolve its path and the repository root, including link, junction,
and traversal effects, then compare the resolved locations. Textual containment
is not sufficient. Preserve the supplied path and the observed resolution. A
path that escapes the canonical repository root, cannot be resolved, or has an
unresolved link, junction, or traversal-sensitive component remains visible as
`UNVERIFIED`; on RESUME it normally produces `VERIFY`. A path outside the
repository or an external handoff is never treated as project-local evidence
solely because its text appears in the artifact.

## Sensitive-content screen and redaction

Before persistence, screen the proposed artifact for common secret, credential, personally identifying information, and private-URL patterns. This screen is heuristic, not exhaustive secret detection. At minimum consider tokens and API keys, passwords, embedded credentials, private incident or service URLs, email addresses, and other direct personal identifiers.

Redact sensitive values while retaining the useful non-sensitive conclusion. For example, preserve a negative test result with its command and observed result while replacing a credential-bearing URL or token with a clear redaction marker. Record the redaction decision and the evidence supporting the retained claim without reproducing the sensitive value.

Refuse CREATE when safe redaction cannot be established without destroying the handoff's meaning. Ask the operator for a safe way to preserve the necessary context. Never claim that the screen proves the artifact contains no secrets.

## CREATE refusal conditions

Refuse to write when any of these conditions applies:

- The destination already exists.
- Repository identity cannot be established.
- A required authority anchor is claimed but cannot be identified.
- Sensitive content cannot be safely redacted.
- The artifact would label unverified belief as verified fact.

Report the specific failed condition and the narrowest required probe or
operator decision. A blocked or refused CREATE never emits a handoff-shaped
draft. If a safe summary is useful, emit only the mandatory non-durable safe
summary above. Do not create a partial durable handoff that conceals the failure.
