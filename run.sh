#!/usr/bin/env bash
set -e
bash install.sh
echo "[+] Starting FastAPI application using Uvicorn..."
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000
