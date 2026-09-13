from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class DEStatus:
    name: str
    available: bool
    capabilities: tuple[str, ...]


class BaseDEAdapter(ABC):
    name = "generic"

    @abstractmethod
    def status(self) -> DEStatus:
        raise NotImplementedError

    def integration_plan(self) -> list[str]:
        return ["install user-level desktop entry", "apply theme only after consent"]
