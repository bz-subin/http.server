from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote
import module.answer as answer
class MyRequestHendler(BaseHTTPRequestHandler):
    def do_GET(self): # 대놓고 보여줌
        self.send_response(200) #서버 상태
        self.send_header("content-type","text/html; charset=utf-8") #줄 내용 속성 설정
        self.end_headers() # 내용 설정 완료!
        self.wfile.write(
        """
        <body>
        <h1>매슬로우 욕구</h1>
        
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
        un_user = unquote(user_data) #16진수 -> 문자열 #*응답을 읽음
        
        server_front = [
            self.send_response(200), #데이터 잘 받았어
            self.send_header("content-type","text/html; charset=utf-8"), #줄 내용 속성 설정
            self.end_headers(), # 내용 설정 완료!
        ]

        def simple_title(tag, answer):  #* 함수를 만들려는 이유. 제목을 쉽게 쓰기 위해서.(태그랑 내용 적으면 됨)
            answer_all ="<"+tag+">" + answer + "</"+tag+">"    
            re_answer = self.wfile.write(answer_all.encode()) #화면에 띄울것(내가 적을것)
            script = "<script>console.log('응답을 받았습니다')</script>"
            con = self.wfile.write(script.encode())#콘솔
            return re_answer,con

        def simple_body(tag, answer):  #* 함수를 만들려는 이유. 제목을 쉽게 쓰기 위해서.(태그랑 내용 적으면 됨)
            answer_all ="<"+tag+">" + answer + "</"+tag+">"    
            re_answer = self.wfile.write(answer_all.encode()) #화면에 띄울것(내가 적을것)
            script = "<script>console.log('사용자가 내용을 조회중입니당')</script>"
            con = self.wfile.write(script.encode())#콘솔
            return re_answer,con



        print(un_user)#*터미널에 뜨게 함
        if "1단계" in un_user:
            server_front
            simple_title("h1","매슬로우 욕구 1단계")  #욕구 두 줄 나올것.
            simple_title("h3","생리적 욕구")  #욕구 두 줄 나올것.
            simple_body("p",answer.body[0])

        elif "2단계" in un_user:
            server_front
            simple_title("h1","매슬로우 욕구 2단계")  #욕구 두 줄 나올것.
            simple_title("h3","안전의 욕구")  #욕구 두 줄 나올것.
            simple_body("p",answer.body[1])

        elif "3단계" in un_user:
            server_front
            simple_title("h1","매슬로우 욕구 3단계")  #욕구 두 줄 나올것.
            simple_title("h3", "사회적 욕구")  #욕구 두 줄 나올것.
            simple_body("p",answer.body[2])

        elif "4단계" in un_user:
            server_front
            simple_title("h1","매슬로우 욕구 4단계")  #욕구 두 줄 나올것
            simple_title("h3","존중의 욕구")  #욕구 두 줄 나올것
            simple_body("p",answer.body[3])

        elif "5단계" in un_user:
            server_front
            simple_title("h1", "매슬로우 욕구 5단계")  #욕구 두 줄 나올것
            simple_title("h3", "자아실현의 욕구")  #욕구 두 줄 나올것
            simple_body("p",answer.body[4])

        else:
            server_front
            simple_title("h1", "굿") 


host = "localhost"
port = 8001

servers = HTTPServer((host,port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")


try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()


            # simple_body("""<p><pre>

            # </pre></p>""" )

