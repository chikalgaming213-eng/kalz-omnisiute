from pathlib import Path
root = Path('kalz')
fixed = []
for path in root.rglob('*.py'):
    if '__pycache__' in path.parts:
        continue
    text = path.read_text(encoding='utf-8')
    if '_LOGIC_RULES = {rule.name: rule for rule in [' in text and text.rstrip().endswith(']}}'):
        path.write_text(text.replace(']}}\n', ']}\n'), encoding='utf-8')
        fixed.append(str(path))
print('fixed=', len(fixed))
