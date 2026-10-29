# L02 — ARP between two isolated Linux namespaces
**Status:** prepared; privileged commands not executed during packaging.
**Purpose:** observe a real request/reply and cache without using the physical network. This is a point-to-point veth lab, **not a switch-learning demonstration**.

## Permission and stop conditions
Use a disposable Linux VM with iproute2, ping, and tcpdump already installed. Obtain explicit approval for privileged commands. Do not run on production or bypass security restrictions. First inspect `ip netns list` and `ip link show`; stop if `cnw_a`, `cnw_b`, `cnw_a0`, or `cnw_b0` already exists. Only remove objects created by this lab.

## Create the isolated topology
```bash
sudo ip netns add cnw_a
sudo ip netns add cnw_b
sudo ip link add cnw_a0 type veth peer name cnw_b0
sudo ip link set cnw_a0 netns cnw_a
sudo ip link set cnw_b0 netns cnw_b
sudo ip -n cnw_a link set lo up
sudo ip -n cnw_b link set lo up
sudo ip -n cnw_a addr add 192.0.2.10/24 dev cnw_a0
sudo ip -n cnw_b addr add 192.0.2.20/24 dev cnw_b0
sudo ip -n cnw_a link set cnw_a0 up
sudo ip -n cnw_b link set cnw_b0 up
```
No host forwarding, host route, physical bridge, internet attachment, or default gateway is configured. If a step fails, stop and inspect; do not continue with a half-created topology.

## Observe ordinary discovery
In terminal A, inspect the initial neighbor table and start the capture:
```bash
sudo ip -n cnw_a neigh show
sudo ip netns exec cnw_a tcpdump -ni cnw_a0 -c 2 arp
```
In terminal B:
```bash
sudo ip netns exec cnw_a ping -c 1 -W 2 192.0.2.20
sudo ip -n cnw_a neigh show
```
Expected, not observed here: an ARP request/reply around first delivery, an ICMP response, and a learned neighbor mapping. If the mapping was already present, the expected discovery may not recur. Do not flush a physical interface's cache to force it.

## Optional failure contrast
With approval and the same isolated topology, ping `192.0.2.99`, which no lab peer owns. Inspect the neighbor state after resolution attempts. Retry counts/timing vary. This lab has no gateway, so do not infer all application error behavior from this one result.

## Cleanup
Stop any remaining capture with Ctrl+C before removing the namespaces you created:
```bash
sudo ip netns del cnw_a
sudo ip netns del cnw_b
ip netns list
```
The veth interfaces should disappear with their namespaces when no process holds them open. If creation failed before interfaces moved, inspect and remove only that lab-created pair. Never delete pre-existing namespaces or interfaces merely because a name resembles the example.

**Sources:** IP-NETNS, IP-NEIGH, RFC826. Record actual environment and outputs using the lab-record template.
