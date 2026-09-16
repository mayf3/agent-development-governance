# Model convergence: author scenario review

```text
RECORD_KIND = non-authoritative author self-review
SPEC = AGENT_MODEL_CONVERGENCE_V1 (proposed)
BASE_HEAD = 9dcd0c49a5932e44e2801317b6281bdc6a168d25
DATE = 2026-09-15
INDEPENDENT_REVIEW = NOT_PERFORMED
PRODUCT_RUNTIME_TESTS = NOT_PERFORMED
```

This record evaluates the proposed wording against explicit counterexamples. It is not a consumer census, an executed product test, independent review, or evidence that any real identity mapping is correct. The PR binds the reviewed document blobs to its exact candidate commit. The actual reported identity incident is input to Issue #15; the cases below are deliberately de-identified design probes.

| Case | Input | Required disposition under the proposal | Author assessment / rule |
|---|---|---|---|
| 1. Historical identity duplication | A workflow uses an older principal; one service says active while another denies current admission. | Investigate the affected fact owners and real references; establish mappings in the owning product. Do not infer illegality or a successor from that disagreement alone. | Covered by `CTR-CONV-001`, `CTR-CONV-002`. |
| 2. Legitimate multiple IDs | One agent has an application ID, a security principal, and two clients during authorized rotation. | Preserve distinct roles and permitted rotation; do not collapse IDs or invent a universal 1:1 client rule. | Covered by `CTR-CONV-002`. |
| 3. Partial emergency repair | Replacing one reference makes publish succeed, but old references and fallback remain. | Report mitigation or a bounded stage, not completed convergence. | Covered by `CTR-CONV-003`, `CTR-CONV-006`. |
| 4. Permanent fallback proposal | On failure, try old UUID, old name, then an alias table indefinitely. | Evaluate migration/removal first. No silent acting-identity switch; a bridge needs actual consumers and an exit. | Covered by `CTR-CONV-002` through `CTR-CONV-004`. |
| 5. Duplicate configuration paths | A new configuration key is supported, but an old key and another writable store still independently choose the runtime value. | Identify the owning fact and actual readers/writers, migrate those consumers, stop retired writes, and inspect startup/recovery and deployment. | Covered by `CTR-CONV-001`, `CTR-CONV-005`. |
| 6. Supported old protocol | An external API version is still explicitly supported; its input is translated into current storage. | Do not retire the support obligation by labeling it legacy. Translation must preserve existing identity/authorization Contracts and not create retired-format objects. | Covered by `CTR-CONV-004`, `CTR-CONV-008`. |
| 7. Bridge with an expiry | A real consumer remains; the recorded retirement date arrives before migration is safe. | Explicitly resolve the exception under existing authority. Neither silent renewal nor date-triggered destructive deletion is permitted. | Covered by `CTR-CONV-004`, `CTR-CONV-005`. |
| 8. Read-only history | Old principal values remain in immutable audit records, but cannot grant current eligibility. | Preserve explainability and list history separately from active references. Zero means zero in the stated active scope, not erasing history. | Covered by `CTR-CONV-005`, `CTR-CONV-006`. |
| 9. Recovery revival | A restart/bootstrap or retry path recreates the retired principal or duplicate task. | Final convergence fails even when the normal current path works. Fix the authorized affected recovery path and verify it. | Covered by `CTR-CONV-005`, `CTR-CONV-006`. |
| 10. Unknown coverage and deployment drift | Grep is clean; only one table was inspected; production still runs old code. | Keep uninspected coverage unknown and distinguish source completion from deployed closure. Do not report final PASS or zero. | Covered by `CTR-CONV-001`, `CTR-CONV-006`. |
| 11. Routine unrelated edit | A small authorized text or code edit does not replace a model or touch migration/identity/state-source ambiguity. | No empty convergence table, global census, or new approval round. Stop at the existing task boundary. | Covered by `CTR-CONV-007`. |
| 12. Unsafe adoption shortcut | An agent treats source acceptance as permission to merge identities, transfer grants, delete production rows, or activate all consumers. | Reject the scope expansion; preserve local adoption and existing product/operation authority. | Covered by `CTR-CONV-005`, `CTR-CONV-008`. |

## Authoring outcome and limits

The authored rules explicitly address all twelve probes. This is an author interpretation, not a mechanically proven semantic result or an independent acceptance verdict. The Spec has eight Contracts with explicit Acceptance coverage; later distribution canaries and actual consumer retirement Evidence remain unexecuted.

The proposal also names the required integration surface: the existing shared README, PREFLIGHT mode, REVIEW mode, Change Brief template, and Review Record template. Merely merging the proposed Spec does not satisfy distribution delivery. No new compatibility registry, review workflow, or permanent model is introduced by these files.
