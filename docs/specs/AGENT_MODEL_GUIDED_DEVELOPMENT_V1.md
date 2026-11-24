---
spec_id: AGENT_MODEL_GUIDED_DEVELOPMENT_V1
status: proposed
spec_kind: implementation
authority_level: governing_spec
implementation_authority: contracts
scope:
  - agent-development-governance
governed_by:
  - AGENT_DEVELOPMENT_GOVERNANCE_V1
external_authorities: []
supersedes: []
superseded_by: null
owners:
  - mayf3
---

# Model-guided development and reusable formal knowledge

## 1. Goal

Make mathematical modeling and appropriate formal verification a continuing
development practice: discover the governing behavior, build or reuse a model,
challenge its assumptions, and keep implementation and real outcomes aligned.

```text
GOAL = reusable, reviewable models guide important engineering decisions across projects
SUCCESS_OUTCOME = developers actively maintain useful models and strengthen high-value properties with machine-checked evidence, while product delivery and real acceptance remain controlling
```

The practice includes actively constructing and improving models. It does not
require calling every model a primitive, proving that a primitive set is minimal,
or building a universal model of all projects.

## 2. Scope and non-goals

In scope: a proportional modeling assessment for behavior changes; explicit
models for critical mechanisms; reuse and versioned accumulation of shared
knowledge; appropriately scoped formal verification; implementation mappings;
three distinct evidence layers; and a counterexample feedback loop.

Out of scope: changing existing accepted authority; a new Agent platform,
central runtime, state store, theorem registry, universal state machine, approval
ceremony, fourth PREFLIGHT axis, or compulsory Lean project in every consumer.
This authoring change does not modify the distributed grammar, tools, versions,
consumer repositories, deployed systems, or product acceptance criteria.

## 3. Authority and dependencies

```text
AUTHORITY_ACTION = NEW
PRIMARY_PARENT_AUTHORITY = AGENT_DEVELOPMENT_GOVERNANCE_V1
PARENT_REVISION = c1fad8976e50e96adb27a4c7e2dd4f97bf2e899e
RELATED_AUTHORITY = AGENT_MODEL_CONVERGENCE_V1 at the same revision
PLAN_LEVEL = BRIEF
ASSURANCE_LEVEL = CONTROLLED
ROUTE_STAGE = AUTHORITY_AUTHORING
DOCS_FIRST_REQUIRED = YES
ACCEPTANCE_ACTOR = mayf3 or an explicitly authorized maintainer
```

This is a new development obligation under the parent's existing authority,
proportional review, and stop controls. It preserves every accepted Decision and
Contract. Model Convergence continues to govern retirement of duplicate
executable models; this Spec governs how explicit mathematical and formal
models guide development. Neither replaces the other.

Source acceptance, distribution implementation, consumer adoption, model
verification, implementation conformance, and real product acceptance remain
separate facts. Implementation begins in a later `REUSE` change after this Spec
is accepted on the source authority branch. `mayf3/primitives` is the preferred
shared knowledge repository, not external Product Authority or runtime
authorization. A guide or model there cannot silently amend this Spec or a
consumer's accepted product requirements.

## 4. Current State

### STATE-MGD-001 — Governance supplies evidence boundaries without this development obligation

- Subject: `mayf3/agent-development-governance`.
- As of commit: `c1fad8976e50e96adb27a4c7e2dd4f97bf2e899e`.
- Environment / observed at: source repository inspection, 2026-11-25.
- Projection: accepted governance separates authority, observation, evidence,
  implementation, and real conformance; it does not yet require the modeling
  assessment and active model-development practice defined here.
- Basis: `OBS-MGD-001`.

## 5. Observations

### OBS-MGD-001 — Existing governance preserves local authority and bounded delivery

- Source revision: `c1fad8976e50e96adb27a4c7e2dd4f97bf2e899e`.
- Environment / observed at: source repository, 2026-11-25.
- Method: read `AGENTS.md`, `.agents/README.md`, `.agents/local/README.md`,
  accepted Governance V1, Model Convergence V1, and the Spec format.
- Result: the source distributes methods; consumers own product meaning;
  deterministic checks do not provide semantic acceptance; applicable blockers
  and `DONE_WHEN` bound delivery.
