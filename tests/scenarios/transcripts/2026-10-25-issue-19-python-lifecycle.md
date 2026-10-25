# Issue 19 Python lifecycle observations

These are observed Windows host results, not macOS/Linux execution. Exact Python guide blocks are retained in the guide at its receipt digest. The captured final model responses below are unedited. Actual Skill tool calls/results and injected source roots are included; repeated injected public skill bodies and session initialization metadata are omitted. This is not a claim that four behavioral conformance prompts ran.

## Exact fresh-session prompts

```text
Read-only installed-plugin discovery probe. Invoke the Skill tool separately for superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, and superpowers-backplane:managing-superpowers-handoffs, in that order. This probe requests only actual skill loading and reporting the three loaded package roots; it does not request setup, implementation, handoff creation/resume, issue intake or mutation. Do not create any file. Report any missing skill honestly.
```

```text
Read-only uninstall discovery probe. Invoke Skill superpowers:using-superpowers. Then inspect your available Skill tool skill inventory and report whether superpowers-backplane:managing-superpowers-backlog and superpowers-backplane:managing-superpowers-handoffs are absent. Do not try to install anything, read files, create a handoff, or mutate GitHub. Do not invent a successful load of unavailable skills.
```

## Native command replay

```text
python-before-replay: 21 exact source files; preservation PASS
Executing exact Python guide block 0
Disposable Claude profile: U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Dedicated catalog directory: U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\catalog
Prior verified 40-character Backplane commit: b0d702f8821d6d29184118410ec6ff2d8fb63438
Reviewed candidate 40-character Backplane commit: 5e01704fcdda13eefeeac52d8892da26e7164ffd
b0d702f8821d6d29184118410ec6ff2d8fb63438
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Validating marketplace manifest: U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\catalog\.claude-plugin\marketplace.json

✔ Validation passed
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
[
  {
    "name": "superpowers-backplane",
    "source": "directory",
    "path": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\catalog",
    "installLocation": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\catalog"
  },
  {
    "name": "superpowers-dev",
    "source": "directory",
    "path": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers",
    "installLocation": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers"
  }
]
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
[
  {
    "id": "superpowers-backplane@superpowers-backplane",
    "version": "0.1.0",
    "scope": "user",
    "enabled": true,
    "installPath": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0",
    "installedAt": "2026-10-25T16:28:17.900Z",
    "lastUpdated": "2026-10-25T16:28:17.900Z",
    "projectEnabled": false
  },
  {
    "id": "superpowers@superpowers-dev",
    "version": "7.0.0",
    "scope": "user",
    "enabled": true,
    "installPath": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-dev\\superpowers\\7.0.0",
    "readFromFolder": "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers",
    "folderVersion": "7.0.0",
    "installedAt": "2026-10-25T16:16:00.363Z",
    "lastUpdated": "2026-10-25T16:16:00.363Z",
    "projectEnabled": false
  },
  {
    "id": "cowork-plugin-management@synced",
    "version": "0.2.2",
    "scope": "synced",
    "enabled": true,
    "installPath": "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\synced\\5be94afe-931f-4e50-9eb7-2c854097b334_977856c7-71a7-4075-bc14-9b42ecb2650e\\cowork-plugin-management"
  }
]
python-guide-0: 21 exact source files; preservation PASS
Executing exact Python guide block 1
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Adding marketplace…✔ Marketplace 'superpowers-backplane' already on disk — declared in user settings
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Installing plugin "superpowers-backplane@superpowers-backplane"...✔ Plugin "superpowers-backplane@superpowers-backplane" is already installed (scope: user)
python-guide-1: 21 exact source files; preservation PASS
Executing exact Python guide block 2
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Installing plugin "superpowers-backplane@superpowers-backplane"...✔ Plugin "superpowers-backplane@superpowers-backplane" is already installed (scope: user)
python-guide-2: 21 exact source files; preservation PASS
python-guide-2: fresh Skill-only discovery; CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
python-guide-2: discovery PASS; session=e36c6065-fe56-4600-8130-6d8cfd5a13db
Executing exact Python guide block 3
5e01704fcdda13eefeeac52d8892da26e7164ffd
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Validating marketplace manifest: U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\catalog\.claude-plugin\marketplace.json

✔ Validation passed
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Updating marketplace: superpowers-backplane...Validating local marketplace
✔ Successfully updated marketplace: superpowers-backplane
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Checking for updates for plugin "superpowers-backplane@superpowers-backplane" at user scope…
✔ Plugin "superpowers-backplane" updated from 0.1.0 to 0.1.1 for scope user. Restart to apply changes.
python-guide-3: 21 exact source files; preservation PASS
python-guide-3: fresh Skill-only discovery; CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
python-guide-3: discovery PASS; session=e1fe55c4-e425-4c3b-9c94-f507b69cf40e
Executing exact Python guide block 4
b0d702f8821d6d29184118410ec6ff2d8fb63438
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Validating marketplace manifest: U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\catalog\.claude-plugin\marketplace.json

✔ Validation passed
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Updating marketplace: superpowers-backplane...Validating local marketplace
✔ Successfully updated marketplace: superpowers-backplane
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
✔ Successfully uninstalled plugin: superpowers-backplane (scope: user)
python-guide-4: 0 exact source files; preservation PASS
Executing exact Python guide block 5
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Installing plugin "superpowers-backplane@superpowers-backplane"...✔ Successfully installed plugin: superpowers-backplane@superpowers-backplane (scope: user)
python-guide-5: 21 exact source files; preservation PASS
python-guide-5: fresh Skill-only discovery; CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
python-guide-5: discovery PASS; session=375afa41-9653-439f-96e9-58dd7c3d39e2
Executing exact Python guide block 6
Candidate rejected before replacement: Command failed; inspect state before repair: {"message":"No commit found for SHA: 0000000000000000000000000000000000000000","documentation_url":"https://docs.github.com/rest/commits/commits#get-a-commit","status":"422"}gh: No commit found for SHA: 0000000000000000000000000000000000000000 (HTTP 422)

python-guide-6: 21 exact source files; preservation PASS
Executing exact Python guide block 7
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
✔ Successfully uninstalled plugin: superpowers-backplane (scope: user)
python-guide-7: 0 exact source files; preservation PASS
python-guide-7: fresh Skill-only discovery; CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
python-guide-7: discovery PASS; session=6d74de58-746d-4c45-aaf4-4b9f7880ee13
Executing exact Python guide block 8
CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
Installing plugin "superpowers-backplane@superpowers-backplane"...✔ Successfully installed plugin: superpowers-backplane@superpowers-backplane (scope: user)
python-guide-8: 21 exact source files; preservation PASS
python-guide-8: fresh Skill-only discovery; CLAUDE_CONFIG_DIR=U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile
python-guide-8: discovery PASS; session=b25e8fe0-44f6-4f97-adda-27410c1f0b54
All nine Python lifecycle blocks replayed; B restored.

```

