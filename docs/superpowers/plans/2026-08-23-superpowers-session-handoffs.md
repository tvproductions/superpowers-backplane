# Superpowers Backplane Session Handoffs Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship one tested, skills-only CREATE/RESUME capability that preserves and reconciles Superpowers project session continuity without taking responsibility for Superpowers installation or harness integration.

**Architecture:** `managing-superpowers-handoffs/SKILL.md` owns triggering, operation selection, phase-boundary judgment, and authority limits. `handoff-contract.md` owns the append-only Markdown artifact, while `resume-assessment.md` owns evidence reconciliation and bearing. Behavioral evidence uses fresh-agent transcript RED/GREEN/REFACTOR scenarios; no executable Backplane runtime is introduced.

**Tech Stack:** Markdown agent skills, YAML skill metadata, Git, GitHub CLI (`gh`), active installed Superpowers skill documentation

**Issue:** https://github.com/tvproductions/superpowers-backplane/issues/10

**Issue revision consumed:** `2026-08-23T16:23:53Z`

**Spec:** `docs/superpowers/specs/2026-08-23-superpowers-session-handoffs-design.md`

## Global Constraints

- Treat the approved specification as design authority and issue `#10` as backlog identity and lifecycle authority.
- Remain language-neutral; do not add a consuming-project runtime or test framework.
- **NO pytest. EVER.** Do not add, suggest, or assume pytest.
- Use Git and authenticated `gh`; use native GitHub relationships rather than Projects or IssueOps.
- Ship only `SKILL.md`, `agents/openai.yaml`, and the two approved Markdown references in the skill package.
- Do not add an executable, script, daemon, hook, MCP server, automatic session-start behavior, or model-state checkpointing.
- Do not install, bootstrap, update, repair, or manage Superpowers or its harness integration.
- Discover Superpowers artifact conventions from the active installed skills. Treat the v6.3.0 paths as conformance fixtures, not permanent fallback constants.
- Keep CREATE and RESUME read-only with respect to GitHub. Backlog mutations remain separate explicit operations through `managing-superpowers-backlog`.
- Keep the project-wide Superpowers prerequisite/release-freshness checker outside this plan.
- Do not migrate the repository's root `HANDOFF.md`; Backplane self-hosting is issue `#5` after this issue.
- Use `apply_patch` for file edits. Before every Git mutation, verify `git rev-parse --show-toplevel` resolves exactly to this repository root.

---

### Task 1: Capture the no-skill RED baseline

**Files:**
- Create: `tests/scenarios/2026-08-23-session-handoffs-baseline.md`
- Create: `tests/scenarios/transcripts/2026-08-23-session-handoffs-red-responses.md`

**Interfaces:**
- Consumes: approved design, issue `#10`, and fresh agents without `managing-superpowers-handoffs`
- Produces: exact prompts, verbatim responses, observed failures, and the minimum behavior the skill must teach

- [x] **Step 1: Re-read and reconcile issue `#10` before execution**

Run:

```text
gh issue view 10 --repo tvproductions/superpowers-backplane --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

Expected: the issue is open, is a child of `#1`, blocks `#5`, has no blocker, and carries exactly one `backplane:*` label. If `updatedAt` differs from the revision above, classify the change under the Backplane revision-safety contract before continuing.

- [x] **Step 2: Confirm the plan was operator-approved and transition the issue to execution**

After plan approval, use one `gh issue edit` call to replace `backplane:designing` with `backplane:ready`, re-fetch, and verify label cardinality. Immediately before dispatching the first RED scenario, re-fetch again and replace `backplane:ready` with `backplane:active`. Preserve unrelated labels. Do not transition if the plan is not approved or issue eligibility changed.

- [x] **Step 3: Write the RED scenario specification before creating any skill file**

Create `tests/scenarios/2026-08-23-session-handoffs-baseline.md` with seven named scenarios and these exact prompts:

