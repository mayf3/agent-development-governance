# Bootstrap review synthesis

This document records how the initial review feedback was reconciled into the central V0 candidate. It is rationale, not a substitute for the normative grammar, protocol, or Spec.

## 1. Direction retained

The review corpus consistently supported:

- `.agents/` for stable Grammar, Protocol, and Skills;
- `docs/specs/` for repository-owned governing Specs;
- six entity primitives plus first-class relational primitive `Evidence`;
- Spec-first base-branch rule;
- `REUSE / AMEND / SUPERSEDE / NEW` preflight;
- independent `PREFLIGHT / AUTHOR / REVIEW / COMPLIANCE` modes;
- Spec lifecycle separated from implementation reality;
- Contract-by-Contract conformance;
- semantic review separated from deterministic checks.

The bootstrap therefore does not redesign those foundations.

## 2. Authority precedence and central-repository boundary

Problem identified:

- lower-level Specs could appear to override Product Direction;
- current metadata could not compute partial supersession;
- cross-repository dependencies risked becoming accidental governance.

Resolution:

```text
Product Direction
> Architecture / invariant authority
> governing Spec
> code, tests, runtime
```

Lower levels refine but do not override parents. V0 forbids partial supersession. External authorities are referenced at exact revisions and remain owned by their repositories.

The new central repository is a distribution source, not a global product authority. A consumer’s local, commit-pinned adoption is the act that makes the shared rules authoritative there.

## 3. Accepted meaning and review binding

Problem identified:

- same-ID `AMEND` could change an accepted Contract’s meaning;
- a review recommendation could become detached from the final merged content.

Resolution:

- proposed Specs may change freely;
- accepted same-ID edits are editorial or strictly additive only;
- additive items use new stable IDs within unchanged Goal, scope, authority, and accepted Decisions;
- a new Decision or independent obligation uses a new Spec;
- changed existing meaning uses whole-Spec supersession;
- Contract IDs are never renumbered or repurposed;
- review records exact base commit, reviewed Spec commit, reviewer identity, final accepted head, and semantic delta;
- semantic delta after review invalidates the review.

## 4. State, Observation, and Claim

Problem identified:

- “State = what the code actually is” had no branch, deployment, environment, data, or time coordinates;
- unsourced Current State prose could bypass Observation provenance;
- `VERIFIED CLAIM` blurred Claim into Observation.

Resolution:

```text
State = time-indexed projection supported by Observations and Claims
```

Load-bearing State statements cite basis. Claim support is `SUPPORTED`, `INFERRED`, or `OPEN_ASSUMPTION`.

The semantic primitives are grouped into:

```text
Epistemic entities: Observation, Claim, State
Normative entities: Goal, Decision, Contract
Relational primitive: Evidence
```

## 5. Evidence and tests

Problem identified:

`Test ≠ Evidence` was correct in spirit but too broad.

Resolution:

```text
Test Definition ≠ Evidence
Executed Test Result with coordinates = Observation
Qualified Observation-to-target relation = Evidence
```

A file or log is provenance material. Evidence is a first-class relational primitive with its own stable ID, source Observations, target, polarity, coordinates, sufficiency, limitations, and provenance. In a governing Spec it supports or contradicts Claims and State assertions; in a Conformance Record it satisfies, violates, or remains inconclusive for a Contract at bound implementation coordinates. The same Observation can support one Claim and contradict another, so Evidence cannot be reduced to an intrinsic label on the Observation.

## 6. Implementation and conformance dimensions

Problem identified:

One enum mixed progress (`NOT_STARTED`), coverage (`PARTIAL`), knowledge (`UNKNOWN`), and conformance (`VERIFIED`, `DRIFTED`).

Resolution:

```text
IMPLEMENTATION_STATE = NOT_STARTED | IN_PROGRESS | COMPLETE
VERIFICATION_STATE = NOT_RUN | PARTIAL | SUFFICIENT
CONFORMANCE = UNKNOWN | VERIFIED | DRIFTED
```

Conformance is a point-in-time relation over Spec revision, implementation commit, environment, time, and evidence.

## 7. Rejected proposal disagreement

Some reviews recommended adding `rejected` to Spec lifecycle so investigation knowledge would not disappear. Another review preferred preserving the narrow lifecycle and using persistent investigation records.

Resolution:

- governing Spec lifecycle remains `proposed / accepted / superseded`;
- `rejected`, `no_change`, `reuse`, and `deferred` are Investigation Record dispositions;
- important investigation outcomes must persist in a repository file, issue, or investigation PR with a stable link.

Reason:

A rejected proposal never became governing authority. Persisting it is necessary, but classifying it as authority lifecycle would violate the same type separation the framework is designed to enforce.

## 8. Program Specs

Problem identified:

A broad Program Spec could be used as permission to implement all child work.

Resolution:

Every Spec declares:

```text
spec_kind = invariant | program | implementation
implementation_authority = none | contracts
```

Acceptance of a Program Spec does not imply child implementation authority.

## 9. Mechanical and emergency seams

Problem identified:

Authors could label semantic changes as “small refactors,” while strict Spec-first rules could obstruct incident containment.

Resolution:

- uncertain means non-mechanical;
- mechanical exemptions require independent review;
- dependency, schema, permission, lifecycle, retry, timeout, and changed tests are non-mechanical by default;
- emergency pre-Spec action is limited to rollback, disablement, shutdown, revocation, or isolation;
- durable repair requires post-incident Spec reconciliation.

## 10. Dependency mechanism

Options considered:

### Floating branch

Rejected because consumer authority could change without a consumer commit.

### Git submodule

Rejected as the V0 default because Agents may not initialize it, the consumer tree contains a gitlink rather than ordinary files, and update review is less direct.

### Vendored exact snapshot with lock

Selected because the exact rules live in the consumer base, updates are ordinary reviewed diffs, and rollback is a Git revert.

## 11. Adoption truthfulness and integrity

A central distribution introduces a new failure mode that was not present in a single-repository bootstrap: tooling can accidentally claim that a local adoption was accepted merely because files were prepared.

Resolution:

- the first vendor operation writes `adoption.status = proposed`;
- proposed locks have null `accepted_by` and `accepted_at`;
- an authorized local actor performs a separate finalization after review;
- the adoption becomes active only when the accepted snapshot is merged into the designated authority branch;
- the vendor tool verifies that the declared source commit equals the clean source checkout `HEAD`;
- updates refuse to overwrite files that have drifted from the previous lock unless a recovery override is explicit.

## 12. Context loading

The original bootstrap repeated substantial governance content across README and Skill surfaces. The central candidate assigns one owner per layer:

- `.agents/README.md` owns the compact semantic constitution;
- the Skill root is a router;
- `modes/` owns mode-specific procedure and output;
- detailed protocol and format documents are read on demand;
- rationale is never mandatory operating context.

## 13. Deliberate V0 non-goals

- no central Spec registry;
- no database;
- no partial authority graph;
- no semantic CI reviewer;
- no claim that manual instructions are branch protection;
- no bulk history migration;
- no automatic consumer update.

The next phase should be two or three pilot Spec cycles. Deterministic syntax and base-branch gates should be driven by observed repeated failures, not speculative completeness.
