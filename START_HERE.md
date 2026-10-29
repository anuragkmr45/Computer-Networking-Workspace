# Start here

## 1. Extract and inspect
Extract the ZIP into a dedicated folder, for example `Computer-Networking-Mastery`. Keep the folder structure, including the hidden `.agents` directory. Read `AGENTS.md` before letting an agent use it. Do not install these instructions globally or copy them into unrelated projects.

No setup command is required to read the notes. Open `visuals/arp-next-hop-demo.html` in a browser for the local interactive walkthrough; it has no network requests or account integration. If browser policy blocks local HTML, use the Markdown notes rather than weakening that policy.

## 2. Give your agent this folder
Use a ChatGPT/Codex interface that actually supports opening a local project or folder and reading/writing its files. Select this extracted folder as the working project. Labels and availability vary by client; an ordinary desktop chat is not automatically a folder-writing agent.

If you already use Codex CLI, open a terminal in the extracted folder and run your installed `codex` command. This ZIP does not install Codex or modify global configuration. Check current official installation documentation if it is absent.

For Codex, repository instructions use `AGENTS.md` and local skills live under `.agents/skills`. See the official references OAI-AGENTS and OAI-SKILLS in [SOURCES](references/SOURCES.md). Start at this root so project guidance can be discovered. Other clients must be explicitly asked to read the same files; their chat histories are not shared.

## 3. Paste this first message
```text
Use this folder as my Computer Networking learning workspace.
Read AGENTS.md, context/STUDENT_PROFILE.md, context/LEARNING_STATE.md,
and context/DECISIONS.md. Confirm which local files you can read and whether
workspace writes are available. Do not change global settings or connect apps.
Resume the saved learning path without onboarding or another mandatory quiz.
Teach the next cohesive unit, then checkpoint meaningful learning evidence.
```

The same prompt is in [prompts/START_SESSION.md](prompts/START_SESSION.md). If a client lacks file access, attach the four named files and the current topic notes; request a paste-ready checkpoint instead of pretending it was saved.

## 4. First lesson already chosen
The next lesson is a joined-up explanation of **Ethernet frames, MAC learning, flooding, and how the switch carries the ARP exchange**. Reuse the current laptop/server example and explain before checking. Do not restart all of ARP or demand more onboarding.

The learner chose correct answers in assisted ARP/subnet scenarios. Independent subnet calculations, switch behavior, and real labs are not yet demonstrated. See [learning evidence](progress/README.md).

## 5. Choose a mode naturally
| Say | Tutor action |
|---|---|
| Continue learning | Resume the saved cohesive unit |
| Recall ARP | Show concise recall triggers; offer retrieval without immediately revealing solutions |
| Practice subnetting | Use an appropriate exercise, hints, and checked numerical reasoning |
| Go deeper into this | Add one relevant level of mechanism, implementation, failure, or design reasoning |
| Lab mode | Check OS/tool permissions only when needed for that lab; avoid production |
| Feedback: fewer quizzes | Record the request and adjust pacing; do not weaken evidence rules |
| Checkpoint | Save state, evidence, session note, and meaningful note changes if writable |
| Review curriculum | Inspect gaps and propose substantial changes for approval |

## 6. Optional local validation
Python 3.10 or newer is sufficient. No packages need installing. Run from the workspace root:
```bash
python tools/validate_workspace.py
python -m unittest discover -s tests -v
python tools/netcalc.py subnet 192.168.10.20/16 --destination 192.168.11.80
python tools/loopback_tcp_demo.py
```
Use `python3` or `py -3` where appropriate. The TCP demonstration uses only loopback; an endpoint-security policy may still disallow sockets. Do not disable security controls to make it run.

## 7. Privacy, permission, and recovery
- There is no Notion connection, account-level integration, scheduled task, or synchronization in this package.
- Agent use may send selected context to a model service. A folder on your disk is not a guarantee of entirely offline processing.
- Keep approval and sandbox controls enabled. Writing progress is not permission to run privileged network commands, create paid resources, or modify production.
- Review diffs before backups. A private Git repository is optional; do not push automatically. Avoid concurrent writers to progress files.
- Never place credentials, employer network diagrams, raw private captures, or confidential incident data in learning notes. Use synthetic or redacted examples.
- If saving fails, the tutor must say which file failed and provide the unsaved checkpoint for manual recovery.
