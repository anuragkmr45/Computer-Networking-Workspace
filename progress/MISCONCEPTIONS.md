# Misconceptions and remaining checks

| ID | Observed issue | Corrective anchor | Current status |
|---|---|---|---|
| MC01 | Used all-ones mask when discussing /24 | /24 is 255.255.255.0; AND produces a network address | Explained; independent calculation pending |
| MC02 | Blended ARP, route choice, and switch knowledge | Route chooses next hop; ARP maps next-hop IPv4 to MAC; switch maps MAC/VLAN to port | Explained; independent trace pending |
| MC03 | Router searches for server then tries another server | Forwarding uses route lookup, not a fresh search or shortest-path calculation per packet | Explained; independent application pending |
| MC04 | Application creates TCP segment | Application supplies bytes; TCP is the transport protocol | Explained; reconstruction pending |

Do not label an error permanently fixed because the tutor supplied the correction. Add future recurrence and successful independent evidence rather than deleting history.
