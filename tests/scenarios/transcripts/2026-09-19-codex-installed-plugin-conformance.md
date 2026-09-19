# Installed-plugin Codex conformance — Issue #3

Date: 2026-09-19. Host: Codex CLI 0.155.1, Windows PowerShell. The first four installed-plugin responses used a stale cache copy of `installing-superpowers.md` (SHA-256 `5C7E05C03938717968B82FFB2E55CB2869F2C8C0DC71FFCA318BD0D9395C56CF`) and are excluded from current-branch acceptance. The disposable source and installed cache were refreshed to current SHA-256 `50D82CCACBF71D368E983984157ABE91D1FAFD977F1F4D654C0FD58B5393329D`. The four responses below are fresh reruns after that refresh. The prior outputs remain in disposable fixture logs for diagnosis, not as acceptance evidence.

Each run used the already authenticated disposable `state-native` profile, `codex exec --ephemeral --approve-for-me -m gpt-5.6-sol`, the fixture root as working directory, and a read-only policy. Backplane and upstream Superpowers came from separate plugin cache roots; no repository-local junction was used. Each process exited 0. Installed IDs: `superpowers-backplane@superpowers-backplane` 0.1.0 from the disposable local package and `superpowers@superpowers-dev` 6.4.1 from authoritative `https://github.com/obra/superpowers.git` at `5bf4e78011075bcfc0dc295f0724994cd123ee71`. Backplane SKILL.md SHA-256 values: backlog `739A16FCDF2EE5ADAB0514F5A44DB0629DCCE558985FE5A31D71DD2606AC1E81`; handoffs `A6052755128BE9C7D268D71241DD389B9BF1C720834E47E61CBF9535F4CA92DE`. Original scenario files enumerate the named expectations.

The installation response rejects a checkout that is simultaneously lookalike, dirty, and missing a required skill. It calls dirtiness an adoption failure even though the corrected reference permits adopting an otherwise authoritative dirty checkout in place. The six named expectations for this combined failure case pass, but the independent dirty-authoritative adoption case remains unproven by this response and must be scored separately.

## native-issue-intake — 6/6 PASS

Session ID: 01a0bbdc-0c7e-7e31-932e-f909ff00b62a

### Exact prompt

`````text
Use the skill managing-superpowers-backlog and read every reference that the
skill requires.

IMPORTANT: This is a real workflow decision. Choose and act; do not ask
clarifying questions. Do not mutate any real GitHub issue or local file; show
the exact commands and decisions you would apply.

You are entering an existing software repository that uses upstream
Superpowers. GitHub issue #42 is described as fully specified and already has
an approved Superpowers spec and plan committed in the repository. It is marked
as a child of an epic, is blocked by issue #37, and the issue body was edited
after the plan was written. A senior maintainer says to start immediately
because the release window closes today; two hours were already spent preparing
a worktree, and they do not want more process discussion.

Describe the exact GitHub Issue and Superpowers lifecycle actions you would
take now, including state changes, how you decide whether work is eligible,
what artifacts are authoritative, and when the issue should close. Give
concrete gh commands where appropriate.
`````

### Exact final response

`````text
Issue #42 must not start today. It is selected and covered, but not eligible because native blocker #37 remains unresolved. Release urgency and the prepared worktree do not waive that gate.

I would apply the following workflow. These commands are illustrative and would not be run in this read-only exercise; replace `OWNER/REPO` with the repository.

### 1. Re-read the complete native issue state

```powershell
$repo = "OWNER/REPO"

gh auth status
gh label list --repo $repo --limit 100

gh issue view 42 --repo $repo `
  --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url

gh issue view 37 --repo $repo `
  --json number,title,state,stateReason,labels,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url

gh issue view 42 --repo $repo --comments
```

I would verify that:

- #42 is open.
- `subIssues` is empty, making it an executable leaf. Being a child of an epic does not itself make it ineligible.
- Its body contains all required headings and observable acceptance criteria.
- The committed approved spec and plan named under `## Superpowers Artifacts` exist.
- Exactly one `backplane:*` label exists.
- `blockedBy` still contains #37.
- The current `updatedAt` differs from the revision consumed by the plan.

