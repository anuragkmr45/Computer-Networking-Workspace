# Progress and evidence

`state.json` is the structured current record. `evidence.jsonl` is append-only event history. `review_queue.json` stores suggested reviews, not running reminders. The concise human checkpoint is `context/LEARNING_STATE.md`; update it together with state.

## Dimension values
| Value | Meaning |
|---|---|
| not_assessed | No adequate evidence; not a failing grade |
| guided | Demonstrated with explanation, options, hints, or immediate repetition |
| independent | Correct reasoning on a task without required help; cite evidence |
| transfer | Correct application to a materially unfamiliar case; cite evidence |
| retained | Successful delayed retrieval or application; cite dated evidence |
| not_applicable | Explicitly justified for this topic/dimension |

Do not collapse the dimensions into an unsupported overall percentage. A practical lab can be complete while design is unassessed; recognition can be correct while independent calculation is still untested.

## Current evidence limits
Six migrated events exist. None demonstrates completed local labs, independent subnet calculations, advanced protocol understanding, or delayed recall. All advanced topics remain unassessed. Content prepared by the tutor does not raise competence.

## Recording a new attempt
Use a unique event ID, topic IDs, task, response summary, assistance, outcome, source/date, and independent_mastery flag. Keep literal sensitive details out. Link the event from affected topics. For a retained rating add the earlier learning date and delay; do not infer it from calendar time alone.

Run `python tools/review_due.py --include-unscheduled` to list review candidates. This script only prints records; it does not send notifications or alter state.
