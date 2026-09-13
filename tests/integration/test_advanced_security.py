import hashlib
import time

from kalz.securityx.keys import KeyManager, KEY_POLICIES
from kalz.securityx.aead import AEADBox, ENCRYPTION_PROFILES
from kalz.securityx.channel import SecureChannel, CHANNEL_POLICIES
from kalz.securityx.access import AccessController, Principal, ACCESS_POLICIES
from kalz.securityx.secrets import SecretStore, SECRET_POLICIES


def test_signing_key_lifecycle():
    manager = KeyManager(); record = manager.create_signing_key()
    payload = b'authenticated payload'; signature = manager.sign(record.key_id, payload)
    assert manager.verify(record, payload, signature)
    manager.revoke(record.key_id)
    assert record.key_id in manager.records and len(KEY_POLICIES) >= 300


def test_aead_round_trip():
    box = AEADBox(hashlib.sha256(b'test-key').digest(), 'test')
    envelope = box.encrypt(b'secret', b'context')
    assert box.decrypt(envelope) == b'secret'
    assert len(ENCRYPTION_PROFILES) >= 300


def test_secure_channel_round_trip():
    alice, alice_public = SecureChannel.keypair(); bob, bob_public = SecureChannel.keypair()
    alice_channel = SecureChannel(SecureChannel.derive(alice, bob_public), 'channel')
    bob_channel = SecureChannel(SecureChannel.derive(bob, alice_public), 'channel')
    message = alice_channel.send(b'hello')
    assert bob_channel.receive(message) == b'hello'
    assert len(CHANNEL_POLICIES) >= 300


def test_access_and_secrets():
    controller = AccessController(); controller.grant_role('operator', {'read'})
    principal = Principal('user', frozenset({'operator'}), frozenset())
    assert controller.decide(principal, 'reports', 'read').allowed
    box = AEADBox(hashlib.sha256(b'secret-key').digest(), 'secrets')
    store = SecretStore(box); version = store.put('token', b'value')
    assert store.get('token') == b'value'
    assert version.version == 1 and len(ACCESS_POLICIES) >= 300 and len(SECRET_POLICIES) >= 300
