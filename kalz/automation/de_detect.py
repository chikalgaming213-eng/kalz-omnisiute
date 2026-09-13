from __future__ import annotations

import os

SUPPORTED = ("kde", "xfce", "gnome", "cinnamon", "mate", "lxqt", "lxde", "budgie", "pantheon", "sway", "i3", "hyprland", "cosmic")


def detect_de() -> str:
    raw = " ".join((os.getenv("XDG_CURRENT_DESKTOP", ""), os.getenv("DESKTOP_SESSION", ""))).lower()
    for name in SUPPORTED:
        if name in raw:
            return name
    return "generic"
