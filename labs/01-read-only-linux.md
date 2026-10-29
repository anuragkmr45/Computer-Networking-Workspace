# L01 — Observe the three host-side pieces
**Status:** instructions prepared; not executed on the learner's machine.
**Prerequisites:** Linux with iproute2. Use a personal/approved environment. These commands display state; do not change routes or flush caches.

## Predict
What should identify the interface, the next hop, and the known local IP-to-MAC mappings? Write the prediction before reading output.

## Observe
```bash
ip -br link
ip -4 route show
ip -4 neigh show
ip -4 route get 192.0.2.80
```
`route get` asks the kernel for a route decision; it is not a ping or proof that the destination exists. An empty neighbor table is not by itself an error. The Linux neighbor table can contain usable but non-REACHABLE entries, so do not reduce it to "valid versus missing" without examining the state.

## Explain
Identify the selected interface and any `via` next hop in your actual route result. Explain which IP would need resolution on Ethernet. Compare this with the neighbor table without assuming the OS uses the exact interface names in examples.

## Cleanup and privacy
No configuration cleanup is required because these are display/query commands. Do not paste an employer's topology or addresses into chat. Redact output or substitute the supplied synthetic examples.

**Sources:** IP-NEIGH and host/router references in the source register; consult `ip route help` for the installed iproute2 build. Stop on unsupported commands; do not guess Windows/macOS equivalents.
