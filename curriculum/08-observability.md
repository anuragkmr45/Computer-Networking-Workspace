# M08 — Measurement, performance, and troubleshooting

**Status:** curriculum specification; not a claim that lessons have been completed.
**Prerequisites:** M05, M07

## Topic scope
- **M08.01** — Hypothesis-driven troubleshooting and layered tests
- **M08.02** — Packet capture, counters, logs, metrics, and trace correlation
- **M08.03** — Latency distributions, throughput, goodput, and bottlenecks
- **M08.04** — Queues, buffering, Little's-law intuition, and saturation
- **M08.05** — Loss, retransmissions, reordering, and duplicate observations
- **M08.06** — Capture offloads, timestamp limitations, and false conclusions
- **M08.07** — DNS, TCP, TLS, and application timing breakdowns
- **M08.08** — Incident evidence, reproducibility, and verification of a fix

## Theory and mechanisms
Choose observations that can distinguish competing causes; keep symptoms, hypotheses, measurements, and conclusions separate.

## Numericals and algorithmic work
Build BDP/capacity/queueing estimates and check units; state the limits of steady-state models and percentiles.

## Practical route
Collect before/after evidence in an isolated fault exercise. Do not treat a single ping as an application SLO.

## Senior/principal application
Produce a short incident narrative and reject an unsupported root-cause claim.

## Evidence to collect
Ask for a mechanism explanation and an unfamiliar application. Add calculations, state traces, experiments, troubleshooting, and a design rationale when applicable. Record what was attempted, assistance, observations, and remaining gaps. Untested dimensions stay unassessed; watching a video or reading a generated note is not mastery.

## Lesson expansion rule
Prepare detailed lessons only as needed. Record stable topic IDs in notes and evidence. Use source dates and version-specific documentation for implementations. A learner may request a useful specialization without completing every unrelated branch.

## Sources to consult
LINUX-SCALING, UMASS-LABS, RFC9293 in [the source register](../references/SOURCES.md). These are starting references, not proof that each listed topic is fully covered by a single source. Retrieve topic-specific standards and vendor documentation before advanced teaching.

[Back to curriculum](README.md)
