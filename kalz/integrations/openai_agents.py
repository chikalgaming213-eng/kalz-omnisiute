from __future__ import annotations

import inspect
import os
from dataclasses import dataclass
from typing import Any, Awaitable, Callable

from .openai_client import OpenAIConfigurationError


class AgentConfigurationError(RuntimeError):
    """Raised when the Agents SDK or agent configuration is unavailable."""


@dataclass(frozen=True)
class AgentConfig:
    name: str = "kalz-agent"
    instructions: str = "You are a safe operations assistant. Use only approved tools."
    model: str = "gpt-4.1-mini"
    max_turns: int = 8
    tool_names: tuple[str, ...] = ()


@dataclass(frozen=True)
class AgentResult:
    text: str
    turns: int
    tools_used: tuple[str, ...]


class AgentToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Callable[..., Any]] = {}

    def register(self, name: str, function: Callable[..., Any]) -> None:
        if not name or not name.replace("_", "").isalnum():
            raise ValueError("tool name must be alphanumeric with underscores")
        if name in self._tools:
            raise ValueError(f"duplicate tool: {name}")
        self._tools[name] = function

    def allow(self, names: tuple[str, ...]) -> dict[str, Callable[..., Any]]:
        unknown = set(names) - self._tools.keys()
        if unknown:
            raise AgentConfigurationError(f"unknown agent tools: {sorted(unknown)}")
        return {name: self._tools[name] for name in names}

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._tools))


class OpenAIAgent:
    """Optional OpenAI Agents SDK facade with explicit tool allowlisting."""

    def __init__(self, config: AgentConfig | None = None, registry: AgentToolRegistry | None = None) -> None:
        self.config = config or AgentConfig()
        self.registry = registry or AgentToolRegistry()

    def _sdk(self) -> tuple[Any, Any, Any]:
        try:
            from agents import Agent, Runner, function_tool
        except ImportError as exc:
            raise AgentConfigurationError("install openai-agents to enable agent mode") from exc
        return Agent, Runner, function_tool

    def build(self) -> Any:
        Agent, _, function_tool = self._sdk()
        approved = self.registry.allow(self.config.tool_names)
        tools = []
        for name, function in approved.items():
            wrapped = function_tool(function)
            tools.append(wrapped)
        kwargs = {"name": self.config.name, "instructions": self.config.instructions, "model": self.config.model}
        if tools:
            kwargs["tools"] = tools
        return Agent(**kwargs)

    async def run_async(self, prompt: str) -> AgentResult:
        if not prompt.strip():
            raise ValueError("prompt must not be empty")
        _, Runner, _ = self._sdk()
        agent = self.build()
        result = await Runner.run(agent, prompt, max_turns=self.config.max_turns)
        text = getattr(result, "final_output", "") or ""
        tools = tuple(getattr(item, "name", "") for item in getattr(result, "new_items", []) if getattr(item, "name", ""))
        return AgentResult(text=text, turns=self.config.max_turns, tools_used=tools)

    def run(self, prompt: str) -> AgentResult:
        import asyncio
        return asyncio.run(self.run_async(prompt))

    def health(self) -> dict[str, Any]:
        return {"name": self.config.name, "model": self.config.model, "max_turns": self.config.max_turns, "tools": self.registry.names(), "api_key_configured": bool(os.getenv("OPENAI_API_KEY"))}
