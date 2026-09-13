from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import os

@dataclass
class AppConfig:
    app_name: str = 'Kalz OmniSuite'
    mode: str = 'safe'
    data_dir: Path = field(default_factory=lambda: Path(os.getenv('XDG_STATE_HOME', Path.home() / '.local/state')) / 'kalz')
    audit_file: Path | None = None
    db_file: Path | None = None
    dry_run: bool = True
    def __post_init__(self) -> None:
        self.data_dir = Path(self.data_dir).expanduser()
        self.audit_file = self.audit_file or self.data_dir / 'audit.jsonl'
        self.db_file = self.db_file or self.data_dir / 'kalz.sqlite3'
        self.data_dir.mkdir(parents=True, exist_ok=True)
