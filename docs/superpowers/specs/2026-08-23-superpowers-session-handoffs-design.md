# Superpowers Backplane Session Handoffs Design

**Status:** Proposed for operator review

## Purpose

Superpowers produces durable specifications and plans, while Backplane preserves
the product arc in native GitHub Issues. Neither currently preserves the live
thread that is lost when an implementation session ends: observed environment
facts, corrections to the plan, rejected approaches, deferred obligations,
verification state, uncertainty, and the exact reason one next action still
makes sense.

Backplane will add a skills-only session-handoff capability fitted to upstream
Superpowers. It will help an outgoing session preserve that live thread and help
an incoming session reconcile it against current authority before choosing
where to start.

The capability is advisory. A handoff never becomes design authority,
execution authority, backlog authority, or an authorization gate.

## Scope

### Included

- One reusable skill supporting CREATE and RESUME operations.
- A portable, project-local Markdown handoff contract.
- Evidence attribution and explicit uncertainty.
- Git, GitHub issue, specification, and plan drift reconciliation.
- A resume assessment that answers what bearing prior state has on the next
  action.
- Integration with `managing-superpowers-backlog` and upstream Superpowers
  skills without modifying or copying upstream Superpowers.
- Transcript-based RED/GREEN/REFACTOR conformance evidence.

### Excluded

- A Backplane executable, daemon, hook, MCP server, or required project runtime.
- Automatic session-start loading or context-limit detection.
- Transactional runtime checkpointing, replay, or restoration of model state.
- Automatic Git commits, pushes, issue transitions, or handoff archival.
- Treating the newest file as authoritative merely because it is newest.
- Replacing harness-native resume, compaction, memory, or checkpoint features.

## Comparative Basis

The design adopts gzkit as the strongest examined end-to-end reference while
preserving advantages found elsewhere:

- From gzkit: evidence-aware CREATE/RESUME separation, lineage, durable
  artifacts, issue and decision references, explicit uncertainty, and the
  principle that a handoff advises rather than authorizes.
- From Matt Pocock's handoff: tailor the artifact to the incoming session's
  declared purpose, reference durable artifacts instead of copying them, name
  suggested skills, and choose handoff deliberately at a phase boundary.
- From runtime checkpoint systems such as LangGraph: distinguish exact saved
  machine state from a human-readable summary. Backplane must not claim the
  former.
- From repository-memory and repository-map systems: reconstruct current
  project state from durable sources rather than trusting narrative recall.
- From handoff-debt research: preserve context that is expensive or impossible
  to rediscover while keeping the initial context substantially smaller than a
  raw execution trace.

## Architecture

Create one skill package:

```text
skills/managing-superpowers-handoffs/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── handoff-contract.md
    └── resume-assessment.md
```

`SKILL.md` owns operation selection, phase-boundary guidance, the CREATE and
RESUME procedures, authority boundaries, and failure behavior.

`handoff-contract.md` owns the portable artifact format, storage and naming
rules, required sections, claim attribution, lineage, redaction, and collision
behavior.

`resume-assessment.md` owns drift probes, claim reconciliation, next-step
precondition checks, verdict definitions, and the required incoming-session
report shape.

CREATE and RESUME remain in one skill so their shared vocabulary cannot drift
between independently triggered skills. Detailed contracts remain in references
to keep the triggering surface concise.

## Storage and Identity

Default storage is:

```text
docs/superpowers/handoffs/<UTC-basic-timestamp>-<safe-kebab-slug>.md
```

The filename is unique and append-only. CREATE must check that the destination
does not exist and refuse rather than overwrite it. A user may explicitly
request an ephemeral external location, but project-local durable storage is
the default because it supports cross-session, cross-model, and cross-machine
transfer when the project chooses to commit or otherwise transport the file.

Each artifact records:

- format version, creation time, repository identity, branch, and HEAD;
- the incoming session's declared purpose;
- work-item URL and consumed `updatedAt` revision when backlog-tracked;
- specification and plan paths and their observed Git identity;
- zero or more predecessor handoff paths;
- creator identity when known, without inventing a session identifier.

The skill does not maintain a mutable `latest` pointer. On RESUME, an explicit
path is preferred. Without one, the skill discovers candidates and selects only
when current branch, work item, plan, and lineage make the choice unambiguous.
Otherwise it presents candidates and asks the operator to choose.

## CREATE Contract

CREATE begins by asking or inferring the purpose of the incoming session. It
then reads project instructions and durable authorities before writing.

The outgoing handoff contains these sections in this order:

1. **Incoming purpose** — what the next session is expected to accomplish.
2. **Authority anchors** — issue, specification, plan, repository, branch, and
   revision references; reference settled artifacts rather than copying them.
3. **Verified current state** — commands run and observed results, including
   worktree and verification state.
4. **Live thread** — information that exists only in the outgoing session.
5. **Corrections to prior beliefs** — plan or assumption changes supported by
   observed evidence.
6. **Decisions and provenance** — operator rulings and agent choices kept
   distinct.
7. **Negative results** — attempted approaches, observed failure, and why they
   should not be repeated without new evidence.
8. **Deferred obligations** — discovered work that must survive but is not
   silently added to current scope.
9. **Risks and unknowns** — every load-bearing gap marked explicitly.
10. **Proposed next steps** — ordered actions with preconditions and verification
    seams.
11. **Suggested skills** — exact upstream Superpowers and Backplane skills the
    incoming session is likely to need.