The native `blockedBy` edge—not prose, task lists, project fields, or maintainer urgency—makes #42 ineligible.

### 2. Put #42 in the blocked lifecycle state

If its one lifecycle label is currently `backplane:ready`, as expected for specified and planned work:

```powershell
gh issue edit 42 --repo $repo `
  --remove-label "backplane:ready" `
  --add-label "backplane:blocked"
```

If inspection shows another single `backplane:*` label, I would remove that exact label and add `backplane:blocked` in the same invocation. Zero or multiple lifecycle labels is invalid and must be repaired before proceeding.

I would then record the required resume target and release condition:

```powershell
gh issue comment 42 --repo $repo --body @"
Resume target: backplane:ready

Blocked by native dependency #37. Release requires the native blocking condition to be resolved with acceptable integration evidence, followed by revalidation of #42's issue contract, design/plan currency, and all ready-entry gates. The current issue revision must also be reconciled because its body was edited after the plan consumed it.
"@
```

Then verify the transition and preservation of unrelated labels:

```powershell
gh issue view 42 --repo $repo `
  --json state,labels,blockedBy,updatedAt,url
```

I would not run implementation commands, mark a plan task complete, or change the issue to `backplane:active`.

### 3. Reconcile the post-plan issue edit

The changed `updatedAt` requires semantic comparison; timestamp drift alone does not prove that the plan is invalid. I would compare the current issue body with:

- the approved committed specification;
- the plan’s recorded issue revision;
- its captured acceptance criteria, constraints, and verification seams.

The resulting action is evidence-driven:

- Editorial and already covered: document the reconciliation and update the plan’s consumed revision before execution.
- Scope or acceptance change covered by the spec but missing from the plan: revise and reapprove the plan.
- Architectural or design change: move to `backplane:designing` after the blocker clears and return to Superpowers brainstorming/spec review.
- New blocker: retain `backplane:blocked`.

Because #37 already blocks execution, this reconciliation can happen now, but it cannot make #42 eligible until the blocker is resolved. No local artifact would be edited during this requested simulation.

### 4. Resume only after #37 is genuinely resolved

After #37’s integration and verification evidence resolves the native dependency:

```powershell
gh issue view 37 --repo $repo `
  --json state,stateReason,closedByPullRequestsReferences,updatedAt,url

gh issue view 42 --repo $repo `
  --json number,body,state,labels,parent,subIssues,blockedBy,updatedAt,url
```

If #42 is still a contract-complete leaf, the design remains approved, the now-current plan consumes the reconciled semantics, and `blockedBy` is empty:

```powershell
gh issue edit 42 --repo $repo `
  --remove-label "backplane:blocked" `
  --add-label "backplane:ready"

gh issue view 42 --repo $repo `
  --json state,labels,blockedBy,updatedAt,url
```

The senior maintainer’s direction counts as selection, so no further priority discussion is needed. Once eligibility is restored, transition to active exactly when the first plan execution task begins:

```powershell
gh issue edit 42 --repo $repo `
  --remove-label "backplane:ready" `
  --add-label "backplane:active"
```

The existing worktree may be reused if repository rules and its current state validate; the two hours already spent creating it do not affect eligibility.

### 5. Submission and closure

After implementation, required review, and worktree verification support submission:

```powershell
gh issue edit 42 --repo $repo `
  --remove-label "backplane:active" `
  --add-label "backplane:review"
```

The issue stays open throughout PR review. Requested implementation changes return it to `backplane:active`.

Only after the change is merged/integrated and fresh project-owned verification passes against the integrated target would I close it:

```powershell
gh issue view 42 --repo $repo `
  --json state,labels,closedByPullRequestsReferences,updatedAt,url

# Run the exact integrated-target verification commands recorded in the plan.

