from __future__ import annotations

from kalz.automation.de_detect import detect_de
from kalz.de_integration.base import BaseDEAdapter
from kalz.de_integration.generic.adapter import GenericAdapter
from kalz.de_integration.gnome.adapter import GNOMEAdapter
from kalz.de_integration.kde.adapter import KDEAdapter
from kalz.de_integration.xfce.adapter import XFCEAdapter

ADAPTERS = {'kde': KDEAdapter, 'xfce': XFCEAdapter, 'gnome': GNOMEAdapter}

def get_adapter(name: str | None = None) -> BaseDEAdapter:
    return ADAPTERS.get(name or detect_de(), GenericAdapter)()
