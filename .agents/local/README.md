# Repository-local governance

This file contains rules that belong only to `mayf3/agent-development-governance`. It is not part of the reusable consumer distribution.

## Repository purpose

Publish immutable, versioned governance distributions that consuming repositories may explicitly adopt at an exact commit.

## Current authority state

```text
BOOTSTRAP_SPEC = AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0
BOOTSTRAP_SPEC_STATUS = accepted
BOOTSTRAP_EXCEPTION = closed_after_acceptance
OPERATIONAL_LAYER_SPEC = AGENT_OPERATIONAL_LAYER_V1
OPERATIONAL_LAYER_SPEC_STATUS = accepted
OPERATIONAL_LAYER_ACTIVE_ON_MAIN = yes
ACCEPTANCE_ACTOR = mayf3 or another explicitly authorized maintainer
STABLE_RELEASE = none
```

The one-time bootstrap exception ended when the accepted bootstrap Spec merged to `main`. `AGENT_OPERATIONAL_LAYER_V1` is accepted and active on `main`.

PR #3 contained no implementation. Its accepted Contracts may authorize bounded implementation in this repository only through a separate task, worktree, and PR whose base contains the accepted authority. The central Spec does not automatically authorize consumer-repository product changes.

## Local precedence

```text
Explicit repository-owner direction
> accepted local Product Direction / Architecture authority
> accepted local governing Spec
> repository files, tests, tooling, and runtime observations
```

The reusable distribution describes the grammar and process. It does not override explicit product decisions in consuming repositories.

## Release constraints

- A draft version must not be represented as an accepted stable governance release.
- Release tags are immutable; changed normative meaning requires a new version.
- Consumer updates must pin an exact commit and occur through a local docs-only adoption PR.
- `distribution/manifest.json` must match all distributed files.
- Distribution-integrity tools may validate bytes and metadata; they must not claim semantic acceptance.
