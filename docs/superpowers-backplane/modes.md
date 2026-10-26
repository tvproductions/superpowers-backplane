# Lite and heavy modes

## Ownership and status

Backplane owns these mode definitions and the associated requirements tracking,
issue classification/lifecycle labels, backlog monitoring, release monitoring
and handoff workflows. gz-skills-first-starter refers here; it supplies shared
engineering and release policy rather than a parallel lifecycle. gz-skills
supplies portable procedures and its existing explicit profile-selection helper.
Superpowers supplies feature design, planning, implementation and review.

This document records the operator's October 26, 2026 ownership decision and
the intended modes. It does not establish a newly implemented mode switch,
monitoring service, completed release system or end-to-end host acceptance.
Use the [governance contract](governance.md) for existing workflow semantics and
the current handoff/native issues for verified delivery and remaining work.

## Mode definitions

| Mode | Intended participation |
| --- | --- |
| Lite | Portable engineering procedures and bounded development work without requiring Backplane's ongoing product-wide requirements, backlog and release lifecycle. Existing project records and handoffs remain authoritative; portable handoff/release procedures may be used under project policy. |
| Heavy | Superpowers feature work coordinated by Backplane's product-wide requirements, labels, dependencies, backlog/release monitoring and handoff continuity, with gz-skills procedures available beneath that workflow. Readiness requires the actual selected capabilities and host integration to be verified. |

The distinction is the extent of ongoing product management, not weaker quality
or permission to skip adopted release policy. For starter-governed projects,
both modes retain that starter's applicable engineering, SemVer and major-PRD
requirements. Unrelated consumers keep their own policy; selecting a mode alone
does not adopt the starter or mandate its Python/tooling choices.

Mode selection is explicit. The existing gz-skills setup helper records
`lite` or `heavy` in its existing two-field settings schema. Preserve that
contract and existing choices. A pending/null selection is not a third mode.
A stored choice is intent, not proof of installation, active orchestration or
delivered monitoring. Do not migrate settings, infer a choice from installed
plugins or activate Backplane merely because this document exists.

## Continuity and release monitoring

Requirements remain in approved project documents/issues, with traceable
references to work and accepted delivery evidence. Native GitHub issues and
relationships retain their identity and state; labels describe classification
and lifecycle. Backlog monitoring reports readiness, dependencies, blockers and
progress under those authorities.

Release monitoring accounts for selected scope, requirement coverage, validation
gaps and readiness under the project's release policy. It does not equate
completion, a milestone or a green check with permission to publish. The
project's authorized release procedure, optionally using `gzs-release`, owns
publication and verification.

Handoffs preserve the work's intent, consumed issue/spec/plan revisions,
completed work, evidence, unresolved obligations and resume point across
sessions or machines. Reconcile live repository and GitHub state on resume;
a checkpoint is a dated account, not a second mutable authority.

Keep unfinished capabilities and unavailable host evidence explicit. Until
the selected workflow is ready and explicitly adopted, preserve the project's
existing authorities rather than moving their management into the template.
