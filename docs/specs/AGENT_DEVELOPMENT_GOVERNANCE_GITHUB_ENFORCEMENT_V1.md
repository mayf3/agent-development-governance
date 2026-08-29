---
spec_id: AGENT_DEVELOPMENT_GOVERNANCE_GITHUB_ENFORCEMENT_V1
status: proposed
spec_kind: program
authority_level: governing_spec
implementation_authority: none
scope:
  - shared-github-enforcement-standard
  - required-child-topology
  - cross-repository-rollout-sequencing
  - trust-and-validation-minimums
governed_by:
  - AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0
external_authorities: []
supersedes: []
superseded_by: null
owners:
  - mayf3
---

# AGENT_DEVELOPMENT_GOVERNANCE_GITHUB_ENFORCEMENT_V1

## 1. Goal

Define one central GitHub-enforcement standard and the mandatory local-activation program for `mayf3/agent-development-governance`, the future trusted producer repository, `mayf3/dsh-agent-core`, `mayf3/auth-service`, and `mayf3/svc-workflow` without directly authorizing any implementation or repository setting.

```text
GOAL = shared enforcement invariants with repository-local activation authority
SUCCESS_OUTCOME = independently accepted children can implement one trust model and rollout sequence without central authority crossing repository boundaries
AMENDMENT_ROUND = 1
AMENDMENT_CLASS = CENTRAL_STANDARD_PLUS_LOCAL_ACTIVATION
PREFLIGHT_CLASSIFICATION = AMEND
SPEC_STATUS = proposed
SPEC_KIND = program
IMPLEMENTATION_AUTHORITY = none
CROSS_REPOSITORY_AUTHORITY_MODEL = CENTRAL_STANDARD_PLUS_LOCAL_ACTIVATION
CONSUMER_LOCAL_ACCEPTANCE_REQUIRED = YES
```

This amendment replaces the proposed PR Head `4087ddf137aaf73a921230bd55b41f903717e550` in place. Because the Spec remains proposed, its stable items may be reorganized before independent review. No second central Spec or PR is created.

## 2. Scope and non-goals

### In scope

The central Program owns only:

- the shared GitHub enforcement standard;
- required child topology and cross-repository authority edges;
- rollout and bootstrap ordering;
- minimum trust, lifecycle, merge, validation, evidence, rollback, and anti-lockout invariants;
- blockers that must be closed by children before local activation.

### Out of scope

```text
CENTRAL_STANDARD_DIRECTLY_AUTHORIZES_CONSUMER_SETTINGS = NO
CENTRAL_STANDARD_DIRECTLY_AUTHORIZES_CHECK_PRODUCER_CODE = NO
CENTRAL_STANDARD_DIRECTLY_AUTHORIZES_GITHUB_APP_CREATION = NO
CENTRAL_STANDARD_DIRECTLY_AUTHORIZES_RULESET_MUTATION = NO
CENTRAL_STANDARD_DIRECTLY_AUTHORIZES_PRODUCT_CODE = NO
```

This Program does not:

- create or accept any required child;
- implement or deploy producer code;
- create a repository, GitHub App, installation, identity, credential, Grant, ruleset, workflow, branch protection, database, or deployment;
- authorize any consumer product implementation;
- mark any PR Ready, accepted, or merged;
- claim that current GitHub or DSH identity can automate Agent-independence proof;
- treat the present unprotected state as a safe rollback target.

## 3. Authority and dependencies

```text
PRIMARY_PARENT_AUTHORITY = AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0
PARENT_REVISION_IN_AUTHORING_BASE = d32b946cbbbc1baa99165d7656fc22e8823a651f
AUTHORITY_ACTION = AMEND
SAME_SCOPE_CENTRAL_AUTHORITY = THIS_PROPOSED_SPEC_ONLY
IMPLEMENTATION_AUTHORITY = none
CONSUMER_LOCAL_ACCEPTANCE_REQUIRED = YES
AUTHORITY_CONFLICT = NONE
PARTIAL_SUPERSESSION = NONE
```

The accepted parent requires commit-pinned local adoption and forbids a central repository from automatically becoming consumer product authority. This Program refines that boundary: it standardizes the shape of enforcement, while each owning repository must accept its own implementation-authorizing child before local code, Apps, or settings change.

### Required child topology

No child file is authored by this amendment. The following topology is mandatory after this Program is independently reviewed, owner-accepted, and merged to governance `main`.

| Required child Spec | Owning repository | Required `governed_by` | Required external relation | Preconditions | Prohibited authority |
|---|---|---|---|---|---|
| `AGENT_DEVELOPMENT_GOVERNANCE_TRUSTED_CHECK_PRODUCER_V1` | `mayf3/agent-governance-check-producer` | local repository authority, if any | `mayf3/agent-development-governance` / this Program at its exact accepted commit / `constrained_by` | central Program accepted and exact commit pinned; producer repository exists under owner control | no consumer settings, product behavior, or acceptance of consumer children |
| `AGENT_DEVELOPMENT_GOVERNANCE_SOURCE_BOOTSTRAP_PROTECTION_V1` | `mayf3/agent-development-governance` | this Program | none; local child of this Program | central Program accepted on governance `main`; current native settings inventoried | no producer implementation, App creation, or consumer settings |
| `DSH_AGENT_CORE_GITHUB_ENFORCEMENT_ACTIVATION_V1` | `mayf3/dsh-agent-core` | accepted local governance authority | `mayf3/agent-development-governance` / this Program at its exact accepted commit / `constrained_by` | central pin accepted locally; producer and Apps proven; shadow complete; blockers closed | no authority over auth-service, svc-workflow, producer, or product code |
| `AUTH_SERVICE_GITHUB_ENFORCEMENT_ACTIVATION_V1` | `mayf3/auth-service` | accepted local governance authority | `mayf3/agent-development-governance` / this Program at its exact accepted commit / `constrained_by` | central pin accepted locally; producer and Apps proven; prior canary GO; shadow complete | no authority over other repositories, credentials, Grants, database, deployment, or product code |
| `SVC_WORKFLOW_GITHUB_ENFORCEMENT_ACTIVATION_V1` | `mayf3/svc-workflow` | accepted local governance authority | `mayf3/agent-development-governance` / this Program at its exact accepted commit / `constrained_by` | central pin accepted locally; producer and Apps proven; prior phases GO; workflow blockers closed | no authority over other repositories, workflow product behavior, database, or deployment |

Each child must use its owning repository's accepted authority chain, explicitly set `implementation_authority`, and preserve the central Program as an exact-revision external constraint where the owning repository differs. Merely declaring a child ID in this Program creates no child authority.