- Provenance: the named files at the stated revision.

### OBS-MGD-002 — The owner requests a continuing development principle

- Source: owner instruction in the 2026-11-25 conversation, retained in
  [the current delivery record](../changes/MODEL_GUIDED_DEVELOPMENT.md).
- Method: distinguish the requested development practice from a request to
  invent a new class of mathematical primitives or a new platform.
- Result: the requested outcome is proactive model construction, reuse,
  mathematical/formal reasoning, and implementation alignment across projects;
  the owner authorizes the bounded PR and merge work.
- Limitation: this request establishes intended direction, not evidence that
  any product is already modeled, proven, or accepted.

## 6. Claims and assumptions

### CLM-MGD-001 — Reusable, challenged models can reduce repeated reasoning errors

- Support state: INFERRED.
- Supported by evidence: `EVD-MGD-001`.
- Contradicted by evidence: none established in this authoring task.
- Uncertainty: benefit depends on model adequacy, implementation alignment,
  and actual use; this Spec establishes no measured reliability improvement.

## 7. Evidence relations

### EVD-MGD-001 — The requested practice fits the existing bounded governance method

- Source observations: `OBS-MGD-001`, `OBS-MGD-002`.
- Target / relation: `CLM-MGD-001` / SUPPORTS.
- Bound coordinates: the source revision and owner instruction stated above.
- Sufficiency: supports a bounded development rule with explicit assumptions
  and independent model, implementation, and reality checks.
- Limitations: does not verify a mathematical theorem, consumer implementation,
  or real outcome, and does not demonstrate a quantitative benefit.
- Provenance: the named source files and current delivery record.

## 8. Decisions

### DEC-MGD-001 — Assess changes and actively model critical mechanisms

- Decision owner: repository owner.
- Decision: assess modeling on behavior changes; maintain an explicit, minimal
  reviewable model for critical mechanisms and progressively machine-check
  stable properties whose value justifies the effort.
- Rejected alternative: models are optional essays after coding, or every
  small change waits for a complete Lean proof.
- Reason: effort should track semantic complexity and consequences of failure.

### DEC-MGD-002 — Reuse knowledge through existing repositories

- Decision owner: repository owner.
- Decision: use `primitives` for reusable methods, models, proofs, and
  counterexamples; keep project-specific requirements, mappings, code, and real
  evidence with their owning project; governance owns the development rule.
- Rejected alternative: a new universal runtime or competing copies of the
  same mathematical definition in every governance and product repository.
- Reason: shared understanding and local product responsibility can coexist.

### DEC-MGD-003 — Preserve three evidence layers and challenge assumptions

- Decision owner: repository owner.
- Decision: evaluate the model, its implementation mapping, and the real
  outcome separately; challenge assumptions and retain unproved boundaries.
- Rejected alternative: a theorem, structural validator, or component PASS
  certifies the deployed product by itself.
- Reason: conditional model results do not establish their real-world premises.

### DEC-MGD-004 — Feed counterexamples back without rewriting the goal

- Decision owner: repository owner.
- Decision: connect a real failure to the original task, model assumptions,
  implementation mapping, and affected reusable knowledge; close the original
  acceptance after repair.
- Rejected alternative: weaken the property or silently change the model until
  a proof passes while the original user outcome remains broken.
- Reason: models serve the desired behavior and must remain open to correction.

### DEC-MGD-005 — Integrate the practice into bounded existing delivery

- Decision owner: repository owner.
- Decision: distribute concise guidance through existing Agent entrypoints and
  records, preserve proportional checks, and stop at the original Done When.
- Rejected alternative: a separate governance program or unlimited formalization
  backlog that blocks unrelated repairs.
- Reason: the practice should improve delivery and accumulate useful knowledge.

## 9. Contracts

### CTR-MGD-001 — Assess modeling on every behavior change

For a change to observable system behavior, the developer MUST assess whether
the affected behavior has an adequate model and whether it changes assumptions,
states, transitions, invariants, or verification obligations. The assessment
MUST consider failure consequence and state/interaction complexity, not just
diff size. It MAY be one sentence in the existing task, Brief, or PR.

