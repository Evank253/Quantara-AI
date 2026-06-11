#!/usr/bin/env bash
set -euo pipefail
echo "Starting prototype stubs..."
python3 services/tool-gateway/server.py &>/tmp/tool-gateway.log &
TG_PID=$!
sleep 1
echo "Running RAG demo..."
python3 - <<'PY'
from services.retrieval.rag_demo import index_documents, aggregate_answer
idx = [
    {"id":"d1","text":"Quantara simulation docs and examples."},
    {"id":"d2","text":"High-precision numeric kernels: MPFR usage."},
    {"id":"d3","text":"Agent orchestration and provenance patterns."},
]
index_documents(idx)
print(aggregate_answer("MPFR numeric kernels"))
PY
echo "Running MPFR demo (bc placeholder)..."
python3 services/numeric/mpfr_demo.py
echo "Stopping tool gateway..."
kill $TG_PID || true
echo "Done."
