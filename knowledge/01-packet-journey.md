# Packet journey: different decisions at different layers
**Topics:** M01.03, M04.01 · **Scope:** ordinary TCP/IPv4 over Ethernet; no NAT, tunnels, proxies, or special routes in this example.

## Reconstruct the idea
The application supplies bytes. TCP carries a reliable byte stream and uses ports to distinguish endpoints. An application write is not guaranteed to become exactly one segment, and a receive call is not a message boundary. [RFC9293](../references/SOURCES.md#rfc9293)

```text
Ethernet frame
└── IPv4 packet
    └── TCP segment
        └── application bytes
```

A route lookup selects an outgoing path/next hop. Ethernet delivery then needs the next hop's MAC. At a router, the incoming link frame ends; the packet is forwarded in another suitable link frame. In an ordinary no-NAT example, the remote destination IP remains the destination; IPv4 TTL is decremented, so not every IP-header field stays unchanged. [RFC1812](../references/SOURCES.md#rfc1812)

## Original worked example
Laptop `192.168.10.20/24`; gateway `192.168.10.1`; target `192.168.11.80`. Assume only a connected route and a default route.

| Outgoing field | Value/owner |
|---|---|
| Source IP | 192.168.10.20 |
| Destination IP | 192.168.11.80 |
| Source MAC | Laptop's outgoing Ethernet interface |
| Destination MAC | Gateway's interface on the laptop's LAN |

The packet is for the server; this first frame is for the gateway. A different link may use a different link-layer format, and NAT or tunnels require a separately drawn example.

## Keep three lookups separate
| Lookup | Purpose |
|---|---|
| Route table | Choose destination-prefix match, outgoing interface, and next hop |
| ARP/neighbor table | Resolve the selected local next-hop IPv4 address to a MAC |
| Switch MAC table | Select a port in the relevant VLAN for a frame |

These conceptual roles are supported by [RFC1122](../references/SOURCES.md#rfc1122), [RFC826](../references/SOURCES.md#rfc826), and [Cisco switching](../references/SOURCES.md#cisco-switch).

**Recall anchor:** final IP destination and next-link MAC destination answer different questions.

**Evidence:** E001 and E002 show overview/guided understanding, not complete independent reconstruction. Next connection: [switching](04-switching.md).
