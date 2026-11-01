# Remaining OpenCode acceptance probe contract

**Status:** Proposed execution detail for review with the five issue plans. The
approved adoption and host-leaf rescope specifications remain design authority.
This document supplies test interfaces, not another backlog or lifecycle.

## Fixed inputs and ownership

- Source baseline: standalone main `34c59af8164be3a8516f7750c0b98e0fff48e405`.
- Existing authenticated test profiles: `.sp-bp/work/issue-20/profiles/v1` and
  `v2`. Verify ownership, effective configuration, native auth and model catalog
  before reuse. Authentication is never copied; no normal host profile fallback.
- Selected binaries: retained verified V1 1.18.31 and V2 2.1.4. Floors remain
  V1 1.18.29 and V2 2.0.4. Record absolute executable paths, versions and hashes.
- Upstream baseline: independent stable 7.0.1 at
  `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`. Never modify its installation.
  An absent-upstream fixture may obtain a separately installed stable copy
  through the current documented host channel after checking that channel.
- Each issue owns `.sp-bp/work/issue-N/`, its ledger, fixtures, captures and
  helper copies. Restore prior configuration after a case. Read earlier helpers
  from tracked transcripts, not by executing another task's working script.
- Start from tracked corrected
  `tests/scenarios/transcripts/2026-11-01-issue-20-unblock-host-smoke.py.txt` and
  its matching receipt tests. Parameterize root, worktree, profile, output and
  expected upstream instead of retaining its old hardcoded worktree/source.
- New guide: `docs/installing-opencode.md` retains one entry point, with separate
  V1/V2 setup and operation sections. Do not duplicate canonical skill text.
- Use Git/gh directly for routine operations. Owned processing uses managed
  Python 3.14 through `uv run --no-project python`, Ruff and ty; no new consumer
  runtime or test-framework requirement.

## Isolation and native command vectors

Validate canonical workspace registration/shared Git directory before project
mutations. Verify canonical containment, ignore coverage and empty/known contents
before fixture creation. Record each fixture root, origin, starting revision and
purpose; use `git clone --no-hardlinks` without alternates for local sources.

Use the corrected #20 child environment contract: isolate HOME/USERPROFILE,
APPDATA/LOCALAPPDATA/ProgramData, XDG config/data/cache/state, all temporary
roots and OPENCODE_CONFIG_DIR; strip inherited OPENCODE_* pointers first. Keep
V1's owned short cache and V2's isolated-global-config cwd to prevent ancestor
skill discovery. Reuse only host-supported existing authentication paths. If gh
needs an explicit GH_CONFIG_DIR in the isolated child, establish that it is the
already authorized gh store and set the pointer for that child; do not copy it.

Retain the verified actual native vectors (absolute verified executable first):

```text
V1: --version
V1: debug paths
V1: debug config
V1: debug skill
V1: auth list
V1: run --format json --model <verified-authenticated-model> <case-prompt>
V2: --version
V2: debug paths
V2: auth list
V2: run --standalone --format json --model <verified-authenticated-model> <case-prompt>
```

For V2 inventories, start one owned loopback private server with an ephemeral
password, wait for the expected plugins/skills in that same server/location and
query `/api/config`, `/api/plugin`, `/api/skill`. Never attach to the normal
background service. Do not persist the password. Preserve actual V1 `input.name`
and V2 `input.id` tool results; successful process exit alone proves no load.
Check current primary host docs and installed help before adding command flags.

## Reusable receipt and scoring interface

Each issue creates owned `acceptance.py` and `test_acceptance.py`; their source
is retained as `tests/scenarios/transcripts/2026-11-01-issue-N-*.py.txt`.
The CLI is:

```text
uv run --no-project python .sp-bp/work/issue-N/acceptance.py preflight
uv run --no-project python .sp-bp/work/issue-N/acceptance.py run --case <case-id>
uv run --no-project python .sp-bp/work/issue-N/acceptance.py verify <receipt-path>
```

Expose `classify(row: dict[str, object]) -> str`, returning FAIL for an observed
false required check, UNKNOWN for absent/unverified required evidence, otherwise
PASS. Required row fields: id, variant, case, native/synthetic classification,
host executable/version/hash, candidate/prior/restored source SHA as applicable,
installed package root and file-blob comparisons, upstream origin/version/commit,
effective configuration sources, authenticated model identity, exact command
vectors and exit statuses, actual tool-call/result identities, capture hashes,
before/after protected snapshots, result and recovery action when applicable.
Keep whole raw streams ignored; retain screened successful results as well as
errors, rather than leaving load proof solely in ignored scratch.

