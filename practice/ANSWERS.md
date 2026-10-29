# Conceptual answer key

Use only after an attempt or when the learner requests an explanation. Source IDs resolve in [SOURCES](../references/SOURCES.md). Worked address/table values are original derivations.

## Q01
The sender lacks the next-hop MAC, so ordinary discovery addresses all devices in its local broadcast domain. The request carries the sender MAC; the owner can reply directly to it. Source: RFC826.

## Q02
Resolve the selected gateway's local IPv4 address. The outgoing Ethernet destination is the gateway's local MAC; the IP destination remains the remote server in the stated no-NAT scenario. Sources: RFC1122, CISCO-ARP.

## Q03
No new discovery is required while a mapping is usable. Inspect the neighbor table and, in an authorized lab, a trace. Refresh and failure behavior are implementation-dependent. Sources: CISCO-ARP, IP-NEIGH.

## Q04
255.255.0.0 gives 192.168.0.0 for both addresses. The connected route treats the target as on-link, so resolve 192.168.11.80 itself. This does not prove common L2 membership or return-path correctness.

## Q05
/24 yields laptop network 192.168.10.0 and target network 192.168.11.0. Select the default gateway under the stated routes. Ethernet destination changes to gateway MAC; destination IP still identifies the server.

## Q06
Request arriving at port 1 learns L->1 and floods to 2,3. Reply arriving at 2 learns S->2 and forwards to 1. Data arriving at 1 refreshes L->1 and forwards to 2. MAC-X is not learned merely because X received a broadcast; it must transmit a source frame. Source: CISCO-SWITCH.

## Q07
The selected route still says on-link. Neighbor-resolution failure is not an instruction to replace that route with a less-specific default; delivery to the selected next hop fails under this model. Sources: RFC1122, RFC1812.

## Q08
No. The IP calculation does not create link-layer connectivity; the ordinary ARP broadcast cannot reach the other isolated VLAN. A complete diagnosis checks both addressing and L2 topology. Sources: CISCO-ARP, CISCO-SWITCH.

## Q09
ARP cache and switch table are independent. The data frame has a unicast destination MAC already known by the host, but the switch has not learned its port and floods eligible ports in the VLAN. Source: CISCO-SWITCH.

## Q10
The /32 route is more specific than /16 and wins this lookup, assuming it is installed and usable under the stated model. The real route table, not a shortcut alone, decides. Source: RFC1812.

## Q11
No. TCP provides an ordered byte stream; applications must define message framing and handle partial reads. Source: RFC9293.

## Q12
ARP uses fields containing IPv4 addresses, but ordinary Ethernet carries ARP directly: Ethernet->ARP. TCP data follows Ethernet->IP->TCP->bytes. Field values and encapsulation are different concepts. Source: RFC826.
