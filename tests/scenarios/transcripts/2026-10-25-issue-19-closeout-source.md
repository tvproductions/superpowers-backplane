# Issue 19 native closeout helper

Actual source used after the published integrated satisfaction evaluation. uv-managed Python 3.14.9; Ruff format/check and ty passed. No new product runtime.

SHA-256: `f17ca315615e566fb5311ffe4ace958ec7b313738fa6ef5a4c8506dcdafcc462`

````python
"""Complete explicitly authorized #19 after published exact-target evidence."""

import json
from pathlib import Path

from lifecycle import ISSUE_FIELDS, Harness, read_json, write_json

root = Path.cwd()
work = root / ".sp-bp/work/issue-19"
out = work / "issue19-closeout"
out.mkdir(exist_ok=True)
h = Harness(root)
repo = "tvproductions/superpowers-backplane"
storage = "cde87943bdac5e92cab2eb21c2685251f7aab5d1"
delivery = "7d7ecac36f8dc74ce1a0895ab934468332f92f53"
verification = read_json(work / "integrated/verification.json")
assert verification["result"] == "PASS" and verification["delivery"] == delivery
assert h.command(["git", "rev-parse", "HEAD"]).strip() == storage
assert not h.command(["git", "status", "--porcelain"]).strip()
evaluation = "tests/scenarios/2026-10-25-issue-19-satisfaction.md"
for path in (
    evaluation,
    "tests/scenarios/2026-10-25-issue-19-integrated-verification.json",
):
    local = h.command(["git", "rev-parse", f"{storage}:{path}"]).strip()
    remote = json.loads(
        h.command(["gh", "api", f"repos/{repo}/contents/{path}?ref={storage}"])
    )["sha"]
    assert local == remote, path
command = ["gh", "issue", "view", "19", "--repo", repo, "--json", ISSUE_FIELDS]


def intake(name):
    record = json.loads(h.command(command))
    write_json(out / f"{name}.json", record)
    return record


before = intake("before")
expected = read_json(
    root / "tests/scenarios/2026-10-25-issue-19-review-submission.json"
)["after"]
for key in expected:
    if key != "updatedAt":
        assert expected[key] == before[key], key
assert before["state"] == "OPEN" and [x["name"] for x in before["labels"]] == [
    "backplane:review"
]
assert before["subIssues"]["totalCount"] == 0 and all(
    x["state"] == "CLOSED" for x in before["blockedBy"]["nodes"]
)
url = f"https://github.com/{repo}/blob/{storage}/{evaluation}"
new_body = (
    before["body"].rstrip()
    + f"\n\nIntegrated evaluation: [Issue #19 satisfaction assessment]({url}) evaluates delivery `{delivery}` from merged PR #36. All #19 criteria and verification seams are SATISFIED in the recorded Windows Claude scope, with exact current-delivery installation/discovery and protected-state verification. Its evidence storage commit `{storage}` is distinct from the tested delivery. The earlier design-preparation statement is historical. Final Claude acceptance #11, release and broader host/stack acceptance remain separate.\n"
)
body_path = out / "body-with-evaluation.md"
body_path.write_text(new_body, encoding="utf-8", newline="\n")
h.command(["gh", "issue", "edit", "19", "--repo", repo, "--body-file", str(body_path)])
after_pointer = intake("after-pointer")
assert after_pointer["body"].replace("\r\n", "\n") == new_body.replace("\r\n", "\n")
for key in before:
    if key not in ("body", "updatedAt"):
        assert before[key] == after_pointer[key], key
comment = f"Issue #19 SATISFIED at integrated delivery {delivery} (PR #36); published evaluation: {url}\n\nOperator explicitly approved final publication/merge, integrated verification and completed closure. The merged tree exactly equals approved head ade4e438d156ea7bb68a5e3b009718fde3b39a43; all 308 tracked blobs matched gh-served source. Nine guide Python blocks match the full 3.14.9 replay, four legacy blocks parse unchanged, strict validation and five regressions/Ruff/ty pass. Current disposable installed package is exactly {delivery}, version 0.1.0; all 21 source blobs and actual three-skill discovery pass with protected state preserved. Retained 23/23 behavioral expectations apply to unchanged canonical skills/upstream 7.0.1; no new prompt set is claimed. Real #34 verified completion and actual same-marketplace sentinel preservation resolve lifecycle/review obligations.\n\nFresh whole-change review's sole Important evidence gap is resolved. Two historical transcript-only formatting minors are retained; the unfiltered full whitespace check is not clean. Windows Claude scope only; no #11 acceptance, release, tag, Project or repository checkpoint claim.\n\nPre-closure reconciliation: full native intake preserved objective, scope, criteria, parent #1, closed blocker #18 and blocking #11, no children or closing PRs, and exactly backplane:review. The evaluation-pointer body edit is editorial and changes no requirement/delivery input; re-fetch immediately before closure."
comment_path = out / "evaluation-comment.md"
comment_path.write_text(comment, encoding="utf-8", newline="\n")
comment_url = h.command(
    ["gh", "issue", "comment", "19", "--repo", repo, "--body-file", str(comment_path)]
).strip()
closing = intake("immediately-before-close")
for key in after_pointer:
    if key != "updatedAt":
        assert closing[key] == after_pointer[key], key
h.command(["gh", "issue", "close", "19", "--repo", repo, "--reason", "completed"])
closed = intake("closed-before-label-removal")
assert closed["state"] == "CLOSED" and closed["stateReason"] == "COMPLETED"
assert [x["name"] for x in closed["labels"]] == ["backplane:review"]
h.command(
    ["gh", "issue", "edit", "19", "--repo", repo, "--remove-label", "backplane:review"]
)
final = intake("final")
assert (
    final["state"] == "CLOSED"
    and final["stateReason"] == "COMPLETED"
    and final["labels"] == []
)
for key in closing:
    if key not in ("state", "stateReason", "labels", "updatedAt"):
        assert final[key] == closing[key], key
parent = json.loads(
    h.command(["gh", "issue", "view", "1", "--repo", repo, "--json", ISSUE_FIELDS])
)
dependent = json.loads(
    h.command(["gh", "issue", "view", "11", "--repo", repo, "--json", ISSUE_FIELDS])
)
write_json(out / "parent.json", parent)
write_json(out / "dependent.json", dependent)
assert parent["state"] == dependent["state"] == "OPEN"
assert all(x["state"] == "CLOSED" for x in dependent["blockedBy"]["nodes"])
write_json(
    out / "result.json",
    {
        "delivery": delivery,
        "evaluation_storage": storage,
        "evaluation": url,
        "comment": comment_url,
        "result": "CLOSED/COMPLETED",
        "revision": final["updatedAt"],
        "labels": [],
        "parent_open": True,
        "parent_completed_children": parent["subIssuesSummary"]["completed"],
        "parent_total_children": parent["subIssuesSummary"]["total"],
        "issue11": "OPEN/backlog; native blockers resolved, plan absent, not ready or selected",
        "no_release": True,
    },
)
print(
    "Issue #19 CLOSED/COMPLETED verified, no lifecycle labels; #11 and parent remain open"
)
````
