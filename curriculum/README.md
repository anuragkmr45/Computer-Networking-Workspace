# Curriculum — foundations to principal-level networking

This is the v1 scope designed for your stated goals. It combines networking fundamentals with software, Linux, AWS, on-premises, container, operational, and architectural perspectives. It is an expansion beyond the playlist, not a summary of unseen videos or the unreadable attachment.

## Sequence
Start with M01–M04, weaving a brief address/mask preview into local delivery. Continue through transport, applications, and Linux. Measurement starts early and deepens in M08. Enterprise, security, cloud, containers, automation, and architecture then branch according to prerequisites. M14–M15 are advanced depth tracks, not barriers to useful AWS/Kubernetes competence.

| ID | Module | Prerequisites |
|---|---|---|
| M01 | [Networking mental models](01-foundations.md) | None |
| M02 | [Ethernet, ARP, switching, and local networks](02-local-networks.md) | M01 |
| M03 | [IPv4, IPv6, and address planning](03-addressing.md) | M01 |
| M04 | [Forwarding and routing foundations](04-routing.md) | M02, M03 |
| M05 | [Reliability, transport, and congestion](05-transport.md) | M04 |
| M06 | [DNS, HTTP, TLS, and application paths](06-application-protocols.md) | M05 |
| M07 | [Linux networking and socket programming](07-linux-host.md) | M04, M05 |
| M08 | [Measurement, performance, and troubleshooting](08-observability.md) | M05, M07 |
| M09 | [Enterprise routing and resilience](09-enterprise-routing.md) | M04, M08 |
| M10 | [Network security, WANs, and QoS](10-security-wan.md) | M06, M09 |
| M11 | [AWS, hybrid, and multi-cloud networking](11-aws-hybrid.md) | M08, M09, M10 |
| M12 | [Docker and Kubernetes networking](12-containers.md) | M06, M07, M10 |
| M13 | [Automation, configuration, and verification](13-automation.md) | M07, M09, M10 |
| M14 | [Data-center fabrics and storage connectivity](14-data-center.md) | M09, M12, M13 |
| M15 | [Host hardware, high-performance, and AI networking](15-high-performance.md) | M07, M08, M14 |
| M16 | [Principal-level design and operational leadership](16-principal-design.md) | M08, M11, M12, M13 |

## Depth and completion
For each topic separate **Explain / Calculate / Trace / Implement / Debug / Design / Delayed recall**. Some dimensions are inapplicable; do not manufacture exercises merely to fill a table. A written lesson is content coverage; demonstrated independent work is competence evidence. A topic can be revisited at greater depth without repeating the whole module.

## Starting bridge
Your next cohesive unit is M02.02 (switch learning and forwarding), linked to M02.03 (ARP), M03.02 (mask reasoning), and M04.01 (route choice). This focused bridge does not imply that all preceding module content is mastered.

## Optional specialization backlog
Service-provider routing (IS-IS, MPLS, segment routing, traffic engineering); deeper wireless/RF; optical transport; specialized firewall platforms; advanced storage; cloud-provider branches; programmable data planes. Quantum networking is a separately scoped later research track if your actual role requires it—not a prerequisite for ordinary IP/Ethernet networking.

Add a branch only after recording the need, prerequisites, practical environment, sources, and desired evidence. Keep the main recall path navigable.

## Certification use
See [CERTIFICATIONS](../references/CERTIFICATIONS.md). Domain-level overlaps are provided, while objective-level auditing remains pending. No salary, promotion, exam-pass, or universal certification-completeness guarantee is made.
