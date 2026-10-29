# Local delivery — fast recall

**One chain:** choose the next hop -> resolve its local MAC if needed -> send the frame -> switch forwards by destination MAC.

| Mechanism | Lookup/decision |
|---|---|
| Host route lookup | Destination IP prefix -> interface/next hop |
| ARP | Selected next-hop IPv4 -> local MAC |
| Switch learning | Source MAC + VLAN -> incoming port |
| Switch forwarding | Destination MAC + VLAN -> outgoing port(s) |

`/24 = 255.255.255.0`; `/16 = 255.255.0.0`. AND gives the network address, not the mask. Under our connected/default-route assumptions, local target -> target MAC; remote target -> gateway MAC. The remote target remains the IP destination without NAT.

Missing mapping: ordinary request is broadcast, reply normally unicast, cache avoids needless repeats. ARP does not carry application data. Failure does not automatically override the selected route. A correct-looking subnet does not prove a shared VLAN or working return path.

**Trap:** an empty host ARP cache and an empty switch MAC table are different problems.

**Recall prompts:** Which device/table acts next? Which IP is being resolved? How can the reply be unicast? Which ports receive a broadcast? What evidence would show a real failure?

Sources and fuller assumptions: [packet journey](../knowledge/01-packet-journey.md), [ARP](../knowledge/03-arp.md), [switching](../knowledge/04-switching.md).
