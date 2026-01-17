from http.server import HTTPServer, BaseHTTPRequestHandler
#http안에 있는 server에서 HTTPServer이라는것과 BaseHTTPRequestHandler을 가져온다.
class MyRequestHendler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type","text/html; charset=utf-8")
        self.send_header("content-length","text/html; charset=utf-8")
        self.end_headers()
        re_length = int("content-length")
        self.rfile.read(re_length.decode())
        self.wfile.write("<h1>가나다</h1>".encode())


#BaseHTTPRequestHandler을 받아와서 MyRequestHandler라는 클래스를 실행한다.
#(서버 상태, 초기 설정, 실제 입력 내용)

host = "localhost"
port = 8000
#

#인스턴트
servers = HTTPServer((host,port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")

try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()
