---
spec_id: AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0
status: accepted
spec_kind: implementation
authority_level: governing_spec
implementation_authority: contracts
scope:
  - agent-development-governance
governed_by: []
external_authorities: []
supersedes: []
superseded_by: null
owners:
  - mayf3
---

# AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0

## 1. Goal

Create a reusable, versioned governance distribution that lets Agent-developed repositories share one semantic grammar and Spec workflow without surrendering their own product authority or accepting mutable remote rules.

```text
GOAL = common development grammar with explicit local adoption
SUCCESS_OUTCOME = a consumer can pin, vendor, read, review, and update the governance as repository-visible authority
```

## 2. Scope and non-goals

### In scope

- six entity primitives plus first-class relational primitive `Evidence`;
- authority precedence and cross-repository boundary;
- Spec lifecycle and format;
- PREFLIGHT / AUTHOR / REVIEW / COMPLIANCE Skill;
- review commit binding;
- accepted-meaning immutability;
- whole-Spec supersession;
- qualified conformance records;
- persistent Investigation Records;
- commit-pinned vendoring and lock integrity;
- draft bootstrap and stable-release path.

### Out of scope

- product rules for Forum, auth-service, Agent Core, or any consumer;
- central Spec registry or database;
- partial or per-Contract supersession;
- automatic semantic review;
- an unbypassable base-branch merge gate;
- bulk migration of historical repository documents;
- runtime fetching of governance rules.

## 3. Authority and dependencies

This is the first repository bootstrap and therefore has no accepted local parent authority already present in its base.

```text
BOOTSTRAP_EXCEPTION = INITIAL_REPOSITORY_CREATION_ONLY
ACCEPTANCE_ACTOR = mayf3 or explicitly authorized maintainer
CENTRAL_REPOSITORY_PRODUCT_AUTHORITY = NONE_OVER_CONSUMERS
```

The distribution becomes authoritative in a consumer only through that consumer’s explicit, commit-pinned adoption and local acceptance.

## 4. Current State

### STATE-001 — Review consensus supports the core direction but requires authority closure

- Subject: proposed Development Grammar and Spec Governance V0 design
- As of artifact: `docs/rationale/review-corpus/` at this Spec revision
- Environment: design review, before independent central-repository acceptance
- Projection: reviewers consistently support the six entity primitives, Evidence relation model, `.agents` / `docs/specs` split, lifecycle/conformance separation, base-branch rule, and four Skill modes; unresolved findings concentrate on authority precedence, immutable accepted meaning, commit-bound review, qualified conformance, and State/Observation boundaries.
- Basis: `OBS-001`, `OBS-002`, `EVD-001`, `CLM-001`

### STATE-002 — Accepted bootstrap candidate exists; no stable release exists yet

- Subject: this repository distribution
- As of artifact: the repository revision containing this Spec
- Environment: Git repository candidate branch and release metadata
- Observed at: 2026-08-19
- Projection: version is `0.1.0-draft.1`; this Spec is prepared as accepted on the candidate branch but becomes active repository authority only after merge; no stable tag exists.
- Basis: repository `VERSION`, `README.md`, this Spec status

## 5. Observations

### OBS-001 — Review direction is strongly positive

- Subject: architecture direction
- Source: persisted owner-supplied review corpus
- Observed at: 2026-08-18
- Method: compare stated verdicts and preserved design elements
- Result: reviews retain the six entity primitives and Evidence relationship, directory split, Spec-first base rule, lifecycle/conformance separation, and Skill modes rather than requesting a redesign.
- Provenance: `docs/rationale/review-corpus/REVIEW_A.md` and `docs/rationale/review-corpus/REVIEW_B.md`

### OBS-002 — Repeated blockers concern type and authority closure

- Subject: blocker themes
- Source: persisted owner-supplied review corpus
- Observed at: 2026-08-18
- Method: synthesize repeated findings
- Result: repeated concerns include parent authority precedence, accepted Contract immutability, exact review revision binding, version-qualified conformance, time-indexed State, and mixed implementation/conformance enums.
- Provenance: `docs/rationale/review-corpus/REVIEW_A.md` and `docs/rationale/review-corpus/REVIEW_B.md`

### OBS-003 — A shared remote branch would be mutable from a consumer’s perspective