## Initial update failure, before correction

```text
Checking for updates for plugin "superpowers-backplane@superpowers-backplane" at user scope…
✘ Failed to update plugin "superpowers-backplane@superpowers-backplane": Failed to clone repository: Cloning into 'U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\temp_github_1792945385804_12mz42'...
git@github.com: Permission denied (publickey). 
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

```

## python-guide-2-discovery

```json
{
  "row": "python-guide-2-discovery",
  "session": "e36c6065-fe56-4600-8130-6d8cfd5a13db",
  "raw_trace_sha256": "01410fdecd83e0f508c485427d1f8f9ed2b5f9edece170a72d67bd98c1a2ab04",
  "tool_calls": [
    {
      "id": "toolu_013LHp2U7BVWYZun1QKafP9K",
      "name": "Skill",
      "input": {
        "skill": "superpowers:using-superpowers"
      }
    },
    {
      "id": "toolu_01MVveyhMDogdq4qFYZtEpXx",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-backlog"
      }
    },
    {
      "id": "toolu_01QrPd2xa1FyDXSv3UNmKhzP",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-handoffs"
      }
    }
  ],
  "tool_results": [
    {
      "tool_use_id": "toolu_013LHp2U7BVWYZun1QKafP9K",
      "is_error": false,
      "content": "Launching skill: superpowers:using-superpowers"
    },
    {
      "tool_use_id": "toolu_01MVveyhMDogdq4qFYZtEpXx",
      "is_error": false,
      "content": "Launching skill: superpowers-backplane:managing-superpowers-backlog"
    },
    {
      "tool_use_id": "toolu_01QrPd2xa1FyDXSv3UNmKhzP",
      "is_error": false,
      "content": "Launching skill: superpowers-backplane:managing-superpowers-handoffs"
    }
  ],
  "loaded_roots": [
    "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers",
    "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog",
    "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-handoffs"
  ],
  "subtype": "success",
  "is_error": false,
  "model_usage": {
    "claude-opus-5-5": {
      "inputTokens": 8,
      "outputTokens": 830,
      "cacheReadInputTokens": 67501,
      "cacheCreationInputTokens": 19212,
      "webSearchRequests": 0,
      "costUSD": 0.1838282,
      "contextWindow": 1000000,
      "maxOutputTokens": 128000,
      "thinkingTokens": 152,
      "canonicalModel": "claude-opus-5-5",
      "provider": "firstParty",
      "costBasis": "list"
    }
  }
}
```

All three skills loaded through the Skill tool, in the order you asked. None were missing. I didn't create or change any files, and I made no GitHub or Git calls. I stopped at loading: I didn't run any operation inside the skills.

