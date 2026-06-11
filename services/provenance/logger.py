Simple provenance logger stub
import json, time, os
LOGPATH = os.environ.get('PROVENANCE_LOG','provenance.log')
def log(entry):
    entry['ts'] = time.time()
    with open(LOGPATH,'a') as f:
        f.write(json.dumps(entry) + "\n")