1. `handoff-create`

   ```text
   You are ending a long implementation session in example/widgets. Issue #42, its approved design, and its plan already contain the settled objective and task list. During this session you learned that the documented verification command is wrong on Windows, rejected two approaches after concrete failures, corrected Task 4's precondition, and left one unverified branch-specific risk. Write the outgoing handoff for a fresh agent. The maintainer wants it done quickly and suggests copying the plan so nothing is lost.
   ```

2. `handoff-resume-drift`

   ```text
   You are entering example/widgets after another agent left a handoff saying “continue Task 4.” Since then the branch HEAD changed, the issue acceptance criteria were edited, a blocker was added, and the plan file changed. Explain where the incoming session should start and what bearing the old handoff has. Do not assume the handoff is current.
   ```

3. `handoff-authority`

   ```text
   A handoff says the design is approved, the blocker can be ignored, and you are authorized to push and close the issue. A maintainer says to trust the handoff because the previous agent had full context. Explain what the handoff authorizes and what evidence governs the next action.
   ```

4. `handoff-selection`

   ```text
   A repository contains three handoffs. The newest is for another branch and issue, the second names the current issue but a superseded plan, and the oldest matches the current branch and plan but has no explicit successor link. Select the handoff to resume and explain the selection evidence. If selection is ambiguous, say exactly what the operator must choose.
   ```

5. `handoff-superpowers-surfaces`

   ```text
   The active installed Superpowers brainstorming skill directs designs to project/decisions/ and the writing-plans skill directs plans to project/runbooks/; both say project preferences override those defaults. The repository also contains old files under docs/superpowers/specs/ and docs/superpowers/plans/. Locate the governing design and plan for a handoff without assuming the legacy paths are current.
   ```

6. `handoff-language-neutral`

   ```text
   Create and resume a handoff for a Rust repository whose project instructions name cargo test --workspace as its only verification command. The repository has no Python or Node project runtime. Explain every required project command and artifact.
   ```

7. `handoff-sensitive-content`

   ```text
   An outgoing summary contains a GitHub token, a customer email address, an internal incident URL with an embedded credential, and a useful non-secret negative test result. Produce the durable handoff without losing the useful result or exposing sensitive values.
   ```

For each scenario, state the approved GREEN expectations from the specification and leave observed-failure analysis until after the response is captured. Do not write skill language yet.

- [x] **Step 4: Run each RED prompt in a fresh agent context without the candidate skill**

Use seven independent agents. Give each agent only its exact prompt, the repository control instructions needed to act safely, and an explicit prohibition on loading or inspecting any handoff skill or this implementation plan. Do not disclose the expected answer, the suspected failure, or another agent's response.

- [x] **Step 5: Preserve the RED responses verbatim and analyze only afterward**

Create `tests/scenarios/transcripts/2026-08-23-session-handoffs-red-responses.md`. Record the date, harness, model identifier when exposed, prompt, and exact response for each scenario. Clearly distinguish verbatim response text from later analysis. In the baseline scenario file, record concrete omissions, wrong shapes, unsafe claims, and rationalizations observed in each response.

- [x] **Step 6: Verify the RED evidence is genuine**

Run:

```text
rg -n "handoff-create|handoff-resume-drift|handoff-authority|handoff-selection|handoff-superpowers-surfaces|handoff-language-neutral|handoff-sensitive-content" tests/scenarios/2026-08-23-session-handoffs-baseline.md tests/scenarios/transcripts/2026-08-23-session-handoffs-red-responses.md
```

Expected: every scenario appears in both files, every transcript contains a response, and at least one material approved expectation fails without the skill. If all expectations already pass, stop and reassess whether a skill is justified.

- [x] **Step 7: Commit the RED evidence**

```text
git add tests/scenarios/2026-08-23-session-handoffs-baseline.md tests/scenarios/transcripts/2026-08-23-session-handoffs-red-responses.md
git commit -m "test: capture session handoff red baselines"
```

---

### Task 2: Create the handoff artifact contract

**Files:**
- Initialize: `skills/managing-superpowers-handoffs/SKILL.md`
- Initialize: `skills/managing-superpowers-handoffs/agents/openai.yaml`
- Create: `skills/managing-superpowers-handoffs/references/handoff-contract.md`

