# Governing Specs in this repository

The reusable syntax contract is `.agents/protocol/SPEC_FORMAT_V0.md`.

This directory contains repository-local governing Specs. It does not contain the shared distribution files themselves.

Lifecycle:

```text
proposed | accepted | superseded
```

Implementation progress, verification coverage, runtime state, and conformance are recorded separately.

## Current index

| Spec ID | Status | Kind | Implementation authority | Purpose |
|---|---|---|---|---|
| `AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0` | superseded | implementation | contracts | Bootstrap the initial reusable governance distribution and its integrity tooling |
| `AGENT_OPERATIONAL_LAYER_V1` | accepted | implementation | contracts | Define bounded task Skills and a typed, non-normative repository-local Record corpus |
| `AGENT_DEVELOPMENT_GOVERNANCE_V1` | accepted | implementation | contracts | Replace the single heavy non-mechanical route with independent Authority, Plan, and Assurance decisions while preserving V0 protections |

`AGENT_OPERATIONAL_LAYER_V1` is accepted and active on `main`.

Its implementation progress, verification coverage, conformance, and release state remain separate from Spec lifecycle. PR #5 does not supersede, amend, implement, or silently reparent it.

The `accepted` Governance V1 and `superseded` V0 rows reflect this candidate branch. They become active on `main` only after independent final-head recheck and merge; until then `main` remains governed by V0. Governance V1 supersedes only V0 and carries the compatible Operational Layer forward without changing that authority's accepted frontmatter. Future Operational Layer implementation must re-run PREFLIGHT against the exact active Governance V1 and exact accepted Operational Layer revisions; any conflict or semantic parent change requires a separate authority action.

## Bootstrap note

The one-time bootstrap exception is historical and ended when `AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0` became accepted on `main`. It must not be reused for this or any later governance change.
