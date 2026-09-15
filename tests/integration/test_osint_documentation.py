from pathlib import Path

from kalz.osint.catalog import OSINT_TOOLS

ROOT = Path(__file__).resolve().parents[2]
DOC = (ROOT / 'docs/osint.md').read_text(encoding='utf-8')
README = (ROOT / 'README.md').read_text(encoding='utf-8')


def test_every_osint_repository_has_installation_documentation():
    for tool in OSINT_TOOLS:
        assert tool.repository in DOC, tool.repository
        assert f'https://github.com/{tool.repository}' in DOC, tool.repository


def test_documentation_covers_installation_and_safety_contract():
    required_sections = (
        '## Prasyarat Umum',
        '## Installation Matrix',
        '## Kalz Integration Boundary',
        '## Credential Matrix',
        '## Verification Checklist',
        '## Troubleshooting',
    )
    assert all(section in DOC for section in required_sections)
    assert 'OSINT Installation Matrix' in README
    assert 'tidak dipasang otomatis' in README
