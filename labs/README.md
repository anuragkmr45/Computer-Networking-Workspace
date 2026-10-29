# Practical learning

## Ready starter guides
| Lab | Scope | Execution status in learner environment |
|---|---|---|
| [01 — Inspect Linux state](01-read-only-linux.md) | Read-only observation | Not executed |
| [02 — Isolated ARP](02-isolated-arp.md) | Disposable Linux VM, explicit privileged approval | Not executed |
| [03 — TCP over loopback](03-loopback-tcp.md) | Local Python client/server, no external host | Not executed |
| [04 — Platform backlog](04-platform-lab-backlog.md) | Docker/Kubernetes/AWS designs and future lab specs | Design briefs, not executed guides |

The offline visualizer is an illustration, not a real network capture. The build validation report may record sandbox tests of packaged tools; that does not mean labs ran on your laptop.

## Before any lab
Identify the OS, environment, authority, tool versions, exact traffic scope, expected changes, observations, and cleanup. Prefer a disposable VM for privileged work. Never use production to demonstrate a beginner concept. Do not install tools or provision paid resources without permission. Follow a lab's stop conditions rather than disabling security controls.

## Evidence
Use `templates/LAB_RECORD.md`. Separate predicted output from observed output; record what failed as well as what succeeded. Redact identifying details. Keep packet captures and credentials out of the repository by default.
