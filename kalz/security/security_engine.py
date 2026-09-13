from __future__ import annotations

import hashlib
import ipaddress
import json
import re
import time
from dataclasses import dataclass, field
from typing import Any

class SecurityError(ValueError): pass

@dataclass(frozen=True)
class SecurityContext:
    actor: str
    mode: str = "safe"
    consent: bool = False
    targets: frozenset[str] = frozenset()
    capabilities: frozenset[str] = frozenset()
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class SecurityDecision:
    rule: str
    allowed: bool
    reason: str
    risk: str
    evidence: dict[str, Any]

class SecurityRule:
    family = "generic"
    name = "rule"
    risk = "low"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        if not context.actor.strip(): return SecurityDecision(self.name, False, "actor required", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"type": type(value).__name__})
    def enforce(self, value: Any, context: SecurityContext) -> Any:
        decision = self.evaluate(value, context)
        if not decision.allowed: raise SecurityError(decision.reason)
        return value
    def fingerprint(self, value: Any, context: SecurityContext) -> str:
        return hashlib.sha256(json.dumps({"rule": self.name, "value": repr(value), "actor": context.actor}, sort_keys=True).encode()).hexdigest()

class ArgvInputRule(SecurityRule):
    family = 'input'
    name = 'argv'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 0})

class PackageInputRule(SecurityRule):
    family = 'input'
    name = 'package'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 1})

class PathInputRule(SecurityRule):
    family = 'input'
    name = 'path'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 2})

class UrlInputRule(SecurityRule):
    family = 'input'
    name = 'url'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 3})

class HostnameInputRule(SecurityRule):
    family = 'input'
    name = 'hostname'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 4})

class IpInputRule(SecurityRule):
    family = 'input'
    name = 'ip'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 5})

class PortInputRule(SecurityRule):
    family = 'input'
    name = 'port'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 6})

class FilenameInputRule(SecurityRule):
    family = 'input'
    name = 'filename'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 7})

class WorkflowInputRule(SecurityRule):
    family = 'input'
    name = 'workflow'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 8})

class PluginInputRule(SecurityRule):
    family = 'input'
    name = 'plugin'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 9})

class ThemeInputRule(SecurityRule):
    family = 'input'
    name = 'theme'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 10})

class LocaleInputRule(SecurityRule):
    family = 'input'
    name = 'locale'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 11})

class TimezoneInputRule(SecurityRule):
    family = 'input'
    name = 'timezone'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 12})

class DurationInputRule(SecurityRule):
    family = 'input'
    name = 'duration'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 13})

class SizeInputRule(SecurityRule):
    family = 'input'
    name = 'size'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 14})

class CountInputRule(SecurityRule):
    family = 'input'
    name = 'count'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 15})

class EnumInputRule(SecurityRule):
    family = 'input'
    name = 'enum'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 16})

class JsonInputRule(SecurityRule):
    family = 'input'
    name = 'json'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 17})

class YamlInputRule(SecurityRule):
    family = 'input'
    name = 'yaml'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 18})

class TomlInputRule(SecurityRule):
    family = 'input'
    name = 'toml'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 19})

class TargetScopeRule(SecurityRule):
    family = 'scope'
    name = 'target'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 20})

class CidrScopeRule(SecurityRule):
    family = 'scope'
    name = 'cidr'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 21})

class DomainScopeRule(SecurityRule):
    family = 'scope'
    name = 'domain'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 22})

class ServiceScopeRule(SecurityRule):
    family = 'scope'
    name = 'service'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 23})

class PortScopeRule(SecurityRule):
    family = 'scope'
    name = 'port'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 24})

class FileScopeRule(SecurityRule):
    family = 'scope'
    name = 'file'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 25})

class DirectoryScopeRule(SecurityRule):
    family = 'scope'
    name = 'directory'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 26})

class UserScopeRule(SecurityRule):
    family = 'scope'
    name = 'user'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 27})

class GroupScopeRule(SecurityRule):
    family = 'scope'
    name = 'group'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 28})

class ProcessScopeRule(SecurityRule):
    family = 'scope'
    name = 'process'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 29})

class PackageScopeRule(SecurityRule):
    family = 'scope'
    name = 'package'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 30})

class RepositoryScopeRule(SecurityRule):
    family = 'scope'
    name = 'repository'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 31})

class DesktopScopeRule(SecurityRule):
    family = 'scope'
    name = 'desktop'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 32})

class DisplayScopeRule(SecurityRule):
    family = 'scope'
    name = 'display'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 33})

class SessionScopeRule(SecurityRule):
    family = 'scope'
    name = 'session'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 34})

class WorkflowScopeRule(SecurityRule):
    family = 'scope'
    name = 'workflow'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 35})

class JobScopeRule(SecurityRule):
    family = 'scope'
    name = 'job'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 36})

class ReportScopeRule(SecurityRule):
    family = 'scope'
    name = 'report'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 37})

class PluginScopeRule(SecurityRule):
    family = 'scope'
    name = 'plugin'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 38})

class AssetScopeRule(SecurityRule):
    family = 'scope'
    name = 'asset'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if True and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 39})

class SafeModePolicyRule(SecurityRule):
    family = 'policy'
    name = 'safe_mode'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 40})

class StandardModePolicyRule(SecurityRule):
    family = 'policy'
    name = 'standard_mode'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 41})

class AdvancedModePolicyRule(SecurityRule):
    family = 'policy'
    name = 'advanced_mode'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 42})

class LabModePolicyRule(SecurityRule):
    family = 'policy'
    name = 'lab_mode'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 43})

class PrivilegePolicyRule(SecurityRule):
    family = 'policy'
    name = 'privilege'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 44})

class NetworkPolicyRule(SecurityRule):
    family = 'policy'
    name = 'network'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 45})

class FilesystemPolicyRule(SecurityRule):
    family = 'policy'
    name = 'filesystem'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 46})

class PackagePolicyRule(SecurityRule):
    family = 'policy'
    name = 'package'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 47})

class ServicePolicyRule(SecurityRule):
    family = 'policy'
    name = 'service'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 48})

class DesktopPolicyRule(SecurityRule):
    family = 'policy'
    name = 'desktop'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 49})

class BackupPolicyRule(SecurityRule):
    family = 'policy'
    name = 'backup'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 50})

class RestorePolicyRule(SecurityRule):
    family = 'policy'
    name = 'restore'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 51})