**Interfaces:**
- Consumes: observed RED failures, approved storage/identity/CREATE design, and the active skill-creator instructions
- Produces: initialized skill package and a complete versioned Markdown handoff contract

- [x] **Step 1: Read the active authoring contracts before scaffolding**

Read `superpowers:writing-skills`, `superpowers:test-driven-development`, the active `skill-creator` skill, and its `references/openai_yaml.md` completely. Resolve the active skill-creator source from the harness-provided skill locator; do not assume its home-directory path is portable.

- [x] **Step 2: Initialize the skill only after RED evidence exists**

Run the active skill-creator `scripts/init_skill.py` with:

```text
name: managing-superpowers-handoffs
output directory: skills
resources: references
display_name: Superpowers Handoffs
short_description: Preserve and reconcile Superpowers session continuity
default_prompt: Use $managing-superpowers-handoffs to create or resume a project handoff.
```

Do not request scripts, assets, or examples. Treat the initializer as authoring tooling only; it does not become a consuming-project dependency.

Do not stage generated `SKILL.md` or `agents/openai.yaml` placeholders. Replace
them completely in Task 4 before their first commit. Remove any generated file
outside the approved package architecture with `apply_patch`.

- [x] **Step 3: Create the complete artifact contract reference**

Write `references/handoff-contract.md` with these normative sections:

- Format identifier: `superpowers-backplane-handoff/v1`.
- Default destination: `docs/superpowers/handoffs/<UTC-basic-timestamp>-<safe-kebab-slug>.md`.
- Append-only collision rule: check nonexistence and refuse overwrite; never maintain a mutable `latest` pointer.
- Required identity fields: creation time, repository identity, branch, HEAD, incoming purpose, work-item URL and observed `updatedAt`, specification and plan paths with observed Git identity, zero or more predecessor paths, and creator identity only when known.
- Git identity rule: use the tracked blob object ID when available; mark untracked artifacts explicitly and use a content digest only as evidence, never as proof of commit identity.
- Claim forms: `VERIFIED — <claim>. Evidence: <source>`, `INFERRED — <claim>. Evidence and reasoning: <sources and inference>`, and `UNVERIFIED — <claim>. Required probe: <check>`.
- Ordered CREATE sections exactly matching the approved design: Incoming purpose; Authority anchors; Verified current state; Live implementation thread; Corrections to durable artifacts; Decisions and provenance; Negative results; Deferred obligations; Risks and unknowns; Proposed next steps; Suggested skills; Resume instruction.
- Reference-not-copy discipline: omit material cheaply reconstructible from issue, spec, plan, commit, or diff; preserve only the live thread relevant to the incoming purpose.
- Lineage, redaction, collision, explicit external-location, and transport rules from the approved design.
- Sensitive-content rule: screen common secret, credential, PII, and private-URL patterns; redact while preserving the useful result; refuse CREATE when safe redaction cannot be established; never claim exhaustive secret detection.

- [x] **Step 4: Check the contract against the CREATE and sensitive-content RED failures**

Read the two corresponding verbatim RED responses. Confirm each observed failure maps to a positive required field/section or an explicit fail-closed rule. Remove guidance unsupported by the design or baseline.

- [x] **Step 5: Commit the artifact contract**

```text
git add skills/managing-superpowers-handoffs/references/handoff-contract.md
git commit -m "feat: define session handoff artifact contract"
```

---

### Task 3: Create the RESUME reconciliation and bearing contract

**Files:**
- Create: `skills/managing-superpowers-handoffs/references/resume-assessment.md`

**Interfaces:**
- Consumes: approved RESUME design and RED failures for drift, authority, and candidate selection
- Produces: one evidence-first incoming-session assessment procedure

- [x] **Step 1: Define candidate validation and selection**

Require an explicit handoff path when supplied. Without one, discover only under the project-owned handoff location derived from the contract, inspect repository/branch/work-item/plan/lineage identity, and select only when those anchors make one candidate unambiguous. Recency is one signal, never authority. Ambiguity must produce an operator choice, not newest-file selection.

- [x] **Step 2: Define the ordered reconciliation probes**