| # | Skill | Package root (the folder above `skills\<name>`) |
|---|---|---|
| 1 | `superpowers:using-superpowers` | `U:\repos\agents\superpowers-backplane\.agents\superpowers` |
| 2 | `superpowers-backplane:managing-superpowers-backlog` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.0` |
| 3 | `superpowers-backplane:managing-superpowers-handoffs` | Same as #2 |

`superpowers:using-superpowers` did not load from the plugin cache. It loaded from the repository's own `.agents\superpowers` checkout. The two Backplane skills loaded from the issue-19 test profile's plugin cache, at `superpowers-backplane` version `0.1.0`. If this probe was meant to show upstream Superpowers being found as an installed plugin, this run doesn't show that. It shows the copy of upstream checked out inside the repo instead.

The package roots are each skill's reported base directory with `skills\<name>` removed. I didn't open those folders to check them.

## python-guide-3-discovery

```json
{
  "row": "python-guide-3-discovery",
  "session": "e1fe55c4-e425-4c3b-9c94-f507b69cf40e",
  "raw_trace_sha256": "fe9d8859131406ee9a76fd3da9a3b404d4eb44371eda16d6e212d43f6e008616",
  "tool_calls": [
    {
      "id": "toolu_018ib2TYL6mqQT6QaZJhcvph",
      "name": "Skill",
      "input": {
        "skill": "superpowers:using-superpowers"
      }
    },
    {
      "id": "toolu_01UXHQgUqwXhAdwVbTTAjfth",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-backlog"
      }
    },
    {
      "id": "toolu_01GvRhTV1p4sQbd5h8RmBznu",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-handoffs"
      }
    }
  ],
  "tool_results": [
    {
      "tool_use_id": "toolu_018ib2TYL6mqQT6QaZJhcvph",
      "is_error": false,
      "content": "Launching skill: superpowers:using-superpowers"
    },
    {
      "tool_use_id": "toolu_01UXHQgUqwXhAdwVbTTAjfth",
      "is_error": false,
      "content": "Launching skill: superpowers-backplane:managing-superpowers-backlog"
    },
    {
      "tool_use_id": "toolu_01GvRhTV1p4sQbd5h8RmBznu",
      "is_error": false,
      "content": "Launching skill: superpowers-backplane:managing-superpowers-handoffs"
    }
  ],
  "loaded_roots": [
    "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers",
    "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.1\\skills\\managing-superpowers-backlog",
    "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.1\\skills\\managing-superpowers-handoffs"
  ],
  "subtype": "success",
  "is_error": false,
  "model_usage": {
    "claude-opus-5-5": {
      "inputTokens": 8,
      "outputTokens": 853,
      "cacheReadInputTokens": 82560,
      "cacheCreationInputTokens": 4153,
      "webSearchRequests": 0,
      "costUSD": 0.066828,
      "contextWindow": 1000000,
      "maxOutputTokens": 128000,
      "thinkingTokens": 109,
      "canonicalModel": "claude-opus-5-5",
      "provider": "firstParty",
      "costBasis": "list"
    }
  }
}
```

I loaded all three skills with separate Skill calls, in the order you asked. None was missing.

| # | Skill | Loaded package root |
|---|---|---|
| 1 | `superpowers:using-superpowers` | `U:\repos\agents\superpowers-backplane\.agents\superpowers\skills\using-superpowers` |
| 2 | `superpowers-backplane:managing-superpowers-backlog` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.1\skills\managing-superpowers-backlog` |
| 3 | `superpowers-backplane:managing-superpowers-handoffs` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.1\skills\managing-superpowers-handoffs` |

- **Where they resolved from:**
  - **Upstream Superpowers:** this skill resolved to the sibling upstream checkout at `.agents\superpowers`, not to a plugin cache folder.
  - **Both Backplane skills:** these resolved to the plugin cache under the isolated issue-19 profile, version `0.1.1`.
- **Out of scope:** I only loaded the skills. I did not read any reference files they link to or run any of their steps (installation checks, GitHub reads, handoff create or resume).
- **No changes:** I created or changed no files, ran no Git or GitHub commands, and wrote nothing to memory.

## python-guide-5-discovery

```json
{
  "row": "python-guide-5-discovery",
  "session": "375afa41-9653-439f-96e9-58dd7c3d39e2",
  "raw_trace_sha256": "854eb8f1ffbc5434bc932e30c195acd8549606f39d9815c6364b37b91f9e1538",
  "tool_calls": [
    {
      "id": "toolu_016BPqJSXtqUVZwsn7cBi6tk",
      "name": "Skill",
      "input": {
        "skill": "superpowers:using-superpowers"
      }
    },
    {
      "id": "toolu_01StrAAcAp18CouAHDwzMnW8",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-backlog"
      }
    },
    {
      "id": "toolu_01XEHYoQB6y6cQqSEK22yG9b",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-handoffs"
      }
    }
  ],
  "tool_results": [
    {
      "tool_use_id": "toolu_016BPqJSXtqUVZwsn7cBi6tk",
      "is_error": false,
      "content": "Launching skill: superpowers:using-superpowers"
    },
    {
      "tool_use_id": "toolu_01StrAAcAp18CouAHDwzMnW8",
      "is_error": false,
      "content": "Launching skill: superpowers-backplane:managing-superpowers-backlog"
    },
    {
      "tool_use_id": "toolu_01XEHYoQB6y6cQqSEK22yG9b",
      "is_error": false,
      "content": "Launching skill: superpowers-backplane:managing-superpowers-handoffs"
    }
  ],
  "loaded_roots": [
    "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers",
    "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog",
    "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-handoffs"
  ],
  "subtype": "success",
  "is_error": false,
  "model_usage": {
    "claude-opus-5-5": {
      "inputTokens": 8,
      "outputTokens": 1112,
      "cacheReadInputTokens": 86713,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0396146,
      "contextWindow": 1000000,
      "maxOutputTokens": 128000,
      "thinkingTokens": 212,
      "canonicalModel": "claude-opus-5-5",
      "provider": "firstParty",
      "costBasis": "list"
    }
  }
}
```

All three skills loaded through the Skill tool, in the order you asked. None were missing.

| # | Skill | Loaded skill directory | Package root |
|---|---|---|---|
| 1 | `superpowers:using-superpowers` | `U:\repos\agents\superpowers-backplane\.agents\superpowers\skills\using-superpowers` | `U:\repos\agents\superpowers-backplane\.agents\superpowers` |
| 2 | `superpowers-backplane:managing-superpowers-backlog` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.0\skills\managing-superpowers-backlog` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.0` |
| 3 | `superpowers-backplane:managing-superpowers-handoffs` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.0\skills\managing-superpowers-handoffs` | Same as #2 |

