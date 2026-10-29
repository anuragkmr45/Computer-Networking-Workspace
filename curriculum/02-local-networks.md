# M02 — Ethernet, ARP, switching, and local networks

**Status:** curriculum specification; not a claim that lessons have been completed.
**Prerequisites:** M01

## Topic scope
- **M02.01** — Ethernet frames and MAC address scope
- **M02.02** — Source-MAC learning, known unicast, and flooding
- **M02.03** — ARP discovery, caching, and next-hop resolution
- **M02.04** — VLANs, access ports, trunks, and broadcast domains
- **M02.05** — Loops, STP/RSTP, and convergence
- **M02.06** — Link aggregation and first-hop boundaries
- **M02.07** — Wi-Fi association, shared medium, channels, and roaming
- **M02.08** — Local-delivery failures and table-by-table diagnosis

## Theory and mechanisms
Separate the host route table, host neighbor table, and switch MAC table; trace each exchange within one VLAN.

## Numericals and algorithmic work
Trace switch-table state and forwarding ports across frames; calculate simple Ethernet overhead only with explicit wire-format assumptions.

## Practical route
Use the offline ARP walkthrough, then the isolated two-namespace guide in labs/02-isolated-arp.md when authorized.

## Senior/principal application
Explain segmentation trade-offs and why an oversized L2 domain changes blast radius.

## Evidence to collect
Ask for a mechanism explanation and an unfamiliar application. Add calculations, state traces, experiments, troubleshooting, and a design rationale when applicable. Record what was attempted, assistance, observations, and remaining gaps. Untested dimensions stay unassessed; watching a video or reading a generated note is not mastery.

## Lesson expansion rule
Prepare detailed lessons only as needed. Record stable topic IDs in notes and evidence. Use source dates and version-specific documentation for implementations. A learner may request a useful specialization without completing every unrelated branch.

## Sources to consult
RFC826, CISCO-ARP, CISCO-SWITCH, IP-NEIGH in [the source register](../references/SOURCES.md). These are starting references, not proof that each listed topic is fully covered by a single source. Retrieve topic-specific standards and vendor documentation before advanced teaching.

[Back to curriculum](README.md)
