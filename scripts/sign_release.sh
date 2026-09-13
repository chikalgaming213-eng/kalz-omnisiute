#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PYTHONPATH="$ROOT" exec python "$ROOT/scripts/kalz_action.py" sign-plan "$@"
