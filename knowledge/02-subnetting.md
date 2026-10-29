# Subnetting: the calculation behind the decision
**Topics:** M03.01–M03.03 · **Scope:** a simple IPv4 connected-subnet/default-route example. More-specific routes, policy, VPNs, and link isolation can change delivery behavior.

## The operation
A prefix length counts the network-prefix bits. A /24 mask is `255.255.255.0`; /16 is `255.255.0.0`. Bitwise AND of the IP and mask gives its network address. These are different objects: host address, mask, and network address. See [Python's address model](../references/SOURCES.md#py-ipaddress) and [host routing requirements](../references/SOURCES.md#rfc1122).

## Worked example from our discussion
```text
Laptop:      192.168.10.20
Destination: 192.168.11.80

/24:  laptop AND mask = 192.168.10.0
      target AND mask = 192.168.11.0  -> different

/16:  laptop AND mask = 192.168.0.0
      target AND mask = 192.168.0.0   -> same
```
The /16 calculation uses the laptop's mask to judge its own on-link route. It does not reveal the server's actual configuration or prove a working return path. Treating a destination as on-link does not magically bridge separate VLANs.

## A non-octet boundary: /26
```text
IP:          192.168.10.130
Mask:        255.255.255.192
Last octet:  10000010  (130)
AND:         11000000  (192)
Result:      10000000  (128)
```
Thus the containing network is `192.168.10.128/26`. It contains 64 addresses, ending at `.191`. Under conventional IPv4 LAN assumptions, `.128` is the network address, `.191` the directed broadcast, and `.129`–`.190` are 62 host addresses. Do not blindly apply "subtract two" to /31 point-to-point links, /32 host routes, or cloud-provider reservations. The utility labels these cases separately.

## Original reasoning checklist
Write the mask. Compute the laptop's network. Apply that same mask to the target. Then consult the actual routing assumptions. Decide the next-hop IP before asking about ARP. State what you know about the L2 and return paths.

Check arithmetic after your attempt:
```bash
python tools/netcalc.py subnet 192.168.10.130/26 --destination 192.168.10.190
```

**Evidence:** E005 establishes correct recognition of the /16 choice, not independent binary calculation. Practise N05–N08 in the numerical pack.
