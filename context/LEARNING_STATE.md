# Current learning checkpoint

**Checkpoint:** 2026-10-29, migrated from this temporary conversation.
**Track:** networking fundamentals; connection between subnetting, next-hop selection, ARP, and Ethernet switching.
**Status:** guided understanding / recognition demonstrated, not independent mastery.

## What actually happened
The learner described broad encapsulation but confused /24 with an all-ones mask and conflated routing, ARP, and switch knowledge. After explanation, they correctly named the remote server's destination IP and the gateway's destination MAC. They explicitly said they did not know ARP's working; the tutor explained request, reply, and caching. The learner then explained that an unknown next-hop MAC motivates a broadcast and chose the correct /16 ARP target and ARP-failure option. These were assisted, immediate answers, not delayed or practical evidence.

## Resume here
Teach **MAC learning + broadcast flooding + known/unknown unicast + ARP through a switch** as one connected lesson. Use one switch, a laptop, and two other hosts in one VLAN. Show which table each device consults, how the switch learns from source MACs, and how an ARP broadcast differs from subsequent unicast data. Clarify before asking. At a natural stopping point, use one open explanation or a tiny table trace—not another chain of multiple-choice questions.

Then return to a worked subnet calculation (/24 versus /16, followed by a non-octet mask such as /26). Let the learner try one independent variation when ready. Practical lab work remains optional until the local environment is known.

## Already prepared, not yet learned
Written seed notes, question bank, numerical set, lab guides, and interactive visualizer exist in this package. Their existence is not learning evidence. All advanced curriculum topics remain unassessed.

## Teaching adjustment
No further onboarding or mandatory assessment is required to use this workspace. The learner wants delivery and useful cohesive lessons, not prolonged diagnostics.

## Files to consult next
- `knowledge/04-switching.md` and `knowledge/03-arp.md`
- `recall/01-local-delivery.md`
- `progress/state.json`, `progress/evidence.jsonl`
- `curriculum/02-local-networks.md`

## Save discipline
Keep this file synchronized with the structured state. Do not claim future or cross-device sessions have access until these files are actually opened. No Notion writes, local learner labs, or independent mastery are recorded.