class UpdatePolicyRule(SecurityRule):
    family = 'policy'
    name = 'update'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 52})

class PluginPolicyRule(SecurityRule):
    family = 'policy'
    name = 'plugin'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 53})

class ApiPolicyRule(SecurityRule):
    family = 'policy'
    name = 'api'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 54})

class SchedulerPolicyRule(SecurityRule):
    family = 'policy'
    name = 'scheduler'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 55})

class ReportPolicyRule(SecurityRule):
    family = 'policy'
    name = 'report'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 56})

class ExportPolicyRule(SecurityRule):
    family = 'policy'
    name = 'export'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 57})

class ImportPolicyRule(SecurityRule):
    family = 'policy'
    name = 'import'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 58})

class ReleasePolicyRule(SecurityRule):
    family = 'policy'
    name = 'release'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if True and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 59})

class ChainAuditRule(SecurityRule):
    family = 'audit'
    name = 'chain'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 60})

class RecordAuditRule(SecurityRule):
    family = 'audit'
    name = 'record'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 61})

class TimestampAuditRule(SecurityRule):
    family = 'audit'
    name = 'timestamp'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 62})

class ActorAuditRule(SecurityRule):
    family = 'audit'
    name = 'actor'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 63})

class ConsentAuditRule(SecurityRule):
    family = 'audit'
    name = 'consent'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 64})

class ScopeAuditRule(SecurityRule):
    family = 'audit'
    name = 'scope'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 65})

class CommandAuditRule(SecurityRule):
    family = 'audit'
    name = 'command'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 66})

class ResultAuditRule(SecurityRule):
    family = 'audit'
    name = 'result'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 67})

class ErrorAuditRule(SecurityRule):
    family = 'audit'
    name = 'error'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 68})

class RedactionAuditRule(SecurityRule):
    family = 'audit'
    name = 'redaction'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 69})

class RotationAuditRule(SecurityRule):
    family = 'audit'
    name = 'rotation'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 70})

class RetentionAuditRule(SecurityRule):
    family = 'audit'
    name = 'retention'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 71})

class ExportAuditRule(SecurityRule):
    family = 'audit'
    name = 'export'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 72})

class VerifyAuditRule(SecurityRule):
    family = 'audit'
    name = 'verify'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 73})

class SignatureAuditRule(SecurityRule):
    family = 'audit'
    name = 'signature'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 74})

class KeyAuditRule(SecurityRule):
    family = 'audit'
    name = 'key'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 75})

class CheckpointAuditRule(SecurityRule):
    family = 'audit'
    name = 'checkpoint'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 76})

class ReplayAuditRule(SecurityRule):
    family = 'audit'
    name = 'replay'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 77})

class DiffAuditRule(SecurityRule):
    family = 'audit'
    name = 'diff'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 78})

class IntegrityAuditRule(SecurityRule):
    family = 'audit'
    name = 'integrity'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 79})

class ConsentControlRule(SecurityRule):
    family = 'control'
    name = 'consent'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 80})

class RateControlRule(SecurityRule):
    family = 'control'
    name = 'rate'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 81})

class QuotaControlRule(SecurityRule):
    family = 'control'
    name = 'quota'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 82})

class TimeoutControlRule(SecurityRule):
    family = 'control'
    name = 'timeout'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 83})

class CancellationControlRule(SecurityRule):
    family = 'control'
    name = 'cancellation'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 84})

class PanicControlRule(SecurityRule):
    family = 'control'
    name = 'panic'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 85})

class LockControlRule(SecurityRule):
    family = 'control'
    name = 'lock'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 86})

class UnlockControlRule(SecurityRule):
    family = 'control'
    name = 'unlock'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 87})

class RedactionControlRule(SecurityRule):
    family = 'control'
    name = 'redaction'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 88})

class SandboxControlRule(SecurityRule):
    family = 'control'
    name = 'sandbox'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 89})

class IsolationControlRule(SecurityRule):
    family = 'control'
    name = 'isolation'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 90})

class ResourceControlRule(SecurityRule):
    family = 'control'
    name = 'resource'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 91})

class CpuControlRule(SecurityRule):
    family = 'control'
    name = 'cpu'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 92})

class MemoryControlRule(SecurityRule):
    family = 'control'
    name = 'memory'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 93})

class DiskControlRule(SecurityRule):
    family = 'control'
    name = 'disk'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 94})

class NetworkControlRule(SecurityRule):
    family = 'control'
    name = 'network'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 95})

class ConcurrencyControlRule(SecurityRule):
    family = 'control'
    name = 'concurrency'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 96})

class RetryControlRule(SecurityRule):
    family = 'control'
    name = 'retry'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 97})

class BackoffControlRule(SecurityRule):
    family = 'control'
    name = 'backoff'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 98})

class CircuitControlRule(SecurityRule):
    family = 'control'
    name = 'circuit'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 99})

class ActorIdentityRule(SecurityRule):
    family = 'identity'
    name = 'actor'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 100})

class SessionIdentityRule(SecurityRule):
    family = 'identity'
    name = 'session'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 101})

class TokenIdentityRule(SecurityRule):
    family = 'identity'
    name = 'token'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 102})

class ApiKeyIdentityRule(SecurityRule):
    family = 'identity'
    name = 'api_key'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 103})

class CertificateIdentityRule(SecurityRule):
    family = 'identity'
    name = 'certificate'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 104})

class SignatureIdentityRule(SecurityRule):
    family = 'identity'
    name = 'signature'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 105})

class RoleIdentityRule(SecurityRule):
    family = 'identity'
    name = 'role'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 106})

class PermissionIdentityRule(SecurityRule):
    family = 'identity'
    name = 'permission'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 107})

class CapabilityIdentityRule(SecurityRule):
    family = 'identity'
    name = 'capability'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 108})

class PluginIdentityRule(SecurityRule):
    family = 'identity'
    name = 'plugin'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 109})

class DeviceIdentityRule(SecurityRule):
    family = 'identity'
    name = 'device'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 110})

class DesktopIdentityRule(SecurityRule):
    family = 'identity'
    name = 'desktop'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 111})

class OperatorIdentityRule(SecurityRule):
    family = 'identity'
    name = 'operator'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 112})

class TicketIdentityRule(SecurityRule):
    family = 'identity'
    name = 'ticket'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 113})

