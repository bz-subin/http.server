from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHendler(BaseHTTPRequestHandler):
    def do_GET(self): # 대놓고 보여줌
        self.send_response(200) #서버 상태
        self.send_header("content-type","text/html; charset=utf-8") #줄 내용 속성 설정
        self.end_headers() # 내용 설정 완료!
        self.wfile.write("<h1>가나다</h1>".encode()) # 보내줄 내용
        
    def do_POST(self, con_length): # 숨겨서 보여줌(아이디, 비밀번호)
        self.headers("content-length")
        self.rfile.read("content-length".decode())
        con_length = "content-length"
        con_length = int(con_length) 
        print(con_length)

        self.send_response(200)
        self.wfile.write(re_length.encode())
        
host = "localhost"
port = 8001

servers = HTTPServer((host,port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")


try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()


