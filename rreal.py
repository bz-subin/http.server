from http.server import HTTPServer, BaseHTTPRequestHandler
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
        con_length = self.headers.get("content-length",0) #몇 글자인지 확인/못 찾으면 0 가져옴 
        con_length = int(con_length)
        # 입력한 문자의 길이만큼 읽기 때문에, 읽기한 부분을 변수로 만든 뒤 나중에 출력 할 떄 그 변수를 decode 해야함.
        user_data = self.rfile.read(con_length).decode() #읽기

        data = [] # 배열 만든다. 하나씩 담을거임.
        # data_last = []
#* print(user_data) #* %붙어있는지, 한 글자씩 나오는지 체크 => my_msg=%E3%85%81%E3%85%81
        # user_data = "".join(user_data) #왜 그런지 모르겠는데, 한글자씩 나옴.
        if not user_data.isdigit(): #*요청이 문자인가?(숫자가 아닌가?)
            for idx, vel in enumerate(user_data).split("%"): # %에 폭력 행사 -> %가 사라지고 글자가 제각각 나뉨
                if vel == "my_msg=":
                    idx=idx+1
                    user_data[idx:]
                    print(user_data)    
                # print(cut_data)
        #         data.append(cut_data) # 쪼개진 친구를 data에 담는다.                        
        #         int_data = int(data,16)
        #         data_last.append(int_data)   
        #     p=bytes(data_last).decode()
        #     print(p)
        # else:
        #     print(user_data)              
            
            
            # for data_vel in user_data:
            #     data.append(data_vel)
            #     print(data)
            #     print(data_vel)
            #     # if data_vel == "my_msg=":  #my_msg를 찾아서 그게 어딘지 구해서(배열[인덱스]), 그 부분부터 끝까지만 보관하겠다
                #     data_vel.replace("my_msg=","")
                #     print(user_data) #*데이터 확인


#1을 입력하면 두칸이 됨. my_msg랑 1이랑.  -> 슬라이싱으로 1부터 1까지 한다.
                    

        self.send_response(200) #데이터 잘 받았어
        self.send_header("content-type","text/html; charset=utf-8") #줄 내용 속성 설정
        self.end_headers() # 내용 설정 완료!
        self.wfile.write("<h1>굿</h1>".encode())

host = "localhost"
port = 8000

servers = HTTPServer((host,port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")


try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()


