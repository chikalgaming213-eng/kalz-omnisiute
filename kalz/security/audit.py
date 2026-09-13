from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


def _canonical(value: dict[str, Any]) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()


class AuditChain:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _last_hash(self) -> str:
        if not self.path.exists():
            return "0" * 64
        lines = self.path.read_text(encoding="utf-8").splitlines()
        if not lines:
            return "0" * 64
        return json.loads(lines[-1])["hash"]

    def append(self, action: str, details: dict[str, Any]) -> dict[str, Any]:
        record: dict[str, Any] = {
            "ts": datetime.now(UTC).isoformat(),
            "action": action,
            "details": details,
            "prev_hash": self._last_hash(),
        }
        record["hash"] = hashlib.sha256(_canonical(record)).hexdigest()
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, sort_keys=True) + "\n")
        return record

    def verify(self) -> tuple[bool, str]:
        previous = "0" * 64
        if not self.path.exists():
            return True, "empty"
        for index, line in enumerate(self.path.read_text(encoding="utf-8").splitlines(), 1):
            record = json.loads(line)
            actual = record.pop("hash")
            if record.get("prev_hash") != previous:
                return False, f"broken link at line {index}"
            expected = hashlib.sha256(_canonical(record)).hexdigest()
            if actual != expected:
                return False, f"tampered record at line {index}"
            previous = actual
        return True, "ok"
