from pathlib import Path
from PIL import Image

source = Path('/home/ubuntu/upload/file_0000000057f48211abd9084a4fbbc6fb.png')
out = Path('kalz/ui/assets')
out.mkdir(parents=True, exist_ok=True)
if not source.exists():
    raise SystemExit(f'missing source image: {source}')
image = Image.open(source).convert('RGBA')
for size in (16, 24, 32, 48, 64, 96, 128, 256, 512):
    image.resize((size, size), Image.Resampling.LANCZOS).save(out / f'kalz-venom-{size}.png', optimize=True)
image.save(out / 'kalz-venom.png', optimize=True)
print(f'created {len(tuple(out.glob("kalz-venom-*.png")))} icon variants')
