# Numerical practice

These are original model problems. Work by hand first, then check units and assumptions. No lab measurement is implied.

## N01 — Serialization
A 1,500-byte packet is serialized at 100 Mbps. Ignore all other overhead and delays. Find the serialization delay.

## N02 — Propagation
A link is 1,000 km long. Signal speed is 2 x 10^8 m/s. Find one-way propagation delay.

## N03 — Store-and-forward path
One 1,500-byte packet traverses three identical 10-Mbps links. Each has 2 ms propagation. Routers fully receive the packet before forwarding; ignore processing/queueing. Find last-bit arrival time.

## N04 — Pipelining
Send four of the N03 packets back-to-back along that empty path. Find when the last bit of the fourth packet arrives. Equal rates; no loss/processing/queueing beyond serialization.

## N05 — Subnets
Find network, mask, directed broadcast, and conventional usable host range for 192.168.10.130/26.

## N06 — On-link decision
For 192.168.10.20/16, test target 192.168.11.80 using AND. Then repeat with /24. Assume only connected/default routes.

## N07 — VLSM
Allocate disjoint subnets within 10.20.30.0/24 for 100, 50, and 20 conventional IPv4 LAN hosts. Use largest-first allocation with minimal fitting powers of two.

## N08 — Longest prefix
Routes: 10.0.0.0/8 via A; 10.20.0.0/16 via B; 10.20.30.128/25 via C; default via D. Select for 10.20.30.150, 10.20.30.20, and 203.0.113.5. Assume all routes eligible.

## N09 — BDP
A 100-Mbps path has an RTT of 40 ms. Compute the bandwidth-delay product in bits and decimal bytes.

## N10 — Window-limited rate
A fixed 64,000-byte in-flight window and RTT 80 ms limit a no-loss stream. Link rate is 100 Mbps. Estimate the ideal upper bound from these two constraints, ignoring startup and overhead.

## N11 — Stop-and-Wait
Data frame size is 1,000 bytes; rate 1 Mbps; propagation round trip 20 ms. Ignore ACK serialization, processing, and loss. Find utilization and data rate.

## N12 — Flow-controlled pipeline
Use the N11 model, but allow enough fixed-size frames in flight for continuous sending. What minimum whole-frame window covers the send-to-ACK cycle? Ignore ACK serialization and loss.

## N13 — Overhead
An abstract link transfers 1,000 payload bytes with 50 additional bytes per message. Under this deliberately complete overhead model, what fraction of link bytes are useful payload?

## N14 — IPv4 fragmentation model
A 4,000-byte IPv4 datagram includes a 20-byte header, no options. MTU is 1,500; fragmentation allowed. Find payload sizes, total fragment lengths, offsets in 8-byte units, and MF bits. Ignore link overhead.

## N15 — TCP byte numbering
First data byte has sequence 1001. A sender transmits 1,000 data bytes followed by 500 data bytes; no loss, SYN, or FIN in these ranges. What cumulative next-byte ACK follows each complete in-order range?

## N16 — Educational CRC
For data bits 1101 and generator 1011, append the required zeros and perform modulo-2 division. Find the remainder and transmitted bit string. This toy polynomial is not Ethernet CRC-32.

See the separate numerical solution file only after attempting a problem.
