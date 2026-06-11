#!/usr/bin/env python3
"""Simple provenance logger stub."""
import json
import time
import os
from typing import Dict

LOGPATH = os.environ.get('PROVENANCE_LOG', 'provenance.log')

def log(entry: Dict) -> None:
    """Append a provenance entry (dict) to the provenance log file as JSON.

    The function copies the entry, adds a timestamp, and appends it as a JSON line.
    """
    entry = dict(entry)
    entry['ts'] = time.time()
    # ensure directory exists
    dirpath = os.path.dirname(LOGPATH)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    with open(LOGPATH, 'a') as f:
        f.write(json.dumps(entry) + "\n")
