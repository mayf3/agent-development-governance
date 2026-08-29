---
spec_id: AGENT_DEVELOPMENT_GOVERNANCE_GITHUB_ENFORCEMENT_V1
status: proposed
spec_kind: implementation
authority_level: governing_spec
implementation_authority: contracts
scope:
  - agent-development-governance-github-administration
  - dsh-agent-core-main
  - auth-service-main
  - svc-workflow-main
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

Establish the proposed, reviewable authority for deterministic GitHub merge enforcement on the `main` branches of `mayf3/dsh-agent-core`, `mayf3/auth-service`, and `mayf3/svc-workflow` without changing any GitHub setting in this authoring change.

```text
GOAL = replace critical manual-governance bypass exposure with PR-only, exact-head, check-enforced merges
SUCCESS_OUTCOME = each named main branch rejects direct, destructive, stale, unreviewed, unaccepted, or governance-invalid updates while preserving bounded owner acceptance and emergency containment
SPEC_GOVERNANCE_MODE = AUTHOR
PREFLIGHT_CLASSIFICATION = NEW
SPEC_STATUS = proposed
IMPLEMENTATION_AUTHORITY = contracts
```

This Spec governs GitHub administrative enforcement for the three named repositories. It does not become product authority over their code. Its Contracts may authorize only a later, separately reviewed settings/check implementation after this exact authority is accepted and present in that implementation base.

## 2. Scope and non-goals

### In scope

- the three repositories' `main` branch update path;
- PR-only merge, draft exclusion, force-push denial, and deletion denial;
- a frozen minimum required-check suite and exact check context names;
- governance distribution integrity, Spec lifecycle, implementation-authority, implementation-base, and PR structure checks;
- exact reviewed-Head semantic review records and Agent-independence evidence;
- owner acceptance bound to the final Head and accepted-Head/merge-Head equality;
- current-`main` compatibility verification immediately before merge;
- staged rollout, canary, rollback, lockout prevention, drift detection, and emergency containment;
- a persistent rollout record for settings changes made under an accepted revision of this Spec.

### Out of scope

- changing branch protection, creating or modifying a repository ruleset, or selecting required checks in this authoring PR;
- merging, closing, accepting, or marking ready any PR;
- consumer product code, schema, database, deployment, identity, Grant, credential, or runtime changes;
- authorization of consumer product implementation;
- treating a proposed Spec or an unmerged `status: accepted` value as active authority;
- proving human or Agent independence from GitHub login identity alone;
- eliminating the repository owner's ultimate GitHub platform-root ability to edit repository settings. That residual root capability is monitored and auditable, not falsely claimed to be cryptographically absent.

## 3. Authority and dependencies

```text
PRIMARY_PARENT_AUTHORITY = AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0
PARENT_REVISION_IN_AUTHORING_BASE = d32b946cbbbc1baa99165d7656fc22e8823a651f
AUTHORITY_ACTION = NEW
SAME_SCOPE_AUTHORITY = NONE_FOUND
IMPLEMENTATION_AUTHORITY = contracts
IMPLEMENTATION_AUTHORITY_BOUNDARY = github enforcement settings, trusted checks, rollout records, and rollback only
CONSUMER_PRODUCT_IMPLEMENTATION_AUTHORITY = NONE
EXTERNAL_AUTHORITIES = NONE
AUTHORITY_CONFLICT = NONE
PARTIAL_SUPERSESSION = NONE
```

The parent requires honest separation between manual policy and deterministic enforcement, exact-revision review, explicit implementation authority, and local consumer product authority. This Spec adds a new, bounded GitHub-administration Decision set. It neither changes an existing accepted Contract nor supersedes the parent.

The repository owner supplied explicit cross-repository GitHub-administration direction for the three named repositories. Consumer product Decisions remain local. A future implementation MUST cite the accepted revision of this Spec and MUST be based on a branch whose base already contains that accepted revision; the authoring PR that proposes this Spec cannot implement it.

### Deduplication record

At `2026-08-29T10:50:30Z`, the authoring Agent fetched all remotes, scanned local and remote branch names, searched every governance branch's `docs/**` and `.agents/**` content for GitHub-enforcement, branch-protection, ruleset, required-check, and force-push scope, listed all open PRs in the four repositories, and performed a focused open-PR search. No same-scope authority or PR was found. Existing `AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0` is a parent whose Decision set does not define these enforcement settings. Classification is therefore `NEW`, not `REUSE`, `AMEND`, or `SUPERSEDE`.

## 4. Current State

### STATE-GHE-001 — All three target `main` branches lack GitHub enforcement

