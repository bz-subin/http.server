from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHendler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type","text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h1>가나다</h1>".encode())
        
    def do_POST(self, re_length):
        self.headers("content-length","text/html; charset=utf-8")
        re_length = int("content-length")
        self.rfile.read(re_length.decode())
        print(re_length)
        self.send_response(200)
        self.send_header("content-type","text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(re_length.encode())
        print(re_length)

host = "localhost"
port = 8001

servers = HTTPServer((host,port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")


try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()


