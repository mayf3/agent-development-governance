# Agent entrypoint

Before non-trivial work in this repository:

1. read `.agents/README.md`;
2. read `.agents/local/README.md`;
3. read directly relevant accepted authorities under `docs/specs/`;
4. read `.agents/skills/spec-governance/SKILL.md` and only the selected mode file.

Hard rules:

- classify Authority, Plan, and Assurance independently;
- only active accepted Product Authority creates long-lived obligations;
- a Task, Brief, Investigation, test, runtime fact, or Review comment cannot become Product Authority;
- an Execution Mandate may constrain one operation but cannot change Product Contracts;
- a load-bearing `SPEC_GAP` stops dependent implementation, merge, or operation and returns to PREFLIGHT;
- controlled work needs a valid mandate, runbook, receipt, and independent post-state verification, not automatically a new Spec or platform;
- accepted Decision and Contract meaning is immutable under the same stable ID;
- unrelated `main` movement is not candidate-Head drift;
- when `DONE_WHEN` is satisfied and no `EXPANSION_TRIGGER` fired, stop.

Current enforcement is manual semantic policy plus deterministic integrity and route-consistency checks. Tools do not perform semantic acceptance.