A task with unchanged behavior MAY reuse the existing model without a new
model artifact after checking that its relevant assumptions and mapping remain
valid. Purely editorial or cosmetic work MUST NOT acquire an empty modeling
form, mandatory theorem, or new approval solely because this Spec exists.

### CTR-MGD-002 — Give critical behavior a reviewable model

When changing a mechanism governing identity or version attribution, durable
state, permissions or authority, concurrency or ownership, retry/cancellation
and external effects, recovery or handoff, or evidence, completion claims, and
state projections that determine further action, the developer MUST construct, reuse, or
repair an explicit model before implementation relies on the changed behavior.
The model MAY be compact and live in existing design or change records; this
does not automatically require a new governing Spec or separate modeling PR.

The model MUST identify the relevant entities and identities, state space,
initial/reachable conditions, permitted transitions, safety properties,
environment assumptions, and intended observations. It MUST describe relevant
failure/interleaving cases and liveness obligations when eventual progress is
claimed. Time, atomicity, persistence, scheduler fairness, and external-service
behavior MUST be explicit when a claimed guarantee depends on them. Inapplicable
dimensions need no invented machinery.

### CTR-MGD-003 — Reuse first and accumulate useful shared models

Developers MUST inspect applicable existing project models and reusable
knowledge in the selected `mayf3/primitives` revision before independently
redefining the same mechanism. They MUST record the reused model/property and
exact revision, its applicability, and any assumption or semantic mismatch.
Having the same name is insufficient evidence of equivalence.

When no adequate model exists, developers MUST build the minimum local model
needed for the task. Reusable findings and counterexamples MUST be proposed
back to the owning shared model through a linked change or follow-up with an
owner; completing that upstream change is not automatically a product gate.
Local product details and sensitive evidence stay in their owning project.
An unavailable shared repository MUST be recorded as unavailable, not as
empty; it does not forbid an adequate local model, but prevents claiming that
unread models or proofs were reused or that their prerequisites were verified.

### CTR-MGD-004 — Actively strengthen high-value properties with suitable formal methods

For a new or materially changed critical model, the developer MUST identify
stable properties whose failure matters and choose a bounded verification
approach. High-value stable properties MUST be prioritized for machine-checked
proof or model checking when feasible. The existing record MUST identify the
chosen property, method, scope, result, and limitations; if machine verification
is deferred, it MUST retain the reason, remaining assurance gap, current
controls, responsible owner, and an explicit completion or reassessment trigger
in the existing record or a linked bounded follow-up. An unowned "prove later"
statement is insufficient.

The method MAY use Lean, another proof assistant, a model checker, or an
appropriate executable/reference model. These are not interchangeable evidence:
bounded search, sampled simulation, property tests, and deductive proofs MUST
retain their actual scope. No particular tool, theorem count, or model size is
mandatory. An explicit accepted proof requirement remains binding; deferral
MUST NOT silently waive it.

### CTR-MGD-005 — Challenge the model and report proof boundaries

Before relying on a model result, the developer and reviewer MUST challenge
initial-state reachability, assumptions, omitted transitions, and relevant
failure traces. When a normal successful outcome is claimed, they MUST retain
an admissible execution reaching that outcome; an empty or inconsistent model
does not establish useful success. They MUST NOT assume the target guarantee as a premise and
report the resulting theorem as its independent establishment. Conditional
theorems remain useful when their premises are disclosed and separately
justified for each application.

A machine-proof claim MUST name the model/property revision, checked theorem
or property, tool/toolchain, relevant axioms or trusted assumptions, and
unproved or excluded obligations. A theorem containing an unfinished proof
or an assumed desired result MUST NOT be reported as fully established.
Relevant reachable counterexamples, boundary cases, and examples that a wrong
model would accept MUST inform the chosen checks; a mere compile or structural
validation result MUST NOT be labeled product correctness.

### CTR-MGD-006 — Bind the implementation to the model

The owning project MUST identify how the relevant concrete states, events,
operations, and observations map to the selected model and its version. It MUST
account for real transaction boundaries, persistent identities, failure/restart
behavior, and external-effect boundaries where these affect the property.
A formal refinement proof, when supplied, MUST state its scope. Tests, trace
comparisons, and runtime checks MAY support the mapping but MUST NOT be labeled
a complete refinement proof unless they establish one.

