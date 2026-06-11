import json
import subprocess
import time
import requests


def start_server():
    return subprocess.Popen(["python3", "services/tool-gateway/server.py"])


def test_call_tool_gateway():
    p = start_server()
    try:
        time.sleep(0.8)
        resp = requests.post("http://127.0.0.1:8080/call_tool", json={"tool": "quantara"})
        assert resp.status_code == 200
        data = resp.json()
        assert data.get("status") == "ok"
    finally:
        p.terminate()
        p.wait(timeout=2)
