from kalz.automation.automation_engine import AutomationEngine, AutomationError, OperationContext
from kalz.security.security_engine import SecurityEngine, SecurityContext


def test_automation_registry_and_lifecycle():
    engine = AutomationEngine()
    assert len(engine.operations) >= 220
    context = OperationContext('operation-1', mode='safe', dry_run=True, actor='tester')
    plan = engine.plan('detect_kernel', context)
    assert plan['dry_run'] is True
    result = engine.execute('detect_kernel', context)
    assert result.status == 'planned'
    rollback = engine.rollback('detect_kernel', context)
    assert rollback.status == 'rolled_back'


def test_privileged_automation_is_blocked_in_safe_mode():
    engine = AutomationEngine()
    context = OperationContext('operation-2', mode='safe', dry_run=False, actor='tester')
    try:
        engine.plan('plan_install', context)
    except AutomationError:
        pass
    else:
        raise AssertionError('safe mode must block non-dry-run package changes')


def test_security_registry_scope_and_consent():
    engine = SecurityEngine()
    assert len(engine.rules) >= 210
    allowed = SecurityContext('tester', mode='lab', consent=True, targets=frozenset({'lab.local'}))
    assert engine.evaluate('target', 'lab.local', allowed).allowed
    denied = SecurityContext('tester', mode='safe', consent=False, targets=frozenset({'other.local'}))
    assert not engine.evaluate('target', 'lab.local', denied).allowed
