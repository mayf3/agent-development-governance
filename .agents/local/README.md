# Repository-local governance

This file belongs only to `mayf3/agent-development-governance`. It is not part of the reusable consumer distribution.

## Repository purpose

Publish immutable, versioned governance distributions that consuming repositories may explicitly adopt at an exact commit.

## Current authority state

```text
BOOTSTRAP_SPEC = AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0
BOOTSTRAP_SPEC_STATUS = superseded
BOOTSTRAP_EXCEPTION = closed_after_acceptance
GOVERNANCE_V1_SPEC = AGENT_DEVELOPMENT_GOVERNANCE_V1
GOVERNANCE_V1_SPEC_STATUS = accepted
GOVERNANCE_V1_ACTIVE_ON_MAIN = yes
OPERATIONAL_LAYER_SPEC = AGENT_OPERATIONAL_LAYER_V1
OPERATIONAL_LAYER_SPEC_STATUS = accepted
OPERATIONAL_LAYER_ACTIVE_ON_MAIN = yes
OPERATIONAL_LAYER_IMPLEMENTATION = not_started
ACCEPTANCE_ACTOR = mayf3 or another explicitly authorized maintainer
CONTROLLED_OPERATION_MANDATE_ACTOR = mayf3 or another explicitly authorized operator
STABLE_RELEASE = none
```

A source-repository implementation PR may implement accepted Governance V1 only within its Contracts. It does not automatically authorize consumer product changes, production writes, permissions, credentials, deployment, or Operational Layer implementation.

## Local precedence

```text
Explicit repository-owner direction
> accepted local Product Direction / Architecture authority
> accepted local governing Specs
> valid one-operation Execution Mandate
> repository files, tests, tooling, and runtime observations
```

An Execution Mandate constrains one operation only. It cannot weaken or replace accepted Product Authority.

## Release constraints

- A draft version must not be represented as a stable release.
- Release tags are immutable; changed normative meaning requires a new version.
- Consumer updates pin an exact commit and use a local docs-only adoption PR.
- `distribution/manifest.json` must match all distributed files.
- Integrity and route-consistency tools must not claim semantic acceptance.
