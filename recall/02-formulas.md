# Numerical anchors

These are model equations with conditions, not universal performance predictions. The original worked problems in [numericals](../practice/NUMERICALS.md) define exact assumptions.

| Quantity/model | Equation | Conditions |
|---|---|---|
| Serialization | t = L / R | L in bits; R in bits/s; include the overhead the question specifies |
| Propagation | t = distance / signal speed | Consistent units; not the same as serialization |
| Simplified path delay | Sum of serialization, propagation, processing, queueing | Actual forwarding and pipelining model matters |
| Bandwidth-delay product | BDP = R x RTT | R in bits/s and RTT in seconds -> bits in flight |
| Ideal window-limited rate | At most min(R, W / RTT) | W in bits; ignores loss, startup, protocol/application limits |
| Stop-and-Wait utilization | Tdata / (Tdata + RTTprop + Tack) | No loss/processing; RTTprop excludes serialization |
| Ordinary IPv4 LAN capacity | 2^(32-prefix) - 2 | Not /31, /32, or a provider-specific reservation rule |
| Equal-size store-and-forward pipeline | (links + packets - 1) L/R + sum propagation | Equal rates, no queueing/processing/loss; packet train |

Conversions: 1 byte = 8 bits; decimal Mbps = 10^6 bits/s; ms = 10^-3 s; microseconds = 10^-6 s. MB and MiB differ; do not silently exchange them.

Ask: Which model? Which units? What is excluded? Does the result pass a sanity check? Use `tools/netcalc.py` only after forming the reasoning.
