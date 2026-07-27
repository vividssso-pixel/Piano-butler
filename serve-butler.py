#!/usr/bin/env python3
"""Local server for Piano Butler.

Plain `python3 -m http.server` lets the browser cache butler.html, which means a
change can be live on disk and still invisible in the tab. Everything here is
served with no-store so a normal reload always picks up the current files.

Started by "Open Piano Butler.command"; run directly with `python3 serve-butler.py`.
"""

import http.server
import os
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8899
ROOT = os.path.dirname(os.path.abspath(__file__))


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, *args):
        pass  # keep the Terminal window quiet


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), NoCacheHandler) as httpd:
        print("Serving %s on http://localhost:%d" % (ROOT, PORT))
        httpd.serve_forever()
