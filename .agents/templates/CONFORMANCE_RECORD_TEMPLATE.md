# Conformance Record

## Bound tuple

```text
REPOSITORY =
PRIMARY_AUTHORITY =
AUTHORITY_REVISION =
IMPLEMENTATION_BASE_COMMIT =
IMPLEMENTATION_COMMIT =
ENVIRONMENT =
EVALUATED_AT =
EVALUATOR_ID =
ASSURANCE_LEVEL = ROUTINE | DURABLE | CONTROLLED
REVIEW_SCOPE = AFFECTED | FULL
EXECUTION_MANDATE = <reference | NOT_APPLICABLE>
RECEIPT = <reference | NOT_APPLICABLE>
```

## Affected-surface justification

- affected Contracts:
- directly dependent accepted invariants:
- omitted Contracts and why unaffected:
- reason full matrix is or is not required:

## Contract matrix

| Contract | Implementation / operation | Mechanism | Observation IDs | Evidence IDs | Result |
|---|---|---|---|---|---|
| `CTR-EXAMPLE-001` | `path:symbol` or operation | test/probe/query/manual | `OBS-...` | `EVD-...` | VERIFIED / DRIFTED / UNKNOWN / NOT_APPLICABLE |

Every `NOT_APPLICABLE` result requires a Contract-derived reason.

## Model, implementation, and original acceptance evidence (when applicable)

When an assurance claim relies on a model, reference each layer separately.
Use only the affected scope; this table adds no approval stage or product gate.
Editorial/cosmetic work does not require an empty model-evidence table.

| Layer | Bound target and evidence | Actual result, scope and limitations |
|---|---|---|
| Model | Exact model/property revision; theorem/checker/toolchain; assumptions, axioms and excluded obligations | Proven, bounded, conditional, deferred or unexecuted, with its actual evidence |
| Implementation mapping | Code/input revision; state/action/observation mapping; premise evidence and failure-boundary checks | Formal refinement or scoped tests/traces, without conflating them |
| Original acceptance | Original task/Contract, environment, input and artifact/run coordinates; applicable executed acceptance | Actual required outcome and remaining unknowns, including required human evaluation |

A model proof alone cannot promote the aggregate to product acceptance. Deferred
proof records retain reason, remaining gap, controls, owner and an explicit
completion/reassessment trigger; an accepted proof gate remains binding.
For counterexample repairs, retain the original issue and acceptance, identify
which layer changed, and record the original acceptance result after repair.
Reused evidence requires an affected-coordinate impact check.

## Aggregate

```text
IMPLEMENTATION_STATE = NOT_STARTED | IN_PROGRESS | COMPLETE
VERIFICATION_STATE = NOT_RUN | PARTIAL | SUFFICIENT
CONFORMANCE_RESULT = UNKNOWN | VERIFIED | DRIFTED
CONTRACTS_TOTAL =
CONTRACTS_VERIFIED =
CONTRACTS_DRIFTED =
CONTRACTS_UNKNOWN =
CONTRACTS_NOT_APPLICABLE =
DONE_WHEN_MET = YES | NO
EXPANSION_TRIGGERED = YES | NO
IMPLEMENTATION_READY_TO_MERGE = YES | NO
OPERATION_COMPLETE = YES | NO | NOT_APPLICABLE
NEXT_ACTION = CONTINUE | STOP | RE_PREFLIGHT | OWNER_DECISION
```

Any drift produces aggregate `DRIFTED`; all applicable Contracts verified with sufficient Evidence produces `VERIFIED`; otherwise `UNKNOWN`.

`VERIFIED` applies only to the exact authority/implementation/environment/time tuple. A changed coordinate does not inherit it.

Each load-bearing result names `EVD-*` relations with source Observations, target Contract, relation, exact coordinates, sufficiency, limitations, and provenance.


## Refinement and environment conformance (when applicable)

| Item | Bound coordinate / evidence | Result and limitation |
|---|---|---|
| Concrete/abstract relation | model revision, relation ID, code mapping | |
| Initial correspondence | concrete initial states and abstract initial states | |
| Step simulation | proof or bounded test/trace method, exact scope | |
| Observation mapping | event schema, projection and persisted observations | |
| Trace validation | raw trace hash, schema, code/model revisions, validator revision | |
| Model-based tests | oracle revision, seed, replay corpus, fault coverage | |
| Runtime invariants | invariant IDs, enforcement behavior and observations | |
| Assumption probes | ASM IDs, probe revision, environment snapshot, time/validity | |
| Probe soundness | justification that positive result implies premise for that snapshot | |
| Negative controls | illegal transition, incomplete/stale trace, UNKNOWN probe, forged coordinates | |
| Evidence invalidation | changed coordinates, affected evidence and rerun/impact rationale | |

A trace or finite property-test run is bounded evidence, not a complete
refinement proof. A probe PASS is snapshot-scoped, not a future guarantee.
Keep unexecuted, stale, partial, unavailable and UNKNOWN evidence visible.
