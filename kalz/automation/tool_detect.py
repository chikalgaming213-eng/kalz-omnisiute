from __future__ import annotations

import os
import platform
import shutil
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class SystemProfile:
    distro: str
    distro_version: str
    desktop: str
    session_type: str
    kernel: str
    package_managers: tuple[str, ...]
    virtualization: str | None

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def _os_release() -> dict[str, str]:
    path = Path("/etc/os-release")
    result: dict[str, str] = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if "=" in line:
                key, value = line.split("=", 1)
                result[key] = value.strip().strip('"')
    return result


def detect_profile() -> SystemProfile:
    release = _os_release()
    desktop = os.getenv("XDG_CURRENT_DESKTOP") or os.getenv("DESKTOP_SESSION") or "unknown"
    managers = tuple(name for name in ("apt-get", "dnf", "pacman", "zypper", "flatpak", "snap") if shutil.which(name))
    virt = shutil.which("systemd-detect-virt")
    virtualization = None
    if virt:
        import subprocess
        result = subprocess.run([virt], capture_output=True, text=True, check=False)
        value = result.stdout.strip()
        virtualization = value if value and value != "none" else None
    return SystemProfile(
        distro=release.get("ID", platform.system().lower()),
        distro_version=release.get("VERSION_ID", "unknown"),
        desktop=desktop,
        session_type=os.getenv("XDG_SESSION_TYPE", "unknown"),
        kernel=platform.release(),
        package_managers=managers,
        virtualization=virtualization,
    )
