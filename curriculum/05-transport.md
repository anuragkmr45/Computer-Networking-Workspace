# M05 — Reliability, transport, and congestion

**Status:** curriculum specification; not a claim that lessons have been completed.
**Prerequisites:** M04

## Topic scope
- **M05.01** — Error detection, checksums, and CRC intuition
- **M05.02** — Stop-and-Wait, Go-Back-N, and Selective Repeat models
- **M05.03** — UDP datagrams and application responsibilities
- **M05.04** — TCP byte streams, segmentation, and multiplexing
- **M05.05** — TCP handshake, teardown, and state machine
- **M05.06** — Sequence numbers, ACKs, loss, and reordering
- **M05.07** — Flow control, windows, and bandwidth-delay product
- **M05.08** — Congestion control, fairness, ECN, and buffering
- **M05.09** — Retransmission timing and recovery mechanisms
- **M05.10** — QUIC fundamentals and transport evolution

## Theory and mechanisms
Trace sender/receiver state and distinguish flow control, congestion control, reliability, and application success.

## Numericals and algorithmic work
Compute sequence/ACK evolution, BDP, simplified window-limited rates, ARQ utilization, and educational CRC remainders.

## Practical route
Start with labs/03-loopback-tcp.md; later use authorized traces and isolated impairment experiments.

## Senior/principal application
Explain protocol and timeout choices for a latency-sensitive API versus a bulk transfer.

## Evidence to collect
Ask for a mechanism explanation and an unfamiliar application. Add calculations, state traces, experiments, troubleshooting, and a design rationale when applicable. Record what was attempted, assistance, observations, and remaining gaps. Untested dimensions stay unassessed; watching a video or reading a generated note is not mastery.

## Lesson expansion rule
Prepare detailed lessons only as needed. Record stable topic IDs in notes and evidence. Use source dates and version-specific documentation for implementations. A learner may request a useful specialization without completing every unrelated branch.

## Sources to consult
RFC9293, CS144, UMASS-LABS in [the source register](../references/SOURCES.md). These are starting references, not proof that each listed topic is fully covered by a single source. Retrieve topic-specific standards and vendor documentation before advanced teaching.

[Back to curriculum](README.md)
