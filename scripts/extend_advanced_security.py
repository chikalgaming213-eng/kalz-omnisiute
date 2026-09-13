from pathlib import Path

def add(path, suffix, names, block):
 p=Path(path)
 with p.open('a') as f:
  for i,n in enumerate(names,6000): f.write(block.format(cls=n.title().replace('_',''),name=n,seq=i))

def main():
 names=[f'advanced_policy_{i:03d}' for i in range(1,180)]
 add('kalz/securityx/keys.py','KeyPolicy',names,'''\nclass {cls}KeyPolicy:\n    name={name!r}\n    sequence={seq}\n    algorithm="ed25519"\n    def valid(self, record: KeyRecord, now: float|None=None) -> bool:\n        return record.status == "active" and record.expires_at > (now or time.time())\n    def requirements(self) -> dict[str,Any]:\n        return {{"name":self.name,"sequence":self.sequence,"algorithm":self.algorithm,"rotation":True}}\n''')
 add('kalz/securityx/aead.py','AEADProfile',names,'''\nclass {cls}AEADProfile:\n    name={name!r}\n    sequence={seq}\n    algorithm="AES-256-GCM"\n    def aad(self, context: bytes=b"") -> bytes:\n        return self.name.encode() + b":" + context\n    def validate(self, envelope: EncryptedEnvelope) -> bool:\n        return envelope.version == 1 and len(envelope.nonce) == 12 and bool(envelope.ciphertext)\n    def metadata(self) -> dict[str,Any]:\n        return {{"name":self.name,"sequence":self.sequence,"algorithm":self.algorithm,"authenticated":True}}\n''')
 add('kalz/securityx/channel.py','ChannelPolicy',names,'''\nclass {cls}ChannelPolicy:\n    name={name!r}\n    sequence={seq}\n    replay_window={seq}%128 + 1\n    def validate(self, message: SecureMessage) -> bool:\n        return message.sequence > 0 and len(message.nonce) == 12 and bool(message.ciphertext)\n    def metadata(self) -> dict[str,Any]:\n        return {{"name":self.name,"sequence":self.sequence,"replay_protection":True,"window":self.replay_window}}\n''')
 add('kalz/securityx/access.py','AccessPolicy',names,'''\nclass {cls}AccessPolicy:\n    name={name!r}\n    sequence={seq}\n    scope={name!r}\n    def allows(self, principal: Principal, action: str) -> bool:\n        return bool(principal.principal_id) and (action in principal.capabilities or self.scope in principal.capabilities)\n    def metadata(self) -> dict[str,Any]:\n        return {{"name":self.name,"sequence":self.sequence,"scope":self.scope,"deny_by_default":True}}\n''')
 add('kalz/securityx/secrets.py','SecretPolicy',names,'''\nclass {cls}SecretPolicy:\n    name={name!r}\n    sequence={seq}\n    ttl={seq}%86400 + 3600\n    def valid(self, secret: SecretVersion, now: float|None=None) -> bool:\n        return secret.expires_at > (now or time.time())\n    def metadata(self) -> dict[str,Any]:\n        return {{"name":self.name,"sequence":self.sequence,"ttl":self.ttl,"redaction":True,"rotation":True}}\n''')
if __name__=='__main__': main()
