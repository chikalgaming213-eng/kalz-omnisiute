from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol

@dataclass(frozen=True)
class PluginManifest:
    name: str
    version: str
    capabilities: tuple[str, ...]

class Plugin(Protocol):
    manifest: PluginManifest
    def register(self, registry: dict[str, Any]) -> None: ...

class PluginRegistry:
    def __init__(self) -> None:
        self.plugins: dict[str, PluginManifest] = {}
        self.capabilities: dict[str, Any] = {}
    def register(self, plugin: Plugin) -> None:
        if plugin.manifest.name in self.plugins:
            raise ValueError('duplicate plugin')
        self.plugins[plugin.manifest.name] = plugin.manifest
        plugin.register(self.capabilities)
