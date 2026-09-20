# Codex integrated remote pinned-ref verification

Issue #3, PR #14, and the approved plan's Task 4 Step 4. PR #14 merged into main at 40b7df7ec8ff477972ae2b9a8f87bdea0a0fb119. The first root-package commit is 8bfba888599568cc8f729ba6f0c030ace8e6377f. Both full SHAs resolved through gh api at the expected origin, https://github.com/tvproductions/superpowers-backplane.git. The reviewed feature head a060c82eed375d863e10432487010a2e3d6c007c is an ancestor of the merge commit, and the merge changed no package source files.

Host: Windows PowerShell, Codex CLI 0.155.1, gh 2.101.0. The existing authenticated disposable CODEX_HOME was C:\Users\Jeff\AppData\Local\Temp\backplane-codex-579301d7b6a249e69e38628a9806b287\state-native. The normal user profile was untouched, no credentials were copied, and no new login occurred. Fresh sessions used an empty consumer-remote directory, codex exec --ephemeral --approve-for-me --skip-git-repo-check, and installed plugin caches rather than repository junctions.

## Exact operation sequence and score

1. Remove only the disposable Backplane marketplace, add tvproductions/superpowers-backplane --ref 8bfba888599568cc8f729ba6f0c030ace8e6377f, add superpowers-backplane@superpowers-backplane, and run a fresh read-only discovery session: PASS.
2. Replace that marketplace with --ref 40b7df7ec8ff477972ae2b9a8f87bdea0a0fb119, add the same plugin ID, and run a fresh read-only discovery session: PASS.
3. Replace that marketplace with --ref 8bfba888599568cc8f729ba6f0c030ace8e6377f, add the same plugin ID, and run a fresh read-only discovery session: PASS.
4. Remove only superpowers-backplane@superpowers-backplane and run an extra fresh removal session. Native plugin list had only upstream among the scoped IDs; the fresh session found upstream using-superpowers and no Backplane SKILL.md. The session incorrectly called the unrelated backplane-preservation-sentinel@superpowers-backplane configuration a still-installed Backplane plugin. Its skill-removal observation is PASS; its plugin-identity conclusion is INVALID for the canonical target. The exact native remove result named superpowers-backplane@superpowers-backplane, and the post-removal installed list omitted that ID. The sentinel cache/config entry is distinct from the canonical Backplane plugin.

The resolved marketplace Git HEAD matched the configured immutable SHA after each installed state. The installation-reference SHA-256 changed from 5C7E05C03938717968B82FFB2E55CB2869F2C8C0DC71FFCA318BD0D9395C56CF at the first SHA to 50D82CCACBF71D368E983984157ABE91D1FAFD977F1F4D654C0FD58B5393329D at the merge SHA and back to 5C7E05C03938717968B82FFB2E55CB2869F2C8C0DC71FFCA318BD0D9395C56CF after rollback. The declared package version stayed 0.1.0, so this tests Git ref content replacement and restoration, not released-version update.

The integrated cache's manifest, both Backplane SKILL.md files, and installation reference matched the tracked files on merged main byte for byte. Before merging, four fresh behavioral conformance prompts plus static skill-structure passed against that same Backplane content. The post-merge gh preflight returned all 15 native issue fields for issue #3, exactly one backplane:review label, no open blocker, and label add/remove plus closure-reason flags. The first PowerShell help assertion failed because it compared a string array; joining the help output confirmed all flags were present.

After the probe, the original local fixture marketplace was restored. The original Backplane, unrelated sentinel, and upstream plugin IDs matched the snapshot. Config, sentinel, upstream, two user notes, Backplane manifest, both Backplane SKILL.md files, and installation reference SHA-256 values matched 9/9. Issue #3 and disposable issue #13 retained their pre-probe labels and updatedAt values.

## Captured CLI stage data

