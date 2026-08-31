## Route

```text
GOAL_OR_TARGET =
CURRENT_GAP =
AUTHORITY_ACTION = REUSE | AMEND | SUPERSEDE | NEW |
                   AMEND_OR_NEW_PENDING_OWNERSHIP
PRIMARY_AUTHORITY =
AUTHORITY_REVISION =
PLAN_LEVEL = NONE | BRIEF | EXEC_PLAN
ASSURANCE_LEVEL = ROUTINE | DURABLE | CONTROLLED
EXECUTION_MANDATE = VALID | INVALID | NOT_APPLICABLE
SPEC_GAP_DEPENDENCY = NONE | NON_LOAD_BEARING | LOAD_BEARING
LIVE_AUTHORITY_GAP = NONE | DETECTED
```

## Scope and non-goals

Describe the bounded change, allowed/forbidden effects, implementation choices that are not Contracts, and exclusions.

## Evidence and stop

```text
EVIDENCE_NEEDED =
DONE_WHEN =
EXPANSION_TRIGGER =
NEXT_REAL_ACTION =
```

## Validation / conformance

```text
REVIEW_SCOPE = AFFECTED | FULL
IMPLEMENTATION_STATE =
VERIFICATION_STATE =
CONFORMANCE_RESULT =
IMPLEMENTATION_READY_TO_MERGE =
```

Link executed Observations and qualified Evidence; a test filename alone is not Evidence.

## Review / acceptance binding

```text
REVIEW_TARGET_HEAD =
BASE_HEAD =
CURRENT_BASE_HEAD =
REVIEWER_ID =
FINAL_ACCEPTED_HEAD = <authority acceptance only>
SEMANTIC_DELTA_AFTER_REVIEW =
```

## Explicit non-effects

State consumer, runtime, production, permission, Secret, deployment, migration, and GitHub-setting effects that did not occur.
