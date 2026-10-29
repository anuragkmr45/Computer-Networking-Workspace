# Optional local utilities

Python 3.10+, standard library only. Run from the workspace root. Read the code first. The calculators do not query your network or change settings.

```bash
python tools/netcalc.py subnet 192.168.10.130/26 --destination 192.168.10.190
python tools/netcalc.py delay --bytes 1500 --mbps 100 --km 1000
python tools/netcalc.py bdp --mbps 100 --rtt-ms 40
python tools/netcalc.py crc 1101 1011
python tools/netcalc.py fragment --total 4000 --mtu 1500
python tools/review_due.py --include-unscheduled
python tools/validate_workspace.py
python -m unittest discover -s tests -v
```

`loopback_tcp_demo.py` opens one local client/server exchange at 127.0.0.1; see its lab guide. The validator checks structure, links, records, and basic evidence consistency. It does not establish source truth, learner mastery, exam readiness, or actual desktop/Codex skill discovery.
