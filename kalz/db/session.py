from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

SCHEMA = '''
CREATE TABLE IF NOT EXISTS jobs (id TEXT PRIMARY KEY, status TEXT NOT NULL, tool TEXT NOT NULL, created_at TEXT NOT NULL, result_json TEXT);
CREATE TABLE IF NOT EXISTS scopes (id INTEGER PRIMARY KEY, name TEXT UNIQUE NOT NULL, targets_json TEXT NOT NULL, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS reports (id INTEGER PRIMARY KEY, kind TEXT NOT NULL, body TEXT NOT NULL, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS plugins (name TEXT PRIMARY KEY, version TEXT NOT NULL, enabled INTEGER NOT NULL DEFAULT 0);
'''

class Database:
    def __init__(self, path: Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(self.path)
        self.connection.row_factory = sqlite3.Row
        self.connection.executescript(SCHEMA)
        self.connection.commit()
    def execute(self, sql: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
        cur = self.connection.execute(sql, params)
        self.connection.commit()
        return [dict(row) for row in cur.fetchall()]
    def close(self) -> None:
        self.connection.close()