class ReasonIdentityRule(SecurityRule):
    family = 'identity'
    name = 'reason'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 114})

class ApprovalIdentityRule(SecurityRule):
    family = 'identity'
    name = 'approval'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 115})

class ReviewerIdentityRule(SecurityRule):
    family = 'identity'
    name = 'reviewer'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 116})

class OwnerIdentityRule(SecurityRule):
    family = 'identity'
    name = 'owner'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 117})

class TenantIdentityRule(SecurityRule):
    family = 'identity'
    name = 'tenant'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 118})

class EnvironmentIdentityRule(SecurityRule):
    family = 'identity'
    name = 'environment'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 119})

class HashIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'hash'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 120})

class HmacIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'hmac'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 121})

class ChainIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'chain'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 122})

class ManifestIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'manifest'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 123})

class PackageIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'package'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 124})

class ReleaseIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'release'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 125})

class UpdateIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'update'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 126})

class PluginIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'plugin'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 127})

class AssetIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'asset'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 128})

class ShaderIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'shader'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 129})

class QmlIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'qml'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 130})

class ThemeIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'theme'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 131})

class DatabaseIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'database'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 132})

class MigrationIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'migration'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 133})

class BackupIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'backup'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 134})

class ReportIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'report'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 135})

class WorkflowIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'workflow'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 136})

class ScopeIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'scope'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 137})

class ConfigIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'config'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 138})

class SecretIntegrityRule(SecurityRule):
    family = 'integrity'
    name = 'secret'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 139})

class IpPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'ip'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 140})

class HostnamePrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'hostname'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 141})

class UsernamePrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'username'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 142})

class EmailPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'email'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 143})

class TokenPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'token'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 144})

class SecretPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'secret'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 145})

class PasswordPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'password'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 146})

class CookiePrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'cookie'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 147})

class HeaderPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'header'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 148})

class QueryPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'query'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 149})

class PathPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'path'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 150})

class CommandPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'command'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 151})

class LogPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'log'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 152})

class ReportPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'report'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 153})

class BackupPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'backup'
    risk = 'high'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 154})

class ScopePrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'scope'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 155})

class TargetPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'target'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 156})

class AuditPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'audit'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 157})

class ClipboardPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'clipboard'
    risk = 'low'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 158})

class EnvironmentPrivacyRule(SecurityRule):
    family = 'privacy'
    name = 'environment'
    risk = 'medium'
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if False and str(value) not in context.targets:
            return SecurityDecision(self.name, False, "value outside declared scope", self.risk, {"value": str(value)})
        if False and context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "consent required in safe mode", self.risk, {})
        return SecurityDecision(self.name, True, "rule passed", self.risk, {"family": self.family, "sequence": 159})

RULES: dict[str, SecurityRule] = {}

RULES['argv'] = ArgvInputRule()

RULES['package'] = PackageInputRule()

RULES['path'] = PathInputRule()

RULES['url'] = UrlInputRule()

RULES['hostname'] = HostnameInputRule()

RULES['ip'] = IpInputRule()

RULES['port'] = PortInputRule()

RULES['filename'] = FilenameInputRule()

RULES['workflow'] = WorkflowInputRule()

RULES['plugin'] = PluginInputRule()

RULES['theme'] = ThemeInputRule()

RULES['locale'] = LocaleInputRule()

RULES['timezone'] = TimezoneInputRule()

RULES['duration'] = DurationInputRule()

RULES['size'] = SizeInputRule()

RULES['count'] = CountInputRule()

RULES['enum'] = EnumInputRule()

RULES['json'] = JsonInputRule()

RULES['yaml'] = YamlInputRule()

RULES['toml'] = TomlInputRule()

RULES['target'] = TargetScopeRule()

RULES['cidr'] = CidrScopeRule()

RULES['domain'] = DomainScopeRule()

RULES['service'] = ServiceScopeRule()

RULES['port'] = PortScopeRule()

RULES['file'] = FileScopeRule()

RULES['directory'] = DirectoryScopeRule()

RULES['user'] = UserScopeRule()

RULES['group'] = GroupScopeRule()

RULES['process'] = ProcessScopeRule()

RULES['package'] = PackageScopeRule()

RULES['repository'] = RepositoryScopeRule()

RULES['desktop'] = DesktopScopeRule()

RULES['display'] = DisplayScopeRule()

RULES['session'] = SessionScopeRule()

RULES['workflow'] = WorkflowScopeRule()

RULES['job'] = JobScopeRule()

RULES['report'] = ReportScopeRule()

RULES['plugin'] = PluginScopeRule()

RULES['asset'] = AssetScopeRule()

RULES['safe_mode'] = SafeModePolicyRule()

RULES['standard_mode'] = StandardModePolicyRule()

RULES['advanced_mode'] = AdvancedModePolicyRule()

RULES['lab_mode'] = LabModePolicyRule()

RULES['privilege'] = PrivilegePolicyRule()

RULES['network'] = NetworkPolicyRule()

RULES['filesystem'] = FilesystemPolicyRule()

RULES['package'] = PackagePolicyRule()

RULES['service'] = ServicePolicyRule()

RULES['desktop'] = DesktopPolicyRule()

RULES['backup'] = BackupPolicyRule()

RULES['restore'] = RestorePolicyRule()

RULES['update'] = UpdatePolicyRule()

RULES['plugin'] = PluginPolicyRule()

RULES['api'] = ApiPolicyRule()

RULES['scheduler'] = SchedulerPolicyRule()

RULES['report'] = ReportPolicyRule()

RULES['export'] = ExportPolicyRule()

RULES['import'] = ImportPolicyRule()

RULES['release'] = ReleasePolicyRule()

RULES['chain'] = ChainAuditRule()

RULES['record'] = RecordAuditRule()

RULES['timestamp'] = TimestampAuditRule()

RULES['actor'] = ActorAuditRule()

RULES['consent'] = ConsentAuditRule()

RULES['scope'] = ScopeAuditRule()

RULES['command'] = CommandAuditRule()

RULES['result'] = ResultAuditRule()

RULES['error'] = ErrorAuditRule()

RULES['redaction'] = RedactionAuditRule()

RULES['rotation'] = RotationAuditRule()

RULES['retention'] = RetentionAuditRule()

RULES['export'] = ExportAuditRule()

RULES['verify'] = VerifyAuditRule()

RULES['signature'] = SignatureAuditRule()