- **Superpowers came from the repository checkout, not a plugin cache.** `superpowers:using-superpowers` loaded from the repository's own `.agents/superpowers` folder. The SessionStart hook had also inserted that skill's text, but the root above is the base directory the Skill tool reported.
- **The two Backplane skills came from the profile's plugin cache.** That cache sits under the issue-19 profile, at `superpowers-backplane` version `0.1.0`. Both skills share that one package root.
- **I only took the roots from the Skill tool's output.** I didn't check upstream installation, plugin manifests or revisions, so this report makes no claim about compatibility or provenance.

I didn't create or change any file, did no setup or handoff work, and didn't touch any issue.

## python-guide-7-discovery

```json
{
  "row": "python-guide-7-discovery",
  "session": "6d74de58-746d-4c45-aaf4-4b9f7880ee13",
  "raw_trace_sha256": "d7dff0f19c1d795bc615fb763219dd7df98d2cd5d9518eafd8f0d62ff87046ba",
  "tool_calls": [
    {
      "id": "toolu_01Sguds37xa7rQEeNaNhepbq",
      "name": "Skill",
      "input": {
        "skill": "superpowers:using-superpowers"
      }
    }
  ],
  "tool_results": [
    {
      "tool_use_id": "toolu_01Sguds37xa7rQEeNaNhepbq",
      "is_error": false,
      "content": "Launching skill: superpowers:using-superpowers"
    }
  ],
  "loaded_roots": [
    "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers"
  ],
  "subtype": "success",
  "is_error": false,
  "model_usage": {
    "claude-opus-5-5": {
      "inputTokens": 4,
      "outputTokens": 542,
      "cacheReadInputTokens": 24794,
      "cacheCreationInputTokens": 14957,
      "webSearchRequests": 0,
      "costUSD": 0.1354708,
      "contextWindow": 1000000,
      "maxOutputTokens": 128000,
      "thinkingTokens": 39,
      "canonicalModel": "claude-opus-5-5",
      "provider": "firstParty",
      "costBasis": "list"
    }
  }
}
```

I invoked `superpowers:using-superpowers` and it loaded. I skipped its Claude Code reference file because you said not to read files.

**Result: both skills are absent.** No skill in my current Skill tool inventory has the `superpowers-backplane:` namespace.

| Skill | Status |
|---|---|
| `superpowers-backplane:managing-superpowers-backlog` | **Absent**: not in the inventory |
| `superpowers-backplane:managing-superpowers-handoffs` | **Absent**: not in the inventory |

The `superpowers:` skills that are present are the 15 upstream ones: brainstorming, diagnosing-superpowers, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans and writing-skills. The rest of the inventory is built-in skills, `cowork-plugin-management:*` and `anthropic-skills:*`. None of them are Backplane skills.

I didn't try to load either missing skill. I also didn't install anything, read any files, create a handoff or touch GitHub. This is consistent with the Backplane plugin being uninstalled from this session.

## python-guide-8-discovery

