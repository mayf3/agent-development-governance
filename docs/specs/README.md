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
| `AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0` | accepted | implementation | contracts | Current active bootstrap authority for the V0 reusable governance distribution |
| `AGENT_DEVELOPMENT_GOVERNANCE_V1` | proposed | implementation | contracts | Proposed whole-authority successor introducing goal-driven three-axis routing and bounded execution mandates |

## Bootstrap note

The initial repository necessarily began before an accepted Spec existed in its base. The bootstrap exception is exhausted and must not be reused for V1 authoring, implementation, or consumer work.

## V1 authoring note

The proposed V1 does not become active and does not supersede V0 merely by existing on a branch. Independent review, authorized atomic acceptance, final-head recheck, and merge into the designated authority branch remain required. Distribution implementation follows in a separate change based on accepted V1.