```json
[
  {
    "stage": "first",
    "expectedSha": "8bfba888599568cc8f729ba6f0c030ace8e6377f",
    "resolvedSha": "8bfba888599568cc8f729ba6f0c030ace8e6377f",
    "marketplaceRoot": "C:\\Users\\Jeff\\AppData\\Local\\Temp\\backplane-codex-579301d7b6a249e69e38628a9806b287\\state-native\\.tmp\\marketplaces\\superpowers-backplane",
    "pluginIds": [
      "superpowers-backplane@superpowers-backplane",
      "superpowers@superpowers-dev"
    ],
    "hashes": {
      "reference": "5C7E05C03938717968B82FFB2E55CB2869F2C8C0DC71FFCA318BD0D9395C56CF",
      "upstream": "82C5C8866AD7F5DD4440CE66BD7806BA48A2F13771BEAE5CF112E53F08FE36BA",
      "manifest": "BCD8B9203F102392D3DF62193F74D7040D6386537439560F96BF9E5AB381003E",
      "backlog": "739A16FCDF2EE5ADAB0514F5A44DB0629DCCE558985FE5A31D71DD2606AC1E81",
      "handoffs": "A6052755128BE9C7D268D71241DD389B9BF1C720834E47E61CBF9535F4CA92DE"
    },
    "freshExit": 0,
    "prompt": "Read-only fresh installed-plugin discovery. Open the installed catalog SKILL.md files for superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, and superpowers-backplane:managing-superpowers-handoffs. Report each exact installed plugin ID and cache path, and the configured Backplane marketplace source plus its resolved Git HEAD. Use no repository-local junctions. Do not install, login, modify files or plugins, or change GitHub issues. Mark any unproved item UNKNOWN.",
    "runPath": "C:\\Users\\Jeff\\AppData\\Local\\Temp\\backplane-codex-579301d7b6a249e69e38628a9806b287\\remote-first-run.txt",
    "responsePath": "C:\\Users\\Jeff\\AppData\\Local\\Temp\\backplane-codex-579301d7b6a249e69e38628a9806b287\\remote-first-response.txt"
  },
  {
    "stage": "integrated",
    "expectedSha": "40b7df7ec8ff477972ae2b9a8f87bdea0a0fb119",
    "resolvedSha": "40b7df7ec8ff477972ae2b9a8f87bdea0a0fb119",
    "marketplaceRoot": "C:\\Users\\Jeff\\AppData\\Local\\Temp\\backplane-codex-579301d7b6a249e69e38628a9806b287\\state-native\\.tmp\\marketplaces\\superpowers-backplane",
    "pluginIds": [
      "superpowers-backplane@superpowers-backplane",
      "superpowers@superpowers-dev"
    ],
    "hashes": {
      "reference": "50D82CCACBF71D368E983984157ABE91D1FAFD977F1F4D654C0FD58B5393329D",
      "upstream": "82C5C8866AD7F5DD4440CE66BD7806BA48A2F13771BEAE5CF112E53F08FE36BA",
      "manifest": "BCD8B9203F102392D3DF62193F74D7040D6386537439560F96BF9E5AB381003E",
      "backlog": "739A16FCDF2EE5ADAB0514F5A44DB0629DCCE558985FE5A31D71DD2606AC1E81",
      "handoffs": "A6052755128BE9C7D268D71241DD389B9BF1C720834E47E61CBF9535F4CA92DE"
    },
    "freshExit": 0,
    "prompt": "Read-only fresh installed-plugin discovery. Open the installed catalog SKILL.md files for superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, and superpowers-backplane:managing-superpowers-handoffs. Report each exact installed plugin ID and cache path, and the configured Backplane marketplace source plus its resolved Git HEAD. Use no repository-local junctions. Do not install, login, modify files or plugins, or change GitHub issues. Mark any unproved item UNKNOWN.",
    "runPath": "C:\\Users\\Jeff\\AppData\\Local\\Temp\\backplane-codex-579301d7b6a249e69e38628a9806b287\\remote-integrated-run.txt",
    "responsePath": "C:\\Users\\Jeff\\AppData\\Local\\Temp\\backplane-codex-579301d7b6a249e69e38628a9806b287\\remote-integrated-response.txt"
  },
  {
    "stage": "rollback",
    "expectedSha": "8bfba888599568cc8f729ba6f0c030ace8e6377f",
    "resolvedSha": "8bfba888599568cc8f729ba6f0c030ace8e6377f",
    "marketplaceRoot": "C:\\Users\\Jeff\\AppData\\Local\\Temp\\backplane-codex-579301d7b6a249e69e38628a9806b287\\state-native\\.tmp\\marketplaces\\superpowers-backplane",
    "pluginIds": [
      "superpowers-backplane@superpowers-backplane",
      "superpowers@superpowers-dev"
    ],
    "hashes": {
      "reference": "5C7E05C03938717968B82FFB2E55CB2869F2C8C0DC71FFCA318BD0D9395C56CF",
      "upstream": "82C5C8866AD7F5DD4440CE66BD7806BA48A2F13771BEAE5CF112E53F08FE36BA",
      "manifest": "BCD8B9203F102392D3DF62193F74D7040D6386537439560F96BF9E5AB381003E",
      "backlog": "739A16FCDF2EE5ADAB0514F5A44DB0629DCCE558985FE5A31D71DD2606AC1E81",
      "handoffs": "A6052755128BE9C7D268D71241DD389B9BF1C720834E47E61CBF9535F4CA92DE"
    },
    "freshExit": 0,
    "prompt": "Read-only fresh installed-plugin discovery. Open the installed catalog SKILL.md files for superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, and superpowers-backplane:managing-superpowers-handoffs. Report each exact installed plugin ID and cache path, and the configured Backplane marketplace source plus its resolved Git HEAD. Use no repository-local junctions. Do not install, login, modify files or plugins, or change GitHub issues. Mark any unproved item UNKNOWN.",
    "runPath": "C:\\Users\\Jeff\\AppData\\Local\\Temp\\backplane-codex-579301d7b6a249e69e38628a9806b287\\remote-rollback-run.txt",
    "responsePath": "C:\\Users\\Jeff\\AppData\\Local\\Temp\\backplane-codex-579301d7b6a249e69e38628a9806b287\\remote-rollback-response.txt"
  },
  {
    "stage": "uninstall",
    "expectedSha": "8bfba888599568cc8f729ba6f0c030ace8e6377f",
    "resolvedSha": "8bfba888599568cc8f729ba6f0c030ace8e6377f",
    "pluginIds": [
      "superpowers@superpowers-dev"
    ],
    "freshExit": 0,
    "prompt": "Read-only fresh removal check. Verify the installed catalog still exposes superpowers:using-superpowers from its own plugin cache and no longer exposes either superpowers-backplane skill or installed Backplane plugin. Report exact IDs and paths or UNKNOWN. Do not install, login, or change files, plugins, or issues.",
    "runPath": "C:\\Users\\Jeff\\AppData\\Local\\Temp\\backplane-codex-579301d7b6a249e69e38628a9806b287\\remote-uninstall-run.txt",
    "responsePath": "C:\\Users\\Jeff\\AppData\\Local\\Temp\\backplane-codex-579301d7b6a249e69e38628a9806b287\\remote-uninstall-response.txt"
  }
]
```

