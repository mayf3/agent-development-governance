# Model-Code Conformance V1

**Status: implementation guidance under the accepted model-guided development authority.**
This document defines evidence practices inside the existing PREFLIGHT, Contract,
Assurance, review, and stop rules. It adds no new approval axis, universal
mandatory tool, or automatic consumer adoption.

## 1. Purpose and claim vocabulary

A model proof establishes a property of the declared model under its premises.
It does not by itself establish that a concrete implementation follows that
model or that the premises hold in a running environment.

Keep these results separate and bind each to exact coordinates:

- `MODEL_PROVEN`: named property and model revision checked with the named toolchain,
  assumptions, axioms and excluded obligations.
- `IMPLEMENTATION_CONFORMANT`: named implementation revision conforms within
  an explicit scope and evidence method.
- `ASSUMPTIONS_VERIFIED`: required environmental premises have current,
  scope-bound evidence for the observed environment snapshot.
- `PRODUCT_ACCEPTED`: the original task/Contract passed its actual acceptance.

These are independent dimensions, not a linear status ladder. Missing,
unexecuted, partial, stale, or unavailable evidence remains `UNKNOWN`.

## 2. Concrete-to-abstract refinement

For critical stateful behavior, identify concrete state (C), abstract state
(A), and a relation (R(c,a)) explaining how a concrete state represents an
abstract state.

A refinement argument should state:

1. **Initial correspondence** — every in-scope concrete initial state relates
   to an allowed abstract initial state.
