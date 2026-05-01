#!/usr/bin/env python3
"""Quick local server for the Poker Chip Tracker."""
import http.server
import socketserver
import socket
import os

PORT = 3000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "localhost"

Handler = http.server.SimpleHTTPRequestHandler
Handler.log_message = lambda *a: None  # silence request logs

ip = get_local_ip()
print(f"\n  ♠  Poker Chip Tracker")
print(f"  ─────────────────────────────────────")
print(f"  Local:   http://localhost:{PORT}")
print(f"  Network: http://{ip}:{PORT}   ← share with players")
print(f"  ─────────────────────────────────────")
print(f"  Open the URL on any phone or tablet")
print(f"  on the same Wi-Fi network.")
print(f"  Press Ctrl+C to stop.\n")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
