from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote
class MyRequestHendler(BaseHTTPRequestHandler):
    def do_GET(self): # 대놓고 보여줌
        self.send_response(200) #서버 상태
        self.send_header("content-type","text/html; charset=utf-8") #줄 내용 속성 설정
        self.end_headers() # 내용 설정 완료!
        self.wfile.write(
        """
        <body>
        <h1>커밋 푸쉬 잊지마!</h1>
        
        <form action="/" method="POST">
            <input type="text" name="my_msg"> 
            <input type="submit" value="보내기">
        </form>

        </body>"""
        .encode()) # 보내줄 내용

#보낼 떈 encode(컴퓨터 언어), 받을 땐 decode(우리가 읽을 수 있도록)인듯.

    def do_POST(self): # 숨겨서 보여줌(아이디, 비밀번호)
        print("응답을 받았습니다.")
        con_length = self.headers.get("content-length",0) #몇 글자인지 확인/못 찾으면 0 가져옴 
        con_length = int(con_length)
        # 입력한 문자의 길이만큼 읽기 때문에, 읽기한 부분을 변수로 만든 뒤 나중에 출력 할 떄 그 변수를 decode 해야함.
        user_data = self.rfile.read(con_length).decode() #읽기
        
        un_user = unquote(user_data) #16진수 -> 문자열
        print(un_user)#터미널에 뜨게 함

        self.send_response(200) #데이터 잘 받았어
        self.send_header("content-type","text/html; charset=utf-8") #줄 내용 속성 설정
        self.end_headers() # 내용 설정 완료!
        h1 = "<h1>굿</h1>"
        script = "<script>console.log('응답을 받았습니다')</script>"
        self.wfile.write(h1.encode())
        self.wfile.write(script.encode())

host = "localhost"
port = 8001

servers = HTTPServer((host,port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")


try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()


