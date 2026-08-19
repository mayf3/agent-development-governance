# Bootstrap Review Corpus

```text
CORPUS_ID = AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_REVIEW_CORPUS_2026_08_18
STATUS = historical_input
NORMATIVE_AUTHORITY = NO
UNIQUE_SOURCE_ARTIFACTS = 2
OWNER_SUPPLIED_FILES = 4
BYTE_IDENTICAL_DUPLICATES_OMITTED = 2
```

This bounded corpus persists the owner-supplied review material used by
`AGENT_DEVELOPMENT_GOVERNANCE_BOOTSTRAP_V0` Observations `OBS-001`,
`OBS-002`, and `OBS-004`. It is provenance, not governing authority.

The text is preserved as supplied. Review assertions remain assertions by their
review authors; this index does not silently upgrade them into repository facts.

## Source inventory

### REVIEW_A

- Persisted file: [`REVIEW_A.md`](./REVIEW_A.md)
- Original supplied name: `粘贴的 markdown (1)。md(20260818-155544)`
- SHA-256 of supplied bytes: `d1c43411b6ac0a7d94e9c36c3289d7b8555bd351006b2e5ec22751d262b81615`
- Relevant corpus areas:
  - overall `DIRECTION = KEEP` / no framework rewrite;
  - authority precedence and immutable accepted meaning;
  - qualified conformance and State/Observation closure;
  - persistent Issue / Investigation PR for important no-change or rejected outcomes.

### REVIEW_B

- Persisted file: [`REVIEW_B.md`](./REVIEW_B.md)
- Original supplied name: `粘贴的 markdown (2)。md(5)`
- SHA-256 of supplied bytes: `3d2fec55f123f03fbb121916d93e73a5a7df5da358b40a466f0cd2ca3091858f`
- Relevant corpus areas:
  - `ARCHITECTURE_DIRECTION = STRONGLY_ACCEPT`;
  - epistemic/normative primitive families and time-indexed State;
  - separate implementation, verification, and conformance dimensions;
  - explicit recommendation to add `rejected` to the governing lifecycle.

The additional owner-supplied files named `粘贴的 markdown (3)。md` and
`粘贴的 markdown (4)。md` were byte-identical to `REVIEW_B.md`
(SHA-256 `3d2fec55f123f03fbb121916d93e73a5a7df5da358b40a466f0cd2ca3091858f`), so they are recorded here but not duplicated.

## Use boundary

This corpus may support historical Observations about what the reviews said. It
MUST NOT be cited as proof that the governance design is correct, that a future
revision was reviewed, or that an acceptance actor approved any normative text.