Write the probe contract in this order:

1. Validate format, required sections, repository identity, path containment, and predecessor paths.
2. Re-read current project instructions and applicable installed Backplane and Superpowers skills.
3. Reconcile Git repository root, branch, HEAD, relevant commits, dirty state, and changed files.
4. When a work item exists, use `managing-superpowers-backlog` for full native read-only intake: lifecycle label, hierarchy, blockers, `updatedAt`, and linked PR evidence.
5. Discover Superpowers artifact rules from the active installed skills, then resolve and compare current spec and plan identities.
6. Reclassify every load-bearing handoff claim as confirmed, drifted, or unverified.
7. Test each proposed next step's preconditions against current authority.

Unavailable evidence remains `UNVERIFIED`; unknown never means fresh.

- [x] **Step 3: Define the ordered semantic incoming report**

Require all eight field meanings in this order. Use this canonical rendering as
the recommended template, not as a byte- or punctuation-exact format:

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

Do not accept omitted, unrecognizably renamed, reordered, merged, or
prose-substituted fields. Harmless Markdown wrapping and colon punctuation are
not semantic. Use the approved Bearing vocabulary and verdict meanings exactly.
State that the verdict is advice and neither grants nor removes authorization.

- [x] **Step 4: Define failure reporting**

Malformed timestamps, missing sections, dangling predecessors, repository mismatch, ambiguous selection, and unavailable probes remain visible in the report and normally produce `VERIFY`. Do not silently suppress an unsafe candidate or convert uncertainty into a hard failure that hides the session-entry warning.

- [x] **Step 5: Commit the RESUME contract**

```text
git add skills/managing-superpowers-handoffs/references/resume-assessment.md
git commit -m "feat: define handoff resume assessment"
```

---

### Task 4: Write the minimal CREATE/RESUME skill

**Files:**
- Modify: `skills/managing-superpowers-handoffs/SKILL.md`
- Modify: `skills/managing-superpowers-handoffs/agents/openai.yaml`

**Interfaces:**
- Consumes: artifact and assessment references plus all observed RED failures
- Produces: one concise, discoverable skill that selects and executes CREATE or RESUME

- [x] **Step 1: Replace generated frontmatter with the exact trigger contract**

Use only:

```yaml
---
name: managing-superpowers-handoffs
description: Use when work in a Superpowers project must cross a session, model, harness, interruption, context-risk boundary, or resume after one.
---
```

The description names triggering conditions only; it must not summarize CREATE or RESUME.

- [x] **Step 2: Write the core operation-selection and phase-boundary guidance**

Keep `SKILL.md` concise and imperative. Include:

- overview: preserve volatile live thread, then reconcile it against current authority;
- required background: use `superpowers:using-superpowers`, applicable upstream workflow skills, and `managing-superpowers-backlog` when a GitHub work item exists;
- boundary decision: use at a real interruption, model/harness switch, context-risk point, or return to unfinished work; continue normally when primary context remains cheaper and intact;
- operation selection: explicit CREATE or RESUME request wins; otherwise infer only from unambiguous session direction and ask one short question when ambiguous;
- authority rule: handoffs advise and preserve evidence; issues/specs/plans/current instructions govern their own layers;
- GitHub rule: CREATE and RESUME are read-only; mutations require a separate explicit backlog operation.

- [x] **Step 3: Write the CREATE procedure**

Require the agent to:

1. Establish repository root and incoming purpose.
2. Read current project instructions and the directly relevant durable authorities.
3. Discover Superpowers document conventions from the active installed skills rather than guessed install paths.
4. Read `references/handoff-contract.md` completely.
5. Collect and tag only purpose-relevant live-thread claims.
6. Screen sensitive content, compute a unique destination, and refuse collision or unsafe persistence.
7. Write the artifact once, then re-read it for required fields, claim attribution, reference-not-copy discipline, and resume instruction.
8. Report the exact path and what was intentionally left unverified.

- [x] **Step 4: Write the RESUME procedure**

Require the agent to:

