#!/usr/bin/env python3
"""Offline structural checks; not a proof of pedagogy, truth, or exam coverage."""
from __future__ import annotations
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DIMENSIONS = {'explain', 'calculate', 'trace', 'implement', 'debug', 'design', 'delayed_recall'}
LEVELS = {'not_assessed', 'guided', 'independent', 'transfer', 'retained', 'not_applicable'}


def validate(root: Path = ROOT) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    counts: dict[str, int] = {}
    required = ['README.md','START_HERE.md','AGENTS.md','context/STUDENT_PROFILE.md',
                'context/LEARNING_STATE.md','context/DECISIONS.md','curriculum/catalog.json',
                'progress/state.json','progress/evidence.jsonl','progress/review_queue.json',
                'practice/questions.json','references/sources.json','VALIDATION_REPORT.md']
    for rel in required:
        if not (root / rel).is_file(): errors.append(f'Missing required file: {rel}')
    if errors: return errors, counts
    try:
        for path in root.rglob('*.json'): json.loads(path.read_text(encoding='utf-8'))
        catalog=json.loads((root/'curriculum/catalog.json').read_text(encoding='utf-8'))
        state=json.loads((root/'progress/state.json').read_text(encoding='utf-8'))
        events=[json.loads(line) for line in (root/'progress/evidence.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
        questions=json.loads((root/'practice/questions.json').read_text(encoding='utf-8'))['questions']
        reviews=json.loads((root/'progress/review_queue.json').read_text(encoding='utf-8'))['reviews']
        sources=json.loads((root/'references/sources.json').read_text(encoding='utf-8'))['sources']
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [f'Cannot parse structured content: {exc}'], counts
    modules=catalog['modules']; mids={m['id'] for m in modules}
    tids=[t['id'] for m in modules for t in m['topics']]; topic_ids=set(tids)
    source_ids={s['id'] for s in sources}; eids=[e['id'] for e in events]; event_ids=set(eids)
    qids={q['id'] for q in questions}
    if len(tids)!=len(topic_ids): errors.append('Duplicate topic IDs')
    if len(eids)!=len(event_ids): errors.append('Duplicate evidence IDs')
    if set(state['topics']) != topic_ids: errors.append('State/catalog topic IDs differ')
    for m in modules:
        if not (root/m['file']).is_file(): errors.append(f"Missing module file {m['file']}")
        if not set(m['prerequisites'])<=mids: errors.append(f"Unknown prerequisite in {m['id']}")
        if not set(m['source_ids'])<=source_ids: errors.append(f"Unknown source in {m['id']}")
    for event in events:
        if not set(event['topic_ids'])<=topic_ids: errors.append(f"Unknown event topic in {event['id']}")
    for tid, entry in state['topics'].items():
        if set(entry['dimensions'])!=DIMENSIONS or not set(entry['dimensions'].values())<=LEVELS:
            errors.append(f'Invalid dimensions/levels: {tid}')
        if not set(entry['evidence_ids'])<=event_ids: errors.append(f'Unknown evidence in {tid}')
        if any(v in {'independent','transfer','retained'} for v in entry['dimensions'].values()):
            linked=[e for e in events if e['id'] in entry['evidence_ids']]
            if not any(e.get('independent_mastery') for e in linked):
                errors.append(f'Independent/retained level without supporting event: {tid}')
    for key in ['current_topic','next_topic']:
        if state[key] not in topic_ids: errors.append(f'Unknown {key}')
    for q in questions:
        if q['topic_id'] not in topic_ids: errors.append(f"Unknown question topic: {q['id']}")
    for r in reviews:
        if r['topic_id'] not in topic_ids or not set(r['question_ids'])<=qids:
            errors.append(f"Invalid review references: {r['id']}")
    skills=list((root/'.agents/skills').glob('*/SKILL.md'))
    for path in skills:
        text=path.read_text(encoding='utf-8')
        match=re.match(r'^---\nname: ([a-z0-9-]+)\ndescription: (.+)\n---\n',text)
        if not match or match.group(1)!=path.parent.name: errors.append(f'Invalid skill frontmatter: {path.relative_to(root)}')
    if len(skills)!=6: errors.append(f'Expected six initial skills, found {len(skills)}')
    for path in root.rglob('*.md'):
        text=path.read_text(encoding='utf-8')
        if text.count('```')%2: errors.append(f'Unbalanced code fence: {path.relative_to(root)}')
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',text):
            if re.match(r'^[a-zA-Z][\w+.-]*:',target) or target.startswith('#'): continue
            local=unquote(target.split('#',1)[0])
            if not local: continue
            resolved=(path.parent/local).resolve()
            if not resolved.is_relative_to(root.resolve()): errors.append(f'Link escapes root: {target}')
            elif not resolved.exists(): errors.append(f'Broken link in {path.relative_to(root)}: {target}')
    counts={'modules':len(modules),'topics':len(topic_ids),'evidence_events':len(events),
            'questions':len(questions),'skills':len(skills),'source_records':len(sources)}
    return errors, counts


def main() -> int:
    errors, counts=validate()
    print(json.dumps({'ok':not errors,'counts':counts,'errors':errors,
                      'scope':'Structure only; technical content, client integration, and lab execution need separate review.'}, indent=2))
    return int(bool(errors))

if __name__ == '__main__':
    sys.exit(main())