```json
{
  "row": "python-guide-8-discovery",
  "session": "b25e8fe0-44f6-4f97-adda-27410c1f0b54",
  "raw_trace_sha256": "6d6bae2fd9febdb701997150554bf1252f2d2eca7da5aeb721bf3a5d0d410054",
  "tool_calls": [
    {
      "id": "toolu_01WgTZnwSCMMdsSzyEhLVd6w",
      "name": "Skill",
      "input": {
        "skill": "superpowers:using-superpowers"
      }
    },
    {
      "id": "toolu_01GayxjgiBwbuiJbRhMce5mG",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-backlog"
      }
    },
    {
      "id": "toolu_01RfYHheka45X1zQVdLhirDs",
      "name": "Skill",
      "input": {
        "skill": "superpowers-backplane:managing-superpowers-handoffs"
      }
    }
  ],
  "tool_results": [
    {
      "tool_use_id": "toolu_01WgTZnwSCMMdsSzyEhLVd6w",
      "is_error": false,
      "content": "Launching skill: superpowers:using-superpowers"
    },
    {
      "tool_use_id": "toolu_01GayxjgiBwbuiJbRhMce5mG",
      "is_error": false,
      "content": "Launching skill: superpowers-backplane:managing-superpowers-backlog"
    },
    {
      "tool_use_id": "toolu_01RfYHheka45X1zQVdLhirDs",
      "is_error": false,
      "content": "Launching skill: superpowers-backplane:managing-superpowers-handoffs"
    }
  ],
  "loaded_roots": [
    "U:\\repos\\agents\\superpowers-backplane\\.agents\\superpowers\\skills\\using-superpowers",
    "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-backlog",
    "U:\\repos\\agents\\superpowers-backplane\\.sp-bp\\work\\issue-19\\profile\\plugins\\cache\\superpowers-backplane\\superpowers-backplane\\0.1.0\\skills\\managing-superpowers-handoffs"
  ],
  "subtype": "success",
  "is_error": false,
  "model_usage": {
    "claude-opus-5-5": {
      "inputTokens": 8,
      "outputTokens": 1149,
      "cacheReadInputTokens": 67750,
      "cacheCreationInputTokens": 19295,
      "webSearchRequests": 0,
      "costUSD": 0.19092200000000004,
      "contextWindow": 1000000,
      "maxOutputTokens": 128000,
      "thinkingTokens": 217,
      "canonicalModel": "claude-opus-5-5",
      "provider": "firstParty",
      "costBasis": "list"
    }
  }
}
```

All three skills loaded through the Skill tool, in the order you asked. None were missing.

| # | Skill | Skill base directory reported by the harness | Package root |
|---|---|---|---|
| 1 | `superpowers:using-superpowers` | `U:\repos\agents\superpowers-backplane\.agents\superpowers\skills\using-superpowers` | `U:\repos\agents\superpowers-backplane\.agents\superpowers` |
| 2 | `superpowers-backplane:managing-superpowers-backlog` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.0\skills\managing-superpowers-backlog` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.0` |
| 3 | `superpowers-backplane:managing-superpowers-handoffs` | `U:\repos\agents\superpowers-backplane\.sp-bp\work\issue-19\profile\plugins\cache\superpowers-backplane\superpowers-backplane\0.1.0\skills\managing-superpowers-handoffs` | Same as #2 |

- **Superpowers came from the repository's own upstream checkout.** It loaded from `.agents\superpowers`, not from a plugin cache in the issue-19 profile. Both Backplane skills loaded from that profile's plugin cache, from version `0.1.0` of the `superpowers-backplane` package.
- **Package roots are inferred.** The harness reported each skill's base directory. I took the package root to be the folder above `skills\`. I read no manifest files to confirm this.
- **Nothing else was done.** I created no files, ran no Git or `gh` commands, and touched no GitHub issues. I loaded the skills but did not follow their instructions, including their reference reads and prerequisite checks, because this probe asked only for loading. The SessionStart hook had already inserted the `using-superpowers` text into context. The Skill tool call loaded it again, as you asked.

## Test-only portable verification source

These are native disposable-profile test helpers, not installed product code. Their exact source is retained for independent audit.

### lifecycle.py

SHA-256: `63ec0ecff952d09363014ce70550bf9935dbdcea86626e8a55c866664744ee2f`

