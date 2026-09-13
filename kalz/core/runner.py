from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Sequence

from kalz.events.bus import EventBus
from kalz.security.audit import AuditChain

@dataclass(frozen=True)
class RunResult:
    argv: tuple[str, ...]
    returncode: int
    output: str
    dry_run: bool

class SecureRunner:
    def __init__(self, bus: EventBus, audit: AuditChain) -> None:
        self.bus, self.audit = bus, audit
        self.processes: dict[str, asyncio.subprocess.Process] = {}
    async def run(self, job_id: str, argv: Sequence[str], *, dry_run: bool = True, timeout: float = 60.0) -> RunResult:
        if not argv or any(not isinstance(x, str) or not x for x in argv):
            raise ValueError('argv must contain non-empty strings')
        safe_argv = tuple(argv)
        self.audit.append('job.plan', {'job_id': job_id, 'argv': list(safe_argv), 'dry_run': dry_run})
        await self.bus.publish('job.started', {'job_id': job_id, 'argv': list(safe_argv)})
        if dry_run:
            result = RunResult(safe_argv, 0, '[dry-run] command not executed', True)
        else:
            proc = await asyncio.create_subprocess_exec(*safe_argv, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT)
            self.processes[job_id] = proc
            try:
                raw, _ = await asyncio.wait_for(proc.communicate(), timeout)
                result = RunResult(safe_argv, proc.returncode or 0, raw.decode(errors='replace'), False)
            finally:
                self.processes.pop(job_id, None)
        self.audit.append('job.finished', {'job_id': job_id, 'returncode': result.returncode})
        await self.bus.publish('job.finished', {'job_id': job_id, 'returncode': result.returncode})
        return result
    async def stop(self, job_id: str) -> None:
        proc = self.processes.get(job_id)
        if proc and proc.returncode is None:
            proc.kill()
            await proc.wait()
            await self.bus.publish('job.stopped', {'job_id': job_id})
