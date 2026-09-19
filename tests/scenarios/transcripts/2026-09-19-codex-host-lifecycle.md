# Codex Host Lifecycle Evidence

**Work item:** issue #3. **Status:** in progress; fresh Codex agent-session checks await authentication of the disposable profiles. These CLI checks do not by themselves prove skill discovery in a new session.

## Fixture identity

- Host: Windows PowerShell 7.6.6, `codex-cli 0.155.1`, `gh` 2.101.0.
- Fixture root: `C:\Users\Jeff\AppData\Local\Temp\backplane-codex-579301d7b6a249e69e38628a9806b287`.
- Source: `git archive` of committed Backplane `6c26f0354b0bf231172a13327e2dc898b8b772b5` (package commit `8bfba888599568cc8f729ba6f0c030ace8e6377f`).
- The archive contains root `plugin.json`, `.agents/plugins/marketplace.json`, and the canonical `skills/`; it contains no `.git`, `.agents/superpowers`, or `.agents/skills` discovery junction.
- `CODEX_HOME` was set only in child PowerShell commands to fixture-specific state directories. A new state listed zero marketplaces. The user profile was not changed.
- Backplane backlog `SKILL.md` SHA-256: `739A16FCDF2EE5ADAB0514F5A44DB0629DCCE558985FE5A31D71DD2606AC1E81`.
- Backplane handoffs `SKILL.md` SHA-256: `A6052755128BE9C7D268D71241DD389B9BF1C720834E47E61CBF9535F4CA92DE`.
- Upstream `using-superpowers/SKILL.md` SHA-256: `82C5C8866AD7F5DD4440CE66BD7806BA48A2F13771BEAE5CF112E53F08FE36BA`.
- Backplane `plugin.json` SHA-256 at `0.1.0`: `BCD8B9203F102392D3DF62193F74D7040D6386537439560F96BF9E5AB381003E`.

## Observed local package lifecycle

| Probe | Command and observation | Result |
|---|---|---|
| Register local source | `codex plugin marketplace add <fixture project> --json` returned `marketplaceName=superpowers-backplane`, `alreadyAdded=false`. | PASS |
| Install unrelated sentinel | `codex plugin add backplane-preservation-sentinel@superpowers-backplane --json` installed version `0.0.1`. | PASS |
| Clean Backplane install | `codex plugin add superpowers-backplane@superpowers-backplane --json` installed version `0.1.0` in its own cache. | PASS |
| Repeat install | Repeating the same `plugin add` returned the same ID and version; `plugin list --json` still showed exactly one Backplane and one sentinel. | PASS |
| Fixture version change | Changing only the fixture manifest version to `0.1.1` and rerunning `plugin add` selected `0.1.1`. Candidate manifest SHA-256: `77644DE63A70E71D41CA00095215A8FAF75A868D30B23C530626579F04E016BD`. | PASS |
| Fixture rollback | Restoring the saved `0.1.0` manifest and rerunning `plugin add` restored installed version `0.1.0`; sentinel, marketplace, and user-file hashes were unchanged. | PASS |
| Backplane-only removal | `codex plugin remove superpowers-backplane@superpowers-backplane --json` left zero installed Backplane plugins, one sentinel, and the shared marketplace configured. | PASS |

Sentinel manifest SHA-256 stayed `D8A5155E915669EB5578C30953447FF3D3E56DEEEFC1D7BCC3216FB7158272F9`; shared marketplace SHA-256 stayed `2FEA8CD099346C6378038CB604352E5B5BAE8DCFC5E78C8AC686982071E51749`; unrelated `user-notes.txt` SHA-256 stayed `ED2EC7AEE9F5FEDAEF6BE63FAD983C2AE74745C76AF399FF0973FFACA7FB8728`.

## Separate upstream modes

- **Native:** `state-native` installed Backplane `0.1.0`, sentinel `0.0.1`, and authoritative `superpowers@superpowers-dev` `6.4.1` from `https://github.com/obra/superpowers.git` pinned at `v6.4.1`. Its required installed skill hashes matched the separate source trees.
- **Sibling:** `state-sibling` installed Backplane and sentinel only. `project-sibling/.agents/skills/superpowers` is a fixture junction to the independently identified `obra/superpowers` checkout at `5bf4e78011075bcfc0dc295f0724994cd123ee71`; required skill hashes matched.
- **Absent then installed:** `state-absent` began with no upstream package, then installed the authoritative Git marketplace at stable tag `v6.4.1`; Backplane, sentinel, and upstream remained separate. The current upstream release query returned `v6.4.1`.
- All three modes passed installed-file identity checks. Fresh agent-session discovery and setup decisions remain `UNKNOWN` until a disposable Codex profile is authenticated.

## Git marketplace ref mechanism (host proxy)

- A separate disposable profile installed authoritative Superpowers `v6.3.0`, then attempted `codex plugin marketplace add obra/superpowers --ref v6.4.1`. Codex rejected the changed source with: `marketplace 'superpowers-dev' is already added from a different source; remove it before adding this source`. The prior installation and ref stayed intact.
- `codex plugin marketplace remove superpowers-dev`, `codex plugin marketplace add obra/superpowers --ref v6.4.1`, then `codex plugin add superpowers@superpowers-dev` selected version `6.4.1`. Repeating remove/add/install with `--ref v6.3.0` restored `6.3.0`.
- In a shared local marketplace fixture, removing the marketplace made both Backplane and the unrelated sentinel absent from `plugin list`; readding the unchanged source restored both installed entries and their enabled configuration. A Backplane remote two-ref check remains for final integrated verification.

