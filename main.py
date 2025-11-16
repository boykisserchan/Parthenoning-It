import http.server
import socketserver
from pathlib import Path
from urllib.parse import urlparse

port = 4173
dir = "taggie/build"

class SPAHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=dir, **kwargs)

    def do_GET(self):
        parsed_path = urlparse(self.path).path

        # Strip leading slash
        stripped = parsed_path.lstrip("/")

        # Check if path exists
        path = Path(self.directory) / stripped
        if path.is_file() or path.is_dir():
            return super().do_GET()

        # Fallback for SPA routes, including base path
        if stripped.startswith("taggie/"):
            self.path = "/404.html"  # SvelteKit static fallback
        else:
            self.path = "/404.html"
        return super().do_GET()

with socketserver.TCPServer(("", port), SPAHandler) as httpd:
    print(f"serving cunt @ http://localhost:{port}/taggie")
    httpd.serve_forever()
