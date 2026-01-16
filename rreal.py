from http.server import HTTPServer, BaseHTTPRequestHandler
#http안에 있는 server에서 HTTPServer이라는것과 BaseHTTPRequestHandler을 가져온다.
class MyRequestHendler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type","text/html; charset=utf-8")
        self.end_headers()
        #write 쓸 때 문자열이랑 
        a = self.requestline
        
        h2_first = "<h2>".encode() 
        h2_last = "</h2>".encode()
        # script_first = "<script>".encode()
        # script_last = "</script>".encode()

        self.wfile.write("<body>".encode()
        + h2_first + a.encode() + h2_last #h2 a(로그)
        + "<h2>클릭".encode() + h2_last #h2 클릭
        # + script_first + "console.log(a)".encode() + script_last #콘솔 로그
        + "</body>".encode())

host = "localhost"
port = 800

#인스턴트
servers = HTTPServer((host,port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")

try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()
