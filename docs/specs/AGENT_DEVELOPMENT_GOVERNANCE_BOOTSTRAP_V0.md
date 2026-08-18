---
spec_id: AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0
status: proposed
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

Create a reusable, versioned development grammar and Spec-governance distribution that Agent-developed repositories can adopt at an exact commit without surrendering local product authority or accepting mutable remote rules.

```text
GOAL = common development grammar with explicit local adoption
SUCCESS_OUTCOME = consumers can pin, vendor, review, accept, use, update, and roll back an exact governance revision
```

## 2. Scope and non-goals

In scope: six entity primitives plus first-class relational primitive `Evidence`; authority precedence; Spec format/lifecycle; PREFLIGHT/AUTHOR/REVIEW/COMPLIANCE; commit-bound review; immutable accepted meaning; whole-Spec supersession; qualified conformance; Investigation Records; exact-commit vendoring; release discipline.

Out of scope: consumer product rules; central Spec registry/database; partial or per-Contract supersession; automatic semantic review; an unbypassable base-branch gate; runtime governance fetching; bulk history migration.

## 3. Authority and dependencies

This is the one-time initial repository bootstrap, so no accepted local parent authority could already exist in its base.

```text
BOOTSTRAP_EXCEPTION = INITIAL_REPOSITORY_CREATION_ONLY
ACCEPTANCE_ACTOR = mayf3 or explicitly authorized maintainer
CENTRAL_REPOSITORY_PRODUCT_AUTHORITY = NONE_OVER_CONSUMERS
```

The distribution becomes authoritative in a consumer only after exact-commit vendoring, independent local review, authorized local acceptance, and merge into that consumer's authority branch.

## 4. Current State

### STATE-001 — Direction retained; authority closure required

- Subject: Development Grammar and Spec Governance V0 design
- As of artifact: owner-supplied review corpus, 2026-08-18
- Projection: reviewers retain the primitive model, `.agents` / `docs/specs` split, base-branch rule, lifecycle/conformance separation, and four Skill modes; blockers concentrate on authority precedence, accepted-meaning immutability, exact review binding, qualified conformance, and State provenance.
- Basis: `OBS-001`, `OBS-002`, `EVD-001`, `CLM-001`

### STATE-002 — No stable release exists

- Subject: this repository distribution
- As of artifact: bootstrap candidate
- Projection: `VERSION = 0.1.0-draft.1`; bootstrap status is proposed; no stable tag exists.
- Basis: repository `VERSION`, `README.md`, and this frontmatter

## 5. Observations

### OBS-001 — Reviews preserve the architecture direction

- Source: owner-supplied review responses
- Observed at: 2026-08-18
- Method: compare verdicts and explicitly retained elements
- Result: reviewers request targeted amendments rather than framework redesign.
- Provenance: external bootstrap review corpus

### OBS-002 — Repeated blockers concern authority and type closure

- Source: owner-supplied review responses
- Observed at: 2026-08-18
- Result: repeated concerns are parent precedence, stable accepted meaning, review revision binding, qualified conformance, time-indexed State, and mixed state enums.
- Provenance: external bootstrap review corpus

### OBS-003 — Floating remote governance is mutable for consumers

- Source: Git dependency semantics
- Method: compare floating branch, submodule, and vendored snapshot
- Result: only a vendored exact snapshot guarantees repository-local bytes and an ordinary consumer update diff without runtime fetch or submodule initialization.
- Provenance: `docs/rationale/REVIEW_SYNTHESIS.md`

### OBS-004 — Reviews disagree about rejected proposals

- Source: owner-supplied review responses
- Result: some recommend a `rejected` Spec state; another recommends separate persistent Investigation Records.
- Provenance: external bootstrap review corpus

## 6. Claims and assumptions

### CLM-001 — This is a repository-level development type system

- Support state: SUPPORTED
- Supported by: `EVD-001`
- Uncertainty: real pilots may expose ergonomic gaps.

### CLM-002 — Exact-commit vendoring is the safest V0 dependency model

- Support state: SUPPORTED
- Supported by: `EVD-002`
- Uncertainty: future packaging may improve ergonomics without weakening pinning.

### CLM-003 — Rejection should persist outside governing lifecycle

