from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from apps.api.nexus_api.main import get_graph, healthz


class Handler(BaseHTTPRequestHandler):
    def _send(self, payload: dict):
        body = json.dumps(payload).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == '/healthz':
            self._send(healthz()); return
        if self.path == '/graph':
            self._send(get_graph()); return
        self._send({'status':'ok','path':self.path})


def run_server(port: int = 8000):
    server = HTTPServer(('0.0.0.0', port), Handler)
    server.serve_forever()


if __name__ == '__main__':
    run_server()
