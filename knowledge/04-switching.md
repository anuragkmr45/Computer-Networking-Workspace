# Switching: join the ARP story to actual frame forwarding
**Topic:** M02.02 · **Status:** next lesson prepared, not yet demonstrated.

## Simple mechanism
A learning Ethernet switch records the frame's **source** MAC against the incoming port within its VLAN. It checks the **destination** MAC to forward. Known unicast goes to the learned port; unknown unicast and broadcasts are flooded to eligible forwarding ports in that VLAN except the ingress port. A known destination on the ingress port is filtered rather than sent back. MAC-table learning is distinct from an IP-to-MAC ARP cache. [Cisco switching reference](../references/SOURCES.md#cisco-switch)

## Original trace to teach next
Assume all ports are forwarding in VLAN 10, an empty MAC table, and no filtering/security exceptions.

```text
Laptop MAC-L -- port 1 [Switch] port 2 -- Server MAC-S
                              port 3 -- Other host MAC-X
```

| Event | Table learned from source | Forwarding action |
|---|---|---|
| Laptop broadcasts an ARP request into port 1 | MAC-L -> port 1 | Copy to ports 2 and 3 |
| Server replies to MAC-L into port 2 | MAC-S -> port 2 | Send to port 1 |
| Laptop sends data to MAC-S into port 1 | Refresh MAC-L -> port 1 | Send to port 2 |

Now contrast a different starting condition: the laptop already has an ARP entry but the switch table is empty. The laptop can send unicast data immediately; the switch may flood that unknown unicast. Host ARP and switch learning are independent states.

## Why the distinction matters
When tracing a failure, name the device, table, lookup key, and next action instead of saying "the network knows the address." Separate broadcast-domain membership from an IP-prefix calculation. Do not generalize this simple VLAN trace to every enterprise security feature or an arbitrary cloud network.

## Meaningful check after explanation
Draw the MAC table and outgoing ports after two new frames in Q06. One coherent trace can reveal more than repeated isolated definition questions.

[Fast recall](../recall/01-local-delivery.md) · [ARP note](03-arp.md)
