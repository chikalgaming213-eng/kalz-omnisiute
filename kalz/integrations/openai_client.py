from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass, field
from typing import Any, Iterable


class OpenAIConfigurationError(RuntimeError):
    """Raised when OpenAI integration configuration is missing or unsafe."""


class OpenAIRequestError(RuntimeError):
    """Raised when an OpenAI request fails after retry policy is exhausted."""


@dataclass(frozen=True)
class OpenAIConfig:
    api_key: str
    model: str = "gpt-4.1-mini"
    base_url: str | None = None
    timeout: float = 60.0
    max_retries: int = 2
    organization: str | None = None
    project: str | None = None

    @classmethod
    def from_environment(cls) -> "OpenAIConfig":
        api_key = os.getenv("OPENAI_API_KEY", "").strip()
        if not api_key:
            raise OpenAIConfigurationError("OPENAI_API_KEY is not configured")
        if "\n" in api_key or "\r" in api_key:
            raise OpenAIConfigurationError("OPENAI_API_KEY contains a newline")
        return cls(
            api_key=api_key,
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            base_url=os.getenv("OPENAI_API_BASE") or None,
            timeout=float(os.getenv("OPENAI_TIMEOUT", "60")),
            max_retries=int(os.getenv("OPENAI_MAX_RETRIES", "2")),
            organization=os.getenv("OPENAI_ORGANIZATION") or None,
            project=os.getenv("OPENAI_PROJECT") or None,
        )

    def redacted(self) -> dict[str, Any]:
        return {
            "model": self.model,
            "base_url": self.base_url,
            "timeout": self.timeout,
            "max_retries": self.max_retries,
            "organization": self.organization,
            "project": self.project,
            "api_key_configured": bool(self.api_key),
            "api_key_fingerprint": self.api_key[-4:] if len(self.api_key) >= 4 else "***",
        }


@dataclass(frozen=True)
class ChatMessage:
    role: str
    content: str


@dataclass(frozen=True)
class OpenAIResponse:
    text: str
    model: str
    response_id: str | None
    usage: dict[str, Any] = field(default_factory=dict)
    raw: Any = None


class OpenAIClient:
    """Small, dependency-optional client facade for the OpenAI Responses API."""

    def __init__(self, config: OpenAIConfig | None = None, client: Any = None) -> None:
        self.config = config or OpenAIConfig.from_environment()
        self._client = client
        self.request_count = 0
        self.failure_count = 0

    def _client_or_create(self) -> Any:
        if self._client is not None:
            return self._client
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise OpenAIConfigurationError("install the openai package to enable OpenAI integration") from exc
        kwargs: dict[str, Any] = {"api_key": self.config.api_key, "timeout": self.config.timeout, "max_retries": 0}
        if self.config.base_url:
            kwargs["base_url"] = self.config.base_url
        if self.config.organization:
            kwargs["organization"] = self.config.organization
        if self.config.project:
            kwargs["project"] = self.config.project
        self._client = OpenAI(**kwargs)
        return self._client

    @staticmethod
    def _input(messages: Iterable[ChatMessage]) -> list[dict[str, str]]:
        allowed = {"system", "developer", "user", "assistant"}
        result = []
        for message in messages:
            if message.role not in allowed:
                raise ValueError(f"unsupported message role: {message.role}")
            if not isinstance(message.content, str):
                raise TypeError("message content must be text")
            result.append({"role": message.role, "content": message.content})
        if not result:
            raise ValueError("at least one message is required")
        return result

    def responses(self, messages: Iterable[ChatMessage], *, model: str | None = None, **kwargs: Any) -> OpenAIResponse:
        payload = self._input(messages)
        selected_model = model or self.config.model
        last_error: Exception | None = None
        for attempt in range(self.config.max_retries + 1):
            try:
                self.request_count += 1
                response = self._client_or_create().responses.create(model=selected_model, input=payload, **kwargs)
                text = getattr(response, "output_text", "") or self._extract_text(response)
                usage = self._to_dict(getattr(response, "usage", None))
                return OpenAIResponse(text, selected_model, getattr(response, "id", None), usage, response)
            except Exception as exc:
                self.failure_count += 1
                last_error = exc
                if attempt < self.config.max_retries:
                    time.sleep(min(2 ** attempt, 4))
        raise OpenAIRequestError(f"OpenAI request failed after retries: {last_error}") from last_error

    @staticmethod
    def _extract_text(response: Any) -> str:
        chunks: list[str] = []
        for item in getattr(response, "output", []) or []:
            for content in getattr(item, "content", []) or []:
                text = getattr(content, "text", None)
                if text:
                    chunks.append(text)
        return "".join(chunks)

    @staticmethod
    def _to_dict(value: Any) -> dict[str, Any]:
        if value is None:
            return {}
        if isinstance(value, dict):
            return value
        if hasattr(value, "model_dump"):
            return value.model_dump()
        return {key: getattr(value, key) for key in ("input_tokens", "output_tokens", "total_tokens") if hasattr(value, key)}

    def health(self) -> dict[str, Any]:
        return {"configured": bool(self.config.api_key), "requests": self.request_count, "failures": self.failure_count, "config": self.config.redacted()}


def build_client() -> OpenAIClient:
    return OpenAIClient(OpenAIConfig.from_environment())
