# M01 — Networking mental models

**Status:** curriculum specification; not a claim that lessons have been completed.
**Prerequisites:** None; start here.

## Topic scope
- **M01.01** — Hosts, interfaces, links, and protocols
- **M01.02** — Bits, bytes, rates, and units
- **M01.03** — Encapsulation and protocol data units
- **M01.04** — Addresses, ports, paths, and delivery scope
- **M01.05** — Copper, fiber, radio, duplex, and link negotiation
- **M01.06** — Topologies, failure domains, and network components
- **M01.07** — Latency, throughput, goodput, jitter, and loss
- **M01.08** — Packet switching versus circuit switching

## Theory and mechanisms
Build a coherent path from application bytes to a receiving application; distinguish a model from an implementation.

## Numericals and algorithmic work
Calculate serialization and propagation delay; compare a packet, link, and end-to-end measurement.

## Practical route
Observe interface, route, and neighbor information without changing the host; begin with labs/01-read-only-linux.md.

## Senior/principal application
Explain why a fast link does not guarantee a fast application and identify what to measure first.

## Evidence to collect
Ask for a mechanism explanation and an unfamiliar application. Add calculations, state traces, experiments, troubleshooting, and a design rationale when applicable. Record what was attempted, assistance, observations, and remaining gaps. Untested dimensions stay unassessed; watching a video or reading a generated note is not mastery.

## Lesson expansion rule
Prepare detailed lessons only as needed. Record stable topic IDs in notes and evidence. Use source dates and version-specific documentation for implementations. A learner may request a useful specialization without completing every unrelated branch.

## Sources to consult
RFC1122, RFC9293 in [the source register](../references/SOURCES.md). These are starting references, not proof that each listed topic is fully covered by a single source. Retrieve topic-specific standards and vendor documentation before advanced teaching.

[Back to curriculum](README.md)