RULES['key'] = KeyAuditRule()

RULES['checkpoint'] = CheckpointAuditRule()

RULES['replay'] = ReplayAuditRule()

RULES['diff'] = DiffAuditRule()

RULES['integrity'] = IntegrityAuditRule()

RULES['consent'] = ConsentControlRule()

RULES['rate'] = RateControlRule()

RULES['quota'] = QuotaControlRule()

RULES['timeout'] = TimeoutControlRule()

RULES['cancellation'] = CancellationControlRule()

RULES['panic'] = PanicControlRule()

RULES['lock'] = LockControlRule()

RULES['unlock'] = UnlockControlRule()

RULES['redaction'] = RedactionControlRule()

RULES['sandbox'] = SandboxControlRule()

RULES['isolation'] = IsolationControlRule()

RULES['resource'] = ResourceControlRule()

RULES['cpu'] = CpuControlRule()

RULES['memory'] = MemoryControlRule()

RULES['disk'] = DiskControlRule()

RULES['network'] = NetworkControlRule()

RULES['concurrency'] = ConcurrencyControlRule()

RULES['retry'] = RetryControlRule()

RULES['backoff'] = BackoffControlRule()

RULES['circuit'] = CircuitControlRule()

RULES['actor'] = ActorIdentityRule()

RULES['session'] = SessionIdentityRule()

RULES['token'] = TokenIdentityRule()

RULES['api_key'] = ApiKeyIdentityRule()

RULES['certificate'] = CertificateIdentityRule()

RULES['signature'] = SignatureIdentityRule()

RULES['role'] = RoleIdentityRule()

RULES['permission'] = PermissionIdentityRule()

RULES['capability'] = CapabilityIdentityRule()

RULES['plugin'] = PluginIdentityRule()

RULES['device'] = DeviceIdentityRule()

RULES['desktop'] = DesktopIdentityRule()

RULES['operator'] = OperatorIdentityRule()

RULES['ticket'] = TicketIdentityRule()

RULES['reason'] = ReasonIdentityRule()

RULES['approval'] = ApprovalIdentityRule()

RULES['reviewer'] = ReviewerIdentityRule()

RULES['owner'] = OwnerIdentityRule()

RULES['tenant'] = TenantIdentityRule()

RULES['environment'] = EnvironmentIdentityRule()

RULES['hash'] = HashIntegrityRule()

RULES['hmac'] = HmacIntegrityRule()

RULES['chain'] = ChainIntegrityRule()

RULES['manifest'] = ManifestIntegrityRule()

RULES['package'] = PackageIntegrityRule()

RULES['release'] = ReleaseIntegrityRule()

RULES['update'] = UpdateIntegrityRule()

RULES['plugin'] = PluginIntegrityRule()

RULES['asset'] = AssetIntegrityRule()

RULES['shader'] = ShaderIntegrityRule()

RULES['qml'] = QmlIntegrityRule()

RULES['theme'] = ThemeIntegrityRule()

RULES['database'] = DatabaseIntegrityRule()

RULES['migration'] = MigrationIntegrityRule()

RULES['backup'] = BackupIntegrityRule()

RULES['report'] = ReportIntegrityRule()

RULES['workflow'] = WorkflowIntegrityRule()

RULES['scope'] = ScopeIntegrityRule()

RULES['config'] = ConfigIntegrityRule()

RULES['secret'] = SecretIntegrityRule()

RULES['ip'] = IpPrivacyRule()

RULES['hostname'] = HostnamePrivacyRule()

RULES['username'] = UsernamePrivacyRule()

RULES['email'] = EmailPrivacyRule()

RULES['token'] = TokenPrivacyRule()

RULES['secret'] = SecretPrivacyRule()

RULES['password'] = PasswordPrivacyRule()

RULES['cookie'] = CookiePrivacyRule()

RULES['header'] = HeaderPrivacyRule()

RULES['query'] = QueryPrivacyRule()

RULES['path'] = PathPrivacyRule()

RULES['command'] = CommandPrivacyRule()

RULES['log'] = LogPrivacyRule()

RULES['report'] = ReportPrivacyRule()

RULES['backup'] = BackupPrivacyRule()

RULES['scope'] = ScopePrivacyRule()

RULES['target'] = TargetPrivacyRule()

RULES['audit'] = AuditPrivacyRule()

RULES['clipboard'] = ClipboardPrivacyRule()

RULES['environment'] = EnvironmentPrivacyRule()

class SecurityEngine:
    def __init__(self) -> None:
        self.rules = dict(RULES)
        self.decisions: list[SecurityDecision] = []
    def register(self, rule: SecurityRule) -> None:
        if rule.name in self.rules: raise SecurityError("duplicate rule")
        self.rules[rule.name] = rule
    def evaluate(self, name: str, value: Any, context: SecurityContext) -> SecurityDecision:
        if name not in self.rules: raise SecurityError(f"unknown rule: {name}")
        decision = self.rules[name].evaluate(value, context)
        self.decisions.append(decision)
        return decision
    def enforce(self, name: str, value: Any, context: SecurityContext) -> Any:
        return self.rules[name].enforce(value, context)
    def report(self) -> dict[str, Any]:
        return {"rules": len(self.rules), "decisions": [decision.__dict__ for decision in self.decisions]}

class EnvironmentExtendedRule(SecurityRule):
    family = 'extended'
    name = 'environment'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1000, "value_type": type(value).__name__})

class FilesystemAclExtendedRule(SecurityRule):
    family = 'extended'
    name = 'filesystem_acl'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1001, "value_type": type(value).__name__})

class FilesystemMountExtendedRule(SecurityRule):
    family = 'extended'
    name = 'filesystem_mount'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1002, "value_type": type(value).__name__})

class FilesystemLinkExtendedRule(SecurityRule):
    family = 'extended'
    name = 'filesystem_link'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1003, "value_type": type(value).__name__})

class NetworkRouteExtendedRule(SecurityRule):
    family = 'extended'
    name = 'network_route'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1004, "value_type": type(value).__name__})

class NetworkDnsExtendedRule(SecurityRule):
    family = 'extended'
    name = 'network_dns'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1005, "value_type": type(value).__name__})

class NetworkProxyExtendedRule(SecurityRule):
    family = 'extended'
    name = 'network_proxy'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1006, "value_type": type(value).__name__})

