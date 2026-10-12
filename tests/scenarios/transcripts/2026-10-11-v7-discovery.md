All three are **actively discovered** in this session’s supplied skill inventory, rather than merely found on disk. I read each listed `SKILL.md` completely.

Paths below are relative to `C:\Users\Jeff\source\repos\agents\superpowers-backplane`:

| Active inventory name | Discovered path | Resolved junction target |
|---|---|---|
| `superpowers:using-superpowers` | `.agents\skills\superpowers\using-superpowers\SKILL.md` | `.agents\superpowers\skills\using-superpowers\SKILL.md` |
| `superpowers-backplane:managing-superpowers-backlog` | `.agents\skills\managing-superpowers-backlog\SKILL.md` | `skills\managing-superpowers-backlog\SKILL.md` |
| `superpowers-backplane:managing-superpowers-handoffs` | `.agents\skills\managing-superpowers-handoffs\SKILL.md` | `skills\managing-superpowers-handoffs\SKILL.md` |

`git -C .agents/superpowers rev-parse HEAD` returned **`bb92a77741419a4ab5f06e711a283343f1ada0c3`**, exactly matching the requested revision. `SUPERPOWERS.md` and `HANDOFF.md` still record the older `5bf4e78011075bcfc0dc295f0724994cd123ee71`.

No files changed, GitHub contacted, or agents spawned.