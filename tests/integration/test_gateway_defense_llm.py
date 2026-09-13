import time

from kalz.gateway.gateway import APIGateway, Backend, GatewayRequest
from kalz.gateway.load_balancer import LoadBalancer, Node
from kalz.defense.engine import DefenseEngine, SecurityEvent, DEFENSE_RULES
from kalz.defense.hardening import DefenseEngine as HardeningEngine, SecurityEvent as HardeningEvent, HARDENING_CONTROLS
from kalz.observability.logging import DistributedLogStore, LogEvent
from kalz.observability.llm_analysis import LogAnalysisService


def test_gateway_and_load_balancer():
    gateway = APIGateway(); gateway.add_backend(Backend('api', '127.0.0.1')); gateway.route('/health', 'api')
    response = gateway.dispatch(GatewayRequest('request-1', 'GET', '/health'))
    assert response.status == 200 and response.backend == 'api'
    balancer = LoadBalancer([Node('a', '127.0.0.1'), Node('b', '127.0.0.2')])
    assert balancer.choose_round_robin().name == 'a'
    assert balancer.choose_least_load().name in {'a', 'b'}


def test_layered_defense():
    engine = DefenseEngine(); engine.register(next(iter(DEFENSE_RULES.values())))
    event = SecurityEvent('event-1', 'normal', 'source', {}, time.time())
    decision = engine.inspect(event)
    assert 'blocked' in decision and len(DEFENSE_RULES) >= 400
    hardening = HardeningEngine(); hardening.register(next(iter(HARDENING_CONTROLS.values())))
    assert hardening.inspect(HardeningEvent('event-2', 'normal', 'source', {}, time.time()))


def test_llm_log_analysis_fallback_is_safe():
    store = DistributedLogStore(); store.append(LogEvent('e1', 'error', 'database failure', 'db', time.time(), fields={'token': 'secret'}))
    service = LogAnalysisService(store, max_events=10)
    snapshot = service.snapshot()
    assert snapshot['events'][0]['fields']['token'] == '[REDACTED]'
    result = service.analyze()
    assert result.event_count == 1 and result.severity in {'warning', 'unknown'}
