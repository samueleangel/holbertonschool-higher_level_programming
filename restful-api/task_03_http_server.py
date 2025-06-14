#!/usr/bin/python3
import http.server
import socketserver
import json

PORT = 8000  # Define the port to run the server on

# Custom request handler class
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        # Handle root endpoint "/"
        if self.path == "/":
            self.send_response(200)  # HTTP 200 OK
            self.send_header("Content-type", "text/plain")  # Plain text response
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")  # Message content

        # Handle "/data" endpoint
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")  # Must be JSON content type
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode("utf-8"))  # Serialize to JSON and encode

        # Handle "/status" endpoint
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")  # Must return just "OK" as plain text

        # Return 404 for all other endpoints
        else:
            self.send_response(404)  # HTTP 404 Not Found
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

# Set up and start the server
if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
