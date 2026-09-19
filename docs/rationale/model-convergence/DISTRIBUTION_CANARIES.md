# Model Convergence distribution canaries

```text
CANDIDATE = development-governance-v0 1.1.0 distribution candidate
AUTHORITY = AGENT_MODEL_CONVERGENCE_V1 (accepted; ACC-CONV-005 canary requirement)
METHOD = each scenario is routed through the distributed grammar text at the
         candidate Head: PREFLIGHT probe, disposition vocabulary, REVIEW
         convergence-exit conditions, and template conditions
INTEGRITY = tools/build_manifest.py --check; unittest discover -s tests
```

These are design probes of the distributed guidance at this exact candidate,
not production Evidence and not conformance of any consumer. Citations name
the distributed file and section that drive each decision.

## Canary A — legitimate distinct IDs

```text
SCENARIO = agentId / principalId / clientId in one system; genuinely
           different responsibilities (agent execution identity, authorization
           principal, API client credential); no shared single responsibility
EXPECTED = NO forced merge; distinct entities preserved
DECISION = NO_MERGE — the duplication test requires "the same business
           responsibility served by multiple independently maintained
           executable models"; different identifiers alone are explicitly
           not duplication
CITED    = .agents/README.md "Model convergence and retirement": "Different
           identifiers alone are not duplication: preserve genuinely distinct
           entities ... never merge on name similarity, prefixes, or
           unverified historical mapping."
RESULT   = PASS
```

## Canary B — duplicate legacy path without consumers

```text
SCENARIO = one business responsibility; a new canonical path exists plus an
           old still-executable fallback path; no real consumer of the old
           path remains
EXPECTED = review rejects final convergence until the old execution path
           retires
DECISION = REJECT_FINAL_CONVERGENCE — PREFLIGHT question 4 forces evaluation
           of migrate/delete/refactor over a permanent fallback; REVIEW
           requires OLD_EXECUTION_PATH_RETIRED proven before final
           convergence may pass; keeping a consumerless executable fallback
           is exactly the "permanent mapping, fallback, or compatibility
           layer" the grammar prefers against
CITED    = .agents/skills/spec-governance/modes/PREFLIGHT.md "Affected-work
           convergence probe" question 4; .agents/skills/spec-governance/
           modes/REVIEW.md "Convergence exit (conditional)":
           OLD_EXECUTION_PATH_RETIRED
RESULT   = PASS
```

## Canary C — temporary bridge with real consumers

```text
SCENARIO = migration in progress; legacy path still has real consumers;
           proposal keeps it temporarily as a bridge
EXPECTED = bridge allowed, but only with a real consumer and an exit
           condition
DECISION = ALLOWED_AS_TEMPORARY_BRIDGE — the disposition set contains
           TEMPORARY_BRIDGE with "bounded compatibility with a real consumer
           and an exit condition"; templates require REAL_CONSUMERS and
           BRIDGE_EXIT_CONDITION exactly when this disposition is used; and
           "a remaining bridge means a bounded stage, not final retirement"
CITED    = .agents/README.md disposition table; .agents/templates/
           CHANGE_BRIEF_TEMPLATE.md "Model convergence (conditional)";
           REVIEW mode "Convergence exit (conditional)"
RESULT   = PASS
```

## Canary D — stable supported public facade

```text
SCENARIO = a long-supported public facade/compatibility surface is a formal
           support commitment, not a migration leftover
EXPECTED = NOT required to retire; does not block convergence
DECISION = RETAINED_PERMANENTLY — "a stable supported public facade may
           remain permanently; it is not an obsolete path merely because it
           is old"; the review record states a facade "is not required to
           retire"; changing the support promise would need the normal
           authority route, not this rule
CITED    = .agents/README.md "Model convergence and retirement";
           .agents/templates/REVIEW_RECORD_TEMPLATE.md "Model convergence
           exit (conditional)"
RESULT   = PASS
```

## Canary E — recovery revives the retired path

```text
SCENARIO = the old path exited its normal state, but rollback/recovery or a
           restart/bootstrap route makes it executable again; the change
           still claims final convergence
EXPECTED = final convergence claim rejected
DECISION = REJECT_FINAL_CONVERGENCE — REVIEW requires
           RECOVERY_DOES_NOT_REVIVE_OLD_PATH: "applicable restart, recovery,
           retry, replay, and migration reruns do not recreate the retired
           model"; the grammar binds "the retired executable path is excluded
           from affected normal, fallback, and restart/recovery routes"; and
           a rollback that re-enables a retired path reopens the claim
CITED    = .agents/README.md "Model convergence and retirement";
           .agents/skills/spec-governance/modes/REVIEW.md "Convergence exit
           (conditional)"
RESULT   = PASS
```

## Canary F — unrelated small fix

```text
SCENARIO = a bounded fix that touches no historical ID, old field, entrypoint,
           state store, fallback, adapter, dependency replacement, or recovery
           path
EXPECTED = short path; no empty convergence paperwork; no new approval
DECISION = SHORT_ROUTE — the PREFLIGHT probe fires "only when the task
           actually touches" the trigger set; "an unrelated task skips this
           probe entirely: no global census, no empty convergence matrix, no
           new approval"; templates demand only
           MODEL_CONVERGENCE_APPLICABLE = NO and skip the remaining fields
CITED    = .agents/skills/spec-governance/modes/PREFLIGHT.md "Affected-work
           convergence probe"; .agents/templates/CHANGE_BRIEF_TEMPLATE.md and
           .agents/templates/REVIEW_RECORD_TEMPLATE.md conditional notes
RESULT   = PASS
```

## Summary

```text
CANARY_A = PASS (no forced merge of distinct IDs)
CANARY_B = PASS (final convergence rejected while a consumerless old path stays executable)
CANARY_C = PASS (bridge allowed only with consumer + exit condition)
CANARY_D = PASS (stable facade not required to retire)
CANARY_E = PASS (recovery revival rejects final convergence)
CANARY_F = PASS (unrelated fix keeps the short route)
```