## Preservation baseline

- config: D791BCF2543465A13D08557AD6679238B13BC3D4915B3A06AE6E437A90F6C5B5
- sentinel: D8A5155E915669EB5578C30953447FF3D3E56DEEEFC1D7BCC3216FB7158272F9
- guide_note: C400A6B1F8616BD52FB9CD1153CF5C6E81517273A346D6C4D7D3F7322D7814EA
- backlog_skill: 739A16FCDF2EE5ADAB0514F5A44DB0629DCCE558985FE5A31D71DD2606AC1E81
- upstream: 82C5C8866AD7F5DD4440CE66BD7806BA48A2F13771BEAE5CF112E53F08FE36BA
- handoff_skill: A6052755128BE9C7D268D71241DD389B9BF1C720834E47E61CBF9535F4CA92DE
- backplane_ref: 50D82CCACBF71D368E983984157ABE91D1FAFD977F1F4D654C0FD58B5393329D
- root_note: ED2EC7AEE9F5FEDAEF6BE63FAD983C2AE74745C76AF399FF0973FFACA7FB8728
- backplane_manifest: BCD8B9203F102392D3DF62193F74D7040D6386537439560F96BF9E5AB381003E

## first fresh session

Session ID: 01a0bc1f-31ec-7993-b0a0-2096b447ab74

