# M07 — Linux networking and socket programming

**Status:** curriculum specification; not a claim that lessons have been completed.
**Prerequisites:** M04, M05

## Topic scope
- **M07.01** — Socket lifecycle, bind, connect, listen, accept, and close
- **M07.02** — Ports, file descriptors, buffers, and readiness models
- **M07.03** — Host routes, policy routing, source selection, and neighbors
- **M07.04** — Network namespaces, veth pairs, bridges, and virtual interfaces
- **M07.05** — Netfilter/nftables, connection tracking, and host NAT
- **M07.06** — Receive/transmit paths and packet capture location
- **M07.07** — Socket options, keepalives, backlog, and resource limits
- **M07.08** — Permissions, capabilities, and reproducible host labs

## Theory and mechanisms
Connect application behavior to kernel networking without assuming each send is one packet or each receive one message.

## Numericals and algorithmic work
Reason about buffered bytes, in-flight data, file-descriptor budgets, and simple queue bounds with explicit assumptions.

## Practical route
Run a local TCP experiment and isolate virtual interfaces in a disposable Linux VM; inspect before tuning.

## Senior/principal application
Diagnose application, socket, routing, and filtering failures without indiscriminate sysctl changes.

## Evidence to collect
Ask for a mechanism explanation and an unfamiliar application. Add calculations, state traces, experiments, troubleshooting, and a design rationale when applicable. Record what was attempted, assistance, observations, and remaining gaps. Untested dimensions stay unassessed; watching a video or reading a generated note is not mastery.

## Lesson expansion rule
Prepare detailed lessons only as needed. Record stable topic IDs in notes and evidence. Use source dates and version-specific documentation for implementations. A learner may request a useful specialization without completing every unrelated branch.

## Sources to consult
IP-NETNS, IP-NEIGH, LINUX-SCALING, RFC9293 in [the source register](../references/SOURCES.md). These are starting references, not proof that each listed topic is fully covered by a single source. Retrieve topic-specific standards and vendor documentation before advanced teaching.

[Back to curriculum](README.md)
