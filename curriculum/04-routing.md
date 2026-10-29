# M04 — Forwarding and routing foundations

**Status:** curriculum specification; not a claim that lessons have been completed.
**Prerequisites:** M02, M03

## Topic scope
- **M04.01** — Connected routes, default routes, and longest-prefix match
- **M04.02** — Next hops, recursive resolution, and forwarding tables
- **M04.03** — Control plane versus data plane
- **M04.04** — ICMP, TTL/hop limit, traceroute, and diagnostic limitations
- **M04.05** — MTU, IPv4 fragmentation, and path-MTU discovery
- **M04.06** — Static routes, route preferences, and equal-cost paths
- **M04.07** — Dijkstra and Bellman-Ford on small topologies
- **M04.08** — Return paths, asymmetric routing, and black holes

## Theory and mechanisms
Predict each hop using the forwarding table, not a vague search for the server; distinguish a route from reachability.

## Numericals and algorithmic work
Trace longest-prefix selection and shortest-path algorithms; solve fragmentation only under stated header/MTU conditions.

## Practical route
Build a disposable multi-router topology later; record forward and return path evidence before changes.

## Senior/principal application
Justify routing boundaries, MTU strategy, and failure diagnosis order.

## Evidence to collect
Ask for a mechanism explanation and an unfamiliar application. Add calculations, state traces, experiments, troubleshooting, and a design rationale when applicable. Record what was attempted, assistance, observations, and remaining gaps. Untested dimensions stay unassessed; watching a video or reading a generated note is not mastery.

## Lesson expansion rule
Prepare detailed lessons only as needed. Record stable topic IDs in notes and evidence. Use source dates and version-specific documentation for implementations. A learner may request a useful specialization without completing every unrelated branch.

## Sources to consult
RFC1812, RFC1122 in [the source register](../references/SOURCES.md). These are starting references, not proof that each listed topic is fully covered by a single source. Retrieve topic-specific standards and vendor documentation before advanced teaching.

[Back to curriculum](README.md)