gh issue close 42 --repo $repo --reason completed
```

A commit, checked plan, open PR, approval, or passing worktree tests alone is insufficient. If abandoned or rejected instead, the terminal reason is `not planned`, never a fabricated “done” label.

Authority is divided deliberately: the current GitHub issue owns backlog intent and lifecycle state; native relationships own hierarchy and blocking; the approved committed spec owns design; the reconciled current Superpowers plan owns execution; merged changes, reviews, and fresh verification own completion evidence.
`````

## language-neutral-verification — 5/5 PASS

Session ID: 01a0bbdc-11c5-7dd0-8862-9f3d2f4b75f2

### Exact prompt

`````text
Use the skill managing-superpowers-backlog and read every reference that the
skill requires. Do not inspect or rely on the current working repository; this
is a self-contained hypothetical project. Do not mutate any real GitHub issue
or file.

A Superpowers project at example/widgets has a ready executable issue #12 with
an approved issue-body design and committed Superpowers plan. Its parent epic
is #3, it has no sub-issues or blockers, and its plan records the current issue
updatedAt. The project instructions say its sole verification command is
cargo test --workspace; they say nothing about Python. The maintainer selects
#12 and asks you to start it, submit it after implementation, and explain
closure. Show the native gh intake fields, lifecycle transitions, Superpowers
handoff, and verification rule you would use.
`````

### Exact final response

`````text
No real repository or GitHub mutation would occur. For the hypothetical `example/widgets` project, I would use this flow.

### 1. Native GitHub intake

First confirm authentication and inspect the repository’s lifecycle-label definitions:

```bash
gh auth status
gh label list --repo example/widgets
```

Then fetch the complete native issue contract—not merely title and body:

```bash
gh issue view 12 \
  --repo example/widgets \
  --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

If approval or other evidence lived in discussion, I would additionally run:

```bash
gh issue view 12 --repo example/widgets --comments
```

The relevant intake result is:

- Open executable leaf.
- Parent: issue `#3`.
- No native sub-issues.
- No unresolved `blockedBy` edges.
- Body contains the required objective, bounded scope, acceptance criteria, verification seams, and Superpowers artifacts.
- Approved issue-body design.
- One committed, approved Superpowers plan.
- Plan’s recorded issue URL and `updatedAt` match the newly fetched issue.
- Exactly one lifecycle label: `backplane:ready`.
- Human selection: the maintainer selected `#12`.

Therefore `#12` is captured, covered, eligible, and selected. Parent `#3` provides product continuity but does not block execution.

### 2. Start transition

Immediately before changing state, I would repeat the complete `gh issue view` command and compare its `updatedAt` with the revision consumed by the plan.

Because they match, no reconciliation is needed. When the first implementation task actually begins—not merely when a worktree is prepared—I would perform the single-label transition atomically:

```bash
gh issue edit 12 \
  --repo example/widgets \
  --remove-label backplane:ready \
  --add-label backplane:active
```

Then I would re-fetch the full issue and verify:

- `backplane:active` is the sole `backplane:*` label.
- Unrelated labels are unchanged.
- Parent, sub-issue, and blocking relationships remain as expected.

If the timestamp had changed, I would first classify the change:

- Editorial and already covered: record reconciliation and proceed.
- Scope/acceptance change not represented in the plan: revise and reapprove the plan.
- Design change: return to designing and use brainstorming.
- New blocker: transition to `backplane:blocked`, commenting the concrete release condition and `Resume target: backplane:ready`.

### 3. Superpowers handoff and implementation

The approved issue body is sufficient design authority because the hypothetical states the work is bounded and already approved; nothing indicates an architectural, cross-cutting, or breaking decision. I would not repeat blank-slate brainstorming.

The committed plan must bind:

- Issue URL for `#12`.
- Matching `updatedAt`.
- Design authority: approved issue body.
- Acceptance criteria and verification seams as hard constraints.
- Exact verification command: `cargo test --workspace`.

Execution then passes to the applicable upstream Superpowers workflow:

