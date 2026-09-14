#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MODE="${1:-plan}"
PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_DIR="${KALZ_VENV_DIR:-$ROOT/.venv}"

log() { printf '[kalz-bootstrap] %s\n' "$*"; }
fail() { printf '[kalz-bootstrap][error] %s\n' "$*" >&2; exit 1; }

check_python() {
  "$PYTHON_BIN" - <<'PY'
import sys
if sys.version_info < (3, 11):
    raise SystemExit('Python 3.11 or newer is required')
print(f'Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}')
PY
}

plan() {
  check_python
  log "root=$ROOT"
  log "venv=$VENV_DIR"
  log "actions=create-venv,upgrade-tools,install-package,compile,test"
  log "mutations=none"
}

apply() {
  [[ "${KALZ_BOOTSTRAP_APPROVED:-false}" == "true" ]] || fail "set KALZ_BOOTSTRAP_APPROVED=true to apply"
  check_python
  "$PYTHON_BIN" -m venv "$VENV_DIR"
  "$VENV_DIR/bin/python" -m pip install --upgrade pip setuptools wheel
  "$VENV_DIR/bin/python" -m pip install -e "$ROOT[test]"
  "$VENV_DIR/bin/python" -m compileall -q "$ROOT/kalz" "$ROOT/tests" "$ROOT/scripts"
  "$VENV_DIR/bin/python" -m pytest -q
  log "bootstrap complete; activate with: source $VENV_DIR/bin/activate"
}

case "$MODE" in
  plan) plan ;;
  apply) apply ;;
  *) fail "usage: $0 {plan|apply}" ;;
esac
