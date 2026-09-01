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

## Mandatory write isolation

All write work MUST use an isolated worktree or equivalent isolated write surface. An equivalent surface binds an exact parent, writes only to an isolated ref and the single intended tree, does not mutate another active checkout, and aborts rather than silently adopting target-Head movement.

## Emergency containment

Emergency authorization is limited to rollback, disablement or shutdown, revocation, isolation, or equivalent containment tied to an incident. It MUST NOT introduce durable new behavior; permanent repair returns to normal Product Authority.

## Local extensions

Name stricter rules for combined Spec-delta/code PRs, always-controlled surfaces, review independence, and branch protection. Local rules may refine but not silently weaken the adopted governance.
