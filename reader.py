# reader.py
import os
import json

def iter_events(folder):
    """
    Yield parsed JSON objects for each non-empty line.
    Subtle trap: lines may have trailing spaces/newlines.
    """
    for fname in sorted(os.listdir(folder)):
        path = os.path.join(folder, fname)
        with open(path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    # yield nothing on bad line (but log would be better)
                    continue
