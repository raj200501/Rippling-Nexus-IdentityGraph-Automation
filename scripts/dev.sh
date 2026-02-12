#!/usr/bin/env bash
set -euo pipefail
. .venv/bin/activate
python -m apps.api.nexus_api.server &
API_PID=$!
python -m http.server 5173 --directory apps/web &
WEB_PID=$!
trap "kill $API_PID $WEB_PID" EXIT
wait
