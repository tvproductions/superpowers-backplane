# Python wheel and uvx preflight proof

Observed 2026-09-27 on Windows in the uncommitted `design/sdd-ecosystem-v1` worktree. The local Python 3.13 wheel was built with `uv build`:

```text
Successfully built dist\superpowers_backplane-1.0.0.dev0.tar.gz
Successfully built dist\superpowers_backplane-1.0.0.dev0-py3-none-any.whl
```

From the separate repository root checkout, outside the source worktree, the exact built wheel ran with Astral's `uvx` in offline mode:

```powershell
uvx --offline --from C:\Users\Jeff\source\repos\agents\superpowers-backplane\.worktrees\sdd-ecosystem\dist\superpowers_backplane-1.0.0.dev0-py3-none-any.whl backplane preflight --repo tvproductions/superpowers-backplane
```

Exit 0:

```json
{"heavy_readiness": "UNKNOWN", "issue_count": 21, "recorded_issue_count": 0, "repository": "tvproductions/superpowers-backplane"}
```

The same wheel invocation from inside the active worktree also exited 0 with the same four fields. The independent GraphQL total was 21, matching the collected issue count. `preflight` is read-only and reports `UNKNOWN` by design because live issues have not been migrated. This proves a local Windows wheel entry point under `uvx`, including an offline cached run; it does not prove generate/check, Python runtime availability on a clean adopter, published distribution, Claude Code, OpenCode, macOS, or Linux.
