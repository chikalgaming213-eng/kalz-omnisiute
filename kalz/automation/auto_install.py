from __future__ import annotations

import shutil
from dataclasses import dataclass


class InstallerError(ValueError):
    pass


@dataclass(frozen=True)
class InstallPlan:
    manager: str
    packages: tuple[str, ...]
    argv: tuple[str, ...]
    dry_run: bool = True


MANAGERS = {
    "apt-get": ("install", "-y"),
    "dnf": ("install", "-y"),
    "pacman": ("-S", "--noconfirm"),
    "zypper": ("--non-interactive", "install"),
}


def plan_install(packages: list[str], manager: str | None = None) -> InstallPlan:
    if not packages or any(not package.replace("-", "").replace(".", "").isalnum() for package in packages):
        raise InstallerError("package names must be simple validated tokens")
    selected = manager or next((name for name in MANAGERS if shutil.which(name)), None)
    if selected not in MANAGERS:
        raise InstallerError("no supported package manager available")
    argv = (selected, *MANAGERS[selected], *packages)
    return InstallPlan(selected, tuple(packages), argv)