```python
"""Portable orchestration; no shell, profile fallback, or credential copying."""

from collections.abc import Mapping, Sequence
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from typing import Any

REPOSITORY = "tvproductions/superpowers-backplane"
BASELINE = "b0d702f8821d6d29184118410ec6ff2d8fb63438"
FIXTURE = "5e01704fcdda13eefeeac52d8892da26e7164ffd"
BACKPLANE = "superpowers-backplane@superpowers-backplane"
ISSUE_FIELDS = "number,title,body,state,stateReason,issueType,labels,parent,subIssues,subIssuesSummary,blockedBy,blocking,closedByPullRequestsReferences,updatedAt,url"


def run_cli(
    arguments: Sequence[str], *, cwd: Path, overrides: Mapping[str, str] | None = None
) -> str:
    environment = dict(os.environ, PYTHONIOENCODING="utf-8")
    environment.update(overrides or {})
    executable = shutil.which(arguments[0])
    if executable is None:
        raise FileNotFoundError(f"Required executable unavailable: {arguments[0]}")
    result = subprocess.run(
        [executable, *arguments[1:]],
        cwd=cwd,
        env=environment,
        shell=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode:
        raise RuntimeError(
            f"{arguments[0]} exited {result.returncode}: {result.stdout}{result.stderr}"
        )
    return result.stdout


def compare_preservation(before: Any, after: Any) -> None:
    if before != after:
        raise ValueError("Preservation mismatch; retain snapshot before repair")


def verify_file(path: Path, expected_blob: str) -> None:
    content = path.read_bytes()
    header = f"blob {len(content)}\0".encode("ascii")
    if (
        hashlib.sha1(header + content, usedforsecurity=False).hexdigest()
        != expected_blob
    ):
        raise ValueError(f"Installed byte mismatch: {path}")


def validate_revision(revision: str) -> None:
    if re.fullmatch(r"[0-9a-f]{40}", revision) is None:
        raise ValueError("Use a full lowercase 40-character commit SHA")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        newline="\n",
        dir=path.parent,
        prefix=f".{path.name}.",
        delete=False,
    ) as handle:
        temporary = Path(handle.name)
        handle.write(text)
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


class Harness:
    def __init__(
        self, root: Path, profile: Path | None = None, catalog: Path | None = None
    ):
        self.root = root.resolve(strict=True)
        self.work = self.root / ".sp-bp" / "work" / "issue-19"
        self.profile = (profile or self.work / "profile").resolve(strict=True)
        self.catalog = (catalog or self.work / "catalog").resolve()
        self.environment = {"CLAUDE_CONFIG_DIR": str(self.profile)}
        index = int(os.environ.get("GIT_CONFIG_COUNT", "0") or "0")
        self.environment.update(
            {
                "GIT_CONFIG_COUNT": str(index + 1),
                f"GIT_CONFIG_KEY_{index}": f"url.https://github.com/{REPOSITORY}.insteadOf",
                f"GIT_CONFIG_VALUE_{index}": f"git@github.com:{REPOSITORY}",
            }
        )

    def command(self, arguments: Sequence[str]) -> str:
        return run_cli(arguments, cwd=self.root, overrides=self.environment)

    def claude(self, *arguments: str) -> str:
        print(f"CLAUDE_CONFIG_DIR={self.profile}", flush=True)
        output = self.command(["claude", *arguments])
        print(output, end="" if output.endswith("\n") else "\n", flush=True)
        return output

    def source(self, revision: str) -> None:
        validate_revision(revision)
        manifest = self.catalog / ".claude-plugin" / "marketplace.json"
        if self.catalog.exists():
            existing = read_json(manifest)
            entries = existing.get("plugins", [])
            if (
                existing.get("name") != "superpowers-backplane"
                or len(entries) != 1
                or entries[0].get("name") != "superpowers-backplane"
                or entries[0].get("source", {}).get("source") != "github"
                or entries[0].get("source", {}).get("repo") != REPOSITORY
            ):
                raise ValueError(
                    "Occupied catalog is not the verified dedicated Backplane source"
                )
        # Availability is checked before catalog or installed-package mutation.
        available = self.command(
            ["gh", "api", f"repos/{REPOSITORY}/commits/{revision}", "--jq", ".sha"]
        ).strip()
        if available != revision:
            raise ValueError(
                "Source unavailable; retain prior catalog and installation"
            )
        write_json(
            manifest,
            {
                "name": "superpowers-backplane",
                "description": "Pinned Backplane hosted-source catalog",
                "owner": {"name": "tvproductions"},
                "plugins": [
                    {
                        "name": "superpowers-backplane",
                        "description": "Pinned Backplane package",
                        "source": {
                            "source": "github",
                            "repo": REPOSITORY,
                            "sha": revision,
                        },
                    }
                ],
            },
        )

    def discovery(self, row: str, *, absent: bool = False) -> None:
        prompt = (
            "Read-only installed-plugin discovery probe. Invoke the Skill tool separately for "
            "superpowers:using-superpowers, superpowers-backplane:managing-superpowers-backlog, "
            "and superpowers-backplane:managing-superpowers-handoffs, in that order. This probe "
            "requests only actual skill loading and reporting the three loaded package roots; "
            "it does not request setup, implementation, handoff creation/resume, issue intake "
            "or mutation. Do not create any file. Report any missing skill honestly."
        )
        if absent:
            prompt = (
                "Read-only uninstall discovery probe. Invoke Skill superpowers:using-superpowers. "
                "Then inspect your available Skill tool skill inventory and report whether "
                "superpowers-backplane:managing-superpowers-backlog and "
                "superpowers-backplane:managing-superpowers-handoffs are absent. Do not try to "
                "install anything, read files, create a handoff, or mutate GitHub. Do not invent "
                "a successful load of unavailable skills."
            )
        print(
            f"{row}: fresh Skill-only discovery; CLAUDE_CONFIG_DIR={self.profile}",
            flush=True,
        )
        output = run_cli(
            [
                "claude",
                "-p",
                prompt,
                "--tools",
                "Skill",
                "--allowedTools",
                "Skill",
                "--output-format",
                "stream-json",
                "--verbose",
                "--max-turns",
                "8",
            ],
            cwd=self.work / "neutral",
            overrides=self.environment,
        )
        (self.work / f"{row}-discovery.jsonl").write_text(
            output, encoding="utf-8", newline="\n"
        )
        events = [json.loads(line) for line in output.splitlines() if line.strip()]
        result = next(
            event for event in reversed(events) if event.get("type") == "result"
        )
        if result.get("is_error") or result.get("subtype") != "success":
            raise ValueError("Fresh discovery session did not succeed")
        calls = []
        for event in events:
            for block in event.get("message", {}).get("content", []):
                if not isinstance(block, dict):
                    continue
                if block.get("type") == "tool_use" and block.get("name") == "Skill":
                    calls.append(block["input"]["skill"])
                if block.get("type") == "tool_result" and block.get("is_error"):
                    raise ValueError("Discovery tool load failed")
        required = ["superpowers:using-superpowers"]
        if not absent:
            required += [
                "superpowers-backplane:managing-superpowers-backlog",
                "superpowers-backplane:managing-superpowers-handoffs",
            ]
        if any(skill not in calls for skill in required):
            raise ValueError("Missing actual Skill tool invocation")
        if absent:
            initialization = next(
                event for event in events if event.get("subtype") == "init"
            )
            if "skills" not in initialization:
                raise ValueError("Native skill inventory unavailable")
            if any(
                "superpowers-backplane" in str(skill)
                for skill in initialization["skills"]
            ):
                raise ValueError("Backplane remains in fresh native skill inventory")
        write_json(
            self.work / f"{row}-discovery-summary.json",
            {
                "row": row,
                "session": result["session_id"],
                "skills": calls,
                "result": result["result"],
                "absent": absent,
            },
        )
        print(f"{row}: discovery PASS; session={result['session_id']}", flush=True)

    def snapshot(
        self, row: str, revision: str | None, version: str | None
    ) -> dict[str, Any]:
        plugins = json.loads(self.command(["claude", "plugin", "list", "--json"]))
        marketplaces = json.loads(
            self.command(["claude", "plugin", "marketplace", "list", "--json"])
        )
        registry = read_json(self.profile / "plugins" / "installed_plugins.json")[
            "plugins"
        ]
        entries = registry.get(BACKPLANE, [])
        files = []
        if revision is None:
            if any(item["id"] == BACKPLANE for item in plugins):
                raise ValueError("Backplane expected absent")
        else:
            if (
                len(entries) != 1
                or entries[0]["gitCommitSha"] != revision
                or entries[0]["version"] != version
            ):
                raise ValueError("Installed revision/version/cardinality mismatch")
            tree = self.command(
                [
                    "git",
                    "ls-tree",
                    "-r",
                    revision,
                    "--",
                    "skills",
                    "plugin.json",
                    ".claude-plugin/plugin.json",
                    ".claude-plugin/marketplace.json",
                    "README.md",
                ]
            )
            for line in tree.splitlines():
                metadata, relative = line.split("\t", 1)
                blob = metadata.split()[2]
                installed = Path(entries[0]["installPath"]) / Path(relative)
                verify_file(installed, blob)
                files.append(
                    {
                        "path": relative,
                        "blob": blob,
                        "sha256": self.hash_file(installed),
                    }
                )
        upstream = self.root / ".agents" / "superpowers"
        tracked_upstream = run_cli(["git", "ls-files"], cwd=upstream).splitlines()
        normal = Path.home() / ".claude"
        normal_files = []
        for relative in (
            "settings.json",
            "plugins/installed_plugins.json",
            "plugins/known_marketplaces.json",
        ):
            if (normal / relative).is_file():
                normal_files.append(
                    {"path": relative, "sha256": self.hash_file(normal / relative)}
                )
        preservation = {
            "normalProfile": normal_files,
            "upstreamRegistry": registry["superpowers@superpowers-dev"],
            "upstreamMarketplace": [
                item for item in marketplaces if item["name"] == "superpowers-dev"
            ],
            "upstreamFiles": [
                {"path": relative, "sha256": self.hash_file(upstream / relative)}
                for relative in tracked_upstream
                if (upstream / relative).is_file()
            ],
            "upstreamHead": run_cli(["git", "rev-parse", "HEAD"], cwd=upstream).strip(),
            "upstreamStatus": run_cli(
                ["git", "status", "--porcelain"], cwd=upstream
            ).splitlines(),
            "sentinel": self.hash_file(self.profile / "preservation-sentinel.txt"),
            "refs": self.command(["git", "show-ref"]).splitlines(),
            "issue": json.loads(
                self.command(
                    [
                        "gh",
                        "issue",
                        "view",
                        "19",
                        "--repo",
                        REPOSITORY,
                        "--json",
                        ISSUE_FIELDS,
                    ]
                )
            ),
        }
        record = {
            "row": row,
            "plugins": plugins,
            "marketplaces": marketplaces,
            "backplaneFiles": files,
            "preservation": preservation,
        }
        write_json(self.work / f"{row}-snapshot.json", record)
        baseline = read_json(self.work / "comparison-baseline.json")
        compare_preservation(baseline["preservation"], preservation)

        def unrelated(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
            return sorted(
                (item for item in items if item["id"] != BACKPLANE),
                key=lambda item: item["id"],
            )

        compare_preservation(unrelated(baseline["plugins"]), unrelated(plugins))
        print(f"{row}: {len(files)} exact source files; preservation PASS", flush=True)
        return record

    @staticmethod
    def hash_file(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest().upper()

```

