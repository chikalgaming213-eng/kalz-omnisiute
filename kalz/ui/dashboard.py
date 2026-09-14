from __future__ import annotations

import platform
import time
from dataclasses import dataclass, asdict
from typing import Any

from kalz.defense.engine import DefenseEngine
from kalz.gateway.gateway import APIGateway
from kalz.observability.logging import DistributedLogStore
from kalz.observability.metrics import MetricsStore


@dataclass(frozen=True)
class DashboardSnapshot:
    application: str
    version: str
    platform: str
    python: str
    gateway_backends: int
    gateway_requests: int
    log_events: int
    metric_samples: int
    defense_rules: int
    defense_events: int
    generated_at: float

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class DashboardService:
    """Read-only GUI facade; it never executes privileged operations."""

    def __init__(self, metrics: MetricsStore | None = None, logs: DistributedLogStore | None = None, gateway: APIGateway | None = None, defense: DefenseEngine | None = None) -> None:
        self.metrics = metrics or MetricsStore()
        self.logs = logs or DistributedLogStore()
        self.gateway = gateway or APIGateway()
        self.defense = defense or DefenseEngine()

    def snapshot(self) -> DashboardSnapshot:
        return DashboardSnapshot(
            application="Kalz OmniSuite",
            version="0.1.0",
            platform=platform.platform(),
            python=platform.python_version(),
            gateway_backends=len(self.gateway.backends),
            gateway_requests=self.gateway.requests,
            log_events=len(self.logs.query()),
            metric_samples=len(self.metrics.query()),
            defense_rules=len(self.defense.rules),
            defense_events=len(self.defense.events),
            generated_at=time.time(),
        )

    def status_text(self) -> str:
        data = self.snapshot()
        return f"{data.application} {data.version} · {data.platform} · logs={data.log_events} metrics={data.metric_samples} defense={data.defense_rules}"
