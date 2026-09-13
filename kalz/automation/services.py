from __future__ import annotations

import json
import shutil
from datetime import UTC, datetime
from pathlib import Path

class BackupService:
    def snapshot(self, source: Path, destination: Path) -> Path:
        source, destination = source.expanduser(), destination.expanduser()
        if not source.exists(): raise FileNotFoundError(source)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.is_dir(): shutil.copytree(source, destination, dirs_exist_ok=True)
        else: shutil.copy2(source, destination)
        return destination

class ReportService:
    def write_json(self, path: Path, title: str, payload: dict) -> Path:
        body = {'title': title, 'created_at': datetime.now(UTC).isoformat(), 'payload': payload}
        path.parent.mkdir(parents=True, exist_ok=True); path.write_text(json.dumps(body, indent=2), encoding='utf-8'); return path

class ScopeService:
    def load(self, path: Path) -> frozenset[str]:
        targets = [line.strip() for line in path.read_text(encoding='utf-8').splitlines() if line.strip() and not line.startswith('#')]
        return frozenset(targets)
