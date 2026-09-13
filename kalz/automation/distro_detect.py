from __future__ import annotations

import platform
from pathlib import Path


def _release() -> dict[str, str]:
    result: dict[str, str] = {}
    path = Path('/etc/os-release')
    if path.exists():
        for line in path.read_text(encoding='utf-8', errors='replace').splitlines():
            if '=' in line:
                key, value = line.split('=', 1)
                result[key] = value.strip().strip('"')
    return result


def detect_distro() -> dict[str, str]:
    data = _release()
    return {'id': data.get('ID', platform.system().lower()), 'version': data.get('VERSION_ID', 'unknown'), 'kernel': platform.release()}
