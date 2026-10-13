# Recorded checkpoint file/Git exercise

This is test evidence, not an installation or checkpoint helper. It uses invented records and explicitly declared test paths in the authorized issue-31 worktree. No actual repository product checkpoint or GitHub record was published. The historical two pair commits demonstrate an actual index/tree/parent acceptance boundary. Offline/native tracker conclusions remain simulated in the fixed probe.

~~~sh
#!/bin/bash
set -euo pipefail
root=/Users/jeff/Documents/Code/superpowers-backplane
workspace=/Users/jeff/.codex/worktrees/d181/superpowers-backplane
scratch=.sp-bp/work/2026-10-11-github-governance-bridges-implementation/checkpoint-fixture
pair=tests/scenarios/fixtures/issue-31-checkpoint
mkdir -p "$scratch" "$pair"
guard() {
 test "$(git -C "$root" rev-parse --show-toplevel)" = "$root"
 test "$(git rev-parse --show-toplevel)" = "$workspace"
 test "$(git rev-parse --path-format=absolute --git-common-dir)" = "$root/.git"
 if git symbolic-ref -q HEAD; then exit 1; fi
 git -C "$root" worktree list --porcelain | rg -q -Fx "worktree $workspace"
}
pass() { printf 'PASS %s\n' "$1"; }
render() {
 local json="$1" output="$2" hash
 hash=$(shasum -a 256 "$json" | cut -d ' ' -f 1)
 {
 printf '# Invented checkpoint test fixture\n\n'
 printf 'Capture: %s\nJSON SHA256: %s\n' "$(jq -r .capture.id "$json")" "$hash"
 jq -r '"Mode: " + .capture.mode, "Status: " + .capture.status, "Source: " + .source.commit, "\n## Native hierarchy and delivery\n", (.issues[] | "Issue: " + .id + " parent=" + (.parent_id // "none") + " children=" + (.child_ids|join(",")) + " state=" + .state), "\n## Approved obligation and criterion\n", (.requirements[] | .id+": "+.text+" @"+.authority_id+"/"+.authority_revision), (.criteria[] | .id+": "+.text+" delivery="+(.delivery_commit//"unknown")), "\n## Evidence and claims\n", (.evaluations[] | "Evaluation: "+.id+" "+.result+" verified="+(.verified_commit//"unknown")+" evidence="+(.evidence_ids|join(","))+" applicability="+.applicability), "\n## Dispositions, release target and limitations\n", "No parent dispositions; no milestone/release target observed in this invented scope.", (.limitations[]), "No live product state or remote publication is asserted."' "$json"
 } > "$output"
}
validate_pair() {
 local json="$1" markdown="$2" rendered="$scratch/validation-render.md"
 render "$json" "$rendered"
 cmp -s "$rendered" "$markdown"
}
guard
if test -n "$(git diff --cached --name-only)"; then printf 'Unexpected staged entries; stop\n'; exit 1; fi
jq '.capture.id="fixture-C0"' skills/managing-superpowers-backlog/references/checkpoint-complete-example.json > "$scratch/prior.json"
render "$scratch/prior.json" "$scratch/prior.md"
cp skills/managing-superpowers-backlog/references/checkpoint-complete-example.json "$scratch/candidate.json"
render "$scratch/candidate.json" "$scratch/candidate.md"
validate_pair "$scratch/candidate.json" "$scratch/candidate.md"; pass 'valid exact-byte and readable candidate'
sed 's/Capture: fixture-C1/Capture: wrong/' "$scratch/candidate.md" > "$scratch/wrong-id.md"
if validate_pair "$scratch/candidate.json" "$scratch/wrong-id.md"; then exit 1; fi; pass 'wrong capture ID rejected'
sed 's/JSON SHA256:.*/JSON SHA256: wrong/' "$scratch/candidate.md" > "$scratch/wrong-digest.md"
if validate_pair "$scratch/candidate.json" "$scratch/wrong-digest.md"; then exit 1; fi; pass 'wrong digest rejected'
jq '.evaluations[0].result="UNKNOWN" | .evaluations[0].applicability="unreconciled"' "$scratch/candidate.json" > "$scratch/unknown.json"
render "$scratch/unknown.json" "$scratch/unknown.md"
sed 's/Evaluation: EV1 UNKNOWN/Evaluation: EV1 SATISFIED/' "$scratch/unknown.md" > "$scratch/false-claim.md"
if validate_pair "$scratch/unknown.json" "$scratch/false-claim.md"; then exit 1; fi; pass 'correct-digest false readable SATISFIED rejected'
cp "$scratch/prior.json" "$pair/github-state.json"; cp "$scratch/prior.md" "$pair/state.md"
guard; git add -- "$pair/github-state.json" "$pair/state.md"
test "$(git diff --cached --name-only | wc -l | tr -d ' ')" = 2
guard; git commit -m 'test: record invented prior checkpoint pair for issue 31'
prior_commit=$(git rev-parse HEAD)
printf 'K0 %s\n' "$prior_commit"
prior_json_blob=$(git rev-parse "HEAD:$pair/github-state.json"); prior_md_blob=$(git rev-parse "HEAD:$pair/state.md")
printf 'unrelated sentinel fixture\n' > "$pair/sentinel.txt"
sentinel_sha=$(shasum -a 256 "$pair/sentinel.txt" | cut -d ' ' -f 1)
guard; git add -- "$pair/sentinel.txt"
sentinel_index=$(git ls-files --stage -- "$pair/sentinel.txt")
cp "$scratch/candidate.json" "$pair/github-state.json"
guard; git add -- "$pair/github-state.json"
if validate_pair "$pair/github-state.json" "$pair/state.md"; then exit 1; fi; pass 'interrupted JSON-only install rejected; K0 tree retained'
test "$(git rev-parse HEAD)" = "$prior_commit"
test "$(git rev-parse "HEAD:$pair/github-state.json")" = "$prior_json_blob"
guard; git restore --source "$prior_commit" --staged --worktree -- "$pair/github-state.json" "$pair/state.md"
cmp "$scratch/prior.json" "$pair/github-state.json"; cmp "$scratch/prior.md" "$pair/state.md"
test "$(git rev-parse ":$pair/github-state.json")" = "$prior_json_blob"
test "$(git rev-parse ":$pair/state.md")" = "$prior_md_blob"
test "$(git ls-files --stage -- "$pair/sentinel.txt")" = "$sentinel_index"
test "$(shasum -a 256 "$pair/sentinel.txt" | cut -d ' ' -f 1)" = "$sentinel_sha"
pass 'exact K0 worktree/index restoration preserves unrelated staged sentinel'
# All state in this fixture is test-owned. An unrelated staged entry forbids acceptance.
if test -z "$(git diff --cached --name-only | rg -v '^(tests/scenarios/fixtures/issue-31-checkpoint/(state.md|github-state.json))$')"; then exit 1; fi
pass 'unrelated staged sentinel blocks pair-only commit'
guard; git restore --staged -- "$pair/sentinel.txt"
cp "$scratch/candidate.json" "$pair/github-state.json"
printf 'intervening user-owned fixture edit\n' >> "$pair/github-state.json"
user_sha=$(shasum -a 256 "$pair/github-state.json" | cut -d ' ' -f 1)
if cmp -s "$pair/github-state.json" "$scratch/prior.json" || cmp -s "$pair/github-state.json" "$scratch/candidate.json"; then exit 1; fi
# Ownership failed: do not recover. Observe unchanged bytes before explicit fixture reconciliation.
test "$(shasum -a 256 "$pair/github-state.json" | cut -d ' ' -f 1)" = "$user_sha"
pass 'intervening user edit stops automatic recovery and is preserved'
cp "$pair/github-state.json" "$scratch/preserved-user-edit.json"
# Explicit test-owner reconciliation after stop, rather than automatic recovery.
cp "$scratch/prior.json" "$pair/github-state.json"
# No-prior case in scratch: literal removal of only owned paths, with a retained sentinel.
mkdir -p "$scratch/no-prior"
cp "$scratch/candidate.json" "$scratch/no-prior/github-state.json"
printf 'no-prior sentinel\n' > "$scratch/no-prior/sentinel.txt"
cp "$scratch/no-prior/sentinel.txt" "$scratch/no-prior-sentinel.expected"
cmp "$scratch/candidate.json" "$scratch/no-prior/github-state.json"
rm -- "$scratch/no-prior/github-state.json"
test ! -e "$scratch/no-prior/github-state.json"; test ! -e "$scratch/no-prior/state.md"
cmp "$scratch/no-prior-sentinel.expected" "$scratch/no-prior/sentinel.txt"
pass 'no-prior transaction removes only proven file; preserves directory and sentinel (filesystem scope)'
# Same no-prior owned-index case within authorized Git boundary, never a new fixture repository.
new_pair=tests/scenarios/fixtures/issue-31-checkpoint-no-prior
mkdir -p "$new_pair"; cp "$scratch/candidate.json" "$new_pair/github-state.json"
guard; git add -- "$new_pair/github-state.json"
test "$(git rev-parse ":$new_pair/github-state.json")" = "$(git hash-object "$scratch/candidate.json")"
guard; git restore --source "$prior_commit" --staged --worktree -- "$new_pair/github-state.json" "$new_pair/state.md" 2> "$scratch/no-prior-restore.stderr" || {
 # Absent unstaged path is not known to Git; operate only on the recorded owned entry.
 guard; git restore --source "$prior_commit" --staged --worktree -- "$new_pair/github-state.json"
}
test ! -e "$new_pair/github-state.json"; test ! -e "$new_pair/state.md"
test -z "$(git ls-files --stage -- "$new_pair/github-state.json" "$new_pair/state.md")"
pass 'no-prior owned Git entry and transaction file restored to absence'
cp "$scratch/candidate.json" "$pair/github-state.json"; cp "$scratch/candidate.md" "$pair/state.md"
validate_pair "$pair/github-state.json" "$pair/state.md"
guard; git add -- "$pair/github-state.json" "$pair/state.md"
json_blob=$(git hash-object "$scratch/candidate.json"); md_blob=$(git hash-object "$scratch/candidate.md")
test "$(git rev-parse ":$pair/github-state.json")" = "$json_blob"; test "$(git rev-parse ":$pair/state.md")" = "$md_blob"
test "$(git diff --cached --name-only | wc -l | tr -d ' ')" = 2
guard; git commit -m 'test: accept invented candidate pair after guarded recovery'
accepted_commit=$(git rev-parse HEAD)
test "$(git rev-parse HEAD^)" = "$prior_commit"
test "$(git rev-parse "HEAD:$pair/github-state.json")" = "$json_blob"
test "$(git rev-parse "HEAD:$pair/state.md")" = "$md_blob"
test "$(git diff-tree --no-commit-id --name-only -r HEAD | wc -l | tr -d ' ')" = 2
printf '{"fixture_only":true,"prior_commit":"%s","accepted_commit":"%s","phase":"accepted","json_blob":"%s","markdown_blob":"%s","publication":"NOT PERFORMED"}\n' "$prior_commit" "$accepted_commit" "$json_blob" "$md_blob" > "$scratch/accepted-receipt.json"
pass 'actual K1 pair-only tree/index/parent verification; external receipt finalized without rollback'
test "$(shasum -a 256 "$pair/sentinel.txt" | cut -d ' ' -f 1)" = "$sentinel_sha"
pass 'sentinel preserved across complete native Git exercise'
printf 'K1 %s\n' "$accepted_commit"

~~~