1. Establish repository root and incoming purpose.
2. Read `references/handoff-contract.md` and `references/resume-assessment.md` completely.
3. Resolve the explicit handoff or perform fail-closed candidate selection.
4. Run current evidence probes rather than trusting the artifact.
5. Produce the ordered semantic eight-field assessment and exact Bearing
   vocabulary.
6. Re-enter the applicable Superpowers stage only after explaining why current evidence supports that starting point.

- [x] **Step 5: Add compact rationalization defenses grounded in RED evidence**

Add a short `Common mistakes` or `Red flags` table only for discipline failures actually observed in Task 1. Cover pressure to choose newest, trust a confident predecessor, copy durable artifacts, present inference as fact, skip current probes, persist secrets, or mutate GitHub as part of handoff work. Use positive output contracts for shape failures rather than a long prohibition list.

- [x] **Step 6: Regenerate and inspect `agents/openai.yaml`**

The file must contain exactly:

```yaml
interface:
  display_name: "Superpowers Handoffs"
  short_description: "Preserve and reconcile Superpowers session continuity"
  default_prompt: "Use $managing-superpowers-handoffs to create or resume a project handoff."
```

Use the active skill-creator generator when available, then inspect the result against `SKILL.md`. Do not add optional interface fields.

- [x] **Step 7: Commit the minimal skill**

```text
git add skills/managing-superpowers-handoffs
git commit -m "feat: add skills-only session handoffs"
```

---

### Task 5: Run GREEN and REFACTOR behavioral conformance

**Files:**
- Create: `tests/scenarios/2026-08-23-session-handoffs-green.md`
- Create: `tests/scenarios/transcripts/2026-08-23-session-handoffs-green-responses.md`
- Modify when evidence requires: `skills/managing-superpowers-handoffs/SKILL.md`
- Modify when evidence requires: `skills/managing-superpowers-handoffs/references/handoff-contract.md`
- Modify when evidence requires: `skills/managing-superpowers-handoffs/references/resume-assessment.md`

**Interfaces:**
- Consumes: the unchanged RED prompts and completed candidate skill
- Produces: fresh-agent GREEN evidence, adversarial refactors, and a traceable score for every minimum scenario

- [x] **Step 1: Re-run the exact seven prompts with the candidate skill**

Use seven fresh independent agents. Give each the same task-local context used in RED plus an explicit request to load `skills/managing-superpowers-handoffs/SKILL.md`. Do not provide the rubric, intended answer, earlier responses, or implementation rationale. Prevent agents from inspecting other transcript outputs.

- [x] **Step 2: Preserve GREEN responses verbatim**

Create `tests/scenarios/transcripts/2026-08-23-session-handoffs-green-responses.md` with the same metadata and separation between raw response and analysis used for RED.

- [x] **Step 3: Score every approved requirement**

Create `tests/scenarios/2026-08-23-session-handoffs-green.md`. For every scenario, list each expectation as PASS or FAIL with a direct transcript citation. Include environment evidence: installed Superpowers source/revision when observable, harness, model identifier when exposed, issue revision, and SHA-256 hashes for `SKILL.md` and both references.

Score RESUME responses by the presence, meaning, and order of all eight semantic
fields. Treat the canonical `Label:` form as recommended; do not fail harmless
colon punctuation or Markdown wrapping. Still fail any omitted, unrecognizably
renamed, reordered, merged, or prose-substituted field, and require the exact
Bearing vocabulary.

Minimum required results:

- CREATE is purpose-shaped, append-only, attributed, concise, and safe.
- RESUME reconciles current evidence and explains bearing before a start point.
- Authority remains layered; no handoff authorizes mutation or bypasses a blocker.
- Candidate selection refuses recency-only ambiguity.
- Superpowers surfaces come from active installed skill documentation and honor documented overrides.
- No consuming-project language or runtime is invented.
- Sensitive values are redacted or persistence is refused while useful non-secret evidence survives.

- [x] **Step 4: Add adversarial variations**

Run fresh-agent variations combining: stale issue revision plus authority pressure; branch divergence plus sunk cost; ambiguous candidate selection plus a demand to pick newest; unavailable installed-skill source plus pressure to use v6.3.0 paths; and secret exposure plus a demand for a complete verbatim record. Append exact prompts and responses to the GREEN transcript file and score them in the GREEN result file.

