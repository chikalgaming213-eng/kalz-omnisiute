from __future__ import annotations

import importlib
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def run(command: list[str], *, cwd: pathlib.Path = ROOT) -> None:
    print("[verify]", " ".join(command))
    subprocess.run(command, cwd=cwd, check=True)


def import_audit() -> int:
    sys.path.insert(0, str(ROOT))
    modules = []
    for path in sorted((ROOT / "kalz").rglob("*.py")):
        if path.name == "__init__.py" or "__pycache__" in path.parts:
            continue
        module = ".".join(path.relative_to(ROOT).with_suffix("").parts)
        importlib.import_module(module)
        modules.append(module)
    print(f"[verify] imported {len(modules)} runtime modules")
    return len(modules)


def check_files() -> None:
    required = [
        "README.md", "Makefile", "pyproject.toml", "scripts/bootstrap.sh", "scripts/deploy.sh",
        "docs/architecture.md", "docs/deployment.md", "docs/osint.md",
        "kalz/ui/assets/kalz-venom.png", "packaging/flatpak/org.kalz.OmniSuite.yml",
        "packaging/snap/snapcraft.yaml", "packaging/debian/control",
        "packaging/rpm/kalz-omnisiute.spec",
    ]
    missing = [item for item in required if not (ROOT / item).is_file() or (ROOT / item).stat().st_size == 0]
    if missing:
        raise SystemExit(f"missing or empty required files: {missing}")


def check_shell() -> None:
    for path in sorted((ROOT / "scripts").glob("*.sh")):
        run(["bash", "-n", str(path)])


def check_secret_scan() -> None:
    pattern = re.compile(r"sk-proj-|sk-[A-Za-z0-9]{20,}|BEGIN (RSA|OPENSSH|PRIVATE) KEY")
    ignored = {".git", ".venv", "__pycache__", ".github"}
    hits = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in ignored for part in path.parts):
            continue
        if path.relative_to(ROOT).as_posix() in {"README.md", "scripts/deploy.sh", "scripts/verify.py"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if pattern.search(text):
            hits.append(str(path.relative_to(ROOT)))
    if hits:
        raise SystemExit(f"secret-like material found in: {hits}")


def main() -> int:
    check_files()
    check_secret_scan()
    check_shell()
    run([sys.executable, "-m", "compileall", "-q", "kalz", "tests", "scripts"])
    imported = import_audit()
    run([sys.executable, "-m", "kalz", "--doctor"], cwd=ROOT)
    osint = subprocess.run([sys.executable, "-m", "kalz", "--osint"], cwd=ROOT, check=True, capture_output=True, text=True)
    report = json.loads(osint.stdout)
    if report.get("count") < 19:
        raise SystemExit("OSINT catalog count regressed")
    run([sys.executable, "-m", "pytest", "-q"])
    print(f"[verify] all gates passed; modules={imported}, osint={report['count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
