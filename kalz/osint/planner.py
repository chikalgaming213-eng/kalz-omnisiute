from __future__ import annotations

from dataclasses import dataclass, asdict
from urllib.parse import urlparse

from kalz.osint.catalog import OSINTTool, find_osint


class OSINTScopeError(ValueError):
    """Raised when an OSINT plan falls outside public, authorized scope."""


@dataclass(frozen=True)
class OSINTPlan:
    tool: str
    repository: str
    target: str
    category: str
    risk: str
    steps: tuple[str, ...]
    requires_consent: bool
    execution_mode: str = "plan-only"

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


class OSINTPlanner:
    """Builds auditable plans; it does not invoke OSINT binaries or network scans."""

    def __init__(self, tools: tuple[OSINTTool, ...] = ()) -> None:
        from kalz.osint.catalog import OSINT_TOOLS
        self.tools = tools or OSINT_TOOLS

    @staticmethod
    def validate_target(target: str) -> str:
        clean = target.strip()
        if not clean or len(clean) > 253:
            raise OSINTScopeError("target must be a non-empty bounded hostname or public URL")
        if any(token in clean.lower() for token in ("localhost", "127.0.0.1", "0.0.0.0", "169.254.", "file://", "unix://")):
            raise OSINTScopeError("private, local, and file targets are not allowed")
        parsed = urlparse(clean if "://" in clean else f"https://{clean}")
        if not parsed.hostname:
            raise OSINTScopeError("target must contain a hostname")
        return clean

    def plan(self, tool_name: str, target: str) -> OSINTPlan:
        tool = find_osint(tool_name)
        if tool is None:
            raise OSINTScopeError(f"unknown OSINT tool: {tool_name}")
        clean_target = self.validate_target(target)
        steps = (
            "validate consent and authorized scope",
            "collect only public-source inputs",
            "record request, target, and tool in audit chain",
            "run only after explicit operator approval",
            "redact sensitive output before storage",
        )
        return OSINTPlan(tool.name, tool.repository, clean_target, tool.category, tool.risk, steps, True)