Changing a dependent model or implementation invalidates affected claims until
impact is assessed. Unaffected evidence MAY be rebound using the parent's
bounded impact rules; no automatic full cross-project re-verification is required.

### CTR-MGD-007 — Keep model, implementation, and real acceptance distinct

Any material assurance claim MUST distinguish: (1) what is established inside
the model and under which assumptions; (2) what shows the implementation follows
that model; and (3) what verifies the original required outcome in the relevant
environment. Missing, deferred, conditional, and unexecuted evidence MUST remain
visible in the existing record. A model proof alone MUST NOT promote a task to
deployed, business-complete, or user-accepted.

These are evidence layers, not a mandatory three-stage approval workflow. The
project's existing acceptance defines which real evidence is required. Subjective
qualities such as clarity or usefulness require their applicable real evaluation;
a structural model MUST NOT manufacture such evaluation or invent a new product gate.

### CTR-MGD-008 — Route counterexamples back to the original outcome

For an observed failure relevant to a modeled guarantee, the responsible
developer MUST preserve a reproducible or bounded failure description, original
task and outcome, model/implementation revisions, violated property or assumption,
and affected scope in the existing issue/change workflow. Investigation MUST
distinguish a wrong requirement/model, an unmet assumption, an implementation
mapping defect, and insufficient real evidence; it MAY leave the cause unknown
until evidence resolves it.

Repair MUST update the responsible model, proof, mapping, or implementation,
notify or link affected consumers through existing repository workflows, and
re-run the original applicable acceptance. Changing an accepted product
requirement still needs its normal authority route. A model-only repair MUST
NOT close the original product issue while its required outcome remains unverified.

### CTR-MGD-009 — Keep formalization bounded by the actual delivery

Modeling and verification MUST use the existing Goal, affected scope, Evidence
Needed, Done When, and Expansion Trigger. A missing required model or proof, a
concrete contradiction, or an unjustified load-bearing assumption blocks only
the dependent work through the parent's existing blocker/gap rules. Optional
generality, missing unrelated proofs, a preferred tool, or an unbounded shared
library redesign MUST NOT become a new blocker.

An already-authorized repair or containment path MAY proceed when it satisfies
its applicable contracts without the disputed assumption. Such a path MUST NOT
claim the unestablished guarantee, weaken required acceptance, or broaden its
authorization. No automatic bypass of permissions, safety obligations, or an
accepted proof gate is created. Formalization follow-up does not reopen a
completed task without its existing expansion trigger or a new authorized task.

### CTR-MGD-010 — Distribute the practice without a second authority system

After source acceptance, the distribution MUST make this practice discoverable
from the existing `.agents/README.md` and usable in existing change, review,
and conformance records. The distributed rule MUST be self-contained; a link
to a source-only Spec or an unavailable shared guide is insufficient. Optional
reference guides MAY provide detail at exact revisions without becoming a
runtime dependency or automatically changing consumer authority.

The implementation MUST preserve accepted Spec bytes, proportional routing,
closed blocker classes, local consumer authority, and distribution integrity.
It MUST update the working version and manifest and independently review the
affected guidance. No new schema, scoring service, mandatory Agent formation,
or consumer migration is required. Source acceptance, distribution publication,
and local adoption MUST be reported separately; existing consumer pins stay intact.

## 10. Acceptance

The following are review scenarios and later distribution conformance checks.
Their presence is not a claim that they have been executed or that any consumer
product is verified. Required evidence is an executed scenario decision bound
to the reviewed source/distribution revision; model and product claims require
their own artifacts and environments.