### Exact prompt

Read-only fresh installed-plugin discovery. Open the installed catalog SKILL.md files for superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, and superpowers-backplane:managing-superpowers-handoffs. Report each exact installed plugin ID and cache path, and the configured Backplane marketplace source plus its resolved Git HEAD. Use no repository-local junctions. Do not install, login, modify files or plugins, or change GitHub issues. Mark any unproved item UNKNOWN.

### Exact final response

Read-only discovery results:

| Skill | Installed plugin ID | Installed cache path |
|---|---|---|
| `superpowers:using-superpowers` | `superpowers@superpowers-dev` | `C:\Users\Jeff\AppData\Local\Temp\backplane-codex-579301d7b6a249e69e38628a9806b287\state-native\plugins\cache\superpowers-dev\superpowers\6.4.1` |
| `superpowers-backplane:managing-superpowers-backlog` | `superpowers-backplane@superpowers-backplane` | `C:\Users\Jeff\AppData\Local\Temp\backplane-codex-579301d7b6a249e69e38628a9806b287\state-native\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.0` |
| `superpowers-backplane:managing-superpowers-handoffs` | `superpowers-backplane@superpowers-backplane` | `C:\Users\Jeff\AppData\Local\Temp\backplane-codex-579301d7b6a249e69e38628a9806b287\state-native\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.0` |

Backplane marketplace:

- Configured source type: `git`
- Configured source: `https://github.com/tvproductions/superpowers-backplane.git`
- Configured ref: `8bfba888599568cc8f729ba6f0c030ace8e6377f`
- Resolved marketplace Git HEAD: `8bfba888599568cc8f729ba6f0c030ace8e6377f`
- Installed version: `0.1.0`
- Enabled: `true`

The configured ref, marketplace checkout HEAD, and installed cache checkout HEAD all match. No repository-local junctions were used. No files, plugins, logins, or GitHub issues were changed. UNKNOWN items: none.

## integrated fresh session

Session ID: 01a0bc20-9dde-7683-9c12-7dbaad39c158

### Exact prompt

Read-only fresh installed-plugin discovery. Open the installed catalog SKILL.md files for superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, and superpowers-backplane:managing-superpowers-handoffs. Report each exact installed plugin ID and cache path, and the configured Backplane marketplace source plus its resolved Git HEAD. Use no repository-local junctions. Do not install, login, modify files or plugins, or change GitHub issues. Mark any unproved item UNKNOWN.

### Exact final response

Read-only discovery completed using direct installed-cache paths; no repository-local junctions were used.

| Skill | Installed plugin ID | Cache path |
|---|---|---|
| `superpowers:using-superpowers` | `superpowers@superpowers-dev` | [6.4.1](C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/superpowers-dev/superpowers/6.4.1) |
| `superpowers-backplane:managing-superpowers-backlog` | `superpowers-backplane@superpowers-backplane` | [0.1.0](C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/superpowers-backplane/superpowers-backplane/0.1.0) |
| `superpowers-backplane:managing-superpowers-handoffs` | `superpowers-backplane@superpowers-backplane` | [0.1.0](C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/superpowers-backplane/superpowers-backplane/0.1.0) |

Backplane marketplace:

- Marketplace ID: `superpowers-backplane`
- Source type: `git`
- Configured source: `https://github.com/tvproductions/superpowers-backplane.git`
- Configured ref: `40b7df7ec8ff477972ae2b9a8f87bdea0a0fb119`
- Resolved cached Git HEAD: `40b7df7ec8ff477972ae2b9a8f87bdea0a0fb119`
- Cached `origin`: `https://github.com/tvproductions/superpowers-backplane.git`