## Host limitation

- `Start-Process` with redirected stdout failed with `stdout is not a terminal`; process-scoped `CODEX_HOME` and direct `codex` invocation worked. Codex also warned that it would not create PATH aliases under the OS temp directory, while plugin commands completed successfully.
- Disposable profiles report `Not logged in`; the normal user profile reports ChatGPT login. No credential was copied into a fixture. Fresh `codex exec` checks remain pending.

## Published Backplane ref probe on the approved feature branch

- The user approved pushing `feat/codex-installation-surface`; GitHub returned exact published commits `8bfba888599568cc8f729ba6f0c030ace8e6377f` and `6c26f0354b0bf231172a13327e2dc898b8b772b5`. The branch was not merged or released.
- In fresh `state-remote`, `codex plugin marketplace add tvproductions/superpowers-backplane --ref 8bfba888599568cc8f729ba6f0c030ace8e6377f` plus `plugin add` installed Backplane `0.1.0`. The checkout `git rev-parse HEAD` and fixture config both held that SHA. The later guide file was absent.
- Removing only the Backplane marketplace, adding ref `6c26f0354b0bf231172a13327e2dc898b8b772b5`, and running `plugin add` changed the checkout and installed cache: `docs/installing-codex.md` appeared in both despite the unchanged declared `0.1.0` package version.
- Repeating remove/add/install with the first SHA restored its checkout and cache contents: `docs/installing-codex.md` disappeared from both. `plugin remove superpowers-backplane@superpowers-backplane` then left no Backplane installation.
- A second fresh `state-guide` ran the exact four lifecycle PowerShell blocks in `docs/installing-codex.md` after seeding the first SHA. Preflight, candidate switch, rollback, and uninstall all exited successfully; Git HEAD matched the candidate and prior SHA at the respective checkpoints. These two commits test immutable ref handling and cache replacement; they do not represent two released package versions.

## Authentication limitation

- An attempted isolated `codex login --device-auth` displayed a device code, but the account browser page reported that device-code authorization is disabled in ChatGPT security settings. The login process was canceled.
- A subsequent regular `codex login` opened a local browser callback on `localhost:1455`, but no authorization completed; that process was canceled after the user raised concerns about the session. No account setting or normal Codex profile was changed. Fresh agent-session checks remain UNKNOWN.

## Direct preservation run of the written guide

- A short-path disposable profile `sp` started with three installed IDs: `backplane-preservation-sentinel@preservation-probe`, `superpowers-backplane@superpowers-backplane`, and `superpowers@superpowers-dev` at upstream v6.4.1. The sentinel used a separate local marketplace; upstream used the authoritative Git marketplace.
- The exact guide preflight, candidate, rollback, and Backplane-only removal PowerShell blocks ran successfully. Installed counts were 3 after candidate, 3 after rollback, and 2 after removal. The remaining IDs were the sentinel and upstream Superpowers.
- SHA-256 values of the sentinel manifest, upstream `using-superpowers/SKILL.md`, and a fixture user note were equal before and after the sequence. The sentinel manifest remained `D8A5155E915669EB5578C30953447FF3D3E56DEEEFC1D7BCC3216FB7158272F9`; upstream skill remained `82C5C8866AD7F5DD4440CE66BD7806BA48A2F13771BEAE5CF112E53F08FE36BA`.
- A first attempt using deeper `state-preserve-guide` failed while Codex cloned upstream because Git on Windows could not check out `docs/superpowers/specs/2026-06-11-visual-companion-final-hardening-fixup-design.md` (`Filename too long`). The shorter `sp` state passed; this is a disposable profile path-length constraint, not evidence that upstream setup succeeded in an agent session.

## Junction probe excluded from acceptance

- Prompt to a new `codex exec --ephemeral --sandbox read-only` session in a disposable project: `Read-only discovery check. Report whether you can discover the skills superpowers:using-superpowers, managing-superpowers-backlog, and managing-superpowers-handoffs in this fresh Codex session. For each, give its resolved SKILL.md path or UNKNOWN. Do not modify files or GitHub issues.`
- The disposable project linked `.agents/skills` to Backplane `0.1.0` and upstream Superpowers `6.4.1` files in the isolated plugin caches. The session used the already authenticated normal Codex profile only for model access; it did not change that profile's plugin configuration.
- The response identified paths through junctions created specifically for this probe. Its first shell command failed with `helper_sandbox_lock_failed`; a later shell retry completed under different sandbox permissions. This transcript does not establish who approved that retry.
- Acceptance score: INVALID for issue #3 native plugin discovery. Listing test-created junctions does not demonstrate that a newly installed Codex plugin exposes its skills in an authenticated isolated profile. That required check remains UNKNOWN. The response is retained below solely to explain why this probe was excluded.

Exact final response from that limited discovery probe:

All three skills are discoverable:

| Skill | Resolved `SKILL.md` path |
|---|---|
| `superpowers:using-superpowers` | [SKILL.md](<C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/session-project/.agents/skills/superpowers/using-superpowers/SKILL.md>) |
| `managing-superpowers-backlog` | [SKILL.md](<C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/session-project/.agents/skills/managing-superpowers-backlog/SKILL.md>) |
| `managing-superpowers-handoffs` | [SKILL.md](<C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/session-project/.agents/skills/managing-superpowers-handoffs/SKILL.md>) |

No files or GitHub issues were modified.
