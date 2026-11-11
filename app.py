from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if '/bizimev' in self.path:
            cmd = ['yt-dlp', '--no-check-certificates', '-g', '30M_F_2xy9Q']
            url = subprocess.check_output(cmd).decode().splitlines()[0]
            self.send_response(302)
            self.send_header('Location', url)
            self.end_headers()
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Sunucu Aktif")

port = int(os.environ.get("PORT", 8080))
HTTPServer(('0.0.0.0', port), Handler).serve_forever()