### replay_python.py

SHA-256: `3d5830f410b3cdeae0408fd7a76e3bd252bca0ce0336347d09a41812c523e836`

```python
"""Execute the exact Python guide blocks in one disposable-profile session."""

from contextlib import redirect_stdout
from pathlib import Path
import re
import sys
from typing import Any

from lifecycle import BASELINE, FIXTURE, Harness


def main(*, extract_only: bool = False) -> None:
    root = Path(__file__).resolve().parents[3]
    harness = Harness(root)
    guide = root / "docs" / "installing-claude-code.md"
    blocks = re.findall(
        r"(?ms)^```python\r?\n(.*?)^```", guide.read_text(encoding="utf-8")
    )
    if len(blocks) != 9:
        raise ValueError("Expected nine Python lifecycle blocks")
    for index, block in enumerate(blocks):
        compile(block, f"{guide.name}:block-{index}", "exec")
    if extract_only:
        extracted = harness.work / "guide_python.py"
        extracted.write_text("\n\n".join(blocks), encoding="utf-8", newline="\n")
        print(f"Extracted and compiled {len(blocks)} blocks, {extracted.stat().st_size} bytes")
        return
    answers = iter([str(harness.profile), str(harness.catalog), BASELINE, FIXTURE])

    def answer(prompt: str) -> str:
        value = next(answers)
        print(f"{prompt}{value}", flush=True)
        return value

    state: dict[str, Any] = {"input": answer, "__name__": "__guide_replay__"}
    log = harness.work / "python-guide-replay.txt"
    print(f"Exact Python guide replay log: {log}", flush=True)
    with (
        log.open("w", encoding="utf-8", newline="\n") as transcript,
        redirect_stdout(transcript),
    ):
        harness.snapshot("python-before-replay", BASELINE, "0.1.0")
        for index, block in enumerate(blocks):
            print(f"Executing exact Python guide block {index}", flush=True)
            manifest = harness.catalog / ".claude-plugin" / "marketplace.json"
            before_catalog = manifest.read_bytes()
            exec(compile(block, f"{guide.name}:block-{index}", "exec"), state)
            row = f"python-guide-{index}"
            revision = None if index in (4, 7) else FIXTURE if index == 3 else BASELINE
            version = None if revision is None else "0.1.1" if index == 3 else "0.1.0"
            harness.snapshot(row, revision, version)
            if index == 6 and manifest.read_bytes() != before_catalog:
                raise ValueError("Unavailable candidate changed catalog")
            if index in (2, 3, 5, 8):
                harness.discovery(row)
            elif index == 7:
                harness.discovery(row, absent=True)
        print("All nine Python lifecycle blocks replayed; B restored.", flush=True)
    print("Python lifecycle replay PASS; B restored.", flush=True)


if __name__ == "__main__":
    main(extract_only="--extract-only" in sys.argv[1:])

```

