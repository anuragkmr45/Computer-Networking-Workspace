# M03 — IPv4, IPv6, and address planning

**Status:** curriculum specification; not a claim that lessons have been completed.
**Prerequisites:** M01

## Topic scope
- **M03.01** — IPv4 binary and dotted-decimal representation
- **M03.02** — CIDR, masks, on-link tests, and network addresses
- **M03.03** — Subnet sizing, VLSM, and summarization
- **M03.04** — Special-use addresses, /31, /32, and broadcast caveats
- **M03.05** — DHCP lease lifecycle and configuration delivery
- **M03.06** — IPv6 notation, prefixes, scopes, and address types
- **M03.07** — IPv6 neighbor discovery, router advertisements, and SLAAC
- **M03.08** — NAT/PAT, address conservation, and end-to-end implications

## Theory and mechanisms
Perform addressing decisions from bits rather than classful mnemonics; distinguish IPv4 ARP from IPv6 neighbor discovery.

## Numericals and algorithmic work
Solve /24, /16, and non-octet masks; allocate disjoint variable-sized subnets and state usable-address assumptions.

## Practical route
Use tools/netcalc.py to check hand calculations, not replace them; inspect a disposable DHCP or IPv6 lab later.

## Senior/principal application
Create an on-premises/cloud address plan that anticipates growth and overlapping networks.

## Evidence to collect
Ask for a mechanism explanation and an unfamiliar application. Add calculations, state traces, experiments, troubleshooting, and a design rationale when applicable. Record what was attempted, assistance, observations, and remaining gaps. Untested dimensions stay unassessed; watching a video or reading a generated note is not mastery.

## Lesson expansion rule
Prepare detailed lessons only as needed. Record stable topic IDs in notes and evidence. Use source dates and version-specific documentation for implementations. A learner may request a useful specialization without completing every unrelated branch.

## Sources to consult
PY-IPADDRESS, RFC1122, AWS-VPC in [the source register](../references/SOURCES.md). These are starting references, not proof that each listed topic is fully covered by a single source. Retrieve topic-specific standards and vendor documentation before advanced teaching.

[Back to curriculum](README.md)
