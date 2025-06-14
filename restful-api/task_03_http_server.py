#!/usr/bin/python3
"""
Simple HTTP API server using http.server.BaseHTTPRequestHandler.

Endpoints:
- /              -> Returns a simple greeting text.
- /data          -> Returns sample JSON data.
- /status        -> Returns API status (OK).
- Any other path -> Returns 404 Not Found with an error message.
"""

import http.server
import json
from http import HTTPStatus


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path

        if path == "/":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            response_text = "Hello, this is a simple API!"
            self.wfile.write(response_text.encode("utf-8"))

        elif path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif path == "/status":
            data = {"status": "OK"}
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

    def log_message(self, format, *args):
        return


def run(server_class=http.server.HTTPServer,
        handler_class=SimpleAPIHandler,
        port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
