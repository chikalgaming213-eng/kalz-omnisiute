import asyncio
import json
import threading
import urllib.request

from kalz.api.rest import serve
from kalz.config import AppConfig
from kalz.core.runner import SecureRunner
from kalz.db.session import Database
from kalz.events.bus import EventBus
from kalz.plugins.api import PluginManifest, PluginRegistry
from kalz.security.audit import AuditChain


def test_database_and_plugin(tmp_path):
    db = Database(tmp_path / 'x.sqlite3')
    assert db.execute('SELECT name FROM sqlite_master WHERE type=\'table\'')
    class P:
        manifest = PluginManifest('demo', '1.0', ('report',))
        def register(self, registry): registry['demo'] = True
    plugins = PluginRegistry(); plugins.register(P())
    assert plugins.capabilities['demo'] is True


def test_runner_dry_run(tmp_path):
    async def run():
        result = await SecureRunner(EventBus(), AuditChain(tmp_path / 'audit.jsonl')).run('1', ['echo', 'safe'])
        assert result.dry_run and result.returncode == 0
    asyncio.run(run())


def test_api_health():
    server = serve('127.0.0.1', 18765)
    thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
    with urllib.request.urlopen('http://127.0.0.1:18765/health') as response:
        assert json.load(response)['ok'] is True
    server.shutdown(); server.server_close()
