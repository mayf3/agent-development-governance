# Model-guided development delivery record

## Owner direction and authorized boundary

The owner requested on 2026-11-25 that shared mathematical modeling and formal
verification become a continuing development principle across Agent Core,
mobile entrypoints, the personal assistant, and workbenches. The correction was
explicit: actively build and reuse models to guide development; do not turn the
request into construction of a new class of mathematical primitives. The owner
authorized the corresponding pull requests and merges. This is a retained
summary of the conversation instruction, not a fabricated external issue or
proof of product acceptance.

Authorized scope: add the bounded governance principle, make it discoverable
in the existing distribution after source acceptance, and align the shared
method guide in `mayf3/primitives`. Consumer adoption, product modifications,
runtime operations, new platforms, stable release tags, and stable release publication are not
part of this record. The parent coordinator owns commit, push, PR, and merge.

## Current route — source authority authoring

```text
TARGET_REPOSITORY = mayf3/agent-development-governance
BASE_HEAD = c1fad8976e50e96adb27a4c7e2dd4f97bf2e899e
CURRENT_BASE_HEAD = c1fad8976e50e96adb27a4c7e2dd4f97bf2e899e
ISOLATED_WRITE_SURFACE = feat/model-guided-development-authority in dedicated clone
AUTHORITY_ACTION = NEW
PRIMARY_AUTHORITY = AGENT_DEVELOPMENT_GOVERNANCE_V1 at BASE_HEAD
RELATED_AUTHORITY = AGENT_MODEL_CONVERGENCE_V1 at BASE_HEAD
PLAN_LEVEL = BRIEF
ASSURANCE_LEVEL = CONTROLLED
ROUTE_STAGE = AUTHORITY_AUTHORING
AUTHORITY_ACCEPTED_IN_BASE = NO (new model-guided development authority)
MUTATION_AUTHORIZATION = owner-authorized bounded PR/merge task, summarized above
IMPLEMENTATION_ALLOWED = NO until new authority is accepted on main
OPERATION_ALLOWED = NO
```

The new independent obligation uses a new Spec ID. Existing accepted Decisions,
Contracts, and frontmatter are preserved. This phase changes only the new Spec,
the Spec index, and this record. It does not change `.agents/**`, `VERSION`,
distribution bytes, tools, or consumer state.

## Goal and gap

Goal: make models an active and cumulative aid to development, with explicit
assumptions, appropriate formal verification, implementation mappings, and real
acceptance. Gap: the current governance grammar has evidence and convergence
rules but no explicit continuing modeling obligation.

The proposed scope is:

- assess modeling for behavior changes and explicitly model critical mechanisms;
- reuse shared/project models and contribute useful corrections;
- prioritize stable, high-value properties for suitable machine verification;
- keep model, implementation, and real acceptance evidence distinct;
- preserve original failures and goals through the counterexample repair loop;
- keep unrelated proof work and platform design outside bounded product repairs.

## Review and execution boundary

Before authoring merge, independently review the exact candidate, evaluate
`ACC-MGD-001` through `ACC-MGD-007` as source-level semantic scenarios, preserve
accepted authority bytes, and run existing integrity and syntax checks. A source
scenario decision is not production evidence. `ACC-MGD-008` additionally applies
to the later distribution implementation and exact-commit vendor round trip.

The authoring PR may prepare accepted frontmatter only after its independent
review and owner-authorized acceptance; it becomes active on merge. Final-Head
movement receives the parent's applicable delta recheck. This record must not
claim that review, merge, or distribution work occurred before its evidence exists.

## Next phase after source merge

Route the distribution change as `REUSE` against the exact accepted source
commit. Put self-contained concise guidance in `.agents/README.md` and conditional
prompts in the existing Change Brief, Review Record, and Conformance Record
templates. Align the root Agent entrypoint and current status/version surfaces,
rebuild the manifest, run the existing checks, exercise an exact-commit vendor
round trip, and independently review the final candidate. The shared guide is
referenced at its actual immutable commit when available; it is not external
Product Authority or a mandatory live dependency. No skill modification is
required by this planned route.

