# Windows Superpowers 7.0.1 maintenance verification

## Authority and exact update

The operator explicitly requested: “first, update to 7.0.1”. This authorizes
the independent upstream update; it does not publish Backplane, integrate a PR,
or create a release. The repository's existing `SUPERPOWERS.md` already recorded
7.0.1 from another host; this maintenance reconciles the actual Windows checkout.

- Prior: v7.0.0, `bb92a77741419a4ab5f06e711a283343f1ada0c3`.
- Selected and latest stable observed through gh: v7.0.1, published
  `2026-10-21T21:05:11Z`, target `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`.
- Authoritative source: `https://github.com/obra/superpowers.git`.
- Backplane root: `U:/repos/agents/superpowers-backplane`. Its exact root and
  the independent upstream root/origin/clean state were checked before mutation.
- Native Git fetch used the gh credential helper, with process-only overrides;
  no persistent Git configuration changed. The fetched annotated tag peeled to
  the expected commit before detached checkout. HEAD and exact local tag now
  match 7.0.1, with empty porcelain status.
- The `.agents/skills/superpowers` discovery junction resolves to the same new
  commit. No upstream file was patched or used to hold Backplane artifacts.
- The disposable Claude profile's separate `superpowers@superpowers-dev`
  registration was natively updated to 7.0.1 at the same commit and source.
  Backplane and every unrelated plugin were preserved across this explicit
  upstream update. No normal Claude profile was changed.

The release notes were read with gh. Changes retune brainstorming and move long
skill guidance into references; the execution skill's difference removes its
duplicated example without changing the execution gates. Required upstream skills
remain present. This maintenance does not select the edge channel.

## Fresh checks and affected seam replay

The four original scenario prompts ran in separate fresh Claude sessions with
only Skill/Read tools. Full responses were read and manually scored against
all original expectations:

| Named check | Result |
|---|---|
| skill-structure | PASS: both B skills, metadata/source checks and all ten relative links |
| native-issue-intake | PASS 6/6 |
| language-neutral-verification | PASS 5/5 |
| lifecycle-transitions | PASS 6/6 |
| superpowers-installation | PASS 6/6 |

The exact nine Python lifecycle-guide blocks were also replayed with 7.0.1:
repeat-install, B→F update, F→B rollback, unavailable-source rejection,
Backplane-only uninstall and B restoration. Ten immediate snapshots verify
installed source bytes and preservation. Five fresh Claude discovery sessions
observe actual skill loads after the applicable operations, and native Backplane
absence plus upstream availability after uninstall. B is restored at the end.

B remains `b0d702f8821d6d29184118410ec6ff2d8fb63438`; fixture F remains
`5e01704fcdda13eefeeac52d8892da26e7164ffd`. The fixture's 0.1.1 is test-only.
All 21 installed source blobs match their selected B/F trees. Upstream 7.0.1,
unrelated plugin identities, normal-profile hashes, user sentinel, root refs and
complete #19 state remain unchanged throughout the Backplane operation replay.
Intentional prior branch commits and the separately authorized upstream input
change are recorded independently, never normalized away as package preservation.

Portable Python orchestration ran through uv with Python 3.13.14; Ruff and ty
checks pass. The separate-output regression first failed at assertion level and
then passed with the other four regression checks. This keeps 7.0.1 captures in
a separate directory while using the same explicitly selected disposable profile
and catalog. An initial comparison against older initial-install timestamps was
rejected; the immediately preceding pre-update snapshot proved the actual
Backplane registration was unchanged and supplied the correct phase anchor.

## Evidence and applicability

- `tests/scenarios/2026-10-25-windows-superpowers-v7.0.1.json` retains the exact
  source identities, authorized old/new input transition, upstream skill hashes,
  link targets, per-expectation scores, native snapshots and discovery records.
- `tests/scenarios/transcripts/2026-10-25-windows-superpowers-v7.0.1.md` retains
  the exact prompts, actual tool calls, unedited responses and native guide replay.
- Earlier 7.0.0 lifecycle/conformance/fixture records remain at their original
  identities. These new results do not rewrite those events as 7.0.1 executions.

Observed scope is Windows and fresh Claude sessions. The current Codex discovery
link and required source files resolve to 7.0.1, but an additional fresh Codex
model probe was rejected by automatic approval review before execution because
the separate Codex skill-text transfer was not explicitly approved. No bypass or
retry occurred. No fresh Codex, macOS/Linux, other-harness or complete-stack pass
is claimed here.

#19 remains OPEN/active; #34 remains OPEN/blocked on its separately presented
publication/integration gate. The upstream update does not release Backplane or
complete its adoption arc. A gh release listing observed no published Backplane
release; useful guide/policy/evidence changes are intended content for the initial
0.1.0 release, subject to its remaining acceptance and release gates.