- Subject: `main` in `mayf3/dsh-agent-core`, `mayf3/auth-service`, and `mayf3/svc-workflow`
- As of commits: `4bab9c902931164fb6f812e46891daf9ee7bf68f`, `7110463636693b3c2eced9d97ccb186adf46907d`, and `4dd521a5f7ef91e4b02b8a9204529db10f3ceed6`, respectively
- Environment: GitHub REST API, repository default branches
- Observed at: `2026-08-29T10:50:30Z`
- Projection: branch protection is absent, repository ruleset count is zero, no required status checks are configured, and manual governance bypass risk is critical.
- Basis: `OBS-GHE-001`, `OBS-GHE-002`, `OBS-GHE-003`, `EVD-GHE-001`, `CLM-GHE-001`

### STATE-GHE-002 — No existing workflow can satisfy a minimum required-check set

- Subject: GitHub Actions and Check Runs in the three consumer repositories
- As of commits: the three commits in `STATE-GHE-001`
- Environment: GitHub REST API
- Observed at: `2026-08-29T10:50:30Z`
- Projection: `.github/workflows` is absent on each `main`, and the latest `main` commit in each repository has zero Check Runs. Enabling required contexts before installing and proving their producers would lock merges.
- Basis: `OBS-GHE-004`, `EVD-GHE-002`, `CLM-GHE-002`

### STATE-GHE-003 — The governance source has integrity checks but no same-scope enforcement authority

- Subject: `mayf3/agent-development-governance`
- As of commit: `d32b946cbbbc1baa99165d7656fc22e8823a651f`
- Environment: clean local checkout after `git fetch --all --prune`
- Observed at: `2026-08-29T10:50:30Z`
- Projection: distribution unit tests and manifest check pass; the source repository intentionally has no consumer lock file; existing Specs are the bootstrap authority plus an unrelated proposed operational-layer authority on an open Draft PR; no branch, open PR, or governing Spec owns this scope.
- Basis: `OBS-GHE-005`, `OBS-GHE-006`, `EVD-GHE-003`, `CLM-GHE-003`

## 5. Observations

### OBS-GHE-001 — `dsh-agent-core/main` is unprotected

- Subject: `mayf3/dsh-agent-core`, branch `main`
- Repository/source: GitHub REST API
- Commit/artifact: `4bab9c902931164fb6f812e46891daf9ee7bf68f`
- Environment: GitHub repository settings
- Observed at: `2026-08-29T10:50:30Z`
- Method: query `repos/mayf3/dsh-agent-core/branches/main/protection`, `repos/mayf3/dsh-agent-core/rulesets`, workflow contents, and commit Check Runs
- Result: protection endpoint returned `404 Branch not protected`; ruleset count was `0`; workflow path was absent; Check Runs were `[]`.
- Provenance: authoring-session command output bound to this Spec's authoring branch

### OBS-GHE-002 — `auth-service/main` is unprotected

- Subject: `mayf3/auth-service`, branch `main`
- Repository/source: GitHub REST API
- Commit/artifact: `7110463636693b3c2eced9d97ccb186adf46907d`
- Environment: GitHub repository settings
- Observed at: `2026-08-29T10:50:30Z`
- Method: query the same protection, ruleset, workflow, and Check Run endpoints as `OBS-GHE-001`
- Result: protection endpoint returned `404 Branch not protected`; ruleset count was `0`; workflow path was absent; Check Runs were `[]`.
- Provenance: authoring-session command output bound to this Spec's authoring branch

### OBS-GHE-003 — `svc-workflow/main` is unprotected

- Subject: `mayf3/svc-workflow`, branch `main`
- Repository/source: GitHub REST API
- Commit/artifact: `4dd521a5f7ef91e4b02b8a9204529db10f3ceed6`
- Environment: GitHub repository settings
- Observed at: `2026-08-29T10:50:30Z`
- Method: query the same protection, ruleset, workflow, and Check Run endpoints as `OBS-GHE-001`
- Result: protection endpoint returned `404 Branch not protected`; ruleset count was `0`; workflow path was absent; Check Runs were `[]`.
- Provenance: authoring-session command output bound to this Spec's authoring branch

### OBS-GHE-004 — No target currently emits required checks

- Subject: current default-branch automation in all three consumer repositories
- Repository/source: repositories and GitHub Check Runs API
- Commit/artifact: commits in `STATE-GHE-001`
- Environment: GitHub-hosted repository metadata
- Observed at: `2026-08-29T10:50:30Z`
- Method: request `.github/workflows?ref=main` and Check Runs for each exact Head
- Result: every workflow request returned not found and every Check Runs collection was empty.
- Provenance: authoring-session command output

### OBS-GHE-005 — Governance source verification passes its source-repository checks

