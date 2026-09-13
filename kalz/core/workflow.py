from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from kalz.core.runner import SecureRunner, RunResult

@dataclass(frozen=True)
class WorkflowStep:
    name: str
    argv: tuple[str, ...]

class WorkflowEngine:
    def __init__(self, runner: SecureRunner) -> None:
        self.runner = runner
    async def execute(self, workflow_id: str, steps: list[WorkflowStep], *, dry_run: bool = True) -> list[RunResult]:
        results: list[RunResult] = []
        for index, step in enumerate(steps):
            result = await self.runner.run(f'{workflow_id}:{index}', step.argv, dry_run=dry_run)
            results.append(result)
            if result.returncode != 0:
                break
        return results
