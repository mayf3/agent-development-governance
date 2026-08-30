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
| `AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0` | accepted | implementation | contracts | Bootstrap the initial reusable governance distribution and its integrity tooling |
| `AGENT_OPERATIONAL_LAYER_V1` | accepted | implementation | contracts | Define bounded task Skills and a typed, non-normative repository-local Record corpus |

The `accepted` operational-layer row reflects this candidate branch. It becomes active repository authority only after the accepted head passes independent final-head recheck and is merged to `main`.

## Bootstrap note

The one-time bootstrap exception is historical and ended when `AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0` became accepted on `main`. It must not be reused for this or any later governance change.