- Subject: `mayf3/agent-development-governance`
- Repository/source: local clean worktree
- Commit/artifact: `d32b946cbbbc1baa99165d7656fc22e8823a651f`
- Environment: Python standard-library test environment
- Observed at: `2026-08-29T10:50:30Z`
- Method: `python3 -m unittest discover -s tests -v` and `python3 tools/build_manifest.py --check`
- Result: 34 tests passed and the distribution manifest was current. Running the consumer verifier against the source repository correctly failed because the source repository has no consumer `.agents/governance.lock.json`.
- Provenance: authoring-session command output

### OBS-GHE-006 — Authority and open-work scan found no duplicate

- Subject: governance branches, Specs, and open PRs across the governing and consumer repositories
- Repository/source: fetched Git refs and GitHub PR API/search
- Commit/artifact: governance `d32b946cbbbc1baa99165d7656fc22e8823a651f` plus fetched remote refs and open PR snapshots
- Environment: local Git plus GitHub
- Observed at: `2026-08-29T10:50:30Z`
- Method: scan branch names and all referenced governance files; list up to 100 open PRs per repository; search open PRs for enforcement scope
- Result: no matching branch, governing Spec, or open PR existed. The governance repository had one unrelated open Draft PR, `#3`, for Agent operational-layer authority.
- Provenance: authoring-session command output

## 6. Claims and assumptions

### CLM-GHE-001 — Current enforcement permits critical manual bypass

- Support state: SUPPORTED
- Supported by evidence: `EVD-GHE-001`
- Contradicted by evidence: none known
- Uncertainty: an owner may follow manual discipline, but GitHub does not enforce that discipline.

### CLM-GHE-002 — Checks must be installed and proven before active rules

- Support state: SUPPORTED
- Supported by evidence: `EVD-GHE-002`
- Contradicted by evidence: none known
- Uncertainty: none material; requiring nonexistent contexts deterministically blocks ordinary merge.

### CLM-GHE-003 — A new authority is required

- Support state: SUPPORTED
- Supported by evidence: `EVD-GHE-003`
- Contradicted by evidence: none known
- Uncertainty: none material within fetched branches and the recorded open-PR snapshot.

### CLM-GHE-004 — GitHub review identity cannot by itself prove Agent independence

- Support state: INFERRED
- Supported by evidence: `EVD-GHE-004`
- Contradicted by evidence: none known
- Uncertainty: GitHub can prove account and event identity, but multiple local Agents may legitimately act through one owner's GitHub account.

## 7. Evidence relations

### EVD-GHE-001 — Settings observations support the bypass-risk Claim

- Source observations: `OBS-GHE-001`, `OBS-GHE-002`, `OBS-GHE-003`
- Target: `CLM-GHE-001`
- Relation: SUPPORTS
- Bound coordinates: the three exact `main` commits and GitHub settings observed at `2026-08-29T10:50:30Z`
- Strength/sufficiency: strong for the observed repository settings
- Limitations: does not establish whether voluntary manual practice was followed in every historical merge
- Provenance: GitHub REST responses recorded by the authoring session

### EVD-GHE-002 — Workflow inventory supports install-before-enforce ordering

- Source observations: `OBS-GHE-004`
- Target: `CLM-GHE-002`
- Relation: SUPPORTS
- Bound coordinates: the three exact `main` commits at the observation time
- Strength/sufficiency: decisive for the current state
- Limitations: workflows may be added after this observation and must then be re-inventoried
- Provenance: repository contents and Check Runs API responses

### EVD-GHE-003 — Authority scans support `NEW` classification

- Source observations: `OBS-GHE-005`, `OBS-GHE-006`
- Target: `CLM-GHE-003`
- Relation: SUPPORTS
- Bound coordinates: governance base `d32b946cbbbc1baa99165d7656fc22e8823a651f` and open-PR snapshot at the observation time
- Strength/sufficiency: sufficient for authoring preflight
- Limitations: a later concurrent proposal requires deduplication before review or acceptance
- Provenance: fetched refs, Git content search, and GitHub PR API/search

### EVD-GHE-004 — Shared-account operation supports an explicit Agent-attestation layer

- Source observations: `OBS-GHE-006`
- Target: `CLM-GHE-004`
- Relation: SUPPORTS
- Bound coordinates: repository governance model and owner-directed local-Agent execution context at authoring time
- Strength/sufficiency: sufficient to reject GitHub account inequality as the only independence proof
- Limitations: the trusted attestation producer remains implementation work and is not created by this Spec
- Provenance: parent governance identity rules plus this task's execution model

## 8. Decisions

### DEC-GHE-001 — Use active rulesets with no merge bypass actor

- Decision owner: repository owner `mayf3`
- Decision: each named `main` branch will be protected by an active repository ruleset that applies to administrators, has an empty bypass-actor list, requires PR merges, blocks force-push and deletion, and requires all frozen checks.
- Rejected alternatives: voluntary policy only; administrator bypass; one broad bypass team.
- Reason: the owner must retain acceptance authority without possessing a merge-time button that ignores all checks.
- Owner decision remaining: NONE

