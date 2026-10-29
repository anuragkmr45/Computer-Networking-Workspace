# L03 — Application bytes across a local TCP connection
**Prerequisites:** Python 3.10+, permitted loopback sockets; no packages or root needed.
**Scope:** 127.0.0.1 only. This does not demonstrate Ethernet ARP, physical routing, or a remote network.

## Predict and run
Read `tools/loopback_tcp_demo.py`. Predict whether application writes and receive calls must share boundaries, then run:
```bash
python tools/loopback_tcp_demo.py --message "hello networking"
```
The program opens one ephemeral loopback listener, connects one client, streams the message, signals end-of-input, receives an echo, closes sockets, and prints a small JSON record. It uses explicit timeouts and bounded input. Local security software may disallow sockets; do not bypass it.

## Interpret
Inspect endpoint addresses/ports and byte counts. Explain the loop that reads until EOF. Changing receive-buffer chunk size can change application read chunks without proving a particular wire-segmentation pattern. Loopback observations must not be labelled Ethernet packet captures.

## Cleanup and evidence
Sockets close automatically on exit. Record actual result and remaining questions. Build-time testing is reported separately; the learner has not yet run this lab.

**Source:** RFC9293 for the byte-stream model. Python code is original educational implementation, not copied from the standard.
