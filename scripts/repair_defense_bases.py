from pathlib import Path
for filename, name in [('kalz/defense/engine.py','DefenseRule'),('kalz/defense/hardening.py','HardeningControl')]:
    path=Path(filename); text=path.read_text()
    marker='class DefenseError(RuntimeError): pass\n'
    if f'class {name}:' not in text:
        base=f'''\nclass {name}:\n    name = "base"\n    def evaluate(self, event: SecurityEvent) -> dict[str, Any]:\n        return {{"rule": self.name, "allowed": True, "sequence": 0, "automatic": False}}\n\n'''
        text=text.replace(marker, marker+base, 1)
        path.write_text(text)
        print('repaired', filename)