### Cross-repository authority sequence

The only authorized sequence is:

1. independently review the central Program, obtain Owner acceptance, and merge it to governance `main`;
2. downstream repositories pin the exact accepted central commit through their local governance process;
3. accept and merge `AGENT_DEVELOPMENT_GOVERNANCE_TRUSTED_CHECK_PRODUCER_V1` in its owning repository;
4. accept and merge `AGENT_DEVELOPMENT_GOVERNANCE_SOURCE_BOOTSTRAP_PROTECTION_V1` in governance source;
5. implement, reproducibly build, audit, and sign producer code under the accepted producer child;
6. create and install the GitHub Apps and verify minimum permissions;
7. run shadow mode;
8. each consumer separately authors and accepts its local activation child;
9. each consumer performs local implementation, shadow verification, and settings rollout under its child;
10. activate `dsh-agent-core` as canary;
11. activate `auth-service` after canary GO;
12. activate `svc-workflow` after auth-service GO.

No consumer may modify settings directly from this Program.

## 4. Current State

### STATE-GHE-001 — The original proposed Head over-authorizes central implementation

- Subject: PR `mayf3/agent-development-governance#4`
- As of commit: `4087ddf137aaf73a921230bd55b41f903717e550`
- Environment: open Draft PR
- Observed at: amendment preflight
- Projection: the proposed Spec uses `spec_kind: implementation` and `implementation_authority: contracts`, allowing central Contracts to appear to authorize producer and consumer settings work across repository boundaries.
- Basis: `OBS-GHE-001`, `CLM-GHE-001`, `EVD-GHE-001`

### STATE-GHE-002 — Three consumer `main` branches had no protection or required checks at investigation time

- Subject: `mayf3/dsh-agent-core`, `mayf3/auth-service`, and `mayf3/svc-workflow`
- As of commits: `4bab9c902931164fb6f812e46891daf9ee7bf68f`, `7110463636693b3c2eced9d97ccb186adf46907d`, and `4dd521a5f7ef91e4b02b8a9204529db10f3ceed6`
- Environment: GitHub REST observations recorded by the original authoring task
- Observed at: `2026-08-29T10:50:30Z`
- Projection: protection was off, ruleset count was zero, required checks were absent, and no current workflow producer could safely be required.
- Basis: `OBS-GHE-002`, `EVD-GHE-002`, `CLM-GHE-002`

### STATE-GHE-003 — Bootstrap status descriptions drifted from accepted frontmatter

- Subject: governance-source entry documents
- As of commit: `4087ddf137aaf73a921230bd55b41f903717e550`
- Environment: amendment worktree
- Observed at: amendment preflight
- Projection: `AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0` frontmatter is `accepted`, while `AGENTS.md`, `CONTRIBUTING.md`, `.agents/local/README.md`, and the Spec index still described it as proposed or a candidate. This amendment reconciles those status descriptions only and does not change the bootstrap normative body or invent acceptance.
- Basis: `OBS-GHE-003`, `EVD-GHE-003`, `CLM-GHE-003`

### STATE-GHE-004 — Producer and automated Agent identity do not yet exist

- Subject: future trusted check control plane
- As of artifact: read-only investigation record on PR #4
- Environment: pre-implementation design state
- Observed at: amendment preflight
- Projection: no trusted producer child, producer artifact digest, App IDs, installation IDs, or signed DSH Agent-attestation authority exists.
- Basis: `OBS-GHE-004`, `EVD-GHE-004`, `CLM-GHE-004`

## 5. Observations

### OBS-GHE-001 — Original authority form is implementation-authorizing

- Subject: original proposed central Spec
- Repository/source: `mayf3/agent-development-governance`
- Commit/artifact: `4087ddf137aaf73a921230bd55b41f903717e550`
- Environment: PR #4 Draft Head
- Observed at: amendment preflight
- Method: inspect frontmatter, scope, Contracts, and Acceptance
- Result: `spec_kind: implementation`, `implementation_authority: contracts`, and central Contracts directly describe future producer and consumer rollout.
- Provenance: PR #4 original Head

### OBS-GHE-002 — Enforcement remained absent in the consumer snapshot

- Subject: three named consumer `main` branches
- Repository/source: GitHub REST API results persisted by original authoring
- Commit/artifact: exact commits in `STATE-GHE-002`
- Environment: GitHub repository settings
- Observed at: `2026-08-29T10:50:30Z`
- Method: branch-protection, ruleset, workflow-content, and Check Runs queries
- Result: branch protection off, zero rulesets, no workflow path, and no Check Runs on the observed Heads.
- Provenance: original authoring evidence in PR #4 Spec history

### OBS-GHE-003 — Bootstrap lifecycle truth and entry text disagree

- Subject: bootstrap authority status
- Repository/source: governance source tree
- Commit/artifact: `4087ddf137aaf73a921230bd55b41f903717e550`
- Environment: clean amendment base
- Observed at: amendment preflight
- Method: compare bootstrap frontmatter with `AGENTS.md`, `CONTRIBUTING.md`, `.agents/local/README.md`, and `docs/specs/README.md`
- Result: frontmatter says `accepted`; named entry surfaces say proposed/candidate.
- Provenance: repository files at the exact amendment base

### OBS-GHE-004 — Investigation fixed ten blocker clusters

- Subject: central-standard design
- Repository/source: PR #4 ordinary comment `issuecomment-5462537976`
- Commit/artifact: investigation bound to original Head `4087ddf137aaf73a921230bd55b41f903717e550`
- Environment: read-only investigation
- Observed at: before amendment file changes
- Method: persist fixed investigation conclusions and ten blocker clusters
- Result: amendment mode, authority split, bootstrap, producer, identity, lifecycle, merge, required-check, validation, and rollback/evidence models are fixed with no owner Decision or normative TBD remaining.
- Provenance: `https://github.com/mayf3/agent-development-governance/pull/4#issuecomment-5462537976`

## 6. Claims and assumptions

### CLM-GHE-001 — Central implementation authority violates the local-acceptance boundary

- Support state: SUPPORTED
- Supported by evidence: `EVD-GHE-001`
- Contradicted by evidence: none known
- Uncertainty: none material after owner-supplied investigation conclusion.

### CLM-GHE-002 — Settings-first or custom-check-first activation can lock governance source

- Support state: SUPPORTED
- Supported by evidence: `EVD-GHE-002`
- Contradicted by evidence: none known
- Uncertainty: exact future settings IDs do not yet exist and are intentionally not invented.

### CLM-GHE-003 — Bootstrap text repair is lifecycle truth reconciliation

