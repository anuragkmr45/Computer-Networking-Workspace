# ARP: resolve the selected next hop
**Topic:** M02.03 · **Scope:** ordinary IPv4 on Ethernet, one VLAN, no proxy ARP, no conflicting address, and a missing usable mapping.

## What and why
The host has selected a next-hop IPv4 address but needs an Ethernet destination MAC. ARP exchanges messages to learn the mapping; the MAC is not calculated from the IP. An ARP message is carried directly in an Ethernet frame, not inside an IP packet or TCP/UDP. [RFC826](../references/SOURCES.md#rfc826)

## Request and reply
```text
Laptop                      Switch                     Server
192.168.10.20                                           192.168.10.80
MAC-L                                                  MAC-S
  |---- request to FF:FF:FF:FF:FF:FF ---------------------->|
  |     Who has 192.168.10.80? Tell 192.168.10.20.          |
  |     Sender information includes MAC-L.                |
  |<---------------- reply to MAC-L ----------------------|
  |                  192.168.10.80 is at MAC-S.            |
```
The ordinary discovery request is broadcast. The owner can normally reply by unicast because the request identifies the sender's MAC. Ethernet destination and ARP target-hardware fields are separate fields; the broadcast MAC belongs in the Ethernet header. [RFC826](../references/SOURCES.md#rfc826)

## Cache and next use
A usable cache entry can avoid new discovery. For an on-link target, resolve that target; for a gateway-selected route, resolve the gateway's LAN IP. Learned entries require maintenance; there is no universal expiry timer for all operating systems and devices. [Cisco ARP guide](../references/SOURCES.md#cisco-arp)

## Failure and boundaries
Under our simple routing assumptions, failure to resolve an on-link neighbor does not automatically select the default gateway instead. A host may queue packets while resolving and eventually report failure. Exact retry timing and application-visible errors depend on the implementation. Linux exposes neighbor states such as INCOMPLETE, REACHABLE, STALE, and FAILED; STALE does not mean there is no MAC. [Host requirements](../references/SOURCES.md#rfc1122), [Linux neighbor manual](../references/SOURCES.md#ip-neigh)

ARP broadcasts stay within their broadcast domain; matching a subnet mathematically is not proof of L2 reachability. Proxy ARP, gratuitous ARP, conflicts, and IPv6 neighbor discovery are later separate topics. Do not present all address-resolution exchanges as this one ordinary pattern.

## Application
Open [the offline walkthrough](../visuals/arp-next-hop-demo.html). Compare /24 and /16 for the same target. Predict the requested IP before revealing the stages. This is a teaching simulation, not a packet capture.

**Evidence:** E003–E006 are assisted/immediate evidence. No executed ARP lab or delayed recall is yet recorded.
