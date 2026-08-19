# Repository-local governance

This file is owned by the consuming repository and is not overwritten by governance updates.

## Repository identity

```text
REPOSITORY = owner/repository
AUTHORITY_BRANCH = main
GOVERNANCE_LOCK = .agents/governance.lock.json
```

## Authority precedence

```text
<Product Direction authority ID>
> <Architecture / invariant authority IDs>
> accepted governing Specs
> code, tests, runtime, and operational records
```

## Acceptance actors

```text
SPEC_ACCEPTANCE_ACTORS = <repository owner or authorized maintainers>
MECHANICAL_EXEMPTION_REVIEWERS = <roles>
EMERGENCY_AUTHORIZATION_ACTORS = <roles>
```

## Governing locations

```text
PRODUCT_DIRECTION = <path or NONE>
ARCHITECTURE = <paths or NONE>
SPECS = docs/specs/
INVESTIGATIONS = <GitHub Issues / docs/investigations / other stable location>
CONFORMANCE_REPORTS = <PR records / docs/reports>
```

## Local extensions

Add repository-specific rules here. Local extensions may refine the vendored governance but may not silently weaken or contradict the adopted version. A deliberate governance change requires an explicit adoption/update decision.
