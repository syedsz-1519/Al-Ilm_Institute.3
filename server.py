from http.server import SimpleHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

if __name__ == '__main__':
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, Handler)
    print(f'Serving http://localhost:{PORT}/al_ilm_institute.html')
    httpd.serve_forever()
