# Host Installation Leaf Rescoping Evidence

- Design draft: docs/superpowers/specs/2026-09-19-host-installation-leaf-rescoping-design.md
- Execution plan draft: docs/superpowers/plans/2026-09-19-host-installation-leaf-rescoping.md
- Functional authority: docs/superpowers/specs/2026-09-19-v0.1-adoption-installation-contract-design.md
- Scope: native issue graph and ownership only; no host package or guide test.

## Pre-mutation baseline

Read-only gh intake on 2026-09-19 found #1 open with nine children; #11 and
#12 open under #1, each with one backplane:backlog label, zero sub-issues, and
a historical closed #2 blocker. #11 and #12 each block #6. #6 has five native
blockers: #3 (closed), #4, #5, #11, and #12. #11 updatedAt was
2026-09-19T14:11:46Z; #12 was 2026-09-19T14:11:57Z; #6 was
2026-08-23T13:55:24Z. Exact-title issue list returned no proposed C1-C3 or
O1-O5 issue. The six backplane lifecycle labels exist with contract-matching
descriptions. GitHub CLI help exposed issue create --parent, --body-file, and
--label, plus issue edit --add-blocked-by and --body-file.

## RED ownership observation

The approved four-host matrix assigns whole-host Claude work to #11 and both
OpenCode variants to #12, and its historical GREEN note still calls #3 open.
Neither host issue has smaller implementation children or a current plan.
The target graph keeps #11/#12 as executable final leaves and creates eight
sibling leaves under #1, so the present ownership text cannot describe the
target graph.

## Prepared mutation set

Ten complete issue bodies are in ignored local scratch at
.superpowers/sdd/2026-09-19-host-leaf-rescoping/: C1-C3, O1-O5,
final-11, and final-12. Each has the required executable-leaf headings.
The exact post-creation ownership text is drafted in ownership-draft.md in
that same directory. Native parentage and dependencies will be applied as
GitHub relationships; body text does not substitute for those fields.

## Native graph and documentation verification

Pending approved graph publication and issue mutation. Record actual issue
URLs, blocker edges, all open-issue labels, #6 pilot blocker set, document
diff checks, and final integrated source revision here.