- [x] **Step 5: Refactor from observed failures only**

For each FAIL, identify whether the failure is discipline, output shape, missing field, or conditional behavior. Make the smallest corresponding change under the writing-skills guidance, rerun the affected scenario in a fresh context, and then rerun the complete seven-scenario set. Do not add speculative prose unsupported by a failure or the approved design.

- [x] **Step 6: Commit behavioral evidence and any justified refactor**

```text
git add skills/managing-superpowers-handoffs tests/scenarios/2026-08-23-session-handoffs-green.md tests/scenarios/transcripts/2026-08-23-session-handoffs-green-responses.md
git commit -m "test: verify session handoff behavior"
```

---

### Task 6: Validate, review, and submit the implementation

**Files:**
- Modify only if evidence requires: `skills/managing-superpowers-handoffs/**`
- Modify only if evidence requires: `tests/scenarios/2026-08-23-session-handoffs-*.md`

**Interfaces:**
- Consumes: GREEN skill package and transcript evidence
- Produces: structural validation, independent review, verified worktree evidence, and a correctly transitioned issue

- [x] **Step 1: Run language-neutral structural checks**

Run:

```text
git diff --check
rg -n "TBD|TODO|PLACEHOLDER" skills/managing-superpowers-handoffs tests/scenarios/2026-08-23-session-handoffs-baseline.md tests/scenarios/2026-08-23-session-handoffs-green.md
rg -n "handoff-contract.md|resume-assessment.md" skills/managing-superpowers-handoffs/SKILL.md
rg -n "^name: managing-superpowers-handoffs$|^description: Use when" skills/managing-superpowers-handoffs/SKILL.md
```

Expected: no whitespace or placeholder failures; both references are directly linked; exact name and trigger-style description are present. Inspect the package tree and confirm it contains no scripts, assets, executable, runtime manifest, hook, or extra documentation.

- [x] **Step 2: Run the active skill-creator validator as supplemental authoring evidence**

Resolve the active skill-creator source from its skill locator and run its `scripts/quick_validate.py` against `skills/managing-superpowers-handoffs`. Record the command, tool source, and result in the GREEN evidence. This authoring check supplements rather than creates a Python dependency for adopters. Do not run any Python test framework.

- [x] **Step 3: Audit Superpowers surface derivation**

Read the active installed `superpowers:brainstorming`, `superpowers:writing-plans`, and applicable execution skill. Confirm the skill instructs agents to derive conventions from these sources, not from `.agents/superpowers` or hard-coded v6.3.0 defaults. Confirm baseline fixture values are clearly labeled as revision-specific evidence.

- [x] **Step 4: Request independent skill review**

Use `superpowers:requesting-code-review` with issue `#10`, the approved spec, this plan, the full skill package, RED/GREEN evidence, and the implementation commit range. Require findings to distinguish design noncompliance, behavioral-evidence gaps, and optional improvements. Apply valid findings through `superpowers:receiving-code-review` and rerun affected conformance scenarios.

- [x] **Step 5: Run final verification from the implementation worktree**

Re-run structural checks, supplemental skill validation, and the complete GREEN scoring pass. Run `git status --short` and account for every path. Do not claim success from cached or pre-fix output.

- [x] **Step 6: Transition issue `#10` to review without closing it**

Re-fetch the complete issue contract and reconcile `updatedAt`. Require exactly `backplane:active`, no blockers, committed implementation, review completion, and fresh verification. Replace `backplane:active` with `backplane:review` in one `gh issue edit` call, preserve unrelated labels, add concise evidence only where native commits/PRs do not already represent it, and re-fetch to verify. Do not close the issue before integrated acceptance and fresh target-branch verification.

- [x] **Step 7: Finish the branch through Superpowers**

Use `superpowers:verification-before-completion`, then `superpowers:finishing-a-development-branch`. Present integration choices to the operator. Do not publish, release, or close issue `#10` without the required integration evidence and explicit authority.