12. **Resume instruction** — the exact handoff path and instruction to invoke
    RESUME against it.

Every load-bearing claim is marked as one of:

- `VERIFIED: <probe or authoritative source>`
- `INFERRED: <evidence and reasoning>`
- `UNVERIFIED: <reason and proposed probe>`

CREATE screens for common secret and personally identifying patterns, but must
describe that check honestly as heuristic. If sensitive information cannot be
safely removed without destroying the handoff's meaning, CREATE refuses to
write and asks the operator how to proceed.

## RESUME Contract

RESUME never treats a handoff as current merely because it parses or is recent.
It first validates the required document structure, repository identity, path
containment, and predecessor references that it can inspect.

It then reconciles:

- current branch, HEAD relationship, commits, dirty state, and changed relevant
  files;
- current GitHub issue state, lifecycle, hierarchy, blockers, `updatedAt`, and
  linked delivery evidence through `managing-superpowers-backlog`;
- current specification and plan existence and revision;
- each load-bearing claim and each next-step precondition;
- current project instructions and applicable skills.

Elapsed time is one drift signal, never the entire freshness decision. Unknown
state remains unknown; it is never promoted to fresh.

RESUME produces this report:

```text
Selected handoff: <path and selection reason>
Current anchors: <repository / branch / HEAD / issue / plan>
Confirmed claims: <concise list>
Drifted claims: <concise list with evidence>
Unverified claims: <concise list with exact probes>
Next-step assessment: <each proposed step and precondition status>
Bearing: CONTINUE | REVISE | ABANDON | VERIFY
Start here because: <one evidence-backed sentence>
```

Verdicts mean:

- **CONTINUE** — the objective and next action remain supported by current
  authority and verified preconditions.
- **REVISE** — the objective remains live, but the plan or next action no longer
  fits current evidence.
- **ABANDON** — current operator or authoritative project state has rejected,
  superseded, or completed the handed-off objective. The agent does not invent
  abandonment authority.
- **VERIFY** — an unresolved contradiction or unknown load-bearing claim makes
  the correct starting action additional verification.

The verdict is advice. It does not arm or lift a gate and does not itself permit
or forbid mutation.

## Superpowers and Backplane Binding

Use the handoff at a deliberate phase boundary, interruption, model or harness
switch, context-risk point, or return to unfinished work. Do not hand off merely
because a plan exists or because ordinary continuation remains cheaper and
preserves useful primary context.

The handoff surrounds but does not reorder upstream Superpowers:

```text
Backplane issue continuity
  -> Superpowers design and plan
  -> execution / review / verification
  -> CREATE at a real session boundary
  -> RESUME and reconcile
  -> re-enter the applicable Superpowers stage
```

When a GitHub work item is present, use `managing-superpowers-backlog` for
complete native intake. Handoff creation or resumption is read-only with respect
to GitHub. Any lifecycle mutation requires a separate explicit request and the
Backplane transition contract.

## Failure Behavior

Fail closed on writing when:

- the destination collides with an existing file;
- repository identity cannot be established;
- required authority anchors are claimed but cannot be identified;
- secrets cannot be safely redacted;
- the requested artifact would present unverified beliefs as verified facts.

On RESUME, report rather than suppress malformed timestamps, missing sections,
dangling predecessors, repository mismatch, ambiguous candidate selection, and
unavailable probes. These conditions normally produce `VERIFY`; they do not
silently remove the session-entry advisement.

## Conformance Strategy

Develop the skill with documentation TDD and no project runtime dependency:

1. Run no-skill baseline scenarios and preserve verbatim responses.
2. Record observed omissions and rationalizations.
3. Write the smallest skill and references that correct those observed failures.
4. Repeat the same scenarios with the skill loaded.
5. Add adversarial variations for stale issue state, branch divergence,
   ambiguous candidate selection, secret exposure, and pressure to continue.
6. Run structural skill validation as supplemental authoring evidence.

The minimum conformance set is:

- `handoff-create` — preserves the live thread without duplicating settled
  artifacts or inventing evidence;
- `handoff-resume-drift` — refuses to follow a stale next step and produces the
  correct bearing;
- `handoff-authority` — does not treat the handoff as a gate or governing
  authority;
- `handoff-selection` — does not choose the newest candidate when identity is
  ambiguous;
- `handoff-language-neutral` — introduces no consuming-project runtime or test
  framework;
- `handoff-sensitive-content` — redacts or refuses unsafe material.

## Backlog Integration

Create one executable native GitHub issue under the v0.1 product arc for the
skills-only handoff capability. Its implementation must precede Backplane
self-hosting evidence so self-hosting exercises both backlog continuity and
session continuity. The external pilot must install and test both Backplane
skills before release.

The issue, specification, and plan remain layered authorities. This design is
the handoff capability's design authority after operator approval; the issue
owns backlog identity and lifecycle; the plan owns bounded execution.

## Success Criteria

- An outgoing session can create a concise, evidence-attributed handoff whose
  unique value is not already present in issue, spec, plan, commit, or diff.
- An incoming session detects material drift and explains its bearing before
  recommending where to start.
- The skill never claims automatic hooks, runtime checkpointing, transactional
  lineage, or authorization enforcement.
- The skill remains language-neutral and fitted to current stable upstream
  Superpowers.
- Transcript evidence demonstrates improved behavior over a no-skill control.