### DEC-GHE-002 — Separate semantic review from owner acceptance

- Decision owner: repository owner `mayf3`
- Decision: a trusted semantic-review check validates independent Agent execution identity and an exact reviewed Head; a distinct acceptance check validates an owner's explicit acceptance of the exact final Head.
- Rejected alternatives: GitHub approval alone; owner self-review; one combined reviewer/acceptor attestation.
- Reason: GitHub account identity cannot prove local Agent independence, while review recommendation is not owner acceptance.
- Owner decision remaining: NONE

### DEC-GHE-003 — Freeze seven required contexts

- Decision owner: repository owner `mayf3`
- Decision: all three repositories use the exact required contexts in `CTR-GHE-005`; repositories may add stricter checks but may not omit or rename the minimum set during V1 rollout.
- Rejected alternatives: repo-specific ad hoc names; one monolithic opaque check; requiring contexts before producers are proven.
- Reason: stable contexts make settings auditable and prevent silent coverage loss.
- Owner decision remaining: NONE

### DEC-GHE-004 — Roll out in three consumer phases after shadow validation

- Decision owner: repository owner `mayf3`
- Decision: run all checks in non-required shadow mode across all targets, then enable active enforcement in order `dsh-agent-core`, `auth-service`, `svc-workflow`, with a successful canary window and explicit go/no-go record between phases.
- Rejected alternatives: simultaneous activation; security-critical `auth-service` as first canary; settings-first activation.
- Reason: `dsh-agent-core` offers broader PR activity for canary signal without making the authentication authority the first lockout experiment.
- Owner decision remaining: NONE

### DEC-GHE-005 — Emergency action is narrow, logged containment

- Decision owner: repository owner `mayf3`
- Decision: emergency action may suspend one malfunctioning required context or revert the latest settings rollout, but may not permit direct push, force-push, branch deletion, Draft merge, stale acceptance, or a blanket bypass actor.
- Rejected alternatives: disable all protections; permanent owner bypass; undocumented UI repair.
- Reason: recover from enforcement defects without turning containment into durable bypass.
- Owner decision remaining: NONE

## 9. Contracts

### CTR-GHE-001 — `main` is PR-only

For each target repository, updates to `refs/heads/main` MUST be created only by merging a pull request. Direct pushes, including administrator direct pushes, MUST be rejected. The ruleset MUST apply to repository administrators and MUST configure no bypass actor.

### CTR-GHE-002 — Destructive branch updates are forbidden

Force-pushes to and deletion of `refs/heads/main` MUST be rejected for every actor during normal operation and emergency containment.

### CTR-GHE-003 — Draft and unresolved PRs cannot merge

A Draft PR MUST NOT merge. A PR MUST be non-Draft, open, targeted to `main`, free of unresolved required review conversations when that GitHub feature is available, and satisfy every required context on its exact current Head before merge.

### CTR-GHE-004 — Required checks are strict and exact-Head bound

Required checks MUST be configured as strict/up-to-date checks. A success attached to any commit other than the PR's current 40-hex Head MUST NOT satisfy merge eligibility. A skipped, neutral, cancelled, timed-out, stale, missing, or pending result MUST NOT count as success.

### CTR-GHE-005 — Minimum required-check contexts are frozen

Every target `main` ruleset MUST require these exact contexts:

```text
governance/distribution-integrity
governance/spec-lifecycle
governance/structure
governance/semantic-review
governance/acceptance-final-head
governance/current-main-compatibility
repository/validation
```

`repository/validation` MUST execute the repository's accepted build, test, lint, and deterministic generation obligations. Where no such local authority exists, its V1 minimum MUST at least parse/compile supported source and run the repository's existing deterministic tests; it MUST fail rather than report success when no repository validation plan is installed.

### CTR-GHE-006 — Distribution integrity is deterministic

`governance/distribution-integrity` MUST verify the consumer's `.agents/governance.lock.json`, the exact pinned source commit and manifest digest, every vendored file digest, adoption status, acceptance metadata, and local-governance declaration. It MUST fail on missing, proposed, malformed, tampered, floating, or mismatched governance. In the governance source repository's own authoring PRs, the equivalent producer MUST instead run the source manifest check and distribution tests; absence of a consumer lock in the source repository MUST NOT be mislabeled as consumer drift.

### CTR-GHE-007 — Lifecycle, implementation authority, and implementation base are enforced

`governance/spec-lifecycle` MUST evaluate the PR against its exact base and Head and MUST fail when:

