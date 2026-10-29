# M15 — Host hardware, high-performance, and AI networking

**Status:** curriculum specification; not a claim that lessons have been completed.
**Prerequisites:** M07, M08, M14

## Topic scope
- **M15.01** — NIC queues, DMA, interrupts, NAPI, and CPU locality
- **M15.02** — RSS/RPS/RFS/XPS and scaling measurements
- **M15.03** — Checksum/segmentation offloads and capture interpretation
- **M15.04** — eBPF/XDP concepts, observability, and safe deployment
- **M15.05** — Kernel bypass, zero-copy claims, and application trade-offs
- **M15.06** — RDMA/RoCE/InfiniBand concepts and congestion requirements
- **M15.07** — AI/HPC communication patterns and collective operations
- **M15.08** — Benchmark validity, tail latency, fairness, and tuning rollback

## Theory and mechanisms
Explain possible bottlenecks from application to CPU, NIC, and fabric; measure before prescribing a technology.

## Numericals and algorithmic work
Estimate message-transfer lower bounds and communication/compute balance; distinguish model estimates from measured performance.

## Practical route
Begin with read-only measurements. Hardware-specific experiments need compatible equipment and an approved isolated environment.

## Senior/principal application
Defend a network design for distributed compute with clear workload and failure assumptions.

## Evidence to collect
Ask for a mechanism explanation and an unfamiliar application. Add calculations, state traces, experiments, troubleshooting, and a design rationale when applicable. Record what was attempted, assistance, observations, and remaining gaps. Untested dimensions stay unassessed; watching a video or reading a generated note is not mastery.

## Lesson expansion rule
Prepare detailed lessons only as needed. Record stable topic IDs in notes and evidence. Use source dates and version-specific documentation for implementations. A learner may request a useful specialization without completing every unrelated branch.

## Sources to consult
LINUX-SCALING, AWS-VPC in [the source register](../references/SOURCES.md). These are starting references, not proof that each listed topic is fully covered by a single source. Retrieve topic-specific standards and vendor documentation before advanced teaching.

[Back to curriculum](README.md)
