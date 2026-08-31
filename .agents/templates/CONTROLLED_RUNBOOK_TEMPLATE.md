# Controlled Runbook

A Controlled Runbook is an Assurance artifact. It may be embedded in a Brief and does not itself authorize execution or create an ExecPlan.

```text
RUNBOOK_ID =
EXECUTION_MANDATE =
ACTOR_OR_ROLE =
TARGET =
ENVIRONMENT =
EXPECTED_PRE_STATE =
ALLOWED_EFFECTS =
FORBIDDEN_EFFECTS =
MAX_ATTEMPTS =
ABORT_CONDITIONS =
UNKNOWN_OUTCOME_PROBE =
RETRY_RULE =
COMPENSATION_OR_CONTAINMENT =
DONE_WHEN =
NEGATIVE_POSTCONDITIONS =
```

## Preconditions

- exact authority/implementation coordinates:
- mandate validity:
- access/identity:
- backup/rollback or containment:
- Secret-safe logging:
- independent verifier availability:

## Exact operation

1. ...
2. ...

## Receipt

```text
MANDATE_ID
RUNBOOK_ID
ACTOR
ENVIRONMENT
STARTED_AT / ENDED_AT
ATTEMPT
PRE_STATE_REFERENCE
OPERATION_RESULT
POST_STATE_REFERENCE
ABORT / RETRY / COMPENSATION
SECRET_DISCLOSURE = NO
```

## Independent verification

State verifier, exact coordinates, checks, Evidence relation, and result. When Done When is met without an Expansion Trigger, stop.
