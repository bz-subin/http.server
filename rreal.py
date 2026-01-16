from http.server import HTTPServer, BaseHTTPRequestHandler
class MyRequestHendler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type","text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h1>가나다</h1>".encode())

host = "localhost"
port = 800

#인스턴트
servers = HTTPServer((host,port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")

try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()
