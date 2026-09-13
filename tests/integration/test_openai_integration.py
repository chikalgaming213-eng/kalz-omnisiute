import os

import pytest

from kalz.integrations.openai_client import ChatMessage, OpenAIClient, OpenAIConfig, OpenAIConfigurationError
from kalz.integrations.openai_agents import AgentConfig, AgentToolRegistry, OpenAIAgent


class FakeResponse:
    id = 'resp-test'
    output_text = 'ok'
    usage = {'input_tokens': 1, 'output_tokens': 1, 'total_tokens': 2}


class FakeResponses:
    def create(self, **kwargs):
        assert kwargs['model'] == 'test-model'
        assert kwargs['input'][0]['role'] == 'user'
        return FakeResponse()


class FakeClient:
    responses = FakeResponses()


def test_config_requires_environment_key(monkeypatch):
    monkeypatch.delenv('OPENAI_API_KEY', raising=False)
    with pytest.raises(OpenAIConfigurationError):
        OpenAIConfig.from_environment()


def test_responses_adapter_does_not_expose_key():
    config = OpenAIConfig('test-secret-key', model='test-model')
    client = OpenAIClient(config, FakeClient())
    result = client.responses([ChatMessage('user', 'hello')])
    assert result.text == 'ok'
    assert 'test-secret-key' not in str(client.health())
    assert client.health()['requests'] == 1


def test_agent_tool_allowlist(monkeypatch):
    monkeypatch.setenv('OPENAI_API_KEY', 'configured-but-not-used')
    registry = AgentToolRegistry()
    registry.register('health_check', lambda: {'ok': True})
    agent = OpenAIAgent(AgentConfig(tool_names=('health_check',)), registry)
    assert agent.health()['tools'] == ('health_check',)
    assert agent.registry.allow(('health_check',))['health_check']() == {'ok': True}
