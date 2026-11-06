# Format-correction R2 extension delivery record

Authorization: the user-supplied contract task, attributed to Owner ruling A
dated 2026-11-07, authorizes the original responsibility chain to repair this
mechanical classification defect, bump 2.0.0-rc.2 to 2.0.0-rc.3, rebuild the
manifest, commit, push and open an unmerged upstream PR. The attributed ruling
date is not the execution date. This record preserves that mandate; it does
not create Product Authority.

Allowed delta: identify dict and lists containing illegal whole-authority
references as historical format-correction candidates; permit only an
explicitly registered accepted/superseded record's old malformed value to
become precisely `[]`. Keep all other validation and immutable fields closed.
No force/skip/migration switch, consumer changes, merge, tag or publication.
On an unexpected required-gate failure, stop writing implementation and create
`STOPPED-FORMAT-CORRECTION-R2.md`. An expected RED regression is evidence of
the reported defect, not a failed delivery gate.

```text
SPEC_GOVERNANCE_MODE = PREFLIGHT
TARGET_REPOSITORY = mayf3/agent-development-governance
BASE_HEAD = 9d4d0e3a4cf57f95f8078982b1b41fa5aaecff02
CURRENT_BASE_HEAD = 9d4d0e3a4cf57f95f8078982b1b41fa5aaecff02
ISOLATED_PARENT = 9d4d0e3a4cf57f95f8078982b1b41fa5aaecff02
ISOLATED_REF = validate/historical-format-correction-r2-rc3
ISOLATED_WORKTREE = /private/tmp/adg-fmt-r2-rc3
ROUTE_STAGE = IMPLEMENTATION
AUTHORITY_ACCEPTED_IN_BASE = YES
GOAL_OR_TARGET = deliver the bounded malformed-list classification repair for upstream review
CURRENT_GAP = R2 permits registered dict -> [] but rejects the reported list[dict] historical shape
AUTHORITY_ACTION = REUSE
PRIMARY_AUTHORITY = AGENT_DEVELOPMENT_GOVERNANCE_V1@9d4d0e3a4cf57f95f8078982b1b41fa5aaecff02
RELATED_AUTHORITIES = accepted SPEC_FORMAT_V0 section 2.7 at the same base
IMPLEMENTATION_AUTHORITY = contracts
PLAN_LEVEL = BRIEF
ASSURANCE_LEVEL = DURABLE
EXECUTION_MANDATE = VALID
MUTATION_AUTHORIZATION = VALID
ISOLATED_WRITE_SURFACE = YES
CONTROLLED_RUNBOOK_REQUIRED = NO
SPEC_GAP_DEPENDENCY = NONE
LIVE_AUTHORITY_GAP = NONE
EVIDENCE_REVIEWABILITY = PASS
OWNER_DECISION_REQUIRED = NO
BASE_IMPACT = BOUNDED
IMPLEMENTATION_ALLOWED = YES
MERGE_READY = NO (upstream review and merge outside this mandate)
OPERATION_ALLOWED = NO (consumer/runtime operation outside this mandate)
EVIDENCE_NEEDED = baseline, expected RED, GREEN, full CI-equivalent checks, manifest hashes, independent affected-surface and final-Head review, remote/PR readback
DONE_WHEN = bounded repair and regressions pass; rc.3 manifest matches; commit pushed; unmerged PR open
EXPANSION_TRIGGER = required-gate failure, authority gap, widened exemption, occupied rc.3 identity, or relevant conflicting target movement
NEXT_REAL_ACTION = reproduce and repair malformed-list classification, then deliver PR
NEXT_ACTION = CONTINUE
```

Authority interpretation: SPEC_FORMAT section 2.7 and the accepted schema
explicitly permit matching whole legacy-ID retirement references. They remain
legal references and immutable; the malformed-list predicate uses the existing
`is_reference_id` legality rule. A list containing only legal legacy references
must never become eligible for clearing merely because those IDs are not the
strict active-ID form. Duplicates alone do not create this exemption.

Observed baseline: origin/main is the merged R2 PR #22 and VERSION is
2.0.0-rc.2. All 41 existing transition tests passed (discovery, Python 3).
The task's cited historical shape is supplied context, not a new readback of
the consumer repository. Independent read-only authority review found no
load-bearing gap and confirmed the legal legacy-reference boundary.