- Support state: SUPPORTED
- Supported by evidence: `EVD-GHE-003`
- Contradicted by evidence: none known
- Uncertainty: none; bootstrap normative content is unchanged.

### CLM-GHE-004 — Automated Agent independence is unavailable in V1

- Support state: SUPPORTED
- Supported by evidence: `EVD-GHE-004`
- Contradicted by evidence: none known
- Uncertainty: future signed DSH attestation can replace the human ceremony only under a separately accepted authority.

## 7. Evidence relations

### EVD-GHE-001 — Original Head supports the over-authorization Claim

- Source observations: `OBS-GHE-001`
- Target: `CLM-GHE-001`
- Relation: SUPPORTS
- Bound coordinates: PR #4 at `4087ddf137aaf73a921230bd55b41f903717e550`
- Strength/sufficiency: decisive for the proposed authority form
- Limitations: proposed text may be amended in place
- Provenance: original Spec frontmatter and Contracts

### EVD-GHE-002 — Absent producers support two-stage bootstrap

- Source observations: `OBS-GHE-002`, `OBS-GHE-004`
- Target: `CLM-GHE-002`
- Relation: SUPPORTS
- Bound coordinates: consumer snapshot and pre-implementation investigation
- Strength/sufficiency: sufficient to forbid requiring undeployed custom contexts
- Limitations: later child evidence must re-observe live settings
- Provenance: GitHub observations and persisted investigation

### EVD-GHE-003 — File comparison supports bounded status reconciliation

- Source observations: `OBS-GHE-003`
- Target: `CLM-GHE-003`
- Relation: SUPPORTS
- Bound coordinates: amendment base `4087ddf137aaf73a921230bd55b41f903717e550`
- Strength/sufficiency: direct file evidence
- Limitations: does not change stable-release state or historical acceptance events
- Provenance: bootstrap frontmatter and entry surfaces

### EVD-GHE-004 — Missing identity authority supports human V1 gate

- Source observations: `OBS-GHE-004`
- Target: `CLM-GHE-004`
- Relation: SUPPORTS
- Bound coordinates: read-only investigation record and current design state
- Strength/sufficiency: decisive for V1 fail-closed behavior
- Limitations: future signed DSH authority may supersede this manual gate
- Provenance: PR #4 investigation record

## 8. Decisions

### DEC-GHE-001 — Central standard plus local activation

- Decision owner: repository owner `mayf3`
- Decision: this authority is a Program with `implementation_authority:none`; implementation belongs only to accepted children in their owning repositories.
- Rejected alternatives: central implementation authority; direct consumer settings authority; duplicate central Specs.
- Reason: preserve repository-local product and settings authority while sharing invariants.
- Owner decision remaining: NONE

### DEC-GHE-002 — Two-stage governance-source bootstrap

- Decision owner: repository owner `mayf3`
- Decision: merge Program and source-bootstrap child under current manual governance, immediately establish native baseline `B0`, protect producer source, and only then enable App-pinned checks.
- Rejected alternatives: use current unprotected `S0` as rollback; require custom checks before deployment; activate all controls together.
- Reason: avoid self-hosting recursion and lockout.
- Owner decision remaining: NONE

### DEC-GHE-003 — External digest-pinned producer control plane

- Decision owner: repository owner `mayf3`
- Decision: a separately governed producer repository builds immutable signed artifacts; two privilege-separated GitHub Apps produce verification and acceptance/merge outcomes.
- Rejected alternatives: PR-controlled workflow as its own verifier; context-name-only trust; one all-powerful App.
- Reason: separate untrusted PR code from enforcement and acceptance privileges.
- Owner decision remaining: NONE

### DEC-GHE-004 — Human WebAuthn semantic gate for V1

- Decision owner: repository owner `mayf3`
- Decision: independent Human Owner/maintainer WebAuthn ceremony is the V1 semantic gate; Agent execution IDs are informational until signed DSH attestation authority exists.
- Rejected alternatives: infer Agent identity from GitHub account; trust self-declared session IDs; claim current automation.
- Reason: no current authority covers key enrollment, signing, rotation, revocation, canonicalization, replay resistance, and verifier integration.
- Owner decision remaining: NONE

### DEC-GHE-005 — Two-head lifecycle

- Decision owner: repository owner `mayf3`
- Decision: semantic review binds `S`; owner acceptance binds `S`, a lifecycle-finalization recipe, and one-use nonce; deterministic finalization produces `F`; final-head verification allows only lifecycle changes.
- Rejected alternatives: require `S = F`; ask owner to sign unknown `F`; permit arbitrary post-review edits.
- Reason: acceptance necessarily finalizes lifecycle while preserving exact semantic review.
- Owner decision remaining: NONE

### DEC-GHE-006 — Merge-commit-only external broker

- Decision owner: repository owner `mayf3`
- Decision: only merge commits are allowed; an external broker rereads all coordinates, uses merge API `sha=F`, and verifies ancestry after merge.
- Rejected alternatives: squash, rebase merge, unavailable merge queue, old synthetic-compatibility result as final authority.
- Reason: preserve accepted Head identity and close current-main races.
- Owner decision remaining: NONE

### DEC-GHE-007 — Strict positive-only producer conclusions

- Decision owner: repository owner `mayf3`
- Decision: required contexts bind name plus integration ID and return `success` only for complete positive proof; neutral/skipped are never emitted for incomplete or unavailable evidence.
- Rejected alternatives: context name alone; N/A as neutral; infrastructure outage as skipped.
- Reason: GitHub may treat success, neutral, or skipped as satisfying a required context.
- Owner decision remaining: NONE

### DEC-GHE-008 — Repository-specific validation profiles

- Decision owner: repository owner `mayf3`
- Decision: central minimums include complete DSH, auth-service, and svc-workflow profiles plus fail-closed common behavior; local children may strengthen but not weaken them.
- Rejected alternatives: “run existing tests”; PR-owned verifier changes; rerun-to-green.
- Reason: generic test labels do not freeze security-relevant coverage.
- Owner decision remaining: NONE

### DEC-GHE-009 — Cutoff, LOCKDOWN, and safe rollback

- Decision owner: repository owner `mayf3`
- Decision: snapshot all open PRs, enter LOCKDOWN before changing required contexts, freeze pre-cutoff PRs, and roll back only to `B0` or the last safe baseline.
- Rejected alternatives: grandfather old checks/reviews; remove failed context while ordinary merge remains open; return to `S0`.
- Reason: prevent transition races and emergency bypass.
- Owner decision remaining: NONE