- Subject: cross-repository adoption mechanism
- Source: Git semantics
- Observed at: bootstrap design time
- Method: compare floating branch, submodule, and vendored snapshot properties
- Result: a floating branch can change without a consumer commit; a submodule requires separate initialization and exposes a gitlink rather than repository-local file contents; a vendored exact snapshot is present in every clone and update diff.
- Provenance: design analysis recorded in `docs/rationale/REVIEW_SYNTHESIS.md`

### OBS-004 — Reviews recommend different rejection-persistence surfaces

- Subject: rejected/no-change investigation persistence
- Source: persisted owner-supplied review corpus
- Observed at: 2026-08-18
- Method: compare the explicit persistence recommendations in the two unique review artifacts
- Result: `REVIEW_A` requires important no-new-Spec outcomes to persist in a GitHub Issue or Investigation PR, while `REVIEW_B` explicitly recommends adding `rejected` to the governing Spec lifecycle.
- Provenance: `docs/rationale/review-corpus/REVIEW_A.md` section “需要给调查后决定不改留一个轻量持久化出口” and `docs/rationale/review-corpus/REVIEW_B.md` section “当前 Spec 生命周期缺少 rejected”

## 6. Claims and assumptions

### CLM-001 — The framework is a repository-level development type system

- Support state: SUPPORTED
- Supported by evidence: `EVD-001`
- Contradicted by evidence: none known
- Uncertainty: real usage may expose missing ergonomics, but not a need to redesign the primitive split.

### CLM-002 — Vendored, commit-pinned adoption is the safest V0 dependency model

- Support state: SUPPORTED
- Supported by evidence: `EVD-002`
- Contradicted by evidence: none known
- Uncertainty: future package tooling may improve update ergonomics without changing the pinning requirement.

### CLM-003 — Rejected proposals should be persisted outside governing Spec lifecycle

- Support state: INFERRED
- Supported by evidence: `EVD-003`
- Contradicted by evidence: `EVD-004`
- Uncertainty: consumers may choose GitHub Issues or repository Investigation Records as the persistence surface.

## 7. Evidence relations

### EVD-001 — Review observations support the repository-level type-system Claim

- Source observations: `OBS-001`, `OBS-002`
- Target: `CLM-001`
- Relation: SUPPORTS
- Bound coordinates: owner-supplied review corpus as observed on 2026-08-18
- Strength/sufficiency: strong for the bootstrap architecture direction
- Limitations: does not prove long-term ergonomics before real consumer adoption
- Provenance: `docs/rationale/review-corpus/REVIEW_A.md` and `docs/rationale/review-corpus/REVIEW_B.md`

### EVD-002 — Git properties support commit-pinned vendoring for V0

- Source observations: `OBS-003`
- Target: `CLM-002`
- Relation: SUPPORTS
- Bound coordinates: Git semantics and bootstrap design state
- Strength/sufficiency: sufficient for the V0 dependency decision
- Limitations: future packaging may improve ergonomics without relaxing immutable pinning
- Provenance: `docs/rationale/REVIEW_SYNTHESIS.md`

### EVD-003 — Issue/Investigation-PR persistence supports a separate record type

- Source observations: `OBS-004`
- Target: `CLM-003`
- Relation: SUPPORTS
- Bound coordinates: `REVIEW_A` as persisted at this Spec revision
- Strength/sufficiency: inferential rather than decisive
- Limitations: `REVIEW_A` defines a persistence surface but does not explicitly prohibit a `rejected` lifecycle state
- Provenance: `docs/rationale/review-corpus/REVIEW_A.md`

### EVD-004 — Explicit `rejected`-state recommendation challenges the separate-record choice

- Source observations: `OBS-004`
- Target: `CLM-003`
- Relation: CONTRADICTS
- Bound coordinates: `REVIEW_B` as persisted at this Spec revision
- Strength/sufficiency: material counterevidence, not decisive refutation
- Limitations: the recommendation does not resolve the distinction between proposal disposition and active normative authority
- Provenance: `docs/rationale/review-corpus/REVIEW_B.md`

## 8. Decisions

### DEC-001 — Preserve six entity primitives and make Evidence a relational primitive

