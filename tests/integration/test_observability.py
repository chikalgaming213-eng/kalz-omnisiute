import time

from kalz.observability.metrics import MetricsStore, METRIC_DEFINITIONS
from kalz.observability.logging import DistributedLogStore, LogEvent, LOG_SCHEMAS
from kalz.observability.tracing import TraceStore, TRACE_SAMPLERS
from kalz.observability.alerts import AlertEngine, ALERT_RULES
from kalz.observability.export import Exporter, EXPORT_FORMATS


def test_realtime_metrics():
    store = MetricsStore(max_samples=10)
    sample = store.record('latency', 12.5, {'service': 'api'})
    assert sample.value == 12.5
    assert store.aggregate('latency')['count'] == 1
    assert len(METRIC_DEFINITIONS) >= 300


def test_distributed_logging_and_redaction():
    store = DistributedLogStore()
    event = LogEvent('event-1', 'error', 'failure', 'worker', time.time(), fields={'token': 'secret'})
    redacted = store.redact(event, ['token']); store.append(redacted)
    assert store.query(level='error')[0].fields['token'] == '[REDACTED]'
    assert len(LOG_SCHEMAS) >= 300


def test_tracing_and_sampling():
    store = TraceStore(); span = store.start('operation')
    finished = store.finish(span, {'component': 'test'})
    assert finished.end >= finished.start
    assert store.trace(span.trace_id)
    assert len(TRACE_SAMPLERS) >= 300


def test_alerts_and_resolution():
    engine = AlertEngine()
    rule = next(iter(ALERT_RULES.values())).rule(); engine.register(rule)
    alert = engine.evaluate(rule.name, rule.threshold + 1)
    assert alert is not None and engine.active()
    assert engine.resolve(rule.name) == 1


def test_export_integrity():
    exporter = Exporter(); batch = exporter.batch([{'value': 1}], 'batch-1')
    assert exporter.verify(batch)
    assert len(EXPORT_FORMATS) >= 300