- Support state: INFERRED
- Supported by: `EVD-003`
- Contradicted by: `EVD-004`
- Uncertainty: pilots may show that a separate record is too cumbersome.

## 7. Evidence relations

### EVD-001 — Review observations support the type-system Claim

- Source observations: `OBS-001`, `OBS-002`
- Target: `CLM-001`
- Relation: SUPPORTS
- Bound coordinates: review corpus observed 2026-08-18
- Sufficiency: strong for bootstrap direction
- Limitations: does not prove long-term ergonomics

### EVD-002 — Git properties support exact-commit vendoring

- Source observations: `OBS-003`
- Target: `CLM-002`
- Relation: SUPPORTS
- Sufficiency: sufficient for V0 dependency choice
- Limitations: future tooling may change packaging, not identity requirements

### EVD-003 — Lifecycle disagreement supports a separate record type

- Source observations: `OBS-004`
- Target: `CLM-003`
- Relation: SUPPORTS
- Sufficiency: inferential
- Limitations: usability remains unproven

### EVD-004 — The same disagreement challenges the separate-record choice

- Source observations: `OBS-004`
- Target: `CLM-003`
- Relation: CONTRADICTS
- Sufficiency: material counterevidence
- Limitations: does not resolve the authority-type objection

## 8. Decisions

### DEC-001 — Six entity primitives plus relational Evidence

Use epistemic entities `Observation`, `Claim`, `State`; normative entities `Goal`, `Decision`, `Contract`; and first-class relational primitive `Evidence` with stable `EVD-*` IDs. Evidence records source Observations, target, polarity, coordinates, sufficiency, limits, and provenance.

### DEC-002 — Local adoption, not central remote authority

Consumers vendor and accept an exact commit locally. Floating branch dependency, implicit central governance, and a default submodule model are rejected.

### DEC-003 — Narrow governing lifecycle

Governing Specs use `proposed`, `accepted`, and `superseded`. `rejected`, `no_change`, `reuse`, and `deferred` are persistent Investigation Record dispositions.

### DEC-004 — Separate implementation, verification, and conformance

Use independent enums for progress, verification coverage, and conformance. `VERIFIED` is qualified by Spec revision, implementation commit, environment, time, and Evidence.

### DEC-005 — Whole-Spec supersession only in V0

Partial or prose-defined supersession is forbidden until a machine-readable authority graph exists.

### DEC-006 — Bootstrap exception is initial-only

This PR may contain the proposed bootstrap Spec and its bounded foundational implementation because no accepted authority can pre-exist repository creation. The exception ends after bootstrap acceptance and never transfers to consumers.

## 9. Contracts

### CTR-GOV-001 — Consumer authority remains local

This repository MUST NOT claim automatic product or Spec authority over a consumer. A consumer MUST explicitly pin and locally accept an exact revision.

### CTR-GOV-002 — Adoption identity is immutable

Every adoption MUST record a 40-hex source commit, manifest digest, and file digests. Preparation and acceptance MUST be distinct; a proposed lock MUST NOT claim acceptance metadata. Floating references MUST NOT activate governance.

### CTR-GOV-003 — Primitive boundaries are normative

`State` MUST be a time-indexed projection backed by Observations, Claims, and Evidence. `Evidence` MUST be a first-class relation with stable ID, source, target, polarity, coordinates, sufficiency, limits, and provenance. Claim support MUST use `SUPPORTED`, `INFERRED`, or `OPEN_ASSUMPTION`.

### CTR-GOV-004 — Accepted meaning is immutable

An accepted rule MAY be replaced, but its old stable ID MUST retain its original meaning. Existing accepted Decision and Contract meaning MUST NOT change under the same IDs. IDs MUST NOT be renumbered, reused, or repurposed. New Decisions or changed existing meaning require new authority and whole-Spec supersession.

### CTR-GOV-005 — Review binds exact revisions

Acceptance recommendations MUST record reviewed base, reviewed Spec commit, reviewer, final accepted head, and semantic delta. Any semantic delta after review MUST invalidate that review.

### CTR-GOV-006 — Conformance is qualified

A Conformance Record MUST bind Spec revision, implementation commit, environment, time, verification state, result, and Evidence. `VERIFIED` MUST NOT be an unqualified permanent Spec property.