- Decision owner: repository owner
- Decision: use epistemic entity primitives `Observation`, `Claim`, `State`; normative entity primitives `Goal`, `Decision`, `Contract`; and first-class relational primitive `Evidence` with stable `EVD-*` IDs.
- Rejected alternatives: treat all entity primitives as equivalent document headings; treat Evidence as merely a filename or intrinsic property of an Observation; exclude relations from the primitive vocabulary.
- Reason: the family split prevents State from masquerading as raw truth and Goal from masquerading as obligation, while the relational primitive makes support, contradiction, satisfaction, violation, scope, and limits directly auditable and queryable.
- Owner input remaining: NONE

### DEC-002 — Use local adoption rather than central remote authority

- Decision owner: repository owner
- Decision: consumers vendor an exact commit and accept it locally.
- Rejected alternatives: floating branch dependency; implicit central governance; default Git submodule.
- Reason: local bytes, visible diffs, base-branch availability, and no silent upstream change.
- Owner input remaining: NONE

### DEC-003 — Keep governing lifecycle narrow

- Decision owner: repository owner
- Decision: governing Specs use `proposed`, `accepted`, and `superseded`; rejected/no-change/reuse outcomes use Investigation Records.
- Rejected alternative: add `rejected` to governing authority lifecycle.
- Reason: a rejected proposal never became normative authority and belongs to a different semantic type.
- Owner input remaining: NONE

### DEC-004 — Separate implementation, verification, and conformance dimensions

- Decision owner: repository owner
- Decision: use independent enums for implementation progress, verification coverage, and conformance.
- Rejected alternative: one enum mixing `NOT_STARTED`, `PARTIAL`, `VERIFIED`, and `DRIFTED`.
- Reason: the mixed enum violates the grammar’s own type discipline.
- Owner input remaining: NONE

### DEC-005 — Forbid partial supersession in V0

- Decision owner: repository owner
- Decision: only whole-Spec supersession with atomic backlinks is supported.
- Rejected alternative: prose-defined per-Contract replacement.
- Reason: current metadata cannot compute partial precedence safely.
- Owner input remaining: NONE

### DEC-006 — Bound the one-time repository bootstrap exception

- Decision owner: repository owner
- Decision: the first repository-creation PR may contain the proposed bootstrap Spec and the foundational distribution it specifies because no accepted authority can pre-exist the repository; the exception ends after bootstrap acceptance.
- Rejected alternative: treat initial creation as a reusable waiver for later governance or consumer implementation.
- Reason: bootstrap is logically unavoidable but must not become a permanent bypass.
- Owner input remaining: NONE

## 9. Contracts

### CTR-GOV-001 — Consumer authority remains local

This repository MUST NOT claim automatic product or Spec authority over a consuming repository. A consumer MUST explicitly pin and accept an exact source commit before the distribution becomes local governance.

### CTR-GOV-002 — Distributed governance is immutable by revision

Every consumer adoption MUST record a 40-hex source commit and file digests. The adoption lock MUST distinguish preparation from acceptance: a proposed snapshot MUST NOT claim `accepted_by` or `accepted_at`, and only an authorized finalization may set `adoption.status: accepted`. A floating branch, unqualified `latest`, or mutable remote reference MUST NOT be sufficient adoption identity.

### CTR-GOV-003 — Primitive boundaries are normative

The distribution MUST define `State` as a time-indexed projection with explicit provenance. Interpretive, load-bearing State statements MUST be backed by qualified Observations, necessary Claims, and the Evidence relations that connect those Observations to their targets; a directly recorded State fact MAY cite its exact provenance without inventing an unnecessary Claim. The distribution MUST treat `Evidence` as a first-class relational primitive with stable `EVD-*` IDs, qualified sources, targets, polarity, coordinates, sufficiency, and limitations. It MUST use `SUPPORTED`, `INFERRED`, and `OPEN_ASSUMPTION` for Claim support and MUST NOT use `VERIFIED CLAIM` as a primitive category.

### CTR-GOV-004 — Accepted meaning is immutable