class NetworkTlsExtendedRule(SecurityRule):
    family = 'extended'
    name = 'network_tls'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1007, "value_type": type(value).__name__})

class PackageOriginExtendedRule(SecurityRule):
    family = 'extended'
    name = 'package_origin'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1008, "value_type": type(value).__name__})

class PackageVersionExtendedRule(SecurityRule):
    family = 'extended'
    name = 'package_version'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1009, "value_type": type(value).__name__})

class PackageLockExtendedRule(SecurityRule):
    family = 'extended'
    name = 'package_lock'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1010, "value_type": type(value).__name__})

class ServiceOwnerExtendedRule(SecurityRule):
    family = 'extended'
    name = 'service_owner'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1011, "value_type": type(value).__name__})

class ServiceGroupExtendedRule(SecurityRule):
    family = 'extended'
    name = 'service_group'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1012, "value_type": type(value).__name__})

class ServiceModeExtendedRule(SecurityRule):
    family = 'extended'
    name = 'service_mode'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1013, "value_type": type(value).__name__})

class DesktopSessionExtendedRule(SecurityRule):
    family = 'extended'
    name = 'desktop_session'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1014, "value_type": type(value).__name__})

class DesktopExtensionExtendedRule(SecurityRule):
    family = 'extended'
    name = 'desktop_extension'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1015, "value_type": type(value).__name__})

class DesktopThemeExtendedRule(SecurityRule):
    family = 'extended'
    name = 'desktop_theme'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1016, "value_type": type(value).__name__})

class PluginSignatureExtendedRule(SecurityRule):
    family = 'extended'
    name = 'plugin_signature'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1017, "value_type": type(value).__name__})

class PluginCapabilityExtendedRule(SecurityRule):
    family = 'extended'
    name = 'plugin_capability'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1018, "value_type": type(value).__name__})

class PluginOriginExtendedRule(SecurityRule):
    family = 'extended'
    name = 'plugin_origin'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1019, "value_type": type(value).__name__})

class WorkflowGraphExtendedRule(SecurityRule):
    family = 'extended'
    name = 'workflow_graph'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1020, "value_type": type(value).__name__})

class WorkflowVariableExtendedRule(SecurityRule):
    family = 'extended'
    name = 'workflow_variable'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1021, "value_type": type(value).__name__})

class WorkflowSecretExtendedRule(SecurityRule):
    family = 'extended'
    name = 'workflow_secret'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1022, "value_type": type(value).__name__})

class JobOwnerExtendedRule(SecurityRule):
    family = 'extended'
    name = 'job_owner'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1023, "value_type": type(value).__name__})

class JobPriorityExtendedRule(SecurityRule):
    family = 'extended'
    name = 'job_priority'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1024, "value_type": type(value).__name__})

class JobTimeoutExtendedRule(SecurityRule):
    family = 'extended'
    name = 'job_timeout'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1025, "value_type": type(value).__name__})

class JobOutputExtendedRule(SecurityRule):
    family = 'extended'
    name = 'job_output'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1026, "value_type": type(value).__name__})

class ReportOwnerExtendedRule(SecurityRule):
    family = 'extended'
    name = 'report_owner'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1027, "value_type": type(value).__name__})

class ReportDestinationExtendedRule(SecurityRule):
    family = 'extended'
    name = 'report_destination'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1028, "value_type": type(value).__name__})

class ReportFormatExtendedRule(SecurityRule):
    family = 'extended'
    name = 'report_format'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1029, "value_type": type(value).__name__})

class BackupOriginExtendedRule(SecurityRule):
    family = 'extended'
    name = 'backup_origin'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1030, "value_type": type(value).__name__})

class BackupDestinationExtendedRule(SecurityRule):
    family = 'extended'
    name = 'backup_destination'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1031, "value_type": type(value).__name__})

class BackupRetentionExtendedRule(SecurityRule):
    family = 'extended'
    name = 'backup_retention'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1032, "value_type": type(value).__name__})

class UpdateChannelExtendedRule(SecurityRule):
    family = 'extended'
    name = 'update_channel'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1033, "value_type": type(value).__name__})

class UpdateSignatureExtendedRule(SecurityRule):
    family = 'extended'
    name = 'update_signature'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1034, "value_type": type(value).__name__})

class UpdateRollbackExtendedRule(SecurityRule):
    family = 'extended'
    name = 'update_rollback'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1035, "value_type": type(value).__name__})

class ReleaseArtifactExtendedRule(SecurityRule):
    family = 'extended'
    name = 'release_artifact'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1036, "value_type": type(value).__name__})

class ReleaseManifestExtendedRule(SecurityRule):
    family = 'extended'
    name = 'release_manifest'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1037, "value_type": type(value).__name__})

class ReleaseTargetExtendedRule(SecurityRule):
    family = 'extended'
    name = 'release_target'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1038, "value_type": type(value).__name__})

class ReleaseApprovalExtendedRule(SecurityRule):
    family = 'extended'
    name = 'release_approval'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1039, "value_type": type(value).__name__})

for _extended_rule in [
    EnvironmentExtendedRule(),
    FilesystemAclExtendedRule(),
    FilesystemMountExtendedRule(),
    FilesystemLinkExtendedRule(),
    NetworkRouteExtendedRule(),
    NetworkDnsExtendedRule(),
    NetworkProxyExtendedRule(),
    NetworkTlsExtendedRule(),
    PackageOriginExtendedRule(),
    PackageVersionExtendedRule(),
    PackageLockExtendedRule(),
    ServiceOwnerExtendedRule(),
    ServiceGroupExtendedRule(),
    ServiceModeExtendedRule(),
    DesktopSessionExtendedRule(),
    DesktopExtensionExtendedRule(),
    DesktopThemeExtendedRule(),
    PluginSignatureExtendedRule(),
    PluginCapabilityExtendedRule(),
    PluginOriginExtendedRule(),
    WorkflowGraphExtendedRule(),
    WorkflowVariableExtendedRule(),
    WorkflowSecretExtendedRule(),
    JobOwnerExtendedRule(),
    JobPriorityExtendedRule(),
    JobTimeoutExtendedRule(),
    JobOutputExtendedRule(),
    ReportOwnerExtendedRule(),
    ReportDestinationExtendedRule(),
    ReportFormatExtendedRule(),
    BackupOriginExtendedRule(),
    BackupDestinationExtendedRule(),
    BackupRetentionExtendedRule(),
    UpdateChannelExtendedRule(),
    UpdateSignatureExtendedRule(),
    UpdateRollbackExtendedRule(),
    ReleaseArtifactExtendedRule(),
    ReleaseManifestExtendedRule(),
    ReleaseTargetExtendedRule(),
    ReleaseApprovalExtendedRule(),
]:
    RULES[_extended_rule.name] = _extended_rule

