from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHendler(BaseHTTPRequestHandler):
    def do_GET(self): # 대놓고 보여줌
        self.send_response(200) #서버 상태
        self.send_header("content-type","text/html; charset=utf-8") #줄 내용 속성 설정
        self.end_headers() # 내용 설정 완료!
        self.wfile.write("<h1>가나다</h1>".encode()) # 보내줄 내용
        



    def do_POST(self): # 숨겨서 보여줌(아이디, 비밀번호)
        print("췍췍")
        self.send_response(200)
        con_length = self.end_headers.get("content-length") #.get를 써야한다고 함
        self.rfile.read(con_length.decode())
        print(con_length)
        con_length = int(con_length) 
        print(con_length)

        self.wfile.write(
        """
        <body>
        <form action="/" method="POST">
            <input type="text" name="my_msg"> 
            
            <input type="submit" value="보내기">
        </form>
        </body>
        """
        .encode())
        
host = "localhost"
port = 8002

servers = HTTPServer((host,port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")


try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()