An accepted rule MAY later be replaced, but its old stable ID MUST always retain its original meaning. Accepted Decision and Contract meaning MUST NOT change under the same stable IDs. Contract IDs MUST NOT be renumbered, reused, or repurposed. A strictly additive amendment MAY add new stable IDs only within unchanged Goal, scope, authority, and accepted Decisions, and each new Contract MUST be a bounded elaboration of those accepted Decisions rather than an independent obligation. A new Decision, expanded scope, changed authority ownership, or independent obligation MUST use a new authority; replacement of existing meaning MUST use whole-Spec supersession.

### CTR-GOV-005 — Review is bound to exact revisions

Every acceptance recommendation MUST record reviewed base commit, reviewed Spec commit, reviewer identity, final accepted head, and semantic delta after review. Any semantic delta MUST invalidate the prior review.

### CTR-GOV-006 — Conformance is qualified

A Conformance Record MUST bind Spec revision, implementation commit, environment, evaluation time, verification state, result, and evidence. `VERIFIED` MUST NOT be represented as an unqualified permanent property of a Spec.

### CTR-GOV-007 — Implementation authority is explicit

An accepted Program Spec MUST NOT implicitly authorize child implementation. Each Spec MUST declare `implementation_authority: none | contracts`; non-mechanical implementation requires `contracts` in an accepted Spec already present in the base.

### CTR-GOV-008 — Rejected knowledge persists without becoming authority

Important rejected, no-change, reuse, or deferred investigations MUST be persisted in a stable Investigation Record, issue, or investigation PR. They MUST NOT be represented as accepted or superseded governing authority.

### CTR-GOV-009 — V0 enforcement is represented honestly

The distribution MUST distinguish manual policy, distribution-integrity tooling, future syntax gates, and semantic review. It MUST NOT claim an unbypassable merge gate that has not been implemented and required by repository protection.

### CTR-GOV-010 — Emergency handling cannot create durable bypass

Emergency pre-Spec action MUST be limited to rollback, disablement, shutdown, revocation, or isolation; MUST record owner approval and incident reference; and MUST require post-incident Spec reconciliation for durable repair.

### CTR-GOV-011 — The bootstrap exception is non-reusable

The initial repository-creation change MAY contain this proposed bootstrap Spec and its bounded foundational implementation. The bootstrap MUST remain non-stable until independent review and authorized acceptance. After bootstrap acceptance, this exception MUST NOT authorize later governance implementation, consumer product work, or combined Spec-and-implementation changes.

## 10. Acceptance

### ACC-GOV-001 — Local adoption boundary

- Contracts: `CTR-GOV-001`, `CTR-GOV-002`
- Method: run `tools/vendor.py --apply` into a temporary consumer and inspect the lock and copied bytes
- Environment: local test
- Required evidence: exact source commit, manifest digest, per-file digests, vendored files
- Expected result: proposed and accepted adoption states bind the exact same source identity and no upstream movement changes the consumer without a consumer commit
- Failure condition: update to the upstream working tree changes the consumer without a consumer commit, the declared source commit differs from the clean source checkout, or a proposed lock claims acceptance metadata

### ACC-GOV-002 — Primitive and lifecycle audit

- Contracts: `CTR-GOV-003`, `CTR-GOV-004`, `CTR-GOV-007`, `CTR-GOV-008`
- Method: independent semantic review of `.agents/README.md`, protocol, format, Skill, and templates
- Environment: exact candidate commit
- Required evidence: review record bound to commit
- Expected result: Grammar, protocol, format, Skill, templates, and bootstrap authority use one coherent primitive, mutation, lifecycle, and implementation-authority model
- Failure condition: State may be unsourced, accepted IDs may change meaning, Program Spec may silently authorize code, or rejected proposals enter governing lifecycle

### ACC-GOV-003 — Review binding audit

- Contracts: `CTR-GOV-005`
- Method: compare reviewed Spec commit to final accepted head
- Environment: acceptance PR
- Required evidence: exact SHAs and semantic delta classification
- Expected result: the final accepted head is identical to the reviewed semantics or receives a new independent review
- Failure condition: semantic change occurs after review without a new review

### ACC-GOV-004 — Conformance model audit

- Contracts: `CTR-GOV-006`
- Method: fill Conformance template for at least one implementation and verify separate implementation, verification, and conformance dimensions
- Environment: pilot consumer repository
- Required evidence: persisted Contract matrix
- Expected result: implementation progress, verification coverage, and conformance are independently represented and every VERIFIED result is revision/environment qualified
- Failure condition: `PARTIAL` ambiguously means both progress and conformance, or `VERIFIED` lacks version/environment coordinates

