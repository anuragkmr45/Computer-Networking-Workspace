# M06 — DNS, HTTP, TLS, and application paths

**Status:** curriculum specification; not a claim that lessons have been completed.
**Prerequisites:** M05

## Topic scope
- **M06.01** — DNS hierarchy, resolution, caching, and negative answers
- **M06.02** — DNS records, delegation, split DNS, and failure modes
- **M06.03** — HTTP/1.1 framing, persistence, proxies, and connection reuse
- **M06.04** — HTTP/2 streams, multiplexing, compression, and head-of-line effects
- **M06.05** — HTTP/3 and QUIC mapping
- **M06.06** — TLS certificates, trust, handshake, and forward secrecy
- **M06.07** — L4/L7 load balancing, reverse proxies, CDNs, and health checks
- **M06.08** — Supporting services: time, email, file transfer, and service discovery
- **M06.09** — Application timeouts, retries, idempotency, and connection pools

## Theory and mechanisms
Explain a request from naming through transport and application response, stating where encryption and termination occur.

## Numericals and algorithmic work
Construct latency budgets for explicitly specified cold/warm connections; analyze connection-pool and retry load examples.

## Practical route
Observe a local client/server and inspect authorized sample DNS/TLS/HTTP traces; never imply encrypted content is visible without keys.

## Senior/principal application
Choose health checks, retry budgets, cache boundaries, and timeout ownership.

## Evidence to collect
Ask for a mechanism explanation and an unfamiliar application. Add calculations, state traces, experiments, troubleshooting, and a design rationale when applicable. Record what was attempted, assistance, observations, and remaining gaps. Untested dimensions stay unassessed; watching a video or reading a generated note is not mastery.

## Lesson expansion rule
Prepare detailed lessons only as needed. Record stable topic IDs in notes and evidence. Use source dates and version-specific documentation for implementations. A learner may request a useful specialization without completing every unrelated branch.

## Sources to consult
CHAI-INDEX, UMASS-LABS, RFC9293 in [the source register](../references/SOURCES.md). These are starting references, not proof that each listed topic is fully covered by a single source. Retrieve topic-specific standards and vendor documentation before advanced teaching.

[Back to curriculum](README.md)
