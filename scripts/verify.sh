#!/usr/bin/env bash
set -euo pipefail
. .venv/bin/activate
python -m unittest discover -s apps/api/tests -v
python scripts/loc.py > /tmp/loc_report.txt
cat /tmp/loc_report.txt
npm run verify --prefix apps/web