1. a proposed or superseded Spec is used as implementation authority;
2. an unmerged `status: accepted` value is treated as active authority;
3. non-mechanical product, configuration, schema, generated-behavior, or operational implementation lacks one primary accepted Spec already present in the PR base;
4. the primary Spec has `implementation_authority: none`;
5. implementation scope exceeds accepted Contracts;
6. a PR combines changed normative meaning with implementation of that changed meaning;
7. accepted stable IDs change meaning, supersession backlinks are incomplete, or partial supersession is attempted.

A proposed Spec, including this Spec while proposed, MUST NOT authorize product implementation or GitHub-settings rollout.

### CTR-GHE-008 — Structure compares the GitHub PR base and Head correctly

`governance/structure` MUST obtain `BASE_SHA` and `HEAD_SHA` from the trusted `pull_request` event payload or GitHub API, verify both are full commits belonging to the PR, fetch those exact objects, compute `MERGE_BASE=$(git merge-base "$BASE_SHA" "$HEAD_SHA")`, and evaluate the PR change set with:

```text
git diff --name-status "$MERGE_BASE" "$HEAD_SHA"
```

It MUST NOT use the runner checkout's implicit `HEAD`, a locally stale `main`, `HEAD^`, or `git diff "$BASE_SHA" "$HEAD_SHA"` as a substitute for GitHub PR diff semantics. It MUST record all three SHAs. The check MUST fail if the event/API coordinates cannot be proven, if a docs-only authority PR contains non-documentation/product implementation, or if a claimed implementation-only PR mutates governing authority. Compatibility with the latest `main`, which may advance after the event base, belongs to `governance/current-main-compatibility`, not to structure.

### CTR-GHE-009 — Semantic review is bound to the exact reviewed Head

`governance/semantic-review` MUST require a successful Semantic Review Record whose `reviewed_head_sha` equals the PR's exact current Head and whose `reviewed_base_sha` and `merge_base_sha` match the structure record. The record MUST include repository, PR number, Spec IDs, reviewer GitHub actor, reviewer Agent execution identity, author Agent execution identity, review producer GitHub App identity/version, review time, recommendation, findings, and stable record locator. Any semantic change or Head movement invalidates the prior result.

GitHub account inequality or a native GitHub approval alone MUST NOT prove Agent independence. The required check MUST verify that reviewer and author Agent execution identities are distinct and that the review attestation was emitted by the dedicated trusted governance-verifier GitHub App, not by PR-controlled code or a general repository workflow token. The persistent record MUST be the completed GitHub Check Run attached to `reviewed_head_sha`: its output MUST contain the complete canonical Semantic Review Record, its `external_id` MUST contain that record's SHA-256 digest, and its App, Check Run ID, URL, creation time, completion time, and Head SHA form the stable locator. Rerequesting review MUST create a new Check Run rather than overwrite an earlier completed record. A mutable PR comment MAY mirror the result but MUST NOT be the sole record.

### CTR-GHE-010 — Acceptance is an owner action on the final Head only

`governance/acceptance-final-head` MUST require an explicit owner acceptance attestation containing repository, PR number, exact 40-hex `accepted_head_sha`, accepting GitHub actor, acceptance time, semantic-review record locator/digest, and acceptance producer identity/version. The accepted Head MUST equal the PR's current Head and the successful semantic review's `reviewed_head_sha`. Any later commit invalidates acceptance.

An authorized owner MAY issue the exact-Head acceptance action even in a single-owner repository, but that action controls only this required context. It MUST NOT waive, override, synthesize success for, or bypass any other check. The active ruleset MUST have no owner/admin bypass actor.

### CTR-GHE-011 — Accepted Head equals merge Head

Immediately before completing a merge, the enforcement producer MUST read the PR Head from GitHub, require equality with `accepted_head_sha`, and bind the merge request to that expected Head using the GitHub merge API's expected-Head field or equivalent compare-and-swap behavior. If the Head changed, the merge MUST fail closed and require new structure, review, acceptance, validation, and compatibility results.

### CTR-GHE-012 — Current-`main` compatibility is separately rechecked

`governance/current-main-compatibility` MUST fetch the current remote `refs/heads/main` after all earlier review/acceptance events, record `CURRENT_MAIN_SHA` and `HEAD_SHA`, and test the exact candidate against that current base using a clean synthetic merge or equivalent GitHub mergeability calculation. It MUST rerun the repository validation and governance checks whose outcome can change under the synthetic merge. It MUST fail on conflicts, stale current-main coordinates, validation failure, or any material difference between tested candidate and the merge candidate. A successful check becomes stale when `main` advances and MUST be rerun before merge.

### CTR-GHE-013 — Settings rollout is settings-last and fail-safe

No required context may be activated until its producer has run successfully in shadow mode on at least one representative open PR and on a synthetic negative fixture in the same repository. Before each activation, the rollout actor MUST capture the complete pre-change settings snapshot and a proposed post-change snapshot, verify API access, verify a recovery path, and confirm no required context is missing. Check producers and persistent evidence storage MUST be installed before settings are made active.