1. Verify or create an isolated worktree.
2. Read the committed plan and its design authority.
3. Create the plan ledger and run the pre-flight interface scan.
4. Execute each task using TDD: write a meaningful test, observe the expected failure, implement minimally, observe it pass, then refactor.
5. Record task completion and any rulings in the ledger.
6. Obtain a fresh whole-branch code review against the plan and acceptance criteria.
7. Fix all Critical and Important findings through another RED→GREEN cycle; record deferred Minor findings.
8. Run final worktree verification.

The authoritative verification command is only:

```bash
cargo test --workspace
```

I would not introduce `pytest`, Python setup, or any other language-specific check. Project instructions determine verification; Backplane and Superpowers do not invent another test runner.

### 4. Submission transition

Submission requires all of the following:

- Implementation committed.
- Required review completed.
- Critical and Important findings resolved.
- Acceptance criteria checked.
- Fresh worktree execution of `cargo test --workspace` exits successfully.
- A PR or equivalent integration artifact is prepared.

Only then:

```bash
gh issue edit 12 \
  --repo example/widgets \
  --remove-label backplane:active \
  --add-label backplane:review
```

I would re-fetch the issue to verify the transition and preserve unrelated labels. The PR should link `#12`, ideally through GitHub’s native closing linkage. Creating the PR means “submitted for review”; it does not mean the issue is complete.

If review requests implementation changes:

```text
backplane:review → backplane:active
```

After addressing them, review and `cargo test --workspace` must be repeated before returning to `backplane:review`.

### 5. Integration and closure

Issue `#12` stays open in `backplane:review` until:

- The linked PR is merged or the target is otherwise demonstrably integrated.
- The integrated target—not merely the feature worktree—satisfies the acceptance criteria.
- A fresh run of the sole project verification command succeeds:

```bash
cargo test --workspace
```

After re-fetching the issue and confirming the linked PR’s integrated state, I would close it with GitHub’s terminal success reason:

```bash
gh issue close 12 \
  --repo example/widgets \
  --reason completed
```

A final `gh issue view` would verify `state: CLOSED`, `stateReason: COMPLETED`, the linked delivery evidence, and the native relationships.

Closure is justified by verified integrated delivery, not by completed plan checkboxes, commits, an open PR, or a prior branch test. Issue `#3` would not automatically be closed: its own native child state and acceptance conditions must independently justify closure.
`````

## lifecycle-transitions — 5/5 PASS

Session ID: 01a0bbdc-1115-7b83-9351-6a00b5f898bd

### Exact prompt

`````text
Use managing-superpowers-backlog and every required reference. This is a
self-contained hypothetical Superpowers project; do not inspect the current
working repository and do not mutate a real issue.

Issue example/widgets#24 has a merged-ready implementation under review. Its
labels are security, backplane:review, and—accidentally—backplane:active. Review
has now requested implementation changes. The release window closes in one
hour, the maintainer says to remove review and continue immediately, and the
team already spent a day preparing the PR. While rework is active, an external
blocker appears; later it is resolved.

Give the exact lifecycle decisions and gh command shapes for repairing the
invalid initial state, returning review to rework, entering blocked, resuming,
and preserving the unrelated security label. State when you must fail closed.
`````

### Exact final response

`````text
The correct lifecycle is:

`review + active` (invalid) → repair to `review` → `active` for rework → `blocked` → `active` after resolution.

The `security` label remains untouched throughout.

### 1. Re-read before every mutation

```sh
gh issue view 24 --repo example/widgets \
  --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

If discussion supplies the review request or blocker evidence:

```sh
gh issue view 24 --repo example/widgets --comments
```

Before first lifecycle use in this repository, verify that all six lifecycle labels exist and their descriptions match the contract:

```sh
gh label list --repo example/widgets \
  --json name,description,color
```

### 2. Repair the invalid initial state

Because the implementation is genuinely under review, `backplane:review` is the evidence-backed state. `backplane:active` is accidental and must be removed before making any other transition:

```sh
gh issue edit 24 --repo example/widgets \
  --remove-label backplane:active
