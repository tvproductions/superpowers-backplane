# Local tooling refresh — October 31, 2026

The operator approved the preceding freshness-review recommendations with
“yes update those.” Work starts at `0dabbc0327b8dcc7e472b7a5781cb5ce660a225f`
on `main` in the standalone repository. The tree was clean before maintenance.
This report and its [command receipt](2026-10-31-tooling-refresh.json) describe
local execution, not publication or new host acceptance.

## Selected versions and reproducibility

| Surface | Before | After / decision |
| --- | --- | --- |
| Python exact pin | 3.14.9 | 3.14.10; retain the approved 3.14 family |
| Local `.venv` | Absent on this Mac | uv-managed CPython 3.14.10, no system site packages |
| Project Ruff | No local environment | 0.17.3 |
| Project ty | No local environment | 0.0.95 |
| Machine uv | 0.13.6 | Retain; latest stable at check time |
| Machine Ruff / ty | 0.17.3 / 0.0.93 | Unchanged; project commands resolve local tools |
| Superpowers | 7.0.1 at `2ce8aa15` | Retain; current stable |
| gz-skills | 0.8.3 at `d6acc26e` | Retain all three project harness configurations; current release |

Provisioning used:

```text
uv venv --managed-python --python 3.14.10 .venv
uv python pin 3.14.10
uv pip install --python .venv ruff==0.17.3 ty==0.0.95
```

The last command was repeated and checked two already-installed packages with
no changes. Run tools through `uv run --no-project`; the interpreter's observed
prefix is this repository's `.venv`, and its base prefix is uv's managed
`cpython-3.14.10-macos-aarch64-none`. `.venv` remains ignored. The receipt retains
exact versions and reproduction commands; this does not introduce a package,
manifest, lockfile or selected gz-skills profile. There are no repository-managed
runtime dependency groups, containers, CI actions or hook versions to update.
Git, gh and native agent hosts remain independently managed prerequisites.

## Verification and limits

- Python pin, actual interpreter and environment agree at 3.14.10.
- `uv pip check --python .venv` passes; `uv pip list --python .venv --outdated
  --format json` returns an empty list. Only Ruff and ty are installed.
- All nine Python blocks in the current Claude guide parse under 3.14.10.
  ty 0.0.95 checks their combined code without errors.
- Five plugin/settings JSON manifests parse. Native
  `claude plugin validate . --strict --json` succeeds with no manifest errors
  or warnings. Its separate directory-listing findings identify an existing
  missing license and icon; no directory-submission acceptance is claimed.
- Supplemental Ruff lint and format checks on the extracted guide code fail:
  I001 import ordering and existing formatting. The guide bytes equal the
  pre-update HEAD, with the hash recorded in the receipt. These findings were
  discovered by this refresh; the previous host's evidence is preserved and
  is not asserted to reproduce under these current checks. No rule was disabled
  and no guide code was reformatted. A fully passing guide quality gate is not
  claimed.
- Final whitespace, changed-document links and receipt parsing are checked
  separately before delivery. No behavioral or native installation/lifecycle
  replay is claimed. The Windows issue-11/19 helper fixtures are not present
  on this host. No vulnerability audit is configured or performed.

The Python patch contains security and maintenance fixes; no new language API
or code modernization is needed for this environment update. Python 3.15.2 is
the newer upstream family, left outside the approved 3.14 selection. Historic
runtime and acceptance records remain unchanged at their original identities.

## Policy source reconciliation

The [release binding](../../docs/release-policy.md) records the exact source
review and applicability decisions. Starter `v0.7.1` resolves to
`27594dbaec853e6bde037b0aaf3f0427a3f053f9`; reviewed main is
`fc9cdd2b671f7af7e45fddaa1ac2739c75bb2281`, rechecked unchanged. The receipt
hashes six reviewed inputs. Compared with prior reviewed source `35ac0578`,
the source permits optional scheduled dependency scanning without requiring its
adoption. No schedule is added. Its new direct Git/gh guidance is unreleased;
AGENTS explicitly adopts that guidance while preserving Backplane's existing
Python execution command. SemVer, major PRDs and workflow ownership remain
consistent. The starter bundle and its cognitive-engine exception are not
adopted, and no formal starter conformance is claimed.

## Authoritative freshness sources

- [Python 3.14.10 release notes](https://www.python.org/downloads/release/python-31410/)
- [Python 3.15.2 release notes](https://www.python.org/downloads/release/python-3152/)
- [uv 0.13.6](https://github.com/astral-sh/uv/releases/tag/0.13.6)
- [Ruff 0.17.3](https://github.com/astral-sh/ruff/releases/tag/0.17.3)
- [ty 0.0.95](https://github.com/astral-sh/ty/releases/tag/0.0.95)
- [Superpowers 7.0.1](https://github.com/obra/superpowers/releases/tag/v7.0.1)
- [gz-skills 0.8.3](https://github.com/tvproductions/gz-skills/releases/tag/v0.8.3)
- [Starter 0.7.1](https://github.com/tvproductions/gz-skills-first-starter/releases/tag/v0.7.1)

Versions were queried from official release metadata with gh and Python's
release pages. Annotated plugin/starter tags were resolved to their commit
objects. No commit, push, tag, release, normal-profile tool update or installed
plugin-cache modification is part of this maintenance.
