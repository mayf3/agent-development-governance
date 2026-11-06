# STOPPED — format-correction R2 extension

Recorded at 2026-11-06T12:38:07Z. The supplied Owner ruling is attributed to
2026-11-07; that is not a claim about this execution date.

Stop source: the user's red line, “失败即停写 STOPPED-FORMAT-CORRECTION-R2.md”.
The full required suite failed. Implementation writes, commit, push and PR
creation stopped immediately after that result. Subsequent work was read-only
failure diagnosis and this stop record. This record supersedes the Brief's
initial CONTINUE readiness; it does not change Product Authority.

## Exact checkpoint

- Repository: mayf3/agent-development-governance.
- Parent, HEAD and integration base:
  `9d4d0e3a4cf57f95f8078982b1b41fa5aaecff02` (merged R2 PR #22).
- Isolated worktree: `/private/tmp/adg-fmt-r2-rc3`.
- Isolated branch: `validate/historical-format-correction-r2-rc3`.
- Candidate implementation is UNCOMMITTED; HEAD identifies the base only.
- Original user checkout and its untracked handoff files were preserved.
- Local VERSION is 2.0.0-rc.3 and the manifest was rebuilt; complete version
  coherence has NOT passed. No release/tag, consumer adoption or runtime action.

## Actual validation

- Existing transition baseline: 41 tests passed before implementation.
- Expected RED: registered list[dict] -> [] failed on the original validator
  with “mutates accepted supersedes metadata”; test rc 1 as expected.
  Raw log: `docs/evidence/format-correction-r2/red.txt`.
- GREEN: all 13 new regression methods passed, including malformed lists,
  separate candidate markers, unregistered/wrong-ID and nonempty rejection,
  strict/legacy-list immutability, scalar rejection, immutable scope and
  successor/backlink protection. CLI success exposes FORMAT_CORRECTION.
  Raw log: `docs/evidence/format-correction-r2/green.txt`.
- Manifest check: rc 0, “distribution manifest is current”.
  Raw log: `docs/evidence/format-correction-r2/manifest.txt`.
- Full suite: 151 tests, 149 passed, 2 failures; rc 1.
  All existing 41 transition tests and 13 new tests passed in this run.
  Raw log: `docs/evidence/format-correction-r2/suite.txt`.
- Compile, shell syntax, final diff gate, final committed-Head review, push,
  remote/PR verification: NOT EXECUTED after the stop condition.

## Failure diagnosis and minimal closure

1. `test_distribution_version_is_coherent` rejects the stale rc.1 grammar
   version in `.agents/README.md`. The version in
   `.agents/templates/consumer/governance.lock.json` also remains rc.1; the
   test stops on the first file, so that second mismatch is a source readback,
   not a separately executed assertion. Both stale fields already exist on
   parent rc.2, but this rc.3 candidate still must synchronize them. The acting
   agent omitted them during the version update. No test weakening is needed.
2. `test_vendor_cli_default_is_no_write_dry_run` returns 2 because the existing
   `validate_source_checkout` gate rejects dirty distributed source files
   (`tools/vendor.py:158-169`). This is expected clean-source enforcement on
   the uncommitted candidate, not proof of a classification regression.
   Resolving it requires testing the exact committed candidate; do not bypass
   the gate or change its meaning.

Read-only reproduction on the clean existing source checkout
`/private/tmp/adg-vendor-source`, HEAD exactly the parent above, ran the same
two tests with `PYTHONDONTWRITEBYTECODE=1`: version coherence failed for rc.2
versus rc.1; vendor dryrun passed. The source checkout remained clean. No
baseline mutation or consumer write was performed.

Independent read-only review by `/root/authority_boundary_review` confirmed
that malformed eligibility preserves `is_reference_id`, including accepted
whole legacy-ID retirement references. Strict/legacy legal lists are not
eligible for clearing; unresolved/new malformed candidates remain rejected.
The reviewer independently identified the stale consumer-lock version and
the correct clean-source vendor gate. This is affected uncommitted-diff
review, not final-Head approval or upstream acceptance.

```text
FINDING = REQUIRED_GATE_FAILURE
SOURCE = required full regression suite and user failure-stop instruction
COUNTEREXAMPLE = version coherence fails; vendor gate rejects uncommitted distributed source
IMPACT = complete rc.3 delivery is not verified; commit/push/PR not delivered
MINIMAL_CLOSURE = synchronize only the two remaining version fields; rebuild manifest; validate an exact committed candidate without bypass; independent final-Head review; push and open unmerged PR
AFFECTED_READINESS = implementation continuation, PR delivery, release
IMPLEMENTATION_ALLOWED = NO under the triggered stop instruction
MERGE_READY = NO
OPERATION_ALLOWED = NO
NEXT_ACTION = STOP
```

No further implementation changes were made after the failure. The minimal
closure above describes the resumable repair; it is not permission to ignore
the current stop condition.

## Frozen candidate hashes

- `.agents/tools/validate_spec_transition.py` (18577 bytes):
  `5be5fae2ab02b87d1fc138e5da21f91f973b512e2198bcf5149a4ae03331b53e`
- `tests/test_format_correction_r2.py` (7581 bytes):
  `0c5aaf3d09525e12772d51652fc2923ca660a557aeacf656b181309edbd13070`
- `distribution/manifest.json` (4612 bytes):
  `85c138b53c952f0b328004104f9bb756254f7f6c86706b6868619d252878248b`

Tracked diff at stop: validator +54/-19, CHANGELOG +12, README +2/-2,
VERSION +1/-1, manifest +3/-3. New untracked delivery files are the Brief,
13-method regression file, expected RED/GREEN/manifest/full-suite logs and
this stop record. The candidate is preserved for review; no success or full
conformance claim is made.