class EnvironmentExtendedRule(SecurityRule):
    family = 'extended'
    name = 'environment'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1000, "value_type": type(value).__name__})

class FilesystemAclExtendedRule(SecurityRule):
    family = 'extended'
    name = 'filesystem_acl'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1001, "value_type": type(value).__name__})

class FilesystemMountExtendedRule(SecurityRule):
    family = 'extended'
    name = 'filesystem_mount'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1002, "value_type": type(value).__name__})

class FilesystemLinkExtendedRule(SecurityRule):
    family = 'extended'
    name = 'filesystem_link'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1003, "value_type": type(value).__name__})

class NetworkRouteExtendedRule(SecurityRule):
    family = 'extended'
    name = 'network_route'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1004, "value_type": type(value).__name__})

class NetworkDnsExtendedRule(SecurityRule):
    family = 'extended'
    name = 'network_dns'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1005, "value_type": type(value).__name__})

class NetworkProxyExtendedRule(SecurityRule):
    family = 'extended'
    name = 'network_proxy'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1006, "value_type": type(value).__name__})

class NetworkTlsExtendedRule(SecurityRule):
    family = 'extended'
    name = 'network_tls'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1007, "value_type": type(value).__name__})

class PackageOriginExtendedRule(SecurityRule):
    family = 'extended'
    name = 'package_origin'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1008, "value_type": type(value).__name__})

class PackageVersionExtendedRule(SecurityRule):
    family = 'extended'
    name = 'package_version'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1009, "value_type": type(value).__name__})

class PackageLockExtendedRule(SecurityRule):
    family = 'extended'
    name = 'package_lock'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1010, "value_type": type(value).__name__})

class ServiceOwnerExtendedRule(SecurityRule):
    family = 'extended'
    name = 'service_owner'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1011, "value_type": type(value).__name__})

class ServiceGroupExtendedRule(SecurityRule):
    family = 'extended'
    name = 'service_group'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1012, "value_type": type(value).__name__})

class ServiceModeExtendedRule(SecurityRule):
    family = 'extended'
    name = 'service_mode'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1013, "value_type": type(value).__name__})

class DesktopSessionExtendedRule(SecurityRule):
    family = 'extended'
    name = 'desktop_session'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1014, "value_type": type(value).__name__})

class DesktopExtensionExtendedRule(SecurityRule):
    family = 'extended'
    name = 'desktop_extension'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1015, "value_type": type(value).__name__})

class DesktopThemeExtendedRule(SecurityRule):
    family = 'extended'
    name = 'desktop_theme'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1016, "value_type": type(value).__name__})

class PluginSignatureExtendedRule(SecurityRule):
    family = 'extended'
    name = 'plugin_signature'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1017, "value_type": type(value).__name__})

class PluginCapabilityExtendedRule(SecurityRule):
    family = 'extended'
    name = 'plugin_capability'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1018, "value_type": type(value).__name__})

class PluginOriginExtendedRule(SecurityRule):
    family = 'extended'
    name = 'plugin_origin'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1019, "value_type": type(value).__name__})

class WorkflowGraphExtendedRule(SecurityRule):
    family = 'extended'
    name = 'workflow_graph'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1020, "value_type": type(value).__name__})

class WorkflowVariableExtendedRule(SecurityRule):
    family = 'extended'
    name = 'workflow_variable'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1021, "value_type": type(value).__name__})

class WorkflowSecretExtendedRule(SecurityRule):
    family = 'extended'
    name = 'workflow_secret'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1022, "value_type": type(value).__name__})

class JobOwnerExtendedRule(SecurityRule):
    family = 'extended'
    name = 'job_owner'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1023, "value_type": type(value).__name__})

class JobPriorityExtendedRule(SecurityRule):
    family = 'extended'
    name = 'job_priority'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1024, "value_type": type(value).__name__})

class JobTimeoutExtendedRule(SecurityRule):
    family = 'extended'
    name = 'job_timeout'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1025, "value_type": type(value).__name__})

class JobOutputExtendedRule(SecurityRule):
    family = 'extended'
    name = 'job_output'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1026, "value_type": type(value).__name__})

class ReportOwnerExtendedRule(SecurityRule):
    family = 'extended'
    name = 'report_owner'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1027, "value_type": type(value).__name__})

class ReportDestinationExtendedRule(SecurityRule):
    family = 'extended'
    name = 'report_destination'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1028, "value_type": type(value).__name__})

class ReportFormatExtendedRule(SecurityRule):
    family = 'extended'
    name = 'report_format'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1029, "value_type": type(value).__name__})

class BackupOriginExtendedRule(SecurityRule):
    family = 'extended'
    name = 'backup_origin'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1030, "value_type": type(value).__name__})

class BackupDestinationExtendedRule(SecurityRule):
    family = 'extended'
    name = 'backup_destination'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1031, "value_type": type(value).__name__})

class BackupRetentionExtendedRule(SecurityRule):
    family = 'extended'
    name = 'backup_retention'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1032, "value_type": type(value).__name__})

class UpdateChannelExtendedRule(SecurityRule):
    family = 'extended'
    name = 'update_channel'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1033, "value_type": type(value).__name__})

class UpdateSignatureExtendedRule(SecurityRule):
    family = 'extended'
    name = 'update_signature'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1034, "value_type": type(value).__name__})

class UpdateRollbackExtendedRule(SecurityRule):
    family = 'extended'
    name = 'update_rollback'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1035, "value_type": type(value).__name__})

class ReleaseArtifactExtendedRule(SecurityRule):
    family = 'extended'
    name = 'release_artifact'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1036, "value_type": type(value).__name__})

class ReleaseManifestExtendedRule(SecurityRule):
    family = 'extended'
    name = 'release_manifest'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1037, "value_type": type(value).__name__})

class ReleaseTargetExtendedRule(SecurityRule):
    family = 'extended'
    name = 'release_target'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1038, "value_type": type(value).__name__})