### DEC-GHE-010 — External WORM rollout evidence

- Decision owner: repository owner `mayf3`
- Decision: settings records use a canonical JSON schema in external Object Lock/WORM storage and strictly exclude secrets and raw sensitive responses.
- Rejected alternatives: mutable PR comment only; repository branch as sole ledger; full environment or API dumps.
- Reason: settings evidence must survive repository compromise without becoming a credential leak.
- Owner decision remaining: NONE

## 9. Contracts

### CTR-GHE-001 — Central Program has no direct implementation authority

This Program MUST remain `spec_kind: program` and `implementation_authority: none`. It MUST NOT directly authorize consumer settings, producer code, GitHub App creation, ruleset mutation, workflow installation, or product implementation. Acceptance of this Program authorizes only the requirement to author and evaluate the named children.

### CTR-GHE-002 — Local children and acceptance are mandatory

Every implementation or settings action MUST be authorized by an accepted, implementation-authorizing child in the owning repository and present in that implementation base. Consumer children MUST pin the exact accepted central commit as `constrained_by`, MUST be accepted locally, and MUST NOT inherit implementation authority from this Program.

### CTR-GHE-003 — Required child topology and sequence are closed

All five children in §3 MUST exist in their named repositories and satisfy the twelve-step authority sequence before the related activation. A declaration in the topology table is not child acceptance. Skipping, reordering, or combining producer, source-bootstrap, or consumer authority steps MUST block rollout.

### CTR-GHE-004 — Governance source uses `S0`, `B0`, and LOCKDOWN correctly

The source-bootstrap child MUST define:

```text
S0 = current unprotected historical snapshot; never a safe rollback target
B0 = native GitHub PR-only, non-Draft, no-force, no-delete, empty-bypass, merge-commit-only baseline
LOCKDOWN = all main updates forbidden during required-context migration
GOVERNANCE_SOURCE_BOOTSTRAP_MODEL = TWO_STAGE_NO_CUSTOM_CHECK_BOOTSTRAP
```

The Program and source-bootstrap child MUST first merge under existing manual governance. `B0` MUST then be established immediately. Initial bootstrap MUST NOT depend on an undeployed custom check.

### CTR-GHE-005 — Producer source is protected before App-pinned enforcement

After governance-source `B0`, the producer source repository MUST receive an equivalent native safe baseline before producer code is relied upon. Producer source, reproducible build definition, signing policy, and release metadata MUST be protected before any App-pinned required context becomes active. `LOCKDOWN` MUST cover migration gaps.

### CTR-GHE-006 — Producer artifacts are immutable and provenance-bound

The future producer child MUST govern repository `mayf3/agent-governance-check-producer` and require each release to bind:

```text
immutable OCI digest
SBOM digest
builder identity
signature public-key fingerprint
source commit
reproducible build result
security audit result
```

Runtime deployment MUST select the immutable OCI digest, not a tag. The producer MUST be external to PR-controlled code and MUST reject artifact, SBOM, builder, signature, or source mismatches.

### CTR-GHE-007 — App privileges and context identity are separated

The future control plane MUST use:

```text
governance-verifier
  -> governance/distribution-integrity
  -> governance/spec-lifecycle
  -> governance/structure
  -> governance/semantic-review
  -> governance/current-main-compatibility
  -> repository/validation

governance-acceptance-broker
  -> governance/acceptance-final-head
  -> expected-Head merge coordination
```

Every required context MUST bind both exact context name and trusted GitHub `integration_id`; name alone is insufficient. App permissions MUST be least privilege and separated so the verifier cannot accept/merge and the acceptance broker cannot synthesize verification success.

Current unresolved implementation identifiers MUST be represented honestly:

```text
APP_IDS = NOT_YET_AVAILABLE
INSTALLATION_IDS = NOT_YET_AVAILABLE
OCI_DIGEST = NOT_YET_AVAILABLE
TRUSTED_PRODUCER_IDENTITY = UNRESOLVED_PENDING_CHILD
```

No child may invent these values before the corresponding resources and evidence exist.

### CTR-GHE-008 — V1 Agent independence uses Human WebAuthn ceremony

The V1 semantic gate MUST be an independent Human Owner/maintainer WebAuthn ceremony bound to repository, PR, semantic Head `S`, base, review decision, and nonce. `AUTHOR_AGENT_EXECUTION_ID` and `REVIEWER_AGENT_EXECUTION_ID` are informational only and MUST NOT prove independence.

```text
SEMANTIC_REVIEW_GATE = independent Human Owner/maintainer WebAuthn ceremony
AGENT_INDEPENDENCE_AUTOMATION = DEFERRED_PENDING_SIGNED_DSH_ATTESTATION_AUTHORITY
```

Any future automated Agent-independence model requires a separate accepted authority covering host-key enrollment, signatures, rotation, revocation, canonical attestation, replay resistance, and verifier integration.

### CTR-GHE-009 — Lifecycle uses semantic Head `S` and final Head `F`

Owner semantic review MUST bind `S = SEMANTIC_HEAD_SHA`. Owner acceptance MUST bind `S`, the exact allowlisted lifecycle-finalization recipe, and a one-use nonce. A deterministic broker applies that recipe to produce `F = FINAL_ACCEPTED_HEAD_SHA`. Final-head verification MUST prove `diff(S,F)` contains only the accepted lifecycle allowlist, including exact status/acceptance-record finalization and no Goal, scope, authority, Decision, Contract, Acceptance, validation, migration, trust, or security meaning change.

The model MUST NOT require `S = F` and MUST NOT require the Owner to sign `F` before it exists. `governance/acceptance-final-head` binds `F`; any Head movement after `F` invalidates semantic review, acceptance, and every required result.

### CTR-GHE-010 — Merge is merge-commit-only and race-closed

```text
ALLOWED_MERGE_METHODS = MERGE_COMMIT_ONLY
FINAL_ACCEPTED_HEAD_ANCESTOR_REQUIRED = YES
SQUASH = FORBIDDEN
REBASE_MERGE = FORBIDDEN
MERGE_QUEUE = NOT_AVAILABLE_FOR_CURRENT_PERSONAL_REPOSITORIES
EXPECTED_BASE_CAS = UNSUPPORTED
RECOMMENDED_MERGE_COORDINATION = EXTERNAL_MERGE_BROKER
```

Immediately before merge, the external broker MUST reread PR Head, current `main`, Draft state, exact App-bound contexts, and lifecycle records; require Head `= F`; require current `main` to be an ancestor of `F`; require every context successful for `F`; and call the GitHub merge API with `sha=F`. After merge, it MUST verify `F` is an ancestor of `main` and the resulting method is a merge commit.