Before implementing the scorer, unittest assertions must fail for: missing
required fields, truncated native connections, synthetic evidence presented as
mandatory native acceptance, source outside the installed cache, duplicate
Backplane, nonzero native result/timeout, wrong restored SHA, missing positive
tool results, changed unrelated files/plugins, unknown provenance, unsupported
version reported as supported, and failing evidence hidden by a missing field.
The complete positive record must pass. Test the child-root mapping on Windows
case-insensitive inherited environment names and POSIX names. Do not claim a
live case passed because only these processing tests passed.

## Setup case set: #21 V1 and #23 V2

Run S-native (existing authoritative native upstream package), S-sibling
(separately verified compatible checkout) and S-absent (no upstream at baseline,
actual stable installation by the setup workflow, then restart). In each case,
run the exact documented setup request with the target repository/issue for
read-only intake, followed by fresh native three-skill loads. Capture all 15
native issue fields, gh authentication, label flags and closure-reason support.

Run separate preserved-state cases: F-lookalike, F-versionless,
F-duplicate, F-dirty-adopt, F-dirty-update, F-collision, F-gh-auth,
F-gh-intake, F-gh-label, F-gh-close, F-missing-skill, F-incompatible,
F-below-floor, F-unauthenticated. Dirty authoritative adoption may pass without
update; dirty update must refuse. Every refusal names its specific failed check
and safe recovery action. Use independently owned copies for deliberately dirty
or malformed upstream. Never edit shipped upstream or credential stores.

Exercise below-floor with an actual verified below-floor host binary in its
own fixture; a shimmed version string is supplementary synthetic evidence only.
If an intended native condition cannot be constructed, record UNKNOWN and leave
the owning issue incomplete. Capture before failure and immediately after,
before repair. Restore only the exact owned fixture after the comparison.

## Lifecycle case set: #22 V1 and #24 V2

L-install, L-repeat, L-update, L-rollback, L-unavailable-source,
L-failed-verification-recovery, L-uninstall and L-test-restore are separate rows.
Use exact reviewed full SHAs, record native resolved source and compare all
installed package files at every applicable stage. Native configuration uses
singular `plugin` in V1 and plural `plugins` in V2. Remove only Backplane's entry;
upstream, a nontrivial unrelated plugin sentinel, user files and issues survive.
Restart and load all three actual skills after installation/repeat/update/
rollback/restoration; after removal require Backplane absent and upstream
loadable. Snapshot failed-candidate state before restoring and prove the exact
last verified installation afterward. Updating only a local directory is not
hosted Git-package update evidence.

Score five named checks separately: skill-structure, native-issue-intake,
language-neutral-verification, lifecycle-transitions, superpowers-installation.
Retain their governing rubrics; language-neutral responses use the consuming
project's commands, never Backplane's Python tools as adopter requirements.

Use one useful remote documentation fixture per variant, proposed exact titles
`Verify OpenCode V1 adopter operation evidence links` and
`Verify OpenCode V2 adopter operation evidence links`. Each contributes the
reviewed variant guide/evidence links. Before creation obtain explicit operator
approval for its proposed body/title and native lifecycle; plan approval alone
does not invent an existing fixture issue number. Never reopen #34 or use a
production issue as an unapproved experiment. Capture status/selection with zero
mutation, then designing/ready/active/blocked/resume/review/rework/submission and
completed closure with unrelated `documentation` preserved. Completion requires
actual accepted integration and fresh checks. Keep V1 and V2 observations
separate; historical #34 evidence can supplement but cannot replace a missing
required native host observation.

## Final gate, review and publication

Every owning issue stores a readable assessment and JSON receipt under
`tests/scenarios/2026-11-01-issue-N-opencode-acceptance.*`. Map every exact current
criterion and seam; any applicable FAIL or UNKNOWN blocks SATISFIED. Run:

```text
node --test tests/opencode-adapter.test.mjs
uv run --no-project python -m unittest discover -s .sp-bp/work/issue-N -p test_acceptance.py -v
uv run --no-project python .sp-bp/work/issue-N/acceptance.py verify tests/scenarios/2026-11-01-issue-N-opencode-acceptance.json
uv run --no-project ruff check .sp-bp/work/issue-N/acceptance.py .sp-bp/work/issue-N/test_acceptance.py
uv run --no-project ruff format --check .sp-bp/work/issue-N/acceptance.py .sp-bp/work/issue-N/test_acceptance.py
uv run --no-project ty check .sp-bp/work/issue-N/acceptance.py .sp-bp/work/issue-N/test_acceptance.py
git diff --check
```

Compile guide Python and parse PowerShell blocks, verify links/source blobs and
whole native before/after snapshots. Obtain one fresh whole-change review; fix
material findings in one demonstrated RED/GREEN pass and rerun affected/full
gates. User-facing source changes use an isolated native worktree. Publication,
integration and exact remote fixture mutations retain their explicit authority
gates. After authorized publication install the exact hosted delivery, verify
file identities and native loads, publish/link SATISFIED evidence and close only
the accepted owning issue with full native revision/graph guards. No release,
pilot #6 completion or unrelated cleanup is included.