class ReleaseApprovalExtendedRule(SecurityRule):
    family = 'extended'
    name = 'release_approval'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1039, "value_type": type(value).__name__})

class CredentialSourceExtendedRule(SecurityRule):
    family = 'extended'
    name = 'credential_source'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1040, "value_type": type(value).__name__})

class CredentialRotationExtendedRule(SecurityRule):
    family = 'extended'
    name = 'credential_rotation'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1041, "value_type": type(value).__name__})

class CredentialExpiryExtendedRule(SecurityRule):
    family = 'extended'
    name = 'credential_expiry'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1042, "value_type": type(value).__name__})

class AuditExportExtendedRule(SecurityRule):
    family = 'extended'
    name = 'audit_export'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1043, "value_type": type(value).__name__})

class AuditReplayExtendedRule(SecurityRule):
    family = 'extended'
    name = 'audit_replay'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1044, "value_type": type(value).__name__})

class AuditDiffExtendedRule(SecurityRule):
    family = 'extended'
    name = 'audit_diff'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1045, "value_type": type(value).__name__})

class ScopeInheritanceExtendedRule(SecurityRule):
    family = 'extended'
    name = 'scope_inheritance'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1046, "value_type": type(value).__name__})

class ScopeExpiryExtendedRule(SecurityRule):
    family = 'extended'
    name = 'scope_expiry'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1047, "value_type": type(value).__name__})

class ConsentExpiryExtendedRule(SecurityRule):
    family = 'extended'
    name = 'consent_expiry'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1048, "value_type": type(value).__name__})

class PanicStateExtendedRule(SecurityRule):
    family = 'extended'
    name = 'panic_state'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1049, "value_type": type(value).__name__})

class RateWindowExtendedRule(SecurityRule):
    family = 'extended'
    name = 'rate_window'
    risk = "high"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if context.mode == "safe" and not context.consent:
            return SecurityDecision(self.name, False, "explicit consent required", self.risk, {})
        return SecurityDecision(self.name, True, "extended rule passed", self.risk, {"sequence": 1050, "value_type": type(value).__name__})

for _extended_rule in [
    EnvironmentExtendedRule(),
    FilesystemAclExtendedRule(),
    FilesystemMountExtendedRule(),
    FilesystemLinkExtendedRule(),
    NetworkRouteExtendedRule(),
    NetworkDnsExtendedRule(),
    NetworkProxyExtendedRule(),
    NetworkTlsExtendedRule(),
    PackageOriginExtendedRule(),
    PackageVersionExtendedRule(),
    PackageLockExtendedRule(),
    ServiceOwnerExtendedRule(),
    ServiceGroupExtendedRule(),
    ServiceModeExtendedRule(),
    DesktopSessionExtendedRule(),
    DesktopExtensionExtendedRule(),
    DesktopThemeExtendedRule(),
    PluginSignatureExtendedRule(),
    PluginCapabilityExtendedRule(),
    PluginOriginExtendedRule(),
    WorkflowGraphExtendedRule(),
    WorkflowVariableExtendedRule(),
    WorkflowSecretExtendedRule(),
    JobOwnerExtendedRule(),
    JobPriorityExtendedRule(),
    JobTimeoutExtendedRule(),
    JobOutputExtendedRule(),
    ReportOwnerExtendedRule(),
    ReportDestinationExtendedRule(),
    ReportFormatExtendedRule(),
    BackupOriginExtendedRule(),
    BackupDestinationExtendedRule(),
    BackupRetentionExtendedRule(),
    UpdateChannelExtendedRule(),
    UpdateSignatureExtendedRule(),
    UpdateRollbackExtendedRule(),
    ReleaseArtifactExtendedRule(),
    ReleaseManifestExtendedRule(),
    ReleaseTargetExtendedRule(),
    ReleaseApprovalExtendedRule(),
    CredentialSourceExtendedRule(),
    CredentialRotationExtendedRule(),
    CredentialExpiryExtendedRule(),
    AuditExportExtendedRule(),
    AuditReplayExtendedRule(),
    AuditDiffExtendedRule(),
    ScopeInheritanceExtendedRule(),
    ScopeExpiryExtendedRule(),
    ConsentExpiryExtendedRule(),
    PanicStateExtendedRule(),
    RateWindowExtendedRule(),
]:
    RULES[_extended_rule.name] = _extended_rule


class CredentialFormatCatalogRule(SecurityRule):
    family = "catalog"
    name = 'credential_format'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2000})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2000, "value": repr(value)})

class CredentialScopeCatalogRule(SecurityRule):
    family = "catalog"
    name = 'credential_scope'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2001})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2001, "value": repr(value)})

class CredentialOwnerCatalogRule(SecurityRule):
    family = "catalog"
    name = 'credential_owner'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2002})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2002, "value": repr(value)})

class CredentialUsageCatalogRule(SecurityRule):
    family = "catalog"
    name = 'credential_usage'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2003})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2003, "value": repr(value)})

class CredentialBackupCatalogRule(SecurityRule):
    family = "catalog"
    name = 'credential_backup'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2004})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2004, "value": repr(value)})

class CredentialRestoreCatalogRule(SecurityRule):
    family = "catalog"
    name = 'credential_restore'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2005})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2005, "value": repr(value)})

class CredentialExportCatalogRule(SecurityRule):
    family = "catalog"
    name = 'credential_export'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2006})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2006, "value": repr(value)})

class CredentialImportCatalogRule(SecurityRule):
    family = "catalog"
    name = 'credential_import'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2007})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2007, "value": repr(value)})

class AuditOwnerCatalogRule(SecurityRule):
    family = "catalog"
    name = 'audit_owner'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2008})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2008, "value": repr(value)})

class AuditScopeCatalogRule(SecurityRule):
    family = "catalog"
    name = 'audit_scope'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2009})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2009, "value": repr(value)})

class AuditFormatCatalogRule(SecurityRule):
    family = "catalog"
    name = 'audit_format'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2010})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2010, "value": repr(value)})

class AuditDestinationCatalogRule(SecurityRule):
    family = "catalog"
    name = 'audit_destination'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2011})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2011, "value": repr(value)})

class AuditBackupCatalogRule(SecurityRule):
    family = "catalog"
    name = 'audit_backup'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2012})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2012, "value": repr(value)})

class AuditRestoreCatalogRule(SecurityRule):
    family = "catalog"
    name = 'audit_restore'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2013})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2013, "value": repr(value)})

