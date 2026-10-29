# M13 — Automation, configuration, and verification

**Status:** curriculum specification; not a claim that lessons have been completed.
**Prerequisites:** M07, M09, M10

## Topic scope
- **M13.01** — Structured state, source of truth, and configuration models
- **M13.02** — APIs, NETCONF/RESTCONF/gNMI concepts, and telemetry
- **M13.03** — Python/TypeScript tooling and parsing reliable outputs
- **M13.04** — Configuration management and infrastructure as code
- **M13.05** — Idempotency, drift, secrets, and least-privilege credentials
- **M13.06** — Unit/integration checks and network intent validation
- **M13.07** — Change pipelines, staged rollout, rollback, and audit
- **M13.08** — Safe use of AI assistance and verification of generated configuration

## Theory and mechanisms
Treat network automation as tested software with observable postconditions and bounded permissions.

## Numericals and algorithmic work
Compute address allocations and validate invariants; calculate rollout/blast-radius scenarios where useful.

## Practical route
Build an offline config validator first; require a dry-run, diff, test environment, and approval before device changes.

## Senior/principal application
Design a change pipeline that catches a bad route/policy before production.

## Evidence to collect
Ask for a mechanism explanation and an unfamiliar application. Add calculations, state traces, experiments, troubleshooting, and a design rationale when applicable. Record what was attempted, assistance, observations, and remaining gaps. Untested dimensions stay unassessed; watching a video or reading a generated note is not mastery.

## Lesson expansion rule
Prepare detailed lessons only as needed. Record stable topic IDs in notes and evidence. Use source dates and version-specific documentation for implementations. A learner may request a useful specialization without completing every unrelated branch.

## Sources to consult
CISCO-CCNP, JUNIPER-TRACKS, PY-IPADDRESS in [the source register](../references/SOURCES.md). These are starting references, not proof that each listed topic is fully covered by a single source. Retrieve topic-specific standards and vendor documentation before advanced teaching.

[Back to curriculum](README.md)
