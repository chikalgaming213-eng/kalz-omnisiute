from pathlib import Path
for name in ('kalz/automation/automation_engine.py', 'kalz/security/security_engine.py'):
    path = Path(name)
    text = path.read_text(encoding='utf-8')
    text = text.replace('\\n', '\n')
    path.write_text(text, encoding='utf-8')
    print('repaired', name)
