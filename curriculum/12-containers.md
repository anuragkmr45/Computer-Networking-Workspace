# M12 — Docker and Kubernetes networking

**Status:** curriculum specification; not a claim that lessons have been completed.
**Prerequisites:** M06, M07, M10

## Topic scope
- **M12.01** — Container network isolation and runtime bridge behavior
- **M12.02** — Pod networking, CNI responsibility, and IP address management
- **M12.03** — Services, endpoints, kube-proxy alternatives, and load balancing
- **M12.04** — Cluster DNS, ingress, and Gateway API
- **M12.05** — NetworkPolicy and implementation-dependent enforcement
- **M12.06** — Overlays, routing, MTU, egress, and NAT
- **M12.07** — Service mesh trade-offs and mTLS boundaries
- **M12.08** — Cross-node debugging, observability, and upgrade implications

## Theory and mechanisms
Trace a request using the actual cluster/network implementation rather than assuming every cluster has the same packet path.

## Numericals and algorithmic work
Reason about encapsulation overhead, MTU, address consumption, and connection budgets with verified platform assumptions.

## Practical route
Use a disposable local cluster only after version/CNI checks; see the platform lab backlog.

## Senior/principal application
Compare network implementations and explain the security/performance/operability consequences.

## Evidence to collect
Ask for a mechanism explanation and an unfamiliar application. Add calculations, state traces, experiments, troubleshooting, and a design rationale when applicable. Record what was attempted, assistance, observations, and remaining gaps. Untested dimensions stay unassessed; watching a video or reading a generated note is not mastery.

## Lesson expansion rule
Prepare detailed lessons only as needed. Record stable topic IDs in notes and evidence. Use source dates and version-specific documentation for implementations. A learner may request a useful specialization without completing every unrelated branch.

## Sources to consult
K8S-NETWORK, IP-NETNS in [the source register](../references/SOURCES.md). These are starting references, not proof that each listed topic is fully covered by a single source. Retrieve topic-specific standards and vendor documentation before advanced teaching.

[Back to curriculum](README.md)
