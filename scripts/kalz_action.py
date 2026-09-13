from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['detect', 'install-plan', 'build-plan', 'sign-plan'])
    parser.add_argument('items', nargs='*')
    args = parser.parse_args()
    if args.action == 'detect':
        from kalz.automation.de_detect import detect_de
        from kalz.automation.distro_detect import detect_distro
        print(json.dumps({'distro': detect_distro(), 'desktop': detect_de()}, indent=2)); return 0
    if args.action == 'install-plan':
        from kalz.automation.auto_install import plan_install
        print(json.dumps(plan_install(args.items).__dict__, indent=2)); return 0
    if args.action == 'build-plan':
        print(json.dumps({'dry_run': True, 'artifacts': args.items or ['wheel', 'sdist'], 'message': 'run packaging toolchain after review'}, indent=2)); return 0
    print(json.dumps({'dry_run': True, 'signature': 'GPG signing requires explicit release credentials'}, indent=2)); return 0

if __name__ == '__main__':
    raise SystemExit(main())
