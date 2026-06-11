import os
import json
from services.provenance import logger


def test_provenance_log(tmp_path):
    p = tmp_path / "prov.log"
    os.environ['PROVENANCE_LOG'] = str(p)
    entry = {"action": "test", "who": "ci"}
    logger.log(entry)
    content = p.read_text()
    assert '"action": "test"' in content
