import asyncio
from pathlib import Path

from kalz.automation.services import BackupService, ReportService, ScopeService
from kalz.core.workflow import WorkflowEngine, WorkflowStep
from kalz.core.runner import SecureRunner
from kalz.de_integration.factory import get_adapter
from kalz.events.bus import EventBus
from kalz.security.audit import AuditChain


def test_services_and_factory(tmp_path):
    source = tmp_path / 'source.txt'; source.write_text('safe')
    destination = tmp_path / 'backup.txt'
    assert BackupService().snapshot(source, destination).read_text() == 'safe'
    report = ReportService().write_json(tmp_path / 'report.json', 'test', {'ok': True})
    assert 'test' in report.read_text()
    scope = tmp_path / 'scope.txt'; scope.write_text('# comment\nlab.local\n')
    assert ScopeService().load(scope) == frozenset({'lab.local'})
    assert get_adapter('unknown').name == 'generic'


def test_workflow_stops_on_failure(tmp_path):
    async def run():
        runner = SecureRunner(EventBus(), AuditChain(tmp_path / 'audit.jsonl'))
        results = await WorkflowEngine(runner).execute('wf', [WorkflowStep('a', ('echo', 'a')), WorkflowStep('b', ('echo', 'b'))])
        assert len(results) == 2 and all(result.dry_run for result in results)
    asyncio.run(run())
