from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if '/bizimev' in self.path:
            try:
                cmd = [
                    'yt-dlp',
                    '--no-check-certificates',
                    '--extractor-args', 'youtube:player_client=android',
                    '-g', '30M_F_2xy9Q'
                ]
                out = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode().strip()
                lines = [line for line in out.splitlines() if line.startswith('http')]
                if lines:
                    self.send_response(302)
                    self.send_header('Location', lines[0])
                    self.end_headers()
                else:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(out.encode())
            except subprocess.CalledProcessError as e:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(e.output)
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Sunucu Aktif")

port = int(os.environ.get("PORT", 8080))
HTTPServer(('0.0.0.0', port), Handler).serve_forever()