class AuditRotationCatalogRule(SecurityRule):
    family = "catalog"
    name = 'audit_rotation'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2014})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2014, "value": repr(value)})

class ScopeFormatCatalogRule(SecurityRule):
    family = "catalog"
    name = 'scope_format'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2015})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2015, "value": repr(value)})

class ScopeOwnerCatalogRule(SecurityRule):
    family = "catalog"
    name = 'scope_owner'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2016})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2016, "value": repr(value)})

class ScopeTargetCatalogRule(SecurityRule):
    family = "catalog"
    name = 'scope_target'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2017})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2017, "value": repr(value)})

class ScopeServiceCatalogRule(SecurityRule):
    family = "catalog"
    name = 'scope_service'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2018})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2018, "value": repr(value)})

class ScopeChangeCatalogRule(SecurityRule):
    family = "catalog"
    name = 'scope_change'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2019})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2019, "value": repr(value)})

class ConsentActorCatalogRule(SecurityRule):
    family = "catalog"
    name = 'consent_actor'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2020})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2020, "value": repr(value)})

class ConsentReasonCatalogRule(SecurityRule):
    family = "catalog"
    name = 'consent_reason'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2021})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2021, "value": repr(value)})

class ConsentTicketCatalogRule(SecurityRule):
    family = "catalog"
    name = 'consent_ticket'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2022})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2022, "value": repr(value)})

class ConsentDurationCatalogRule(SecurityRule):
    family = "catalog"
    name = 'consent_duration'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2023})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2023, "value": repr(value)})

class ConsentModeCatalogRule(SecurityRule):
    family = "catalog"
    name = 'consent_mode'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2024})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2024, "value": repr(value)})

class PanicActorCatalogRule(SecurityRule):
    family = "catalog"
    name = 'panic_actor'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2025})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2025, "value": repr(value)})

class PanicReasonCatalogRule(SecurityRule):
    family = "catalog"
    name = 'panic_reason'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2026})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2026, "value": repr(value)})

class PanicTimestampCatalogRule(SecurityRule):
    family = "catalog"
    name = 'panic_timestamp'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2027})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2027, "value": repr(value)})

class PanicScopeCatalogRule(SecurityRule):
    family = "catalog"
    name = 'panic_scope'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2028})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2028, "value": repr(value)})

class PanicRecoveryCatalogRule(SecurityRule):
    family = "catalog"
    name = 'panic_recovery'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2029})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2029, "value": repr(value)})

class RateActorCatalogRule(SecurityRule):
    family = "catalog"
    name = 'rate_actor'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2030})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2030, "value": repr(value)})

class RateOperationCatalogRule(SecurityRule):
    family = "catalog"
    name = 'rate_operation'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2031})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2031, "value": repr(value)})

class RateResourceCatalogRule(SecurityRule):
    family = "catalog"
    name = 'rate_resource'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2032})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2032, "value": repr(value)})

class RatePriorityCatalogRule(SecurityRule):
    family = "catalog"
    name = 'rate_priority'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2033})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2033, "value": repr(value)})

class RateRetryCatalogRule(SecurityRule):
    family = "catalog"
    name = 'rate_retry'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2034})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2034, "value": repr(value)})

class RateBackoffCatalogRule(SecurityRule):
    family = "catalog"
    name = 'rate_backoff'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2035})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2035, "value": repr(value)})

class QuotaActorCatalogRule(SecurityRule):
    family = "catalog"
    name = 'quota_actor'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2036})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2036, "value": repr(value)})

class QuotaOperationCatalogRule(SecurityRule):
    family = "catalog"
    name = 'quota_operation'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2037})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2037, "value": repr(value)})

class QuotaResourceCatalogRule(SecurityRule):
    family = "catalog"
    name = 'quota_resource'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2038})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2038, "value": repr(value)})

class QuotaWindowCatalogRule(SecurityRule):
    family = "catalog"
    name = 'quota_window'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2039})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2039, "value": repr(value)})

class QuotaResetCatalogRule(SecurityRule):
    family = "catalog"
    name = 'quota_reset'
    risk = "medium"
    def evaluate(self, value: Any, context: SecurityContext) -> SecurityDecision:
        base = super().evaluate(value, context)
        if not base.allowed: return base
        if not context.consent and context.mode in {"safe", "standard"}:
            return SecurityDecision(self.name, False, "consent required", self.risk, {"sequence": 2040})
        return SecurityDecision(self.name, True, "catalog rule passed", self.risk, {"sequence": 2040, "value": repr(value)})

for _catalog_rule in [
    CredentialFormatCatalogRule(),
    CredentialScopeCatalogRule(),
    CredentialOwnerCatalogRule(),
    CredentialUsageCatalogRule(),
    CredentialBackupCatalogRule(),
    CredentialRestoreCatalogRule(),
    CredentialExportCatalogRule(),
    CredentialImportCatalogRule(),
    AuditOwnerCatalogRule(),
    AuditScopeCatalogRule(),
    AuditFormatCatalogRule(),
    AuditDestinationCatalogRule(),
    AuditBackupCatalogRule(),
    AuditRestoreCatalogRule(),
    AuditRotationCatalogRule(),
    ScopeFormatCatalogRule(),
    ScopeOwnerCatalogRule(),
    ScopeTargetCatalogRule(),
    ScopeServiceCatalogRule(),
    ScopeChangeCatalogRule(),
    ConsentActorCatalogRule(),
    ConsentReasonCatalogRule(),
    ConsentTicketCatalogRule(),
    ConsentDurationCatalogRule(),
    ConsentModeCatalogRule(),
    PanicActorCatalogRule(),
    PanicReasonCatalogRule(),
    PanicTimestampCatalogRule(),
    PanicScopeCatalogRule(),
    PanicRecoveryCatalogRule(),
    RateActorCatalogRule(),
    RateOperationCatalogRule(),
    RateResourceCatalogRule(),
    RatePriorityCatalogRule(),
    RateRetryCatalogRule(),
    RateBackoffCatalogRule(),
    QuotaActorCatalogRule(),
    QuotaOperationCatalogRule(),
    QuotaResourceCatalogRule(),
    QuotaWindowCatalogRule(),
    QuotaResetCatalogRule(),
]:
    RULES[_catalog_rule.name] = _catalog_rule

# Scope authority must win over duplicate metadata names.
RULES["target"] = TargetScopeRule()
