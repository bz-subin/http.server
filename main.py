from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHendler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h1>제목</h1>".encode())
host = "localhost"
port = 8000

servers = HTTPServer((host,port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}")
print("ctrl+C를 누르면 서버가 종료됩니다")

try:
    servers.serve_forever()
except KeyboardInterrupt:
    print("서버가 종료되었습니다.")
    servers.server_close()