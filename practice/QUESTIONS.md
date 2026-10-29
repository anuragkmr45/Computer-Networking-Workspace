# Recall and tracing questions

Assumptions: ordinary IPv4 over Ethernet unless stated; single VLAN and forwarding ports in simple switch exercises; no special security policy, NAT, or proxy ARP unless explicitly introduced.

## Q01 — M02.03
Explain why an ordinary initial ARP request is broadcast and why its reply can normally be unicast.

## Q02 — M02.03
A laptop sends to a remote server through a gateway. Which IPv4 address does it resolve with ARP? Which IP remains the packet destination? State the no-NAT assumption.

## Q03 — M02.03
The next-hop MAC is already usable in the neighbor table. Is a fresh ARP discovery required before every packet? What evidence would you inspect rather than guess?

## Q04 — M03.02
For laptop 192.168.10.20/16 and target 192.168.11.80, calculate both network addresses using the laptop mask. What ARP target follows under connected/default-route assumptions?

## Q05 — M03.02
Repeat Q04 with /24. Explain what changes and what does not change in the first data frame/packet.

## Q06 — M02.02
One switch: MAC-L on port 1, MAC-S on port 2, MAC-X on port 3; same VLAN; empty MAC table. L broadcasts ARP, S replies to L, then L sends data to S. Show the learned entries and outgoing ports after each step.

## Q07 — M02.03
The selected next hop is on-link but no ARP reply arrives. Why does this not by itself cause the host to use its default gateway? Distinguish route choice from neighbor discovery.

## Q08 — M03.02
Two hosts calculate the same IP prefix but are in isolated VLANs with no bridging or proxy. Does matching the prefix guarantee ARP success? What assumption was missing?

## Q09 — M02.02
The sender has a valid ARP entry but the switch has an empty MAC table. Explain why a unicast data frame may be flooded and why this is not an ARP broadcast.

## Q10 — M04.01
A host has a connected 192.168.0.0/16 route and a more-specific route for 192.168.11.80/32 via a reachable router. Which matching route wins in an ordinary longest-prefix lookup? Why is the simple same-subnet shortcut insufficient?

## Q11 — M01.03
An application makes two TCP send calls. Must the receiver get exactly two receive calls with the same boundaries? Explain what TCP provides instead.

## Q12 — M02.03
Why is "ARP message contains IP addresses" not the same as "ARP is carried inside an IP packet"? Draw the encapsulation for ARP versus TCP data.

Answers are in a separate file. Attempt first; ask for a hint rather than treating the solution as recall evidence.
