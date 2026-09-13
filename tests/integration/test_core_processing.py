import asyncio

from kalz.core.orchestration import build_orchestrator
from kalz.core.parser_registry import ParseInput, build_parser_registry
from kalz.core.process_manager import ProcessManager, ProcessSpec
from kalz.core.telemetry import METRIC_CATALOG, TelemetryStore
from kalz.core.updater import UPDATE_CATALOG, UpdateManager


def test_process_manager_lifecycle():
    async def run():
        manager = ProcessManager()
        manager.register(ProcessSpec('demo', ('echo', 'demo')))
        state = await manager.start('demo')
        assert state.status == 'planned'
        assert manager.snapshot()['registered'] == 1
    asyncio.run(run())


def test_parser_registry_catalog():
    registry = build_parser_registry()
    assert len(registry.parsers) >= 300
    result = registry.parse('parser_001', ParseInput('fixture.txt', 'content'))
    assert result.success and result.records


def test_telemetry_catalog():
    store = TelemetryStore()
    assert len(METRIC_CATALOG) >= 300
    sample = next(iter(METRIC_CATALOG.values())).sample(store, 3)
    assert sample.value == 3 and store.summary()['samples'] == 1


def test_update_catalog():
    manager = UpdateManager()
    assert len(UPDATE_CATALOG) >= 300
    manifest = next(iter(UPDATE_CATALOG.values()))
    artifact = manifest.artifact(b'content')
    manager.register(artifact)
    assert manager.plan(artifact.name).dry_run is True


def test_orchestration_catalog():
    orchestrator = build_orchestrator()
    result = orchestrator.execute()
    assert len(orchestrator.nodes) >= 300
    assert result.status == 'planned'
    assert len(result.order) == len(orchestrator.nodes)
