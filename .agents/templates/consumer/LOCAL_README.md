# Repository-local governance

This file is owned by the consuming repository and is not overwritten by governance updates.

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
> valid one-operation Execution Mandate
> code, tests, runtime, and operational records
```

An Execution Mandate cannot create or weaken Product Contracts.

## Authorized actors

```text
SPEC_ACCEPTANCE_ACTORS =
CONTROLLED_OPERATION_MANDATE_ACTORS =
EMERGENCY_AUTHORIZATION_ACTORS =
INDEPENDENT_DURABLE_REVIEWERS =
```

## Governing locations

```text
PRODUCT_DIRECTION = <path or NONE>
ARCHITECTURE = <paths or NONE>
SPECS = docs/specs/
CHANGE_BRIEFS_AND_EXEC_PLANS = <PR records / docs/changes / other>
INVESTIGATIONS = <Issues / docs/investigations / other>
CONFORMANCE_REPORTS = <PR records / docs/reports>
OPERATION_RECEIPTS = <Secret-safe persistent location>
```

## Local extensions

Name stricter rules for combined Spec-delta/code PRs, always-controlled surfaces, review independence, isolated write surfaces, and branch protection. Local rules may refine but not silently weaken the adopted governance.
