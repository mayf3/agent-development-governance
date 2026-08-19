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
| `AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0` | proposed | implementation | contracts | Bootstrap the initial reusable governance distribution and its integrity tooling |

## Bootstrap note

The initial repository necessarily begins before an accepted Spec exists in its base. The bootstrap Spec records that one-time exception. It must not be generalized into a permanent bypass.
