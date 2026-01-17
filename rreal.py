from http.server import HTTPServer, BaseHTTPRequestHandler
#http안에 있는 server에서 HTTPServer이라는것과 BaseHTTPRequestHandler을 가져온다.
class MyRequestHendler(BaseHTTPRequestHandler): #BaseHTTPRequestHandler을 받아서, 클래스를 만듬.
    def do_GET(self): # 서버 상태, 초기값, 초기값 설정 끝 (CRUD open,close 같은 느낌), 보일 내용
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
