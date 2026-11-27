# Change Brief

Current structured decisions use route schema v2; legacy inspection is not a readiness result.

```text
TASK_ID =
TARGET_REPOSITORY =
BASE_HEAD =
REVIEW_TARGET_HEAD = <sha | PENDING>
ROUTE_STAGE = AUTHORITY_AUTHORING | IMPLEMENTATION | OPERATION
AUTHORITY_ACCEPTED_IN_BASE = YES | NO | NOT_APPLICABLE
GOAL_OR_TARGET =
CURRENT_GAP =
AUTHORITY_ACTION = REUSE | AMEND | SUPERSEDE | NEW |
                   AMEND_OR_NEW_PENDING_OWNERSHIP
PRIMARY_AUTHORITY = <ID@revision | NONE>
RELATED_AUTHORITIES = <IDs@revisions | NONE>
ATOMIC_SPEC_IMPLEMENTATION_PERMITTED = YES | NO
PLAN_LEVEL = NONE | BRIEF | EXEC_PLAN
ASSURANCE_LEVEL = ROUTINE | DURABLE | CONTROLLED
```

## Scope

```text
IN_SCOPE =
OUT_OF_SCOPE =
ALLOWED_EFFECTS =
FORBIDDEN_EFFECTS =
```

## Delivery continuity (only for release/recovery or expanding work)

Reuse this Brief, task, PR, or existing release record; do not create a second authority tree.

```text
DELIVERY_ID = <original business outcome; retain across candidate/packet renames>
FROZEN_ACCEPTANCE = <accepted scope and Done-When references, not new product law>
APPLICABLE_GATES = <finite operation/release gate references and status>
VALID_BLOCKERS = <all current valid blockers; do not hide secondary ones>
PRIMARY_BLOCKER = <current execution priority, or NONE>
REVIEW_REPAIR_ROUNDS = <cumulative unsuccessful rounds for this delivery>
LAST_REAL_ACTION = <executed action and result, or explicit waiting state>
```

Use the cumulative history to spot repeated work without new evidence and consider a smaller scope or simpler authorized path. This template sets no numeric cutoff or new gate; task-specific budgets need applicable authorization. Gates satisfied plus valid authorization means perform the next real action. Fresh production preconditions, genuine risks, and required evidence still apply; the record itself grants no permission.

## Relevant knowledge

```text
OBSERVATIONS =
WORKING_GUESS = <only when interpretation affects routing>
EVIDENCE_NEEDED =
```

Each Evidence item states which decision or acceptance result it can change.

## Modeling and verification (affected behavior only)

Assess each behavior change under the grammar's Model-guided development rule.
Use one sentence or references when sufficient; use only the applicable fields
below. Unchanged behavior checks its existing assumptions/mapping. Editorial or
cosmetic work skips this section rather than filling an empty form.

```text
AFFECTED_BEHAVIOR_AND_PROPERTY = <original outcome and properties at risk>
MODEL_CHOICE = <exact existing model/property revision | minimum new/repaired model | no critical mechanism, with reason>
MODEL_BOUNDARY = <entities/state/transitions/assumptions/reachable examples and counterexamples, or reference>
REQUIREMENT_TO_MODEL = <key requirement/acceptance IDs -> model definitions, properties, or explicit empirical-only target>
MODEL_TO_LEAN = <model property IDs -> theorem/proof revision, assumptions, toolchain and result; include unproved obligations>
MODEL_TO_CODE = <model entities/states/transitions/observations -> implementation repository, commit, files/symbols and mapping>
IMPLEMENTATION_REFINEMENT = <concrete-to-model relation and evidence: proof, contract tests, property tests, trace comparison, fault injection; state exact scope>
VERIFICATION_CHOICE = <reuse proof | formalize now | defer with reason, gap, controls, owner and trigger | not applicable with reason>
IMPLEMENTATION_MAPPING = <code/input revision, concrete-to-model mapping and supported premises>
EVIDENCE_LAYERS = <model result / implementation correspondence / original acceptance; retain unknown or unexecuted parts>
TRACEABILITY_GAPS = <missing link, why non-blocking or blocker under existing Contracts, owner and closure trigger>
SHARED_FOLLOW_UP = <reusable correction with owner and link, or NONE>
```

Critical mechanisms need a reviewable model before dependent implementation.
Proof deferral cannot waive an existing proof gate. Upstream model work and
unrelated formalization do not automatically block a bounded authorized repair.

## Model convergence (conditional)

