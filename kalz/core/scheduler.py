from __future__ import annotations

import asyncio
from dataclasses import dataclass
from datetime import datetime, timedelta, UTC
from collections.abc import Awaitable, Callable

@dataclass(frozen=True)
class Schedule:
    name: str
    interval_seconds: int

class Scheduler:
    def __init__(self) -> None:
        self.tasks: dict[str, asyncio.Task[None]] = {}
    def add(self, schedule: Schedule, callback: Callable[[], Awaitable[None]]) -> None:
        async def loop() -> None:
            while True:
                await callback()
                await asyncio.sleep(schedule.interval_seconds)
        self.tasks[schedule.name] = asyncio.create_task(loop())
    def cancel(self, name: str) -> None:
        task = self.tasks.pop(name, None)
        if task: task.cancel()
    async def shutdown(self) -> None:
        for task in self.tasks.values(): task.cancel()
        if self.tasks: await asyncio.gather(*self.tasks.values(), return_exceptions=True)
        self.tasks.clear()
