**PASS — advertised skill discovery and worktree identity verified.**

Read both requested skills through their advertised inventory paths.

| Check | Observed evidence |
|---|---|
| Actual worktree root | `/Users/jeff/.codex/worktrees/d181/superpowers-backplane` |
| Upstream checkout locator | `.agents/superpowers` resolves to `/Users/jeff/Documents/Code/superpowers-backplane/.agents/superpowers` |
| Upstream skill locator | `.agents/skills/superpowers` resolves to that checkout’s `skills/` |
| Backplane locator | `.agents/skills/managing-superpowers-backlog` resolves to `/Users/jeff/.codex/worktrees/d181/superpowers-backplane/skills/managing-superpowers-backlog`, distinct from the source checkout’s skill tree |
| Shared Git directory | `/Users/jeff/Documents/Code/superpowers-backplane/.git` |
| Starting commit | `82fa208cd81b1ae33a6b24e869220f90c9558312` |
| Branch identity | Detached HEAD: empty branch name, symbolic-ref exit 1, registration marked `detached`, raw HEAD contains the commit |
| Registration | Worktree `.git` pointer and registration back-pointer agree |

Upstream has its own `.git` directory, origin `https://github.com/obra/superpowers.git`, and HEAD `bb92a77741419a4ab5f06e711a283343f1ada0c3`, matching `SUPERPOWERS.md`.

Limitations: this verifies local discovery and identity, not GitHub authentication or compatibility scenarios. macOS Git emitted denied temporary cache-write warnings; direct metadata reads corroborated its results. No mutations, agents, or bookkeeping helpers were used.