### CTR-GOV-007 — Implementation authority is explicit

Every Spec MUST declare `implementation_authority: none | contracts`. An accepted Program Spec MUST NOT implicitly authorize child implementation. Non-mechanical implementation requires accepted authorizing Contracts already in the base.

### CTR-GOV-008 — Rejected knowledge persists without becoming authority

Important rejected/no-change/reuse/deferred investigations MUST persist in a stable record, issue, or investigation PR and MUST NOT masquerade as accepted or superseded authority.

### CTR-GOV-009 — Enforcement claims are truthful

The distribution MUST distinguish manual policy, integrity tooling, future syntax gates, semantic review, and actual branch protection. It MUST NOT claim an unimplemented merge gate.

### CTR-GOV-010 — Emergency handling cannot create durable bypass

Pre-Spec emergency action MUST be limited to rollback, disablement, shutdown, revocation, or isolation; record owner approval and incident reference; and require reconciliation before durable repair.

### CTR-GOV-011 — Bootstrap exception is non-reusable

The bootstrap MUST remain non-stable until independent review and authorized acceptance. After acceptance, its exception MUST NOT authorize later governance implementation, consumer product work, or combined Spec-and-implementation changes.

## 10. Acceptance

### ACC-GOV-001 — Local adoption boundary

- Contracts: `CTR-GOV-001`, `CTR-GOV-002`
- Method: real vendor round trip into a temporary consumer
- Failure: declared commit differs from clean source HEAD; proposed lock claims acceptance; upstream changes consumer without a consumer commit

### ACC-GOV-002 — Primitive and lifecycle audit

- Contracts: `CTR-GOV-003`, `CTR-GOV-004`, `CTR-GOV-007`, `CTR-GOV-008`
- Method: independent semantic review of Grammar, protocol, format, Skill, and templates
- Failure: unsourced State; Evidence reduced to material; accepted ID changes meaning; Program silently authorizes code; rejected proposal enters authority lifecycle

### ACC-GOV-003 — Review-binding audit

- Contracts: `CTR-GOV-005`
- Method: compare reviewed Spec commit with final accepted head
- Failure: semantic change after review without a new review

### ACC-GOV-004 — Conformance-model pilot

- Contracts: `CTR-GOV-006`
- Method: complete one Contract matrix in a pilot repository
- Failure: progress and conformance are mixed, or `VERIFIED` lacks coordinates

### ACC-GOV-005 — Integrity-tool test

- Contracts: `CTR-GOV-002`, `CTR-GOV-009`
- Method: manifest check, unit tests, and tamper-detection test
- Failure: tampering passes or tooling claims semantic acceptance

### ACC-GOV-006 — Emergency-boundary review

- Contracts: `CTR-GOV-010`
- Method: semantic review of emergency sections
- Failure: emergency path permits durable new behavior without reconciliation

### ACC-GOV-007 — Bootstrap-boundary review

- Contracts: `CTR-GOV-011`
- Method: inspect Spec status, release state, and later-change rules
- Failure: exception can be reused after acceptance or inherited by consumers

Every active Contract above is covered by at least one Acceptance item.

## 11. Alternatives and disposition

- `ALT-001` Central repository directly governs consumers — rejected: violates ownership and base-commit authority.
- `ALT-002` Git submodule as V0 default — rejected: initialization and discoverability costs; consumer tree contains a gitlink.
- `ALT-003` Add `rejected` to governing lifecycle — rejected: proposal disposition is not normative authority lifecycle.
- `ALT-004` Full semantic CI before pilots — rejected: semantic judgment is not reducible to speculative deterministic checks.

## 12. Migration, compatibility, and rollback

```text
MIGRATION = forward-only from the next non-mechanical change
COMPATIBILITY = consumers pin their adopted version; no automatic upstream change
ROLLBACK = revert the complete consumer adoption/update commit
```

## 13. Open questions

```text
OPEN_OWNER_DECISIONS = NONE
NORMATIVE_TBD = NONE
UNRESOLVED_AUTHORITY_CONFLICT = NONE
PARTIAL_SUPERSESSION = NONE
INDEPENDENT_REVIEW_REQUIRED = YES
READY_TO_MARK_ACCEPTED = NO
```
