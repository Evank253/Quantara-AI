#!/usr/bin/env python3
"""Tool Gateway stub (Python/Flask)"""
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

@app.route('/call_tool', methods=['POST'])
def call_tool():
    payload = request.get_json(silent=True) or {}
    # policy check stub (replace with real checks)
    tool = payload.get('tool')
    if tool == 'quantara':
        return jsonify({"status": "ok", "run_id": "stub-run-001", "output": "quantara stub output"})
    return jsonify({"status": "rejected", "reason": "unknown tool"}), 400

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host='0.0.0.0', port=8080)
