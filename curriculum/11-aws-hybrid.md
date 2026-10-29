# M11 — AWS, hybrid, and multi-cloud networking

**Status:** curriculum specification; not a claim that lessons have been completed.
**Prerequisites:** M08, M09, M10

## Topic scope
- **M11.01** — VPCs, subnets, routing, address planning, and availability zones
- **M11.02** — Security groups, network ACLs, and end-to-end path reasoning
- **M11.03** — Internet/NAT gateways, private access, and VPC endpoints
- **M11.04** — Route 53, hybrid DNS, and resolution boundaries
- **M11.05** — Load balancers, global delivery, and application connectivity
- **M11.06** — Peering, Transit Gateway, VPN, and Direct Connect concepts
- **M11.07** — Multi-account/multi-region isolation, observability, and costs
- **M11.08** — IPv6, migration, IaC validation, and disaster recovery
- **M11.09** — Azure comparison branch: VNet, hybrid links, private access, delivery, security

## Theory and mechanisms
Trace AWS/on-premises communication from both directions and separate provider-specific semantics from physical Ethernet models.

## Numericals and algorithmic work
Allocate addresses under documented provider reservations; estimate transfer/capacity costs only with dated prices and explicit inputs.

## Practical route
Begin with the design-only brief in labs/04-platform-lab-backlog.md. Paid deployment requires budget, approval, and teardown.

## Senior/principal application
Defend a hybrid architecture against overlap, DNS failure, AZ/link loss, policy mistakes, and cost surprises.

## Evidence to collect
Ask for a mechanism explanation and an unfamiliar application. Add calculations, state traces, experiments, troubleshooting, and a design rationale when applicable. Record what was attempted, assistance, observations, and remaining gaps. Untested dimensions stay unassessed; watching a video or reading a generated note is not mastery.

## Lesson expansion rule
Prepare detailed lessons only as needed. Record stable topic IDs in notes and evidence. Use source dates and version-specific documentation for implementations. A learner may request a useful specialization without completing every unrelated branch.

## Sources to consult
AWS-VPC, AWS-ANS, AZURE-NETWORK in [the source register](../references/SOURCES.md). These are starting references, not proof that each listed topic is fully covered by a single source. Retrieve topic-specific standards and vendor documentation before advanced teaching.

[Back to curriculum](README.md)
