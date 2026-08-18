# Repository-local governance

This file contains rules that belong only to `mayf3/agent-development-governance`. It is not part of the reusable consumer distribution.

## Repository purpose

Publish immutable, versioned governance distributions that consuming repositories may explicitly adopt at an exact commit.

## Current authority state

```text
BOOTSTRAP_SPEC = AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0
BOOTSTRAP_SPEC_STATUS = proposed
BOOTSTRAP_EXCEPTION = initial_repository_creation_only
ACCEPTANCE_ACTOR = mayf3 or another explicitly authorized maintainer
STABLE_RELEASE = none
```

The initial repository cannot have an accepted governing Spec already present in its own base branch. That one-time bootstrap fact does not create a reusable exemption for later work.

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
