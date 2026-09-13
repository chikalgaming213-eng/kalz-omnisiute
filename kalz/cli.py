from __future__ import annotations

import argparse
import json
from kalz.api.rest import serve
from kalz.app import run_gui
from kalz.automation.de_detect import detect_de
from kalz.automation.distro_detect import detect_distro
from kalz.automation.tool_detect import detect_profile
from kalz.tools.registry import registry_report

def main() -> int:
    p = argparse.ArgumentParser(prog='kalz')
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('--doctor', action='store_true'); g.add_argument('--registry', action='store_true'); g.add_argument('--gui', action='store_true'); g.add_argument('--api', action='store_true')
    a = p.parse_args()
    if a.doctor:
        data = detect_profile().to_dict(); data['distro'] = detect_distro(); data['desktop_detected'] = detect_de(); print(json.dumps(data, indent=2)); return 0
    if a.registry: print(json.dumps(registry_report(), indent=2)); return 0
    if a.gui: return run_gui()
    if a.api:
        from kalz.api.rest import APIHandler
        APIHandler.profile_provider = lambda: {**detect_profile().to_dict(), 'distro': detect_distro(), 'desktop_detected': detect_de()}
        server = serve(); print('Kalz API listening on http://127.0.0.1:8765', flush=True); server.serve_forever()
    return 0
