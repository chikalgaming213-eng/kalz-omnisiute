from pathlib import Path
p = Path('kalz/security/security_engine.py')
s = p.read_text(encoding='utf-8').replace('    risk = high\n', '    risk = "high"\n').replace('    risk = medium\n', '    risk = "medium"\n')
p.write_text(s, encoding='utf-8')
print('repaired security risk literals')