### ACC-GOV-005 — Integrity tool test

- Contracts: `CTR-GOV-002`, `CTR-GOV-009`
- Method: run repository unit tests and manifest check; tamper with a vendored file and verify detection
- Environment: Python standard-library test environment
- Required evidence: command and result
- Expected result: manifest and tests pass on untampered bytes, tampering is detected, and tooling makes no semantic-acceptance claim
- Failure condition: tampering passes or tooling claims semantic acceptance

### ACC-GOV-006 — Emergency boundary review

- Contracts: `CTR-GOV-010`
- Method: semantic review of protocol and Skill emergency sections
- Environment: exact candidate commit
- Required evidence: review finding
- Expected result: pre-Spec action is limited to containment and any durable repair returns to normal Spec governance
- Failure condition: emergency path permits durable new behavior without reconciliation

### ACC-GOV-007 — Bootstrap exception boundary

- Contracts: `CTR-GOV-011`
- Method: inspect local governance, bootstrap Spec, release state, and later-change rules
- Environment: exact candidate commit
- Required evidence: bootstrap remains proposed before review; exception is named initial-only; no consumer inheritance exists
- Expected result: the exception is usable only for this initial repository creation and cannot authorize any later or consumer implementation
- Failure condition: the exception can be invoked after bootstrap acceptance or used to authorize product implementation

### Contract coverage

| Contract | Acceptance | Covered |
|---|---|---|
| `CTR-GOV-001` | `ACC-GOV-001` | YES |
| `CTR-GOV-002` | `ACC-GOV-001`, `ACC-GOV-005` | YES |
| `CTR-GOV-003` | `ACC-GOV-002` | YES |
| `CTR-GOV-004` | `ACC-GOV-002` | YES |
| `CTR-GOV-005` | `ACC-GOV-003` | YES |
| `CTR-GOV-006` | `ACC-GOV-004` | YES |
| `CTR-GOV-007` | `ACC-GOV-002` | YES |
| `CTR-GOV-008` | `ACC-GOV-002` | YES |
| `CTR-GOV-009` | `ACC-GOV-005` | YES |
| `CTR-GOV-010` | `ACC-GOV-006` | YES |
| `CTR-GOV-011` | `ACC-GOV-007` | YES |

## 11. Alternatives and disposition

### ALT-001 — One central repository directly governs all consumers

- Disposition: rejected
- Reason: violates repository ownership and allows remote authority changes outside a consumer base commit.
- What would reopen: an explicit organization-wide authority model with consumer consent and auditable revision pinning.

### ALT-002 — Git submodule as default distribution

- Disposition: rejected for V0 default
- Reason: separate initialization, weaker Agent discoverability, and gitlink-only content in the consumer tree.
- What would reopen: tooling that guarantees initialization, local readability, and reviewable update diffs.

### ALT-003 — Add `rejected` to Spec lifecycle

- Disposition: rejected
- Reason: conflates proposal disposition with normative authority lifecycle.
- What would reopen: evidence that Investigation Records fail to preserve searchable rejection knowledge.

### ALT-004 — Implement full semantic CI before pilot use

- Disposition: rejected for V0
- Reason: semantic completeness and authority interpretation require judgment; real pilots should determine which deterministic checks are valuable.
- What would reopen: repeated, machine-detectable failure patterns across pilot repositories.

## 12. Migration, compatibility, and rollback

```text
MIGRATION = forward-only adoption from the next non-mechanical change
COMPATIBILITY = consumers pin their adopted version; no automatic upstream change
ROLLBACK = revert the consumer adoption/update commit to its prior pin
EMERGENCY_CONTAINMENT = not applicable to distribution content; repository compromise uses normal credential/release incident handling
```

## 13. Open questions

```text
OPEN_OWNER_DECISIONS = NONE
NORMATIVE_TBD = NONE
UNRESOLVED_AUTHORITY_CONFLICT = NONE
PARTIAL_SUPERSESSION = NONE
INDEPENDENT_REVIEW_REQUIRED = YES
READY_TO_MARK_ACCEPTED = YES
```