If `main` advances after review, the candidate MUST merge current `main` into the PR branch to produce a new Head. All prior semantic review, acceptance, compatibility, validation, and required-check records then become invalid and the lifecycle restarts. An old synthetic compatibility result MUST NOT authorize merge.

### CTR-GHE-011 — Required-check conclusions fail closed

Because GitHub may count `success`, `neutral`, or `skipped` as satisfying a required context, a trusted App producer MUST emit `success` only after complete positive proof. It MUST NOT emit `neutral` or `skipped` for not-applicable, missing dependency, infrastructure unavailable, timeout, unsupported path, cancellation, partial evidence, or missing evidence. Such conditions MUST emit a failing conclusion or remain incomplete until a bounded deadline and then fail. Required contexts MUST be App-bound as in `CTR-GHE-007`.

### CTR-GHE-012 — DSH validation profile is frozen

The `dsh-agent-core` activation child MUST require, at minimum:

1. accepted governance verification against exact base and Head;
2. structure comparison using trusted PR `BASE_SHA`, `HEAD_SHA`, and `MERGE_BASE`, with `git diff --name-status "$MERGE_BASE" "$HEAD_SHA"`;
3. Node.js `20.x` and npm `10.x`, pinned in evidence;
4. deterministic root dependency resolution and immutable lock digest;
5. clean install from the frozen lock without dependency mutation;
6. `npm test` and all repository-required build/type/lint gates at the accepted baseline;
7. generated-file and working-tree cleanliness checks.

Current activation blockers MUST remain explicit until child evidence closes them:

```text
DSH_BLOCKER_DETERMINISTIC_ROOT_LOCK = MISSING
DSH_BLOCKER_STRUCTURE = DRIFT_PRESENT
```

No DSH settings rollout may begin while either blocker remains open.

### CTR-GHE-013 — Auth validation profile is frozen

The `auth-service` activation child MUST require, at minimum:

1. deterministic `npm ci` from the accepted lock and pinned Node/npm toolchain;
2. contract validate, prepare, and candidate-generation stages;
3. contract test suite;
4. OAuth test suite;
5. TypeScript `tsc` verification;
6. production build;
7. migration tests against a disposable PostgreSQL instance initialized from the accepted migration baseline;
8. install, build, and test for every nested provider package included by the PR;
9. generated-contract and working-tree drift checks.

No production database may be used for validation.

### CTR-GHE-014 — Workflow validation profile is frozen

The `svc-workflow` activation child MUST require, at minimum:

1. accepted governance verification against exact base and Head;
2. deterministic contract digest verification;
3. `cargo fmt --check`;
4. `cargo check`;
5. `cargo clippy` with warnings denied;
6. `cargo test`;
7. SDK deterministic install/build/test;
8. real-process RS256/JWKS integration using the accepted identity path;
9. migration and integration tests against disposable PostgreSQL `16`;
10. generated-contract and working-tree drift checks.

Current activation blocker MUST remain explicit until child evidence closes it:

```text
WORKFLOW_BLOCKER_AUTH_INTEGRATION = HS256_RS256_CONTRADICTION
```

No Workflow settings rollout may begin while the blocker remains open.

### CTR-GHE-015 — Validation profiles share fail-closed behavior

For every profile: missing dependency fails; database unavailability blocks/fails without production fallback; the first flaky failure is retained as evidence and rerun MUST NOT replace it with green; timeout, cancellation, skipped, neutral, unsupported, or partial results fail; generated drift fails; and a PR MUST NOT establish its own trust by modifying the verifier or required profile in the same candidate. Trusted verification executes from the externally hosted digest-pinned producer.

### CTR-GHE-016 — Existing PRs are frozen at rollout cutoff

Before any required-context rollout, the rollout actor MUST record every open PR, exact Head, base, Draft state, and existing checks/reviews. The repository MUST enter `LOCKDOWN` before required contexts change. Pre-cutoff PRs are frozen by default and historical checks/reviews are not grandfathered. A frozen PR may resume only after it incorporates the then-current `main`, produces a new Head, and receives a persisted owner-authorized thaw record; all governance, review, acceptance, and validation then restart.

### CTR-GHE-017 — Emergency producer failure preserves LOCKDOWN and `B0`

On producer failure, the operator MUST first enter and verify `LOCKDOWN`, then may temporarily remove only the single failed context while ordinary merge remains forbidden by update restriction. The operator MUST restore producer health and the exact context plus `integration_id`, verify them in shadow, and only then lift `LOCKDOWN`. Rollback MUST target `B0` or the last proven safe baseline and MUST NOT restore unprotected `S0`.

### CTR-GHE-018 — Settings Rollout Records use external WORM canonical JSON

Every settings change, attempted change, rollback, LOCKDOWN transition, thaw, and baseline declaration MUST create an immutable object at:

```text
settings-rollout/v1/<repository-id>/<record-id>.json
```

The object MUST be stored in external Object Lock/WORM storage and canonicalized with RFC 8785 JSON Canonicalization Scheme (JCS). It MAY contain only the allowlisted record fields:

```text
schema and version
record IDs and timestamps
accepted Spec IDs and exact revisions
implementation base
producer OCI and SBOM digests
repository, branch, and ruleset IDs
actor, App, and installation IDs
allowlisted before/after settings and digests
required contexts plus integration IDs
bypass list and allowed merge methods
sanitized API status and error code
evidence locators and rollback reference
```

The record digest, WORM object version/retention identity, and evidence locators MUST be included in the rollout decision.

### CTR-GHE-019 — Secrets and sensitive responses are excluded

Settings records, Check Run output, logs, PR comments, and evidence MUST NOT contain App private keys; installation, OAuth, PAT, access, or refresh tokens; `Authorization`, `Cookie`, or `Set-Cookie`; webhook secrets or signatures; KMS plaintext or data keys; runner credentials; environment dumps; or raw sensitive API responses. Producers MUST sanitize to allowlisted status/error codes and reject record publication when forbidden material is detected.

### CTR-GHE-020 — Central Program never authorizes product behavior

Neither proposed nor accepted state of this Program authorizes consumer product code, schema, database, migration, deployment, identity, Grant, credential, runtime behavior, or unrelated workflow changes. Such work requires its own accepted local implementation authority present in its implementation base. The enforcement children themselves MUST remain bounded to producer, bootstrap, checks, settings, evidence, and rollback concerns.

## 10. Acceptance

### ACC-GHE-001 — Central/local authority negative matrix