### CTR-GHE-014 — Consumer activation order and canary gates are fixed

Activation MUST proceed in this order:

```text
0. shadow mode on dsh-agent-core, auth-service, and svc-workflow
1. active canary on dsh-agent-core
2. active rollout on auth-service
3. active rollout on svc-workflow
```

Each active phase MUST observe at least one successful eligible PR dry-run or merge simulation, one rejected stale/invalid fixture, settings drift status `CLEAN`, and no unresolved lockout incident before the owner records `GO`. A failed phase blocks later phases.

### CTR-GHE-015 — Rollback and emergency containment are bounded

A rollout failure MUST first revert to the exact pre-change settings snapshot. Emergency containment requires owner authorization and an incident ID, must identify the single failing context or settings delta, and may only suspend that context or revert the latest rollout. It MUST preserve PR-only updates, Draft exclusion, force-push denial, deletion denial, exact-Head acceptance, and the no-bypass-actor rule. It MUST record actor, time, before/after snapshots, reason, affected PRs, and restoration deadline. Durable repair requires normal Spec and review flow.

### CTR-GHE-016 — Lockout prevention is tested before activation

Before each active phase, a non-merge dry run MUST prove that the owner can: open/update a PR, obtain every context, issue exact-Head acceptance, observe current-main compatibility, and submit a compare-and-swap merge request without bypass. A separate rollback dry run MUST prove that the exact pre-change settings snapshot can be restored through the documented API path. Any missing permission, unavailable producer, recursive dependency, or ambiguous recovery result blocks activation.

### CTR-GHE-017 — Settings state and drift are persistent and auditable

Every rollout or rollback MUST create a persistent Settings Rollout Record containing the accepted Spec revision, implementation base, repository, branch, actor, timestamps, pre/post canonical settings JSON and digests, required-context list, bypass actors, canary evidence, API responses, and result. A scheduled or event-driven external monitor MUST compare live settings with the accepted snapshot. Unapproved drift, including addition of a bypass actor or removal of a check, MUST raise an incident and block a `CLEAN` rollout gate. The platform-root owner's ability to edit settings is a declared residual risk, not a merge bypass granted by this Spec.

### CTR-GHE-018 — This authority cannot authorize product behavior

While this Spec is `proposed`, it authorizes no implementation. After acceptance, `implementation_authority: contracts` authorizes only the bounded enforcement producers, evidence records, settings rollout, monitoring, and rollback defined here. It MUST NOT authorize consumer product code, deployment, database, identity, Grant, credential, or unrelated workflow behavior. Those changes require their own accepted, implementation-authorizing local authority present in their implementation base.

## 10. Acceptance

### ACC-GHE-001 — Ruleset invariant inspection

- Contracts: `CTR-GHE-001`, `CTR-GHE-002`, `CTR-GHE-003`, `CTR-GHE-004`, `CTR-GHE-005`
- Method: compare canonical live ruleset JSON for each repository to the accepted settings snapshot and exercise rejected direct-push, force-push, deletion, Draft, missing-check, and stale-check fixtures
- Environment: staged repository settings and non-destructive test branches/PRs
- Required evidence: exact repository, ruleset ID/version, canonical JSON digest, fixture Heads, API responses, Check Runs, and evaluation time
- Expected result: only non-Draft PR merge with all seven exact contexts successful on the current Head is eligible; bypass actors are empty
- Failure condition: any prohibited update is accepted, any minimum context is absent/renamed, or owner/admin bypass exists

### ACC-GHE-002 — Distribution and lifecycle negative matrix

- Contracts: `CTR-GHE-006`, `CTR-GHE-007`, `CTR-GHE-018`
- Method: run positive and negative fixtures for valid adoption, tamper, missing/proposed lock, proposed Spec implementation, `implementation_authority:none`, Spec absent from base, combined Spec/implementation, and product work citing this enforcement Spec
- Environment: trusted check producer at an exact implementation commit
- Required evidence: fixture repository/base/Head SHAs, inputs, outputs, and Check Run conclusions
- Expected result: only valid adopted governance and accepted in-base implementation authority pass; this Spec never authorizes product work
- Failure condition: any forbidden fixture succeeds or the governance source is falsely required to carry a consumer lock

### ACC-GHE-003 — Structure coordinate matrix

- Contracts: `CTR-GHE-008`
- Method: execute the structure check against PRs with advanced base, merge commit checkout, rebased Head, docs-only violation, and authority mutation
- Environment: trusted pull-request metadata with exact fetched commits
- Required evidence: `BASE_SHA`, `HEAD_SHA`, `MERGE_BASE`, command, diff, and decision
- Expected result: diff matches GitHub PR semantics and structural violations fail
- Failure condition: result depends on implicit runner `HEAD`, stale local `main`, `HEAD^`, or two-dot base comparison