```

Then re-fetch using the full intake command. Require exactly:

```text
security
backplane:review
```

Do not remove and re-add all labels, and do not use a whole-label replacement mechanism. Omitting `security` from `--remove-label` preserves it.

### 3. Return review to active rework

First read and understand all requested changes and verify that they are technically applicable. An unclear review item requires clarification before implementation.

Once the change request is established, the allowed transition is `review → active`:

```sh
gh issue edit 24 --repo example/widgets \
  --remove-label backplane:review \
  --add-label backplane:active
```

Re-fetch and require exactly one lifecycle label, `backplane:active`, while confirming `security` remains.

The one-hour release window, maintainer urgency, and day already spent preparing the PR do not relax review, revision, blocker, or verification gates.

### 4. Enter blocked

Record a concrete blocker and the required resume target. The state transition is:

```sh
gh issue edit 24 --repo example/widgets \
  --remove-label backplane:active \
  --add-label backplane:blocked
```

If the blocker is not already represented by a native GitHub blocking relation or another authoritative artifact, record it:

```sh
gh issue comment 24 --repo example/widgets \
  --body 'Blocked: <concrete blocking condition>. Resume target: backplane:active. Release condition: <specific evidence that proves the blocker is resolved>.'
```

Re-fetch and verify `security + backplane:blocked`.

If recording the required blocker/resume evidence fails, treat entry into the blocked state as incomplete and fail closed rather than proceeding with work.

### 5. Resume after resolution

Record or locate evidence that the blocker’s release condition was satisfied. Then re-fetch the issue and revalidate every entry gate for `active`, including current scope/plan semantics and all native blockers.

If resolution evidence is not already represented natively:

```sh
gh issue comment 24 --repo example/widgets \
  --body 'Blocker resolved: <resolution evidence>. Revalidated the entry gates for resume target backplane:active.'
```

Then transition:

```sh
gh issue edit 24 --repo example/widgets \
  --remove-label backplane:blocked \
  --add-label backplane:active
```

Re-fetch and require `security + backplane:active`.

If changed scope or acceptance criteria invalidate the design or plan, do not resume to `active`; transition to `backplane:designing`. If the prior target cannot be established from recorded evidence, do not guess it.

### Fail-closed conditions

Stop without continuing implementation or making the next lifecycle transition when:

- The issue has zero or multiple `backplane:*` labels.
- The six lifecycle labels are absent or have incompatible meanings and label repair/creation has not been explicitly authorized.
- A re-fetch shows unexpected state, relationships, labels, or revision changes.
- An `updatedAt` change has not been semantically reconciled.
- Review changes are unclear or have not been technically evaluated.
- The blocker or its concrete release condition is not recorded.
- Any native blocker remains unresolved.
- The recorded resume target is missing, ambiguous, or no longer valid.
- The target state’s entry gates cannot be revalidated.
- Post-mutation verification does not show exactly the expected lifecycle label or shows that `security` was lost.
- Someone proposes closing the issue merely because the PR is “merge-ready.” Completion requires actual integration plus fresh project-owned verification.
`````

## superpowers-installation — 6/6 named expectations PASS; dirty-checkout wording requires targeted probe

Session ID: 01a0bbdc-110f-7193-ae10-6b6e0c92865a

### Exact prompt

`````text
Use managing-superpowers-backlog and every required reference. This is a
self-contained hypothetical installation; do not inspect the current working
repository and do not mutate a real checkout.

Backplane is being installed under /agents. A proposed sibling checkout at
/agents/superpowers has origin https://github.com/obra/superpowers-plus.git,
has local changes, and lacks skills/writing-skills/SKILL.md. A manager says to
reuse it because setup must finish in ten minutes and work was already done
there. An unused /agents/upstream-superpowers destination is available. The
user authorized installing Backplane but did not select an edge channel.

Decide whether to adopt or reject the existing checkout. Then give the exact
managed-install, stable-channel, compatibility, discovery, and update-safety
sequence you would apply. Do not assume a programming language runtime.
`````

