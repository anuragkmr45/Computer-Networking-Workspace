#!/usr/bin/env python3
"""Print suggested reviews only. No notifications, state writes, or scheduler."""
from __future__ import annotations
import argparse
from datetime import date, datetime, timedelta, timezone
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--today', type=date.fromisoformat, default=datetime.now(timezone(timedelta(hours=5, minutes=30))).date())
    parser.add_argument('--include-unscheduled', action='store_true')
    args = parser.parse_args()
    path = Path(__file__).resolve().parents[1] / 'progress/review_queue.json'
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
        selected = []
        for entry in data['reviews']:
            if entry.get('status') == 'completed':
                continue
            when = entry.get('scheduled_for')
            if (when is not None and date.fromisoformat(when) <= args.today) or (when is None and args.include_unscheduled):
                selected.append(entry)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f'Cannot read review queue: {exc}\n')
    print(json.dumps({'as_of': args.today.isoformat(), 'suggestions': selected,
                      'note': 'Candidates only; nothing has been scheduled or changed.'}, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
