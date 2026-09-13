from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Callable

class APIHandler(BaseHTTPRequestHandler):
    profile_provider: Callable[[], dict] = lambda: {}
    def do_GET(self) -> None:
        if self.path == '/health': self._json({'ok': True, 'service': 'kalz'})
        elif self.path == '/api/v1/profile': self._json(self.profile_provider())
        else: self._json({'error': 'not found'}, 404)
    def do_POST(self) -> None:
        if self.path == '/api/v1/plan':
            size = int(self.headers.get('Content-Length', '0'))
            body = json.loads(self.rfile.read(size) or b'{}')
            self._json({'accepted': False, 'dry_run': True, 'packages': body.get('packages', []), 'message': 'review plan before execution'})
        else: self._json({'error': 'not found'}, 404)
    def _json(self, payload: dict, status: int = 200) -> None:
        data = json.dumps(payload).encode()
        self.send_response(status); self.send_header('Content-Type', 'application/json'); self.send_header('Content-Length', str(len(data))); self.end_headers(); self.wfile.write(data)
    def log_message(self, *_args) -> None: return

def serve(host: str = '127.0.0.1', port: int = 8765) -> ThreadingHTTPServer:
    return ThreadingHTTPServer((host, port), APIHandler)
