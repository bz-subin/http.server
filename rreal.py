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

        user_data_li = [user_data]
        # data = [] # 배열 만든다. 하나씩 담을거임.
        # data_last = []
        
        for cut_data in user_data: #쪼갠 데이터를 cut_data에 넣는다 
            print(cut_data)
        user_data = "".join(user_data) #왜 그런지 모르겠는데, 한글자씩 나옴.

#* print(user_data) #* %붙어있는지, 한 글자씩 나오는지 체크 => my_msg=%E3%85%81%E3%85%81

#쪼개고 문자인지 숫자인지 구별. 문자라면% 떼고 숫자나 특수문자면 그냥 해
# 숫자가 아닐 경우(문자, 특수문자)
# 하나씩 하는게 나을지도  ,를 기준으로 나눔.
# <공통 적용> 
# 1. 쪼개기
# 2. my_msg 떼기

        # user_data.split(",") #유저 데이터를 쪼갠다 , 기준으로
        # data.append(user_data)
        # for cut_data in data: #쪼갠 데이터를 cut_data에 넣는다 
        #     print(cut_data)
        # print("최종",cut_data)

        #     user_data = cut_data.split #입력값을 쪼갠다 , 를 기준으로 
            

        # # if not user_data.isdigit(): #*요청이 숫자가 아닌가?(문자+숫자, 특수문자, 등등)
        # #     user_data = user_data.split("%") #문자라면 쪼갠다.
        # print(user_data)
        #     #문자가 들어가있는가?로 바꾸면 좋을듯. 
        # # else: #숫자라면 
            
        #     # +++ : my_msg=%2B%2B%2B
        #     # ㅁㅂ : ['my_msg=', 'E3', '85', '81', 'E3', '85', '82']
        #     # 1111 :  ['my_msg=1111']
        #     # ㅁ1ㅁ1 : ['my_msg=', 'E3', '85', '811', 'E3', '85', '811']
            
        #     #*<할일>
        #     # 1. my_msg 떼기 - 슬라이싱[1:] - E3부터 나올 수 있게.
        #     # 2.문자+숫자의 경우 둘을 나누는 작업이 필요함.  isdigit 
        #     for idx, vel in enumerate(user_data):
        #         if vel == "my_msg=":
        #     print(vel)
                    # idx = idx+1
                # else:
                #     user_data[idx:]
                #     print(vel)
                #     print(idx)
                #     data.append(user_data)

                # print(data)
            # for idx, vel in enumerate(user_data): # %에 폭력 행사 -> %가 사라지고 글자가 제각각 나뉨
            #         idx=idx+1
            #         print(vel)
            #         print(idx)
            #     else:
            #         print(vel)
            #         print(idx)
            #         # user_data[idx:]








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


