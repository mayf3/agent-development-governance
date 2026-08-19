## Change type

```text
CHANGE_CLASS = MECHANICAL | NON_MECHANICAL
PREFLIGHT_MODE = REUSE | AMEND | SUPERSEDE | NEW
PRIMARY_GOVERNING_SPEC = <ID | NONE>
GOVERNING_SPEC_REVISION = <commit/blob | NONE>
SPEC_PRESENT_IN_BASE = YES | NO | NOT_APPLICABLE
```

## What changed

Describe the bounded change.

## Authority and scope

List parent and related accepted authorities. State whether this PR is docs-only, implementation-only, or a mechanical exemption.

## Validation / conformance

For implementation PRs, include the Contract-by-Contract matrix and qualified evidence.

```text
IMPLEMENTATION_STATE = ...
VERIFICATION_STATE = ...
CONFORMANCE = ...
IMPLEMENTATION_READY_TO_MERGE = ...
```

## Review binding for Spec PRs

```text
REVIEWED_BASE_COMMIT = ...
REVIEWED_SPEC_COMMIT = ...
REVIEWER_ID = ...
FINAL_ACCEPTED_HEAD = ...
SEMANTIC_DELTA_AFTER_REVIEW = ...
```