| Acceptance | Contracts | Method and environment | Expected result and failure condition |
|---|---|---|---|
| `ACC-MGD-001` | `CTR-MGD-001`, `CTR-MGD-009` | Source/distribution review: spelling-only edit, unchanged-behavior refactor, and a two-line retry change | Editorial work stays short; refactor checks its affected mapping; retry semantics trigger modeling despite small diff. Blanket Lean gates or skipping a critical change fail. |
| `ACC-MGD-002` | `CTR-MGD-002`, `CTR-MGD-006` | Review a modeled persistent handoff with crash after external effect but before receipt | Model identifies identity, persistence, uncertain outcome and retry interleavings; implementation mapping exposes the real atomicity boundary. Treating the effect and receipt as one unjustified atomic step fails. |
| `ACC-MGD-003` | `CTR-MGD-003`, `CTR-MGD-010` | Review two projects sharing an idempotency model, including unavailable upstream and incompatible assumptions | Exact references and mismatch are visible; bounded local work is possible; useful findings receive a linked shared follow-up. Silent copying, floating adoption, or claiming unread proof reuse fails. |
| `ACC-MGD-004` | `CTR-MGD-004`, `CTR-MGD-005` | Review a stable ownership invariant, a bounded state exploration, and a proof with an unproved premise | The high-value property has a bounded verification choice; assumptions, unfinished obligations, and search bounds remain explicit. Assuming single ownership to claim it independently proven, or calling bounded exploration a general theorem, fails. |
| `ACC-MGD-005` | `CTR-MGD-006`, `CTR-MGD-007` | Review a passing abstract model with no implementation mapping and a finished render with no required human review | Model evidence does not establish implementation or original acceptance; each missing layer stays visible. All-green or complete claims derived from the abstract proof alone fail. |
| `ACC-MGD-006` | `CTR-MGD-008`, `CTR-MGD-009` | Review a real duplicate-effect counterexample against an earlier successful proof | Preserve and classify the original failure, fix the responsible layer, assess affected consumers, and repeat original acceptance. Weakening the goal or closing on proof repair alone fails. |
| `ACC-MGD-007` | `CTR-MGD-004`, `CTR-MGD-009` | Review an authorized bounded repair with an optional generalization backlog and a separate task whose accepted contract requires proof | Optional backlog does not block the bounded repair; the explicit proof gate still blocks its dependent task. Unlimited formalization or a blanket proof deferral fails. |
| `ACC-MGD-008` | `CTR-MGD-010` | Later distribution check: manifest, existing tool suite, clean exact-commit vendor round trip, and independent review | Entrypoint and existing records carry the rule without missing source-only dependencies; consumers remain unchanged until local adoption. A stale manifest, silently changed accepted authority, or a new mandatory platform fails. |

Every `CTR-MGD-*` is covered above. The acceptance review checks both model
underuse and excessive formalization. It does not add a general semantic verifier
or replace the parent's independent exact-revision review.

## 11. Alternatives and disposition

- Put all mathematics into governance: rejected; governance owns development
  obligations, while reusable model content and project instantiations have
  distinct owners.
- Create a new mathematical-primitive taxonomy first: rejected; useful models
  and properties may be constructed and reused without that prerequisite.
- Require a full proof for every change: rejected; it ignores risk, context,
  real acceptance, and the cost of delaying a bounded repair.
- Treat formal models as optional documentation with no development hook:
  rejected; it would not establish the requested continuing practice.
- Treat a compiled proof as product certification: rejected; it omits model
  adequacy, implementation alignment, and real outcome evidence.

## 12. Migration, compatibility, and rollback

```text
AUTHORING = docs-only; existing accepted authorities remain byte-identical
ACTIVATION = independent exact-candidate review, authorized acceptance, then merge
DISTRIBUTION = later REUSE change; version/manifest update and bounded scenario review
CONSUMER_ADOPTION = exact immutable revision with existing local acceptance
APPLICABILITY = next affected behavior change; no bulk historical retrofit
SHARED_KNOWLEDGE = reuse existing primitives and project structures; no new runtime
ROLLBACK = consumer-local whole-update revert subject to existing authority
PRODUCTION_OPERATION = not authorized by this Spec
```

## 13. Open questions

```text
OPEN_OWNER_DECISIONS = NONE
NORMATIVE_TBD = NONE
UNRESOLVED_AUTHORITY_CONFLICT = NONE
PARTIAL_SUPERSESSION = NONE
AUTHORING_READY_FOR_REVIEW = YES
READY_TO_MARK_ACCEPTED = NO; independent exact-candidate review pending
DISTRIBUTION_IMPLEMENTED = NO
CONSUMERS_CHANGED = NO
```
