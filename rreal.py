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
# 입력한 문자의 길이만큼 읽기 때문에, 읽기한 부분을 변수로 만든 뒤 나중에 출력 할 떄 그 변수를 decode 해야함.
        user_data = self.rfile.read(con_length).decode() #읽기
        # print(user_data.unquote())
# urllib.parse.unquote(user_data)

        data = [] # 배열 만든다. 하나씩 담을거임.
        data_last = []
        if type(user_data) == str:  #만약 클라이언트의 요청이 문자열이라면 
            for cut_data in user_data.split("%"): # %에 폭력 행사 -> %가 사라지고 글자가 제각각 나뉨
                data.append(cut_data) # 쪼개진 친구를 data에 담는다.
                # print(data) #* 쪼개서 배열에 넣은 상태.
            for data_idx, data_vel in enumerate(data):
                if data_vel == "my_msg=":  #my_msg를 찾아서 그게 어딘지 구해서(배열[인덱스]), 그 부분부터 끝까지만 보관하겠다
                    data_idx = data_idx + 1 #0부터 시작이니까 인덱스+1 (0번째 재끼고 1번째부터 쓸거라)
                    data[data_idx:] #my_msg 있는 부분 다음부터 보관하겠다.
                else:  #my_data가 아닌 부분
                    int_data = int(data_vel,16)
                    data_last.append(int_data)   
            p = bytes(data_last).decode() # 255 이상이라 에러 난 것으로 추정
            print(p)

        self.send_response(200) #데이터 잘 받았어
        self.wfile.write("전달완료".encode())

host = "localhost"
port = 8006

servers = HTTPServer((host,port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")


try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()