## Done When and expansion boundary

Done When: source authority and its bounded distribution implementation are
independently reviewed, merged under the existing owner authorization, and
reported at exact revisions; the shared method guide is linked at its actual
revision; consumer adoption and real project use remain accurately unclaimed.

Re-PREFLIGHT only for a concrete conflict with accepted authority, a necessary
semantic gap, or an affected integrity failure. Optional universal models,
additional proof tools, broad consumer rollouts, and unrelated documentation
cleanup are not expansion triggers.

## Current evidence

Executed against the authoring working tree on 2026-11-25:

- `python3 tools/build_manifest.py --check`: PASS; distributed bytes unchanged.
- `python3 -m unittest discover -s tests -v`: 151 tests, PASS.
- `python3 -m py_compile tools/*.py .agents/tools/*.py tests/*.py`: PASS.
- `bash -n tools/publish_bootstrap.sh`: PASS.
- `git diff --cached --check`: PASS.
- New Spec metadata checked with the existing transition validator's
  `validate_metadata`; required sections 1–13 and Contract-to-Acceptance
  coverage 10/10 checked directly: PASS.
- All six existing accepted/superseded Spec files compared byte-for-byte
  against the authoring base: unchanged.

These are structural/integrity observations on the authoring candidate, not
independent semantic acceptance, a mathematical proof, or consumer conformance.
## Independent source review and acceptance preparation

The independent reviewer `/root/formal_model_challenge` reviewed local commit
`13983d0cd3b72a28ed9fd89fdfd1680a71142050`, base
`c1fad8976e50e96adb27a4c7e2dd4f97bf2e899e`, on 2026-11-25 and returned
`SPEC_REVIEW = ACCEPT`, `AUTHOR_INDEPENDENCE = PASS`, zero blockers and zero
Spec gaps. Its exact tree `00145cca0393ed1cb9db7e74eb92c45bc20090d2` was also
published as GitHub commit `993f789d5ed870a828a6562bdf27a106a953e218`;
the trees are byte-identical. Both coordinates identify the reviewed content.

Executed source-level scenario decisions:

| Scenario | Observed decision from reading the proposed Contracts | Result |
|---|---|---|
| ACC-MGD-001 | A two-line retry change still triggers modeling; spelling edits stay short; behavior-preserving refactors check their mapping. | PASS |
| ACC-MGD-002 | Effect-before-receipt crash cannot be treated as an unexplained atomic step; unknown effects and actual boundaries remain explicit. | PASS |
| ACC-MGD-003 | A project without downstream idempotency cannot inherit another project's guarantee; unavailable upstream permits an honest local model. | PASS |
| ACC-MGD-004 | Assuming unique ownership does not independently prove it; bounded exploration keeps its bounds; deferred proof retains responsibility and a trigger. | PASS |
| ACC-MGD-005 | Abstract proof without mapping and rendered media without required review cannot become implementation or product acceptance. | PASS |
| ACC-MGD-006 | Weakening no-duplicate-effects to no-duplicate-receipts cannot close the original failed task. | PASS |
| ACC-MGD-007 | Optional generalization does not block an independent authorized repair; an already required proof gate remains binding. | PASS |

These observations establish source-level semantic review, not execution of a
consumer, a new theorem, or distribution acceptance. ACC-MGD-008 remains for
the implementation phase.

The coordinator prepares `accepted` lifecycle under mayf3's explicit current
PR-and-merge authorization; this does not claim an additional human review.
The preparation changes only lifecycle status, the Spec index, and this real
review receipt. Decisions, Contracts, Acceptance scenarios and scope are
unchanged. Source activation occurs only on merge of that accepted content;
final-Head delta review and merge receipts are recorded in the PR to avoid
changing the reviewed candidate merely to record its own SHA.
