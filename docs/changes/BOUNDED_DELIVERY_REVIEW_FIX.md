# Bounded delivery review correction

## Scope and authorization

Owner request (2026-09-26): "我是希望你直接改一下原本的治理仓库".
Target: mayf3/agent-development-governance, isolated branch from
`1d7bbe6a53a471656102d3b078ac02dcb2200587`.
Allowed: correct the reviewed validator/rule inconsistencies, add regression tests,
update current-state summaries and prepare a candidate PR.
Not performed/authorized by this record: production operations, consumer adoption,
credential changes, stable publication, self-acceptance, or self-independent review.

Existing governing Contracts: `CTR-GOV1-011` (dependent gap stop),
`CTR-GOV1-014` (candidate/base and final-Head binding), `CTR-GOV1-015`
(proportional conformance), `CTR-GOV1-019` (closed blocker power), and
`CTR-GOV1-020` (goal/stop controls). Accepted Specs are byte-unchanged.
This is an implementation/change record, not a replacement Product Authority.

## Changes

- Separate review scope from raw Head movement; require evidence for DELTA/FULL.
- A stopping Spec gap identifies the missing decision and actual dependency.
- An open Blocker cannot declare its affected work ready; unrelated work may continue.
- Use existing Brief/PR/release records for bounded delivery, scope/gates, cumulative
  rounds and the next real action. Do not add a release service or recursive records.
- Fix stale current summaries; retain history and immutable release tags.

## Verification and limits

Baseline: 86 unittest tests passed on the pinned parent.
Regression-first: 28 new tests ran against the old validator and exposed the
expected failures before implementation; those tests then passed after correction.
Run the complete CI commands on the final candidate; the PR records actual results.
All examples are synthetic fixtures, never claims about HR or production recovery.

`2.0.0-rc.1` identifies a candidate with a tightened structured-input contract.
Existing unchanged route inputs still work. Resumed movement/gap records add the
new fields; old history is not rewritten, and pinned consumers are unaffected.
The validator cannot prove semantic truth or cross-turn progress. The three-round
convergence guard and execute-next behavior are explicit Agent policy, not a new
runtime enforcement claim. Owner acceptance and independent review remain separate.

Done when: regression and existing CI checks pass, manifest is deterministic,
accepted Specs are unchanged, and this bounded change is committed in a PR.
Do not expand this change into deployment/recovery architecture or consumer rollout.
