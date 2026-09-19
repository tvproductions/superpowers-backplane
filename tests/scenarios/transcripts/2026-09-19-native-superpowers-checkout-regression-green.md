# Checkout regression GREEN response

Reject `/agents/superpowers`. Its origin is `obra/superpowers-plus`, its working tree is dirty, and it lacks `skills/writing-skills/SKILL.md`. The manager’s preference does not make it a compatible upstream checkout.

Use the unused destination for a separate managed checkout of `obra/superpowers` with `gh repo clone obra/superpowers <unused-destination>`. Inspect the latest published release with `gh release view --repo obra/superpowers --json tagName,publishedAt,url` and select that stable release. The user has not selected the edge channel, so do not use the default branch.

Verify the exact origin, clean status, resolved commit, and all four required upstream skills. Then run the compatibility preflight: authenticated `gh`, the required real-issue intake fields and CLI capabilities, all five named conformance checks, and fresh-session discovery of upstream and Backplane skills. Record the source, release, commit, `gh` version, intake result, and Backplane skill hashes. An incomplete or failed check means compatibility is unconfirmed.

Treat later upstream changes as separate updates. Record the current revision, refuse a dirty or unknown installation, review the candidate release notes, and obtain explicit authorization for that revision change before fetching and switching releases. Re-run the preflight and conformance checks; restore the recorded prior revision if compatibility fails where possible. No project language runtime is required.
