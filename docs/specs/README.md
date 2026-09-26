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
| `AGENT_SIX_PACK_DELIVERY_PROFILE_V1` | accepted | implementation | contracts | Define a faithful six-role software-delivery profile with exact-commit handoffs, mutation hardening, and independent final QA |
| `AGENT_MODEL_CONVERGENCE_V1` | accepted | implementation | contracts | Define historical-model convergence and subtraction-first refactoring; distributed since v1.1.0, with consumer-local adoption still required |

`AGENT_MODEL_CONVERGENCE_V1` is accepted source-repository authority on `main`; its distributed implementation shipped in v1.1.0. The [author scenario probes](../rationale/model-convergence/SCENARIO_REVIEW.md) and PR #16 acceptance discussion are historical provenance, not pending activation steps. Source acceptance, distribution publication, consumer adoption, and actual cleanup remain distinct.

`AGENT_OPERATIONAL_LAYER_V1` is accepted and active on `main`.

Its implementation progress, verification coverage, conformance, and release state remain separate from Spec lifecycle. PR #5 does not supersede, amend, implement, or silently reparent it.

`AGENT_SIX_PACK_DELIVERY_PROFILE_V1` is accepted source-repository authority on `main`, governed by Governance V1 and Operational Layer V1. That source acceptance does not activate a six-Agent runtime, change consumers, or authorize consumer product work; runtime implementation and consumer use remain separate.

The `accepted` Governance V1 and `superseded` V0 rows describe the authority currently active on `main`. Governance V1 supersedes only V0 and carries the compatible Operational Layer forward without changing that authority's accepted frontmatter. Future Operational Layer implementation must re-run PREFLIGHT against the exact active Governance V1 and exact accepted Operational Layer revisions; any conflict or semantic parent change requires a separate authority action.

## Bootstrap note

The one-time bootstrap exception is historical and ended when `AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0` became accepted on `main`. It must not be reused for this or any later governance change.

## Proposed release and recovery assurance

| Spec ID | Status | Kind | Implementation authority | Purpose |
|---|---|---|---|---|
| [`AGENT_RELEASE_RECOVERY_ASSURANCE_V1`](AGENT_RELEASE_RECOVERY_ASSURANCE_V1.md) | proposed | implementation | contracts | Define bounded release-artifact, object-role, failure-prestate, test-dimension and recovery-evidence obligations |

This independent docs-only proposal has [source excerpts and mappings](../rationale/release-recovery/SOURCE_MAPPING.md) and [non-authoritative author scenarios](../rationale/release-recovery/SCENARIO_REVIEW.md). It reuses accepted model-convergence obligations without editing them, and does not depend on or modify PR #17. Proposal, source acceptance, distribution implementation/release, consumer-local adoption, and real deployment/recovery verification remain separate. No distribution, consumer, or production behavior is activated by this authoring change.