- Contracts: `CTR-GHE-001`, `CTR-GHE-002`, `CTR-GHE-020`
- Method: evaluate proposed/accepted central Program, missing child, proposed child, accepted child in wrong repository, child absent from base, and product change citing this Program.
- Environment: exact candidate and owning-repository authority graphs.
- Required evidence: Spec revisions, repository/base/Head coordinates, authority resolution, and verdict.
- Expected result: only an accepted in-base local child can authorize its bounded local enforcement implementation; central or product authorization attempts fail.
- Negative cases: central Program cited for ruleset mutation; consumer child accepted only upstream; product code cites an enforcement child.
- Failure condition: any central, cross-owner, proposed, absent-base, or product authorization passes.

### ACC-GHE-002 — Child topology and sequence closure

- Contracts: `CTR-GHE-003`
- Method: validate all five child IDs, owning repositories, `governed_by`/`constrained_by` edges, exact central pin, prerequisites, prohibitions, and twelve ordered stages.
- Environment: authority graph fixture and rollout-plan record.
- Required evidence: machine-readable edge list, exact revisions, stage state, and ordering result.
- Expected result: every required child and edge exists before its stage and no declaration is mistaken for acceptance.
- Negative cases: missing producer child; consumer settings before local child; auth-service before DSH canary GO; reordered source bootstrap.
- Failure condition: a missing, declaration-only, wrong-owner, unaccepted, or out-of-order edge passes.

### ACC-GHE-003 — Governance-source two-stage bootstrap

- Contracts: `CTR-GHE-004`, `CTR-GHE-005`
- Method: simulate Program/source-child manual merge, establish `B0`, protect producer source, enter/exit LOCKDOWN, and then introduce custom contexts.
- Environment: reversible settings fixture with no custom check initially deployed.
- Required evidence: S0 snapshot, B0 canonical settings, LOCKDOWN proof, producer-source baseline, event order, and API outcomes.
- Expected result: B0 precedes producer reliance and App-pinned contexts; S0 is never selected for rollback.
- Negative cases: undeployed check required before B0; custom checks activated before producer-source protection; rollback to S0.
- Failure condition: bootstrap depends on custom checks, leaves an update gap, or treats S0 as safe.

### ACC-GHE-004 — Producer provenance and immutable runtime

- Contracts: `CTR-GHE-006`
- Method: reproduce build and verify source, OCI, SBOM, builder, signature fingerprint, audit, and deployed digest; tamper each coordinate independently.
- Environment: producer child implementation and isolated build/deploy verification.
- Required evidence: accepted child, source commit, build logs, signed OCI digest, SBOM digest, builder identity, fingerprint, audit result, and runtime digest.
- Expected result: exact reproducible signed artifact is deployed by digest.
- Negative cases: mutable tag; mismatched SBOM; unknown builder; bad signature; source mismatch.
- Failure condition: any missing or mismatched provenance coordinate passes.

### ACC-GHE-005 — App privilege and integration binding

- Contracts: `CTR-GHE-007`
- Method: inspect App IDs/installations/permissions and required-context configuration; attempt name spoofing, cross-App conclusion, verifier acceptance, and broker verification synthesis.
- Environment: installed future Apps and settings fixture.
- Required evidence: App/installation IDs, permissions, context names, integration IDs, Check Runs, and denied API calls.
- Expected result: six contexts bind to verifier App; acceptance/merge binds to broker App; privileges cannot cross.
- Negative cases: same name from Actions; wrong integration ID; one App has both privilege sets; unavailable IDs represented as real.
- Failure condition: name-only trust, privilege overlap, spoofed success, or invented identity passes.

### ACC-GHE-006 — Human WebAuthn semantic gate

- Contracts: `CTR-GHE-008`
- Method: verify independent human WebAuthn records and test self-declared Agent IDs, same ceremony replay, wrong Head/base, revoked authenticator, and automated Agent-independence claim.
- Environment: V1 semantic-review gate.
- Required evidence: WebAuthn verifier result, human actor/role, repository/PR/base/S binding, challenge, nonce, timestamp, and replay state.
- Expected result: only a fresh independent authorized human ceremony passes; Agent IDs remain informational.
- Negative cases: GitHub account alone; Agent session string; replayed ceremony; wrong S; unsigned DSH attestation.
- Failure condition: current automation or informational Agent identity is accepted as independence proof.

### ACC-GHE-007 — Two-head lifecycle matrix

- Contracts: `CTR-GHE-009`
- Method: review S, sign S+recipe+nonce, deterministically produce F, and compare semantic/lifecycle diffs; then add a post-F commit.
- Environment: lifecycle fixture controlled by acceptance broker.
- Required evidence: S, recipe digest, one-use nonce, owner acceptance, F, diff classification, Check Run, and post-F invalidation record.
- Expected result: allowlisted lifecycle-only S→F passes; F binds acceptance; post-F movement invalidates all records.
- Negative cases: require S=F; owner asked to pre-sign unknown F; semantic S→F edit; nonce reuse; post-F commit.
- Failure condition: semantic change, replay, unknown recipe, pre-signing, or stale F passes.

### ACC-GHE-008 — Merge method and current-main race

- Contracts: `CTR-GHE-010`
- Method: exercise merge commit, squash, rebase, current-main advance, stale synthetic result, wrong API SHA, ancestry failure, and post-merge verification.
- Environment: external broker against disposable PR branches.
- Required evidence: F, reread Head/main, ancestry command, App-bound contexts, Draft state, merge API request/result, merge commit, and post-merge ancestry.
- Expected result: only merge API `sha=F` succeeds when current main is F ancestor; F is main ancestor afterward.
- Negative cases: main advances after review; squash; rebase; stale compatibility green; wrong expected Head.
- Failure condition: any non-merge method, stale main, non-ancestor base, wrong SHA, or failed post-merge ancestry passes.

### ACC-GHE-009 — Required conclusion and spoof matrix

- Contracts: `CTR-GHE-007`, `CTR-GHE-011`
- Method: produce complete success and fixtures for N/A, missing dependency, outage, timeout, unsupported, cancelled, partial, missing evidence, neutral, skipped, and wrong integration.
- Environment: trusted App producer and required-context fixture.
- Required evidence: context, integration ID, inputs, conclusion, timing, and GitHub eligibility result.
- Expected result: only complete App-bound proof emits success; every incomplete condition blocks.
- Negative cases: neutral N/A; skipped outage; name spoof; timeout converted to green.
- Failure condition: any neutral/skipped/incomplete/spoofed result satisfies merge.

### ACC-GHE-010 — DSH profile and blockers

