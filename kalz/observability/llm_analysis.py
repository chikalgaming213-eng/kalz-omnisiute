from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from kalz.integrations.openai_agents import AgentConfig, AgentToolRegistry, OpenAIAgent
from kalz.observability.logging import DistributedLogStore, LogEvent


@dataclass(frozen=True)
class LogAnalysis:
    summary: str
    severity: str
    likely_causes: tuple[str, ...]
    recommended_actions: tuple[str, ...]
    event_count: int
    used_llm: bool


class LogAnalysisService:
    """Builds a bounded, redacted log context and delegates analysis to an allowlisted agent."""

    def __init__(self, store: DistributedLogStore, agent: OpenAIAgent | None = None, max_events: int = 50) -> None:
        self.store = store
        self.max_events = max_events
        self.agent = agent or self._build_agent()

    def _build_agent(self) -> OpenAIAgent:
        registry = AgentToolRegistry()
        registry.register("observability_snapshot", self.snapshot)
        return OpenAIAgent(
            AgentConfig(
                name="kalz-observability-analyzer",
                instructions="Analyze redacted structured logs. Do not invent facts. Return severity, causes, and safe actions.",
                tool_names=("observability_snapshot",),
                max_turns=4,
            ),
            registry,
        )

    def snapshot(self) -> dict[str, Any]:
        events = self.store.query()
        return {"count": len(events), "events": [self._safe_event(event) for event in events[-self.max_events:]]}

    @staticmethod
    def _safe_event(event: LogEvent) -> dict[str, Any]:
        sensitive = {"token", "password", "secret", "authorization", "api_key", "cookie"}
        fields = {key: "[REDACTED]" if key.lower() in sensitive else value for key, value in event.fields.items()}
        return {"event_id": event.event_id, "level": event.level, "message": event.message[:2048], "service": event.service, "timestamp": event.timestamp, "trace_id": event.trace_id, "fields": fields}

    def build_prompt(self) -> str:
        return "Analyze this observability snapshot and return concise JSON with summary, severity, likely_causes, recommended_actions.\n" + json.dumps(self.snapshot(), sort_keys=True, default=str)

    def analyze(self) -> LogAnalysis:
        snapshot = self.snapshot()
        if not snapshot["events"]:
            return LogAnalysis("No events available", "info", (), ("Continue monitoring",), 0, False)
        try:
            result = self.agent.run(self.build_prompt())
            return LogAnalysis(result.text, "unknown", (), (), snapshot["count"], True)
        except Exception:
            errors = sum(1 for event in snapshot["events"] if event["level"] in {"error", "critical"})
            severity = "critical" if errors >= 5 else "warning" if errors else "info"
            return LogAnalysis(f"{errors} error-level events detected", severity, (), ("Inspect correlated trace IDs", "Review recent deployments"), snapshot["count"], False)