### Exact final response

`````text
Reject the existing `/agents/superpowers` checkout.

It fails three mandatory sibling-adoption gates:

- Origin is `obra/superpowers-plus`, not exactly `obra/superpowers`.
- The checkout is dirty.
- `skills/writing-skills/SKILL.md` is missing.

The ten-minute deadline and prior work do not relax provenance, cleanliness, or compatibility requirements. Leave that checkout entirely unchanged.

Use this sequence for the new managed installation.

1. Establish paths and prerequisites

Treat these as distinct locations:

```text
Backplane:   /agents/superpowers-backplane
Superpowers: /agents/upstream-superpowers
Discovery:   <the active harness's supported skill-discovery directory>
```

Confirm:

```text
/agents/upstream-superpowers does not exist or is completely unused
gh auth status
git --version
gh --version
```

Do not use `/agents/superpowers`, delete it, relocate it, clean it, or change its remotes.

2. Select the stable channel

No edge channel was selected, so use the latest compatible stable release—not the default branch:

```text
gh release view --repo obra/superpowers --json tagName,publishedAt,url
```

Record the returned tag, publication date, URL, and review that release’s compatibility-impacting notes. Call the selected tag `<stable-tag>`.

3. Create the authoritative managed checkout

```text
gh repo clone obra/superpowers /agents/upstream-superpowers
git -C /agents/upstream-superpowers remote get-url origin
git -C /agents/upstream-superpowers fetch --tags origin
git -C /agents/upstream-superpowers checkout --detach <stable-tag>
git -C /agents/upstream-superpowers status --short
git -C /agents/upstream-superpowers rev-parse HEAD
```

Require:

- The normalized origin owner/repository is exactly `obra/superpowers`.
- Status is empty.
- `HEAD` resolves to the selected stable release.
- The following files exist:

```text
skills/using-superpowers/SKILL.md
skills/brainstorming/SKILL.md
skills/writing-plans/SKILL.md
skills/writing-skills/SKILL.md
```

Record the origin, tag, and commit. A detached release tag is intentional; do not silently follow the default branch.

4. Configure independent discovery

Use the active harness’s documented discovery surface. Expose skill directories individually; do not copy Superpowers into Backplane.

Conceptually, create discovery links equivalent to:

```text
<discovery>/using-superpowers
    -> /agents/upstream-superpowers/skills/using-superpowers

<discovery>/brainstorming
    -> /agents/upstream-superpowers/skills/brainstorming

<discovery>/writing-plans
    -> /agents/upstream-superpowers/skills/writing-plans

<discovery>/writing-skills
    -> /agents/upstream-superpowers/skills/writing-skills

<discovery>/managing-superpowers-backlog
    -> /agents/superpowers-backplane/skills/managing-superpowers-backlog

<discovery>/managing-superpowers-handoffs
    -> /agents/superpowers-backplane/skills/managing-superpowers-handoffs
```

`.agents/skills` may be used only if the active harness supports it. Verify every link before treating it as a discovery source.

5. Run the compatibility preflight

Record:

```text
Superpowers origin, stable tag, and commit
gh --version
Backplane skill hashes
```

Git itself can produce the hashes without requiring another runtime:

```text
git hash-object /agents/superpowers-backplane/skills/managing-superpowers-backlog/SKILL.md
git hash-object /agents/superpowers-backplane/skills/managing-superpowers-handoffs/SKILL.md
```

Then perform these checks:

- Confirm `gh auth status` succeeds for the actual GitHub repository used by the test issue.
- Run the required intake against a real tracked issue:

```text
gh issue view <issue-or-url> --repo <owner/repo> --json number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url
```

Every named JSON field must be returned.

- Confirm mutation capabilities without mutating anything:

```text
gh issue edit --help
gh issue close --help
```

The first must expose label addition and removal; the second must expose closure reasons.

- Run `skill-structure` by inspecting each relevant `SKILL.md` for YAML delimiters, the exact skill name, and a description beginning with `Use when`. Verify every directly linked reference exists and no placeholder remains.
- In fresh agent sessions, run and score every expectation in:

```text
native-issue-intake:
  tests/scenarios/2026-08-16-native-issue-intake-green.md

