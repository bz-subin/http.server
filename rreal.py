from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHendler(BaseHTTPRequestHandler):
    def do_GET(self): # 대놓고 보여줌
        self.send_response(200) #서버 상태
        self.send_header("content-type","text/html; charset=utf-8") #줄 내용 속성 설정
        self.end_headers() # 내용 설정 완료!
        self.wfile.write(
        """
        <body>
        <h1>가나다</h1>
        <form action="/" method="POST">
            <input type="text" name="my_msg"> 
            
            <input type="submit" value="보내기">
        </form>
        </body>"""
        .encode()) # 보내줄 내용

#보낼 떈 encode(컴퓨터 언어), 받을 땐 decode(우리가 읽을 수 있도록)인듯.

    def do_POST(self): # 숨겨서 보여줌(아이디, 비밀번호)
        print("오예 시작") #* 출력
        con_length = self.headers.get("content-length",0) #몇 글자인지 확인/못 찾으면 0 가져옴 
        con_length = int(con_length)
        print(con_length) #* 입력값 길이
# 입력한 문자의 길이만큼 읽기 때문에, 읽기한 부분을 변수로 만든 뒤 나중에 출력 할 떄 그 변수를 decode 해야함.
        user_data = self.rfile.read(con_length).decode() #읽기
        # print(user_data.unquote())
# urllib.parse.unquote(user_data)

        data = [] # 배열 만든다. 하나씩 담을거임.
        print(data)
        print(user_data) #*입력값 전체 - 체크용
        if type(user_data) == str:  #만약 클라이언트의 요청이 문자열이라면 
            for cut_data in user_data.split("%"): # %에 폭력 행사 -> %가 사라지고 글자가 제각각 나뉨
                data.append(cut_data) # 쪼개진 친구를 data에 담는다.
            #>>> del data[0]  # 지금 앞에 붙은 my_msg 때문에 int가 잘 안 돌아가는 상황임 개선할 것.
            for data_one in data:
                data_last = int(data_one)
                print(data_last.decode('utf-8'))              

#my_msg=   자동으로 붙는 7글자.
#my_msg=%E3%85%81%E3%85%81%E3%85%81%E3%85%81%E3%85%81%E3%85%81%E3%85%81%E3%85%81%E3%85%81%E3%85%81%E3%85%81%E3%85%81

        self.send_response(200) #데이터 잘 받았어
        self.wfile.write("전달완료".encode())

host = ""
port = 8006

servers = HTTPServer((host,port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")


try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()