2. **Step simulation** — each in-scope concrete transition from (c) to (c'),
   starting with (R(c,a)), is matched by zero or more abstract transitions
   from (a) to (a'), ending with (R(c',a')).
3. **Observation mapping** — concrete events, return values and persisted
   observations map to model events and state.
4. **Boundaries** — excluded I/O, runtime, compiler, FFI, storage and external
   services are named rather than silently assumed correct.

Zero-step matching permits internal/stuttering steps; it does not prove business
progress. If the requirement needs a visible abstract action for every concrete
operation, use a stronger project-specific relation. Safety simulation does not
prove liveness, fairness, termination, or successful external effects.

Use the strongest affordable evidence and name it accurately: code-coordinate
mapping, contract tests, runtime assertions, trace comparison, stateful property
testing, bounded model checking, or a machine-checked refinement proof. Passing
a finite test suite is not a full refinement proof.

## 3. Structured traces

For asynchronous, concurrent, multi-process or recovery-sensitive mechanisms,
prefer structured JSONL events. A project schema should include at least:

```json
{
  "schema": "model-trace/v1",
  "run_id": "opaque-run-id",
  "seq": 42,
  "component": "engine-lifecycle",
  "transition_id": "T_ENGINE_DIE_STALE",
  "from": "RUNNING",
  "event": "PROCESS_DIED",
  "to": "STOPPED",
  "cause_id": "opaque-cause-id",
  "parent_seq": 41,
  "code_revision": "git-sha",
  "model_revision": "git-sha",
  "environment_id": "sanitized-profile"
}
```

Projects may add typed payloads such as guard inputs, generation IDs, request
IDs and external-effect receipts. Do not rely on wall-clock timestamps alone
for cross-thread/process causality; use sequence, parent/correlation IDs or an
explicit happens-before relation.

A trace validator should check schema, legal transitions, event identity,
version/generation attribution, causal constraints, and exact model/code
coordinates. Truncated collection, dropped events, malformed records, unknown
versions or unavailable inputs must fail or produce `UNKNOWN`, never PASS.
Retain the raw trace and a reproducible normalized projection with provenance
and hashes. A trace proves only the recorded execution path.

## 4. Model-based testing and runtime invariants

Where feasible, separate a pure transition/reducer core from I/O and UI shells.
Feed the same deterministic event sequence to the executable model oracle and
the real state core; compare observations after each step.

For risk-relevant state machines, use reproducible stateful property tests and
fault injection for normal paths, duplicate/late/reordered events, concurrency,
timeouts, cancellation, stop/restart, crash/recovery, empty/full queues,
partial persistence and unknown external-effect outcomes. Record seed, event
sequence, environment and exact code/model revisions. Minimize and preserve
failing traces as regression inputs.

Runtime invariant checks should identify the invariant, state, triggering event,
transition ID and causal context. The owning product decides whether a violation
blocks, isolates, degrades or hands off; silent success is not an acceptable
substitute for an explicit failure state.

## 5. Environmental assumptions and probes

For each load-bearing environmental assumption, record:

| Field | Required meaning |
|---|---|
| Assumption ID | Stable identifier, e.g. `ASM-NET-001` |
| Proposition | Exact condition the model relies on |
| Owner/boundary | Application, OS, network, database, external service or operator |
| Probe | Executable check, external guarantee or human observation |
| Timing | Startup, before use, periodic, during operation or recovery |
| Validity | Snapshot, version, timestamp, lease or expiry |
| Failure behavior | Block, degrade, isolate, retry or human handoff |
| Evidence | Actual result, environment, revision, time and provenance |
| Blind spots | What the probe cannot detect and its own trust boundary |

A sound positive probe has an explicit obligation:

`probe(e) = PASS -> assumption(e)`

This conclusion applies only to the observed environment snapshot (e).
Startup success does not establish that a mutable condition remains true later.
Recheck before use or during operation, or use a lease/monitor with explicit
expiry and failure semantics. Timeout, stale data, unavailable probe, version
mismatch or permission failure is not PASS.

The probe implementation, execution identity, endpoint, credentials path,
measurement coverage and collector are themselves part of the trusted boundary.
A probe result is evidence, not an axiom that reality will remain unchanged.

## 6. Agent change separation and negative controls

When a change touches a critical model/property:

- A business implementation repair must not silently weaken the model,
  invariant, test oracle or counterexample to obtain green results.
- A model or assumption change records before/after semantics, rationale,
  affected theorems, mappings, consumers and invalidated evidence; route
  requirement/Contract meaning changes through existing authority rules.
- A validator, oracle, probe or evidence-adapter change is itself a verification
  mechanism change. Add negative controls for illegal transitions, fabricated
  coordinates, truncated traces, stale snapshots and UNKNOWN probe outcomes.
- Separate authoring from independent semantic review for load-bearing claims.
  If the same Agent changes implementation and verifier, require an independent
  review or independently controlled negative/positive tests.
- Classify failures as requirement gap, model defect, unmet assumption,
  implementation drift, verifier defect or insufficient evidence. Keep an
  unresolved cause UNKNOWN.

This is proportional: it does not require multiple Agents for every low-risk
change. It requires that the party changing the object under test cannot silently
change the acceptance oracle and declare itself correct.

## 7. Evidence invalidation

Bind conformance evidence to model/property revision, theorem/toolchain/axiom
audit, implementation commit and dependencies, trace/test input and seed,
environment snapshot, verifier revision, probe time/validity, and original
acceptance coordinates.

Changes to any load-bearing coordinate trigger an affected-scope impact check.
Invalidate and rerun dependent evidence; reuse unaffected evidence only with an
explicit bounded rationale. A historical PASS never transfers automatically to
a new code, model, verifier or environment revision.

## 8. Proportional adoption

- Pure/stateless low-risk logic may use ordinary unit/contract tests.
- Critical lifecycle, authorization, concurrency, persistence, retry/recovery
  and external-effect mechanisms should use an explicit model and the strongest
  practical combination of trace, property testing, probes and proof.
- A small stable pure kernel may justify verified extraction; its host/FFI/I/O
  boundary remains explicit.
- Empirical goals such as usability, visual quality, naturalness and learning
  outcomes require their own real evaluation.

Use the existing Change Brief, Review Record and Conformance Record. Do not
create a parallel approval workflow or block unrelated authorized work with
optional formalization. The project's accepted Contracts and proof gates remain
the authority for what is mandatory.


## 9. Toolchain selection and consumer adoption

This protocol defines assurance obligations, not a universal tool mandate. Select the smallest toolchain that can produce the required evidence for the affected behavior. Record the tool, exact version/container digest, command, configuration/bounds, input hashes, output receipt, and limitations in the existing Change Brief or Conformance Record.

A practical reference profile is maintained in the shared primitives repository: [Model Engineering Toolchain](https://github.com/mayf3/primitives/blob/1f3d2d9a2a2fa90daf24bceca5b6ba6a4dadac86/MODEL_ENGINEERING_TOOLCHAIN.md). It is a reference architecture, not a live dependency or automatic consumer update. A consumer adopting it MUST pin an exact primitives source commit in its own adoption/source-lock record and MUST NOT rely on a moving main branch.

### Tool selection guide

| Need | Candidate | Evidence boundary |
|---|---|---|
| State-machine specification | Quint; existing TLA+ projects may retain TLA+ | Model source and assumptions; not production-code proof |
| Finite state exploration | TLC | Exhaustive only within the declared finite state/configuration scope |
| Symbolic/bounded exploration | Apalache | Record bound, finite parameters, solver and version; bounded results are not unbounded proof |
| Relational satisfiability / structural counterexamples | Alloy 6 | Record scope; not arbitrary unbounded behavior |
| Key mathematical properties | Lean 4 | Bind theorem, model revision, toolchain and axiom audit |
| Rust model-to-code MBT | Quint Connect; proptest for general PBT | Quint Connect's published integration is Rust-focused; other languages need their own adapters |
| TypeScript command/state testing | fast-check | Use command model runner; scheduled runner can explore async interleavings, within generated tests |
| Python stateful testing | Hypothesis RuleBasedStateMachine | Generated finite sequences and shrunk counterexamples |
| Kotlin property testing | Kotest | Add explicit scheduler/fault harness for concurrency claims |
| Dart/Flutter | package:test baseline; evaluate kiri_check or property_testing | Treat third-party stateful libraries as candidates until tested against the consumer's actual reducer and replay needs |
| Cross-process correlation | OpenTelemetry Trace/Span/Links | Correlation only; correctness completeness requires a separate ledger/protocol |

Do not require all tools in one project. Do not select a tool because it appears in a template. Tool maturity, platform compatibility, license, maintenance, determinism, shrinking/replay, and adapter trust must be evaluated for the actual project and pinned version.

### Minimum adoption record

For any non-trivial model-based verification route, record:

```text
TOOLCHAIN_PROFILE = <profile ID/revision>
MODEL_LANGUAGE = <tool/version | NOT_APPLICABLE>
MODEL_CHECKER = <tool/version/config/bound | NOT_APPLICABLE>
PROOF_TOOLCHAIN = <Lean/Dafny/Verus/etc exact version | NOT_APPLICABLE>
PROPERTY_TESTER = <tool/version/seed policy | NOT_APPLICABLE>
IMPLEMENTATION_ADAPTER = <path/symbol/revision | NOT_APPLICABLE>
TRACE_SCHEMA_AND_VALIDATOR = <schema/verifier revision | NOT_APPLICABLE>
ASSUMPTION_PROBE_RUNNER = <tool/revision | NOT_APPLICABLE>
CI_IDENTITY_AND_REQUIRED_CHECK = <independent workflow/check identity>
TOOLCHAIN_LOCK = <lockfile/container digest/receipt>
LIMITATIONS = <scope, bounds, excluded paths, unavailable guarantees>
```

### P0 execution gates

A first pilot should be one critical state machine, not a cross-project platform. It must freeze the original Spec, failure evidence and exact code coordinates; establish model non-emptiness and a required success witness; check required negative scenarios; prove selected properties or clearly label bounded model checks; drive the real SUT through an adapter; validate trace completeness; check assumption freshness; run positive and negative controls; and finally execute the original Acceptance.

At minimum, negative controls must show:
- illegal transition → FAIL / TRACE_DRIFTED;
- missing event or unclosed trace segment → UNKNOWN / TRACE_INCOMPLETE, never PASS;
- expired or scope-mismatched assumption evidence → STALE/UNKNOWN and the dependent guarantee is withdrawn.

A positive control must also pass, so an always-failing validator cannot satisfy the gate. The coding Agent may generate adapters and tests, but a protected/independent CI identity must execute the final checks. Changes to the verifier, normalizer, trace schema or negative-control corpus are verification-mechanism changes and must rerun the verifier's own conformance suite.

The consumer owns business semantics, adapters, runtime evidence and Acceptance. The shared primitives repository owns reusable mathematical/tooling interfaces. Governance owns authority, change separation, evidence review and merge/acceptance gates. No business FSM is moved into the shared primitives repository.