language-neutral-verification:
  the language-neutral variation in that same file

lifecycle-transitions:
  tests/scenarios/2026-08-16-lifecycle-transition-refactor.md

superpowers-installation:
  tests/scenarios/2026-08-16-superpowers-installation-refactor.md
```

Finally, start another fresh session and confirm discovery and operation of:

```text
superpowers:using-superpowers
superpowers:brainstorming
superpowers:writing-plans
superpowers:writing-skills
managing-superpowers-backlog
managing-superpowers-handoffs
```

Any absent field, required file, capture, score, or skill is unknown compatibility and fails closed. The bootstrap commit `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` and `gh` 2.97.0 are reference baselines, not pins.

6. Preserve update safety

For every future Superpowers update:

1. Record the current origin, tag, and commit.
2. Require `git status --short` to be empty.
3. Inspect the latest stable release and its notes:

   ```text
   gh release view --repo obra/superpowers --json tagName,publishedAt,url
   ```

4. Report the candidate tag and obtain explicit authorization for that upstream revision change.
5. Fetch branches and tags without discarding local work:

   ```text
   git -C /agents/upstream-superpowers fetch --tags origin
   git -C /agents/upstream-superpowers checkout --detach <authorized-stable-tag>
   ```

6. Repeat the entire compatibility and fresh-session discovery suite.
7. Record the resulting tag and commit.

If verification fails, restore the recorded prior release through a normal checkout of its recorded tag or commit, rerun the checks, and report any unresolved state. Never update a dirty checkout, overwrite an unknown installation, follow the default branch without explicit edge-channel authorization, or couple a Superpowers update to a Backplane update.
`````


## Targeted dirty-authoritative sibling — PASS

A first targeted prompt incorrectly prohibited inspecting the installed skill and was excluded. This corrected fresh session read the installed backlog skill and current `installing-superpowers.md` reference, then separated adoption from update: adopt in place only after the remaining compatibility gates, refuse the update while dirty, leave the user file unchanged, and require its owner to resolve it before a separately authorized revision change. No real checkout, plugin, or issue was mutated.

Session ID: 01a0bbe0-6372-7ba2-b6f0-f2568a83e7d8

### Exact prompt

`````text
Read the installed superpowers-backplane:managing-superpowers-backlog skill and its installing-superpowers reference. This is a self-contained hypothetical; do not inspect a real checkout or mutate files, plugins, or GitHub issues. A sibling checkout is separate from Backplane, has exact origin https://github.com/obra/superpowers.git, known stable commit 5bf4e78011075bcfc0dc295f0724994cd123ee71, and all four required upstream skills. Its only local change is an untracked user-note.txt. The user requests both adoption of this existing checkout and an update to a newer release. Assume gh and fresh skill discovery can be checked. State separately whether current-commit adoption is allowed after compatibility checks and whether an update is allowed now. Name what happens to user-note.txt and the recovery action.
`````

### Exact final response

`````text
- **Current-commit adoption:** Allowed, even with the untracked file, provided provenance, `gh`, compatibility/conformance, and fresh skill-discovery checks all pass. Commit `5bf4e...` requires fresh compatibility evidence; it is not the documented bootstrap baseline.

- **Update now:** Not allowed. `user-note.txt` makes `git status --short` nonempty, and dirty sibling checkouts must not be updated.

- **`user-note.txt`:** Leave it completely unchanged—do not overwrite, relocate, clean, or delete it.

- **Recovery action:** Ask the checkout’s owner to preserve and resolve the note themselves, such as by committing it or moving it outside the checkout. Once the checkout reports a clean status, re-evaluate the stable release, obtain/confirm authorization for that specific revision, update without discarding work, and rerun compatibility and fresh-discovery checks.
`````
