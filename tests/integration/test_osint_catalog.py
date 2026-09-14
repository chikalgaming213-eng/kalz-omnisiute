import pytest

from kalz.osint.catalog import OSINT_TOOLS, osint_report
from kalz.osint.planner import OSINTPlanner, OSINTScopeError
from kalz.tools.registry import TOOL_INDEX, registry_report


def test_all_requested_osint_entries_are_cataloged():
    names = {item.name for item in OSINT_TOOLS}
    assert len(OSINT_TOOLS) == 19
    assert {'Sherlock', 'Maigret', 'GHunt', 'PhoneInfoga', 'OWASP Amass', 'Subfinder', 'MISP', 'OpenCTI'} <= names
    assert osint_report()['categories']['threat-intelligence'] == 3


def test_osint_entries_have_safe_defaults():
    assert all(item.execution_mode == 'plan-only' and item.requires_consent for item in OSINT_TOOLS)
    assert 'sherlock' in TOOL_INDEX
    assert registry_report()['categories']['osint'] >= 10


def test_planner_rejects_local_targets():
    planner = OSINTPlanner()
    with pytest.raises(OSINTScopeError):
        planner.plan('Sherlock', '127.0.0.1')


def test_planner_creates_auditable_plan():
    plan = OSINTPlanner().plan('Sherlock', 'example.org')
    assert plan.execution_mode == 'plan-only'
    assert plan.requires_consent
    assert 'public-source' in ' '.join(plan.steps)