### test_lifecycle.py

SHA-256: `5b4825e97128460715841c98073133b3506aece87624c09e34ee842ff902de6e`

```python
"""Regression checks for portable, disposable test orchestration."""

import os
from pathlib import Path
import sys
import tempfile
import unittest

from lifecycle import compare_preservation, run_cli, verify_file, validate_revision


class PortableOrchestrationTests(unittest.TestCase):
    def test_child_receives_utf8_paths_and_scoped_environment(self):
        with tempfile.TemporaryDirectory(prefix="backplane space é ") as folder:
            before = os.environ.get("SP_BP_TEST_SENTINEL")
            output = run_cli(
                [
                    sys.executable,
                    "-c",
                    "import os; print(os.environ['SP_BP_TEST_SENTINEL']); print(os.getcwd())",
                ],
                cwd=Path(folder),
                overrides={"SP_BP_TEST_SENTINEL": "portable-é"},
            )
            lines = output.splitlines()
            self.assertGreaterEqual(len(lines), 2)
            self.assertEqual(lines[0], "portable-é")
            self.assertEqual(Path(lines[1]).resolve(), Path(folder).resolve())
            self.assertEqual(os.environ.get("SP_BP_TEST_SENTINEL"), before)

    def test_snapshot_key_order_does_not_hide_changed_values(self):
        compare_preservation(
            {"a": 1, "b": {"sentinel": "original"}},
            {"b": {"sentinel": "original"}, "a": 1},
        )
        with self.assertRaisesRegex(ValueError, "Preservation"):
            compare_preservation({"sentinel": "original"}, {"sentinel": "changed"})

    def test_installed_blob_check_rejects_changed_bytes(self):
        with tempfile.TemporaryDirectory() as folder:
            installed = Path(folder) / "skill.md"
            installed.write_bytes(b"hello\n")
            verify_file(installed, "ce013625030ba8dba906f756967f9e9ca394464a")
            installed.write_bytes(b"hello\r\n")
            with self.assertRaisesRegex(ValueError, "byte mismatch"):
                verify_file(installed, "ce013625030ba8dba906f756967f9e9ca394464a")

    def test_moving_ref_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "40-character"):
            validate_revision("main")
        validate_revision("b0d702f8821d6d29184118410ec6ff2d8fb63438")


if __name__ == "__main__":
    unittest.main()

```