### ACC-GHE-004 — Independent semantic review binding

- Contracts: `CTR-GHE-009`
- Method: validate a good record, same-Agent reviewer record, GitHub-only approval, wrong-Head record, altered-Head record, untrusted producer, and missing-ledger record
- Environment: dedicated trusted governance-verifier GitHub App
- Required evidence: completed Check Run ID/URL/external ID, canonical record/digest, author and reviewer execution identities, exact SHAs, App identity, and producer version
- Expected result: only a trusted, distinct-Agent, exact-Head record passes; every rerequest creates a new completed Check Run record
- Failure condition: account approval alone, same execution identity, mutable comment alone, wrong Head, overwritten prior Check Run, or missing persistent record passes

### ACC-GHE-005 — Owner acceptance without bypass

- Contracts: `CTR-GHE-010`, `CTR-GHE-011`
- Method: issue owner acceptance for an exact Head, then test unchanged Head, changed Head, non-owner actor, missing semantic review, and failed unrelated check
- Environment: single-owner repository simulation with active no-bypass ruleset
- Required evidence: acceptance attestation, Check Runs, expected-Head merge request, and API outcomes
- Expected result: owner acceptance passes only its own context; merge succeeds only for the same Head after every other context succeeds
- Failure condition: acceptance waives another check, stale Head merges, or owner/admin can select a blanket bypass

### ACC-GHE-006 — Current-main compatibility race matrix

- Contracts: `CTR-GHE-012`
- Method: advance `main` after review, rerun synthetic merge validation, and attempt merge with both compatible and incompatible advances
- Environment: clean clones and exact remote refs
- Required evidence: prior/current `main` SHA, Head SHA, synthetic merge tree/commit, rerun outputs, and merge API outcome
- Expected result: compatible changes receive a fresh exact result; conflicts or failures block; another `main` advance stales the result
- Failure condition: a result against old `main` remains sufficient after `main` advances

### ACC-GHE-007 — Shadow, canary, and phased rollout

- Contracts: `CTR-GHE-013`, `CTR-GHE-014`, `CTR-GHE-016`
- Method: execute the frozen phase plan without changing order and record each go/no-go gate
- Environment: all three repositories, shadow producers first, active settings later
- Required evidence: successful and negative fixtures, permission probe, lockout and rollback dry runs, phase records, and owner `GO`
- Expected result: producers precede settings; `dsh-agent-core` completes canary before `auth-service`, which completes before `svc-workflow`
- Failure condition: simultaneous/settings-first activation, skipped phase, failed canary, or unproven recovery

### ACC-GHE-008 — Emergency rollback preserves hard invariants

- Contracts: `CTR-GHE-015`
- Method: simulate one malfunctioning context and restore the exact pre-change snapshot; separately exercise bounded single-context suspension
- Environment: non-production settings fixture or reversible canary
- Required evidence: owner authorization, incident ID, before/after canonical JSON, actor/time, affected context, and restoration deadline
- Expected result: recovery removes only the failing delta while hard invariants and empty bypass list remain
- Failure condition: all protection is disabled, direct/force/delete becomes possible, bypass actor is added, or action is unrecorded

### ACC-GHE-009 — Settings drift detection

- Contracts: `CTR-GHE-017`
- Method: compare live settings to the accepted snapshot, then inject fixture drift by removing one check and adding one bypass actor
- Environment: settings monitor fixture and canary repository
- Required evidence: rollout record, canonical digests, drift events, incident links, and monitor identity
- Expected result: clean state is reported only on exact match; both drift forms alert and block later rollout gates
- Failure condition: drift remains `CLEAN` or platform-root mutability is represented as impossible

### ACC-GHE-010 — Acceptance-only final-Head recheck

- Contracts: `CTR-GHE-003`, `CTR-GHE-004`, `CTR-GHE-009`, `CTR-GHE-010`, `CTR-GHE-011`, `CTR-GHE-012`
- Method: after all records exist, execute a final acceptance-only verifier that reads GitHub's current PR state, Head, base, Draft state, every other required Check Run, review record, acceptance record, and current `main`
- Environment: exact merge candidate immediately before compare-and-swap merge
- Required evidence: one final eligibility record naming every SHA and Check Run ID
- Expected result: every record agrees on one final Head and current `main`; merge request uses that expected Head
- Failure condition: any Head/base/main/check identity differs, any record is stale, or Draft state is true

### Contract coverage

