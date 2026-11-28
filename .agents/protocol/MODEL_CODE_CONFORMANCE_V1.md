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


## 9. Reference toolchain (select by assurance need)

This protocol defines evidence obligations, not a universal mandated toolchain.
The owning repository selects tools proportional to the behavior and risk.
Pin exact tool versions, configuration, adapter revision and CI environment.

| Need | Practical reference | Scope and limitation |
|---|---|---|
| State-machine specification and simulation | Quint; existing TLA+ models may remain TLA+ | Explicit states, actions, invariants and scenarios; model quality still needs requirement review |
| Finite state exploration | TLC | Exhaustive only within the declared finite model/parameter scope |
| Symbolic/bounded exploration | Apalache | Record bound, parameters and solver; bounded results are not unbounded proofs |
| Structural satisfiability/counterexamples | Alloy 6 | Record finite scope; does not establish production code conformance |
| Mathematical theorem proof | Lean 4 | Bind theorem to exact model/property and audit transitive axioms/toolchain |
| Model-to-code replay | Quint Connect for Rust; project-owned adapters for other languages | Do not claim official Dart/Kotlin support unless an adapter is actually maintained and tested |
| Stateful property testing | Hypothesis (Python), Kotest (Kotlin), proptest (Rust), fast-check (TypeScript); Dart package:test plus a project harness, with third-party stateful libraries evaluated before adoption | Record seed, replayable command sequence and shrink result; finite testing is not a general proof |
| Runtime causal correlation | OpenTelemetry TraceId/SpanId/parent/links plus a correctness-event schema | OpenTelemetry correlates spans but sampling, drops and export gaps mean it does not prove trace completeness |
| Evidence graph | Generated JSON/JSON Schema and deterministic checker | Derived index only; never a manually maintained second source of truth |

A tool reference is not a required dependency. A project may use another tool when it supplies equivalent, reviewable evidence. In particular, Quint Connect's documented integration is Rust-oriented; other language support is a consumer-owned adapter obligation.

## 10. Recommended CI sequence and typed outcomes

For a critical stateful slice, a practical pipeline is:

1. **Freeze coordinates** — exact Spec, model, theorem, implementation, mapping, verifier, toolchain and environment revisions.
2. **Check traceability** — duplicate IDs, dangling links, required REQ→MODEL/ACC coverage and MODEL/PROP→THM/MAP coverage.
3. **Check model sanity** — non-empty initial state, satisfiable constraints, required success-path witnesses, required positive and negative scenarios.
4. **Explore the model** — TLC exhaustive finite scope or Apalache bounded/inductiveness checks; preserve bounds and counterexamples.
5. **Check Lean proofs** — clean build, theorem/property binding, toolchain pin, transitive axiom audit and approved trust base.
6. **Run implementation adapters** — model-generated commands/traces against the real state core; record PBT seeds and minimized counterexamples.
7. **Validate runtime traces** — transition legality, exact revisions, causal constraints and explicit completeness/watermark status.
8. **Check environment assumptions** — probe freshness, scope hash, failure behavior and UNKNOWN handling.
9. **Run independent negative controls** — illegal transition must be rejected; missing event must be INCOMPLETE/UNKNOWN; stale coordinates must be STALE; expired assumption must withdraw the dependent guarantee.
10. **Run original acceptance** — execute the original Spec/Contract acceptance in its target environment.

Use typed results such as:

```text
MODEL_PROVEN
MODEL_CHECKED_EXHAUSTIVE_WITHIN_SCOPE
MODEL_CHECKED_BOUNDED
PROGRAM_VERIFIED
TRACE_CONFORMANT
TRACE_INCOMPLETE
TRACE_DRIFTED
TESTED
SIMULATED
ASSUMPTIONS_VALID
UNKNOWN
STALE
ACCEPTED
```

These are claim types, not an automatic promotion ladder. For example, `TRACE_CONFORMANT` cannot be promoted to `PROGRAM_VERIFIED`, and neither implies `ACCEPTED`.

## 11. Machine-readable evidence coordinates

Where the assurance claim warrants it, the Conformance Record should bind the following coordinates (reuse existing project IDs and receipts; do not require empty fields for unrelated routine work):

```text
SPEC_REVISION = <authority/spec revision>
MODEL_REVISION = <exact model source revision>
MODEL_CHECKER_AND_VERSION = <tool/version or NOT_APPLICABLE>
MODEL_CHECK_SCOPE = <finite scope/bound/inductive claim>
LEAN_TOOLCHAIN = <exact version or NOT_APPLICABLE>
LEAN_AXIOM_AUDIT = <receipt/hash or NOT_APPLICABLE>
IMPLEMENTATION_REVISION = <commit>
MAPPING_REVISION = <adapter/map commit>
PBT_FRAMEWORK_AND_VERSION = <tool/version or NOT_APPLICABLE>
PBT_SEED_AND_REPLAY = <seed/path/corpus or NOT_APPLICABLE>
TRACE_SCHEMA_REVISION = <schema revision>
TRACE_VALIDATOR_REVISION = <verifier commit>
TRACE_COMPLETENESS_RECEIPT = <close/watermark/sequence receipt>
ASSUMPTION_PROBE_REVISION = <probe commit>
ENVIRONMENT_SNAPSHOT_AND_TTL = <scope hash/time/expiry>
VERIFIER_NEGATIVE_CONTROL_RECEIPT = <run/artifact>
EVIDENCE_GRAPH_HASH = <generated graph hash or NOT_APPLICABLE>
ORIGINAL_ACCEPTANCE_RECEIPT = <original ACC evidence>
```

A missing or inapplicable item must be stated explicitly. Do not fabricate a PASS for unavailable tools or unexecuted stages. The graph, manifest and receipts are derived evidence; the accepted Spec and project model remain their respective semantic authorities.

For a detailed tool selection and adapter implementation reference, consumers may pin an exact revision of the shared [Model Engineering Toolchain guide](https://github.com/mayf3/primitives/blob/63d9854bf35aa14522461f1725cdc357973d73a5/MODEL_ENGINEERING_TOOLCHAIN.md). The guide is supplemental engineering material, not Product Authority or a permission source.