```text
MODEL_CONVERGENCE_APPLICABLE = YES | NO

# Remaining fields are required only when MODEL_CONVERGENCE_APPLICABLE = YES;
# when NO, skip them and keep the normal route.
RETAIN = <distinct or still-supported entities kept without merge>
RETIRE = <obsolete executable paths that exit execution>
MIGRATE = <consumers moved to the current model>
TEMPORARY_BRIDGE = <bounded compatibility, or NONE>
REAL_CONSUMERS = <actual consumers of any retained bridge or legacy path>
BRIDGE_EXIT_CONDITION = <exit date or objectively verifiable condition, or NONE>
```

## Execution controls

```text
EXECUTION_MANDATE = <reference | inline authorization | NOT_APPLICABLE>
MUTATION_AUTHORIZATION = VALID | INVALID | NOT_APPLICABLE
ISOLATED_WRITE_SURFACE = <worktree/ref/tree coordinates | NOT_APPLICABLE>
CONTROLLED_RUNBOOK = <embedded/reference | NOT_APPLICABLE>
SPEC_GAP_DEPENDENCY = NONE | NON_LOAD_BEARING | LOAD_BEARING
LIVE_AUTHORITY_GAP = NONE | DETECTED
OWNER_DECISION_REQUIRED = YES | NO
EMERGENCY_STATE = NONE | ACTIVE
INCIDENT_REFERENCE = <reference | NOT_APPLICABLE>
```

## Stop

```text
DONE_WHEN =
EXPANSION_TRIGGER = <condition | NOT_APPLICABLE>
NEXT_REAL_ACTION = <product-facing action | NOT_APPLICABLE>
NEXT_ACTION = CONTINUE | STOP | RE_PREFLIGHT | OWNER_DECISION
```


## Refinement and environment evidence (conditional)

For critical stateful behavior, use these fields when they materially help the
change; otherwise reference an existing record or state why not applicable.

```text
CONCRETE_ABSTRACT_RELATION = <R(concrete, abstract) and state mapping>
INITIAL_STATE_CORRESPONDENCE = <evidence or UNKNOWN>
STEP_SIMULATION = <proof | trace/property tests with bounded scope | deferred with owner/trigger>
OBSERVATION_MAPPING = <events/returns/persisted reads -> model observations>
STRUCTURED_TRACE = <schema, trace IDs, code/model revisions, causal fields, or NOT_APPLICABLE>
MODEL_ORACLE_AND_PBT = <oracle, seed/replay, fault classes and exact coverage, or NOT_APPLICABLE>
RUNTIME_INVARIANTS = <invariants and failure behavior, or NOT_APPLICABLE>
ENVIRONMENT_ASSUMPTIONS = <ASM IDs -> probes, timing, validity, failure behavior, blind spots>
PROBE_EVIDENCE = <actual PASS/FAIL/UNKNOWN, environment snapshot, time and provenance>
VERIFIER_NEGATIVE_CONTROLS = <invalid transition/stale or forged trace/UNKNOWN probe tests, or reason not applicable>
EVIDENCE_INVALIDATION = <affected proof/test/probe evidence and recheck decision>
```

A trace/test result is bounded execution evidence, not a full refinement proof.
A positive probe is snapshot-scoped and requires a soundness argument. Preserve
UNKNOWN for unavailable, stale, incomplete or unexecuted evidence.


## Toolchain selection (conditional)

For non-trivial model-based assurance, record the actual tools used and their exact versions/configuration. Do not list tools that were not executed.

```text
TOOLCHAIN_PROFILE = <profile ID/revision | NOT_APPLICABLE>
MODEL_LANGUAGE_AND_VERSION = <tool/version | NOT_APPLICABLE>
MODEL_CHECKER_AND_SCOPE = <tool/version/bound/config | NOT_APPLICABLE>
PROOF_TOOLCHAIN = <tool/version/axiom audit | NOT_APPLICABLE>
PROPERTY_TESTER = <tool/version/seed/replay policy | NOT_APPLICABLE>
IMPLEMENTATION_ADAPTER = <path/symbol/revision | NOT_APPLICABLE>
TRACE_SCHEMA_AND_VALIDATOR = <schema/verifier revision | NOT_APPLICABLE>
ASSUMPTION_PROBE_RUNNER = <tool/revision/TTL | NOT_APPLICABLE>
CI_IDENTITY_AND_REQUIRED_CHECK = <independent check identity | NOT_APPLICABLE>
TOOLCHAIN_LOCK = <lockfile/container digest/receipt | NOT_APPLICABLE>
LIMITATIONS = <bounds, excluded paths, unexecuted checks, unknowns>
```

A tool appearing in the reference guide is not evidence that the consumer adopted or ran it. Bounded model checks, finite PBT and observed traces must retain their own evidence type; they cannot be promoted to a general program proof.