| Contract | Acceptance | Evidence class | Covered |
|---|---|---|---|
| `CTR-GHE-001` | `ACC-GHE-001` | settings/API fixture | YES |
| `CTR-GHE-002` | `ACC-GHE-001` | settings/API fixture | YES |
| `CTR-GHE-003` | `ACC-GHE-001`, `ACC-GHE-010` | PR-state fixture | YES |
| `CTR-GHE-004` | `ACC-GHE-001`, `ACC-GHE-010` | Check Runs | YES |
| `CTR-GHE-005` | `ACC-GHE-001` | canonical settings | YES |
| `CTR-GHE-006` | `ACC-GHE-002` | deterministic matrix | YES |
| `CTR-GHE-007` | `ACC-GHE-002` | lifecycle matrix | YES |
| `CTR-GHE-008` | `ACC-GHE-003` | exact-SHA diff matrix | YES |
| `CTR-GHE-009` | `ACC-GHE-004`, `ACC-GHE-010` | attestation/ledger | YES |
| `CTR-GHE-010` | `ACC-GHE-005`, `ACC-GHE-010` | owner attestation | YES |
| `CTR-GHE-011` | `ACC-GHE-005`, `ACC-GHE-010` | compare-and-swap API | YES |
| `CTR-GHE-012` | `ACC-GHE-006`, `ACC-GHE-010` | synthetic merge | YES |
| `CTR-GHE-013` | `ACC-GHE-007` | rollout record | YES |
| `CTR-GHE-014` | `ACC-GHE-007` | phase records | YES |
| `CTR-GHE-015` | `ACC-GHE-008` | incident/rollback | YES |
| `CTR-GHE-016` | `ACC-GHE-007` | lockout dry run | YES |
| `CTR-GHE-017` | `ACC-GHE-009` | drift monitor | YES |
| `CTR-GHE-018` | `ACC-GHE-002` | authority-negative matrix | YES |

## 11. Alternatives and disposition

### ALT-GHE-001 — Keep manual governance only

- Disposition: rejected
- Reason: observations show no deterministic barrier against direct or stale merge.
- Evidence/Claims considered: `CLM-GHE-001`
- What would reopen: none while critical bypass risk remains.

### ALT-GHE-002 — Use GitHub approval identity as Agent-independence proof

- Disposition: rejected
- Reason: one GitHub owner account may front multiple distinct local Agents; account identity does not prove execution independence.
- Evidence/Claims considered: `CLM-GHE-004`
- What would reopen: GitHub exposes trusted, non-forgeable local Agent execution identities and reviewer/author separation.

### ALT-GHE-003 — Give the owner a ruleset bypass

- Disposition: rejected
- Reason: owner acceptance is a bounded semantic action, not authority to ignore all deterministic checks.
- Evidence/Claims considered: `CLM-GHE-001`
- What would reopen: none for ordinary merges; emergency settings rollback remains separately bounded.

### ALT-GHE-004 — Enable all repositories simultaneously

- Disposition: rejected
- Reason: absent current check producers make lockout likely and eliminate canary learning.
- Evidence/Claims considered: `CLM-GHE-002`
- What would reopen: not for V1.

### ALT-GHE-005 — Make this Spec product authority in consumers

- Disposition: rejected
- Reason: violates the parent's local product-authority boundary and expands this GitHub-administration Decision into unrelated behavior.
- Evidence/Claims considered: `CLM-GHE-003`
- What would reopen: a separately accepted authority model explicitly changing that boundary.

## 12. Migration, compatibility, and rollback

```text
MIGRATION = implement trusted check producers and evidence records in a separate accepted-authority implementation; run shadow on all targets; activate dsh-agent-core, then auth-service, then svc-workflow
COMPATIBILITY = existing open PRs remain unmergeable until refreshed onto current main and all exact-Head records/checks succeed; no historical check result is grandfathered
ROLLBACK = restore the canonical pre-change settings snapshot for the failed phase; do not roll later repositories forward after a failed phase
EMERGENCY_CONTAINMENT = owner-authorized incident may suspend one failed context or revert the latest settings delta while preserving PR-only, no-force, no-delete, non-Draft, exact-Head, and no-bypass invariants
ANTI_LOCKOUT = producers-first shadow validation, permission probe, merge dry run, rollback dry run, and phase go/no-go record
SETTINGS_DRIFT = external comparison of live canonical JSON against the accepted rollout snapshot
```

This authoring change performs none of those migration or settings actions.

## 13. Open questions

```text
OPEN_OWNER_DECISIONS = NONE
NORMATIVE_TBD = NONE
UNRESOLVED_AUTHORITY_CONFLICT = NONE
PARTIAL_SUPERSESSION = NONE
SPEC_STATUS = proposed
IMPLEMENTATION_AUTHORITY = contracts
CONTRACT_COUNT = 18
CONTRACTS_WITH_ACCEPTANCE = 18
READY_TO_MARK_ACCEPTED = NO
INDEPENDENT_REVIEW_REQUIRED = YES
AUTHORING_READY_FOR_REVIEW = YES
```