- Contracts: `CTR-GHE-012`, `CTR-GHE-015`
- Method: execute the frozen DSH profile on exact base/Head and negative fixtures for absent root lock, dependency mutation, structure drift, generated drift, toolchain mismatch, and verifier modification.
- Environment: Node 20/npm 10 clean runner from trusted producer.
- Required evidence: governance result, SHAs/merge-base/diff, tool versions, lock digest, install/test/build outputs, blocker states, and clean tree.
- Expected result: all profile stages pass deterministically and both current blockers are explicitly closed before activation.
- Negative cases: missing lock; structure drift; npm mutation; wrong Node/npm; PR changes verifier to self-pass.
- Failure condition: activation passes with an open blocker or incomplete/non-deterministic profile.

### ACC-GHE-011 — Auth profile and disposable database

- Contracts: `CTR-GHE-013`, `CTR-GHE-015`
- Method: run install, contract validate/prepare/candidate, contract tests, OAuth tests, tsc, build, PostgreSQL migration, nested-provider, and drift stages plus failure fixtures.
- Environment: clean trusted runner and disposable PostgreSQL initialized solely for the candidate.
- Required evidence: tool/lock versions, stage outputs, disposable DB identity/lifecycle, provider matrix, generated diff, and clean tree.
- Expected result: every stage and nested package passes without production dependency.
- Negative cases: DB unavailable; production DB URL; skipped provider; contract drift; first flaky failure hidden by rerun.
- Failure condition: incomplete stages, production DB use, drift, or rerun-to-green passes.

### ACC-GHE-012 — Workflow profile and identity blocker

- Contracts: `CTR-GHE-014`, `CTR-GHE-015`
- Method: run governance, contract digest, Rust fmt/check/clippy/test, SDK build/test, real-process RS256/JWKS, PostgreSQL 16 migration/integration, and drift stages.
- Environment: clean trusted runner, real child processes, and disposable PostgreSQL 16.
- Required evidence: exact SHAs, digests, Rust/tool versions, command outputs, process/JWKS transcript, DB identity/lifecycle, blocker closure, and clean tree.
- Expected result: all stages pass and HS256/RS256 contradiction is resolved by accepted local authority before activation.
- Negative cases: HS256-only fixture; mocked instead of real process; wrong PostgreSQL version; digest drift; blocker still open.
- Failure condition: incomplete identity path, open blocker, skipped integration, DB fallback, or drift passes.

### ACC-GHE-013 — Common validation fail-closed behavior

- Contracts: `CTR-GHE-015`
- Method: inject missing dependency, DB outage, first flaky failure, timeout, cancellation, skipped/neutral/unsupported/partial outcome, generated drift, and candidate verifier edit across all profiles.
- Environment: trusted producer profile harness.
- Required evidence: first-run result, retained failure, producer decision, Check Run conclusion, and provenance.
- Expected result: every negative fixture blocks and the first failure remains visible.
- Negative cases: rerun replaces failure; production DB fallback; PR-owned verifier self-certifies; neutral/skip reports green.
- Failure condition: any incomplete, mutable, rerun-masked, or self-certified evidence passes.

### ACC-GHE-014 — Existing-PR cutoff and thaw

- Contracts: `CTR-GHE-016`
- Method: snapshot mixed open PRs, enter LOCKDOWN, change contexts, attempt old PR merge, then update one PR to current main with a thaw record.
- Environment: rollout simulation with multiple PR Heads.
- Required evidence: cutoff inventory, Head/base/check/review records, LOCKDOWN proof, thaw record, new Head, and restarted checks.
- Expected result: every pre-cutoff PR is frozen; only owner-authorized refreshed Head restarts from zero.
- Negative cases: grandfather old review/check; missing PR from inventory; thaw without current main; reuse old acceptance.
- Failure condition: any pre-cutoff evidence remains merge-authorizing without valid thaw and full restart.

### ACC-GHE-015 — Emergency LOCKDOWN and safe baseline

- Contracts: `CTR-GHE-017`
- Method: fail one producer context, verify LOCKDOWN, remove only that context, attempt ordinary merge, repair/rebind integration, shadow, and restore; test S0 rollback request.
- Environment: reversible canary settings fixture.
- Required evidence: incident/owner authorization, LOCKDOWN API proof, before/after settings, context/integration ID, denied merge, repair/shadow result, and restored baseline.
- Expected result: ordinary merge remains impossible throughout; recovery returns to B0 or later safe baseline.
- Negative cases: context removed before LOCKDOWN; multiple controls removed; bypass actor added; S0 selected; LOCKDOWN lifted before repair.
- Failure condition: emergency creates an update window or restores unprotected state.

### ACC-GHE-016 — WORM record schema and canonicalization

- Contracts: `CTR-GHE-018`
- Method: create canonical settings, rollback, LOCKDOWN, and thaw records; verify RFC 8785 digest, Object Lock retention, path, IDs, allowlist, and immutable replay.
- Environment: external WORM/Object Lock test bucket separated from repositories and producer runtime credentials.
- Required evidence: object path/version, retention identity, canonical bytes/digest, accepted Spec/base, settings digests, contexts/integration IDs, and rollback link.
- Expected result: records are immutable, canonical, complete, and resolvable by the decision digest.
- Negative cases: mutable object; noncanonical key/number encoding; wrong path; omitted integration ID; overwritten record.
- Failure condition: record can mutate, digest is unstable, or required allowlisted evidence is absent.

### ACC-GHE-017 — Secret exclusion and central product boundary

- Contracts: `CTR-GHE-019`, `CTR-GHE-020`
- Method: scan canonical records, Check Runs, logs, and comments with fixtures for every forbidden secret class; separately evaluate product changes citing this Program.
- Environment: producer publication gate and authority resolver.
- Required evidence: allowlist scan result, rejection records, sanitized status/error sample, and authority verdict.
- Expected result: forbidden material is rejected before publication and product changes lack authority.
- Negative cases: PAT, Cookie, webhook signature, KMS plaintext, environment dump, raw API body, product migration citing central Program.
- Failure condition: any forbidden value is persisted or any product implementation is authorized.

### Contract coverage

