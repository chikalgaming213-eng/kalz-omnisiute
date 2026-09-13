from __future__ import annotations

import asyncio
from collections import defaultdict
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any


@dataclass(frozen=True)
class Event:
    topic: str
    payload: dict[str, Any]
    timestamp: str


Handler = Callable[[Event], Awaitable[None]]


class EventBus:
    def __init__(self) -> None:
        self._handlers: dict[str, list[Handler]] = defaultdict(list)

    def subscribe(self, topic: str, handler: Handler) -> None:
        self._handlers[topic].append(handler)

    def unsubscribe(self, topic: str, handler: Handler) -> None:
        if handler in self._handlers.get(topic, []):
            self._handlers[topic].remove(handler)

    async def publish(self, topic: str, payload: dict[str, Any]) -> Event:
        event = Event(topic, payload, datetime.now(UTC).isoformat())
        handlers = [*self._handlers.get(topic, []), *self._handlers.get("*", [])]
        if handlers:
            await asyncio.gather(*(handler(event) for handler in handlers))
        return event
