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
        un_user = unquote(user_data) #16진수 -> 문자열 #*응답을 읽음
        
        server_front = [
            self.send_response(200), #데이터 잘 받았어
            self.send_header("content-type","text/html; charset=utf-8"), #줄 내용 속성 설정
            self.end_headers(), # 내용 설정 완료!
        ]


        def simple_title(answer):  #* 함수를 만들려는 이유. 제목을 쉽게 쓰기 위해서.
            a = self.wfile.write(answer.encode())
            script = "<script>console.log('응답을 받았습니다')</script>"
            b = self.wfile.write(script.encode())
            return a,b
        
        def simple_body(answer):  #* 함수를 만들려는 이유. 제목을 쉽게 쓰기 위해서.
            a = self.wfile.write(answer.encode()) # 쓸 말
            script = "<script>console.log('사용자가 내용을 조회중입니당')</script>"
            b = self.wfile.write(script.encode())# console.log
            return a,b        



        print(un_user)#*터미널에 뜨게 함
        if "1단계" in un_user:
            server_front
            simple_title("<h1>매슬로우 욕구 1단계")  #욕구 두 줄 나올것.
            simple_title("<h3>생리적 욕구</h3>")  #욕구 두 줄 나올것.
            simple_body("""<p><pre>
<정의>
의식주를 포함하여 공기, 수면, 배설, 성욕 등 신체적 균형을 유지하기 위한 모든 요소가 포함됩니다.

<결핍>
심리 : 극도의 예민함과 무력감을 느끼며, 먹는 것이나 잠자는 것 외의 고차원적인 생각(공부, 연애 등)이 불가능해집니다.
행동 : 생존을 위한 본능적인 행동(폭식, 공격성)이 나타나며, 오직 결핍된 요소를 채우기 위한 수단에만 몰두합니다.
신체 : 에너지가 고갈되어 면역력이 급격히 떨어지고, 장기 기능 저하나 실신 등 생명 유지 장치에 비상이 걸립니다.            
</pre></p>""" )


        elif "2단계" in un_user:
            server_front
            simple_title("<h1>매슬로우 욕구 2단계</h1>")  #욕구 두 줄 나올것.
            simple_title("<h3>안전의 욕구</h3>")  #욕구 두 줄 나올것.
            simple_body("""<p><pre>
<정의>
신체적 안전뿐만 아니라 고용 안정, 경제적 보장, 건강 유지, 사고로부터의 보호 등을 포함합니다.

<결핍>
심리 : 미래에 대한 불확실성 때문에 늘 긴장 상태에 놓이며, 작은 변화에도 예민하고 방어적으로 반응하게 됩니다.
행동 : 새로운 도전보다는 현상 유지에 집착하게 되고, 심할 경우 강박적으로 안전을 확인하거나 타인을 쉽게 신뢰하지 못합니다.
신체 : 지속적인 스트레스로 인해 수면 장애나 소화 불량 같은 신체화 증상이 나타날 수 있으며, 이는 다시 1단계인 생리적 욕구를 위협합니다.            
</pre></p>""" )

            
        elif "3단계" in un_user:
            server_front
            simple_title("<h1>매슬로우 욕구 3단계</h1>")  #욕구 두 줄 나올것.
            simple_title("<h3>사회적 욕구</h3>")  #욕구 두 줄 나올것.
            simple_body("""<p><pre>
<정의>
가족, 친구, 동료와의 유대감을 통해 외로움을 극복하고, 특정 집단의 구성원으로서 수용되기를 바라는 본능적 욕구입니다.

<결핍>
심리 : 심각한 소외감과 고독감을 느끼며, 우울증이나 대인기피증 같은 정서적 불안이 발생합니다.
행동 : 타인의 눈치를 과하게 보며 집단에 집착하거나, 반대로 관계를 아예 차단하고 사회적으로 고립되는 행동을 보입니다.
신체 : 면역 체계가 약화되어 질병에 취약해지며, 스트레스로 인한 가슴 답답함이나 무기력증이 나타날 수 있습니다.
</pre></p>""" )

        elif "4단계" in un_user:
            server_front
            simple_title("<h1>매슬로우 욕구 4단계</h1>")  #욕구 두 줄 나올것
            simple_title("<h3>존중의 욕구</h3>")  #욕구 두 줄 나올것
            simple_body("""<p><pre>
<정의>
명성, 지위, 성취를 통해 타인에게 존중받으려는 욕구와 자신감, 독립심 등 스스로를 긍정하는 자존감이 포함됩니다

<결핍>
심리 : 심한 열등감과 무가치함을 느끼며, 타인의 비판에 극도로 예민해지고 자존감이 바닥으로 떨어집니다.
행동 : 인정받기 위해 과시적인 행동을 하거나, 반대로 비난이 두려워 성취를 포기하고 소극적으로 변합니다.
신체 : 만성적인 긴장으로 인한 두통, 만성 피로, 심리적 위축으로 인한 굽은 자세 등 신체적 활력이 저하됩니다.
</pre></p>""" )

        elif "5단계" in un_user:
            server_front
            simple_title("<h1>매슬로우 욕구 5단계</h1>")  #욕구 두 줄 나올것
            simple_title("<h3>자아실현의 욕구</h3>")  #욕구 두 줄 나올것
            simple_body("""<p><pre>
<정의>
개인의 성취, 창조적 활동, 문제 해결 등을 통해 삶의 의미를 찾고 자기 완성에 도달하려는 가장 높은 수준의 욕구입니다.

<결핍>
심리 : 삶의 목적 상실과 허무감을 느끼며, 재능이 썩고 있다는 느낌에 만성적인 권태와 불만족을 경험합니다.
행동 : 새로운 도전을 피하고 현실에 안주하며, 창의적인 활동보다는 기계적이고 반복적인 삶에 갇히게 됩니다.
신체 : 삶의 에너지가 저하되어 노화가 촉진되는 느낌을 받거나, 심리적 공허함이 육체적 무기력증으로 이어집니다.
</pre></p>""" )
        else:
            server_front
            simple_title("<h1>굿</h1>") 


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