| Contract | Acceptance | Evidence class | Covered |
|---|---|---|---|
| `CTR-GHE-001` | `ACC-GHE-001` | authority matrix | YES |
| `CTR-GHE-002` | `ACC-GHE-001` | local authority graph | YES |
| `CTR-GHE-003` | `ACC-GHE-002` | topology/sequence graph | YES |
| `CTR-GHE-004` | `ACC-GHE-003` | settings simulation | YES |
| `CTR-GHE-005` | `ACC-GHE-003` | producer-source baseline | YES |
| `CTR-GHE-006` | `ACC-GHE-004` | signed provenance | YES |
| `CTR-GHE-007` | `ACC-GHE-005`, `ACC-GHE-009` | App/context matrix | YES |
| `CTR-GHE-008` | `ACC-GHE-006` | WebAuthn ceremony | YES |
| `CTR-GHE-009` | `ACC-GHE-007` | two-head lifecycle | YES |
| `CTR-GHE-010` | `ACC-GHE-008` | merge/ancestry race | YES |
| `CTR-GHE-011` | `ACC-GHE-009` | conclusion matrix | YES |
| `CTR-GHE-012` | `ACC-GHE-010` | DSH validation | YES |
| `CTR-GHE-013` | `ACC-GHE-011` | Auth validation | YES |
| `CTR-GHE-014` | `ACC-GHE-012` | Workflow validation | YES |
| `CTR-GHE-015` | `ACC-GHE-010`, `ACC-GHE-011`, `ACC-GHE-012`, `ACC-GHE-013` | fail-closed matrix | YES |
| `CTR-GHE-016` | `ACC-GHE-014` | cutoff/thaw simulation | YES |
| `CTR-GHE-017` | `ACC-GHE-015` | emergency simulation | YES |
| `CTR-GHE-018` | `ACC-GHE-016` | WORM canonical record | YES |
| `CTR-GHE-019` | `ACC-GHE-017` | secret scanning | YES |
| `CTR-GHE-020` | `ACC-GHE-001`, `ACC-GHE-017` | authority-negative matrix | YES |

## 11. Alternatives and disposition

### ALT-GHE-001 — Keep central implementation authority

- Disposition: rejected
- Reason: violates accepted local-adoption boundaries and can appear to authorize settings in repositories that did not locally accept it.
- Evidence/Claims considered: `CLM-GHE-001`
- What would reopen: a separately accepted cross-repository authority model that explicitly replaces local ownership.

### ALT-GHE-002 — Deploy custom checks before native bootstrap

- Disposition: rejected
- Reason: creates self-hosting recursion and lockout while producer identity and artifacts do not exist.
- Evidence/Claims considered: `CLM-GHE-002`
- What would reopen: not for V1; native B0 remains mandatory.

### ALT-GHE-003 — Automate Agent independence now

- Disposition: rejected
- Reason: GitHub identity and self-declared Agent execution IDs do not cover signed DSH trust lifecycle.
- Evidence/Claims considered: `CLM-GHE-004`
- What would reopen: accepted signed DSH attestation authority and conforming verifier integration.

### ALT-GHE-004 — One-head lifecycle

- Disposition: rejected
- Reason: semantic review precedes accepted lifecycle finalization; requiring S=F either signs a nonexistent Head or conflates semantic and lifecycle changes.
- Evidence/Claims considered: persisted investigation blocker.
- What would reopen: a platform-native atomic lifecycle finalization that preserves equivalent two-head proof.

### ALT-GHE-005 — Squash, rebase, or stale compatibility merge

- Disposition: rejected
- Reason: destroys or races the exact accepted Head ancestry required for audit.
- Evidence/Claims considered: persisted investigation blocker.
- What would reopen: not for V1 personal repositories.

### ALT-GHE-006 — Mutable repository-only settings records

- Disposition: rejected
- Reason: settings authority and evidence must survive repository compromise and must not expose credentials.
- Evidence/Claims considered: persisted investigation blocker.
- What would reopen: an equivalent externally immutable, canonical, secret-safe evidence system.

## 12. Migration, compatibility, and rollback

```text
GOVERNANCE_SOURCE_BOOTSTRAP_MODEL = TWO_STAGE_NO_CUSTOM_CHECK_BOOTSTRAP
S0 = historical unprotected snapshot; forbidden rollback target
B0 = native PR-only, non-Draft, no-force, no-delete, empty-bypass, merge-commit-only baseline
LOCKDOWN = all main updates forbidden during context migration or producer emergency
CHECK_PRODUCER_MODEL = EXTERNALLY_HOSTED_DIGEST_PINNED_PRIVILEGE_SEPARATED_GITHUB_APP_CONTROL_PLANE
TRUSTED_PRODUCER_IDENTITY = UNRESOLVED_PENDING_CHILD
AGENT_INDEPENDENCE_MODEL = HUMAN_OWNER_WEBAUTHN_SEMANTIC_GATE_UNTIL_SIGNED_DSH_ATTESTATION_EXISTS
LIFECYCLE_ACCEPTANCE_MODEL = TWO_HEAD_LIFECYCLE_MODEL
ALLOWED_MERGE_METHODS = MERGE_COMMIT_ONLY
RECOMMENDED_MERGE_COORDINATION = EXTERNAL_MERGE_BROKER
SETTINGS_RECORD_SCHEMA = FROZEN
```

Migration follows the twelve-step sequence in §3. Existing PRs use cutoff/LOCKDOWN/thaw under `CTR-GHE-016`. Emergency recovery follows `CTR-GHE-017`; rollback always returns to B0 or a later proven safe baseline, never S0. Compatibility with an advancing `main` requires merging current `main` into the PR Head and restarting all evidence; no historical record is grandfathered.

## 13. Open questions

Implementation identifiers are intentionally unavailable until accepted children create and prove them. Their absence is a blocker to rollout, not a normative design gap.

```text
OPEN_OWNER_DECISIONS = NONE
NORMATIVE_TBD = NONE
UNRESOLVED_AUTHORITY_CONFLICT = NONE
PARTIAL_SUPERSESSION = NONE
APP_IDS = NOT_YET_AVAILABLE
INSTALLATION_IDS = NOT_YET_AVAILABLE
OCI_DIGEST = NOT_YET_AVAILABLE
TRUSTED_PRODUCER_IDENTITY = UNRESOLVED_PENDING_CHILD
AGENT_IDENTITY_ATTESTATION = NOT_AUTOMATABLE_NOW
BLOCKERS_RECEIVED = 10
BLOCKERS_CLOSED_BY_PROGRAM_TEXT = 10
CONTRACT_COUNT = 20
CONTRACTS_WITH_ACCEPTANCE = 20
ACCEPTANCE_COUNT = 17
SPEC_STATUS = proposed
SPEC_KIND = program
IMPLEMENTATION_AUTHORITY = none
READY_TO_MARK_ACCEPTED = NO
FRESH_FULL_REVIEW_REQUIRED = YES
INDEPENDENT_REVIEW_RESULT = PENDING
AUTHORING_READY_FOR_REVIEW = YES
```
