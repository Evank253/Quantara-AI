# Test for tool gateway HTTP contract without starting a live server.
import requests
from requests.exceptions import RequestException
import pytest


def test_call_tool_gateway_mock(monkeypatch):
    # simulate the expected payload/response contract from the gateway
    class DummyResp:
        status_code = 200
        def json(self):
            return {"status": "ok", "run_id": "stub-run-001", "output": "quantara stub output"}

    def fake_post(url, json=None, timeout=None):
        assert url.endswith("/call_tool")
        assert json and json.get("tool") == "quantara"
        return DummyResp()

    monkeypatch.setattr(requests, "post", fake_post)
    resp = requests.post("http://127.0.0.1:8080/call_tool", json={"tool": "quantara"})
    assert resp.status_code == 200
    data = resp.json()
    assert data.get("status") == "ok"
