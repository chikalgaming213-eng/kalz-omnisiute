from __future__ import annotations

import argparse
import json
from kalz.automation.de_detect import detect_de
from kalz.automation.distro_detect import detect_distro
from kalz.automation.tool_detect import detect_profile
from kalz.tools.registry import registry_report


def main() -> int:
    parser = argparse.ArgumentParser(prog="kalz")
    parser.add_argument("--doctor", action="store_true")
    parser.add_argument("--registry", action="store_true")
    args = parser.parse_args()
    if args.doctor:
        profile = detect_profile().to_dict()
        profile["desktop_detected"] = detect_de()
        profile["distro"] = detect_distro()
        print(json.dumps(profile, indent=2))
    elif args.registry:
        print(json.dumps(registry_report(), indent=2))
    else:
        parser.print_help()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