Both cache roots are ordinary directories (`LinkType: null`) with their own `.git` directories. No unproved requested items remain; nothing is marked `UNKNOWN`. No files, plugins, logins, or GitHub issues were changed.

## rollback fresh session

Session ID: 01a0bc22-2cfd-79a1-a1b2-b8780e30de03

### Exact prompt

Read-only fresh installed-plugin discovery. Open the installed catalog SKILL.md files for superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, and superpowers-backplane:managing-superpowers-handoffs. Report each exact installed plugin ID and cache path, and the configured Backplane marketplace source plus its resolved Git HEAD. Use no repository-local junctions. Do not install, login, modify files or plugins, or change GitHub issues. Mark any unproved item UNKNOWN.

### Exact final response

Read-only discovery completed directly from the installed catalog; no repository-local junctions were used.

| Skill | Installed plugin ID | Cache path |
|---|---|---|
| `superpowers:using-superpowers` | `superpowers@superpowers-dev` | [6.4.1 cache](<C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/superpowers-dev/superpowers/6.4.1>) |
| `superpowers-backplane:managing-superpowers-backlog` | `superpowers-backplane@superpowers-backplane` | [0.1.0 cache](<C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/superpowers-backplane/superpowers-backplane/0.1.0>) |
| `superpowers-backplane:managing-superpowers-handoffs` | `superpowers-backplane@superpowers-backplane` | [0.1.0 cache](<C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/plugins/cache/superpowers-backplane/superpowers-backplane/0.1.0>) |

Backplane marketplace:

- Configured source: `https://github.com/tvproductions/superpowers-backplane.git`
- Configured ref: `8bfba888599568cc8f729ba6f0c030ace8e6377f`
- Resolved checkout: [superpowers-backplane](<C:/Users/Jeff/AppData/Local/Temp/backplane-codex-579301d7b6a249e69e38628a9806b287/state-native/.tmp/marketplaces/superpowers-backplane>)
- Resolved Git `HEAD`: `8bfba888599568cc8f729ba6f0c030ace8e6377f`
- Checkout `origin`: `https://github.com/tvproductions/superpowers-backplane.git`

All requested items were proved; none are `UNKNOWN`. No files, plugins, credentials, or GitHub issues were changed.

## uninstall fresh session

Session ID: 01a0bc24-285b-7023-95c0-5c2a06c9e5ed

### Exact prompt

Read-only fresh removal check. Verify the installed catalog still exposes superpowers:using-superpowers from its own plugin cache and no longer exposes either superpowers-backplane skill or installed Backplane plugin. Report exact IDs and paths or UNKNOWN. Do not install, login, or change files, plugins, or issues.

### Exact final response

Read-only check result: partial failure.

- Exposed skill: `superpowers:using-superpowers`
  - Plugin ID: `superpowers@superpowers-dev`
  - Path: `C:\Users\Jeff\AppData\Local\Temp\backplane-codex-579301d7b6a249e69e38628a9806b287\state-native\plugins\cache\superpowers-dev\superpowers\6.4.1\skills\using-superpowers\SKILL.md`

- Exposed `superpowers-backplane` skill: not found
  - Exact skill ID: `UNKNOWN`
  - Path: `UNKNOWN`
  - No `SKILL.md` exists beneath the Backplane cache.

- Installed Backplane plugin: still present and enabled
  - Plugin ID: `backplane-preservation-sentinel@superpowers-backplane`
  - Configuration: `enabled = true`
  - Config path: `C:\Users\Jeff\AppData\Local\Temp\backplane-codex-579301d7b6a249e69e38628a9806b287\state-native\config.toml`
  - Cached manifest: `C:\Users\Jeff\AppData\Local\Temp\backplane-codex-579301d7b6a249e69e38628a9806b287\state-native\plugins\cache\superpowers-backplane\backplane-preservation-sentinel\0.0.1\plugin.json`
  - Marketplace ID: `superpowers-backplane`

Therefore, the skill-removal check passes, but the installed-plugin removal check does not. No files, plugins, logins, or issues were changed.
