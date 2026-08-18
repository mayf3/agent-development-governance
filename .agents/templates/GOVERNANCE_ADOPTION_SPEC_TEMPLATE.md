---
spec_id: REPOSITORY_DEVELOPMENT_GOVERNANCE_ADOPTION_V1
status: proposed
spec_kind: invariant
authority_level: governing_spec
implementation_authority: none
scope:
  - owner/repository
governed_by: []
external_authorities:
  - repository: mayf3/agent-development-governance
    authority_id: AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0
    revision: REPLACE_WITH_40_HEX_SOURCE_COMMIT
    relation: constrained_by
supersedes: []
superseded_by: null
owners:
  - repository-maintainers
---

# REPOSITORY_DEVELOPMENT_GOVERNANCE_ADOPTION_V1

## 1. Goal

Adopt an exact revision of the shared Development Grammar and Spec-governance distribution while preserving this repository's local product and acceptance authority.

## 2. Scope and non-goals

In scope:

- vendored governance bytes and lock;
- local authority precedence and acceptance actors;
- forward-only application to future non-mechanical work;
- explicit future update and rollback process.

Out of scope:

- product behavior changes;
- bulk migration of historical documents;
- claiming semantic CI or branch protection that is not active.

## 3. Authority and dependencies

```text
SOURCE_REPOSITORY = mayf3/agent-development-governance
SOURCE_COMMIT = <40-hex>
DISTRIBUTION_VERSION = <version>
MANIFEST_SHA256 = <sha256>
LOCAL_ACCEPTANCE_ACTOR = <role or identity>
```

The external distribution supplies grammar and protocol content. It does not own this repository's Product Direction, Architecture, Specs, code, or acceptance actions.

## 4. Current State

Record the repository's existing authority files, current enforcement level, existing `.agents` content, and any known conflicts, with commit and provenance coordinates.

## 5. Observations

Record the exact source checkout, vendor dry-run, resulting diff, lock contents, integrity-verifier result, and local authority inventory.

## 6. Claims and assumptions

State whether forward-only adoption is compatible with current repository practice and identify any open assumption that could weaken authority or merge safety.

## 7. Decisions

### DEC-ADOPT-001 — Adopt exact vendored governance

- Decision: adopt the exact source commit recorded above.
- Rejected alternative: floating `main`, `latest`, or implicit remote authority.
- Reason: local bytes, visible diffs, exact base-branch identity, and explicit updates.

### DEC-ADOPT-002 — Preserve local product authority

- Decision: local Product Direction, Architecture, accepted Specs, and authorized maintainers remain authoritative for this repository.
- Rejected alternative: central repository automatically governs consumer product behavior.
- Reason: repository ownership and cross-repository authority boundaries.

## 8. Contracts

### CTR-ADOPT-001 — Exact revision

The repository MUST vendor the distribution from the exact source commit recorded in `.agents/governance.lock.json`. Floating references MUST NOT activate governance.

### CTR-ADOPT-002 — Truthful adoption state

A prepared snapshot MUST remain `adoption.status: proposed` with null acceptance metadata. Only the authorized local acceptance action MAY set `adoption.status: accepted`.

### CTR-ADOPT-003 — Local authority map

`.agents/local/README.md` MUST identify Product Direction, Architecture/invariants, Spec acceptance actors, mechanical-exemption reviewers, emergency actors, and persistent investigation/conformance locations.

### CTR-ADOPT-004 — Explicit updates

No upstream change MAY alter local governance until a separate docs-only update is reviewed, accepted, and merged in this repository.

### CTR-ADOPT-005 — Honest enforcement

The repository MUST represent manual policy, integrity checks, syntax gates, branch protection, and semantic review according to their actual implemented state.

## 9. Acceptance

Every Contract above must map to an Acceptance item that checks the lock, source commit, vendored bytes, local authority file, review/acceptance record, and actual repository enforcement settings.

## 10. Alternatives and disposition

Record rejected submodule, package, floating branch, or local-copy alternatives only when they were materially considered.

## 11. Migration, compatibility, and rollback

```text
MIGRATION = forward-only
HISTORICAL_REWRITE = none
ROLLBACK = revert the complete adoption commit
```

## 12. Open questions

```text
OPEN_OWNER_DECISIONS = <NONE or list>
NORMATIVE_TBD = <NONE or list>
UNRESOLVED_AUTHORITY_CONFLICT = <NONE or list>
READY_TO_MARK_ACCEPTED = NO
```
