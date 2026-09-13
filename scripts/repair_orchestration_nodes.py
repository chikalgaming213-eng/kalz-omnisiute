from pathlib import Path
p = Path('kalz/core/orchestration.py')
s = p.read_text(encoding='utf-8')
s = s.replace('(PipelineNode):', ':')
p.write_text(s, encoding='utf-8')
print('repaired orchestration node classes')
