# M10 — Network security, WANs, and QoS

**Status:** curriculum specification; not a claim that lessons have been completed.
**Prerequisites:** M06, M09

## Topic scope
- **M10.01** — Trust boundaries, segmentation, and least-privilege flows
- **M10.02** — ACLs, stateful firewalls, and policy verification
- **M10.03** — IPsec/IKE concepts, site-to-site VPNs, and remote access
- **M10.04** — Identity, administrative access, AAA, and secure management
- **M10.05** — WAN link choices, SD-WAN, and overlay trade-offs
- **M10.06** — QoS classification, policing, shaping, and scheduling
- **M10.07** — Wireless security and enterprise access controls
- **M10.08** — Defensive monitoring, abuse resilience, and safe change plans

## Theory and mechanisms
Design and verify intended permitted flows without equating a route with authorization or encryption with identity.

## Numericals and algorithmic work
Calculate simple shaping/serialization budgets and policy-order examples; do not invent product defaults.

## Practical route
Use an isolated allow/deny policy exercise with rollback; no unauthorized scanning or interception.

## Senior/principal application
Balance access, performance, recoverability, and operational complexity.

## Evidence to collect
Ask for a mechanism explanation and an unfamiliar application. Add calculations, state traces, experiments, troubleshooting, and a design rationale when applicable. Record what was attempted, assistance, observations, and remaining gaps. Untested dimensions stay unassessed; watching a video or reading a generated note is not mastery.

## Lesson expansion rule
Prepare detailed lessons only as needed. Record stable topic IDs in notes and evidence. Use source dates and version-specific documentation for implementations. A learner may request a useful specialization without completing every unrelated branch.

## Sources to consult
CISCO-CCNP, ISC2-CISSP, PALO-RETIREMENT in [the source register](../references/SOURCES.md). These are starting references, not proof that each listed topic is fully covered by a single source. Retrieve topic-specific standards and vendor documentation before advanced teaching.

[Back to curriculum](README.md)
