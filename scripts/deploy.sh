#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MODE="${1:-plan}"
ENVIRONMENT="${KALZ_ENV:-local}"
RELEASE="${KALZ_RELEASE:-$(git -C "$ROOT" rev-parse --short HEAD 2>/dev/null || echo unknown)}"
DATA_DIR="${KALZ_DATA_DIR:-$ROOT/.kalz-data}"
RELEASE_DIR="$DATA_DIR/releases/$RELEASE"
PREVIOUS_FILE="$DATA_DIR/current-release"

log() { printf '[kalz-deploy] %s\n' "$*"; }
fail() { printf '[kalz-deploy][error] %s\n' "$*" >&2; exit 1; }

require_clean_tree() {
  if [[ -n "$(git -C "$ROOT" status --porcelain)" ]]; then fail "working tree is not clean"; fi
}

secret_scan() {
  if git -C "$ROOT" grep -n -E 'sk-proj-|sk-[A-Za-z0-9]{20,}|BEGIN (RSA|OPENSSH|PRIVATE) KEY' -- . >/dev/null 2>&1; then
    fail "secret-like material detected in tracked files"
  fi
}

plan() {
  log "environment=$ENVIRONMENT"
  log "release=$RELEASE"
  log "root=$ROOT"
  log "data_dir=$DATA_DIR"
  log "python=$(python3 --version 2>&1)"
  log "actions=compile,test,manifest,backup,activate,health"
  log "mutations=none"
}

prepare() {
  require_clean_tree
  secret_scan
  mkdir -p "$RELEASE_DIR" "$DATA_DIR/backups"
  python3 -m compileall -q "$ROOT/kalz" "$ROOT/tests" "$ROOT/scripts"
  python3 -m pytest -q
  git -C "$ROOT" rev-parse HEAD > "$RELEASE_DIR/revision"
  find "$ROOT/kalz" -type f -name '*.py' -print0 | sort -z | xargs -0 sha256sum > "$RELEASE_DIR/manifest.sha256"
  date -u +%Y-%m-%dT%H:%M:%SZ > "$RELEASE_DIR/prepared-at"
}

apply_release() {
  [[ "${KALZ_DEPLOY_APPROVED:-false}" == "true" ]] || fail "set KALZ_DEPLOY_APPROVED=true to apply"
  prepare
  if [[ -f "$PREVIOUS_FILE" ]]; then cp "$PREVIOUS_FILE" "$DATA_DIR/backups/previous-release"; fi
  printf '%s\n' "$RELEASE_DIR" > "$PREVIOUS_FILE"
  log "release activated: $RELEASE_DIR"
  verify
}

verify() {
  [[ -f "$PREVIOUS_FILE" ]] || fail "no active release pointer"
  [[ -f "$(cat "$PREVIOUS_FILE")/manifest.sha256" ]] || fail "release manifest missing"
  python3 -m kalz --doctor >/dev/null 2>&1 || fail "doctor check failed"
  log "verification passed"
}

rollback() {
  [[ "${KALZ_DEPLOY_APPROVED:-false}" == "true" ]] || fail "set KALZ_DEPLOY_APPROVED=true to rollback"
  [[ -f "$DATA_DIR/backups/previous-release" ]] || fail "no previous release backup"
  cp "$DATA_DIR/backups/previous-release" "$PREVIOUS_FILE"
  log "rollback pointer restored to $(cat "$PREVIOUS_FILE")"
}

case "$MODE" in
  plan) plan ;;
  apply) apply_release ;;
  verify) verify ;;
  rollback) rollback ;;
  *) fail "usage: $0 {plan|apply|verify|rollback}" ;;
esac
