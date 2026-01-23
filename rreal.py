from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote

class MyRequestHendler(BaseHTTPRequestHandler):
    def do_GET(self): 
            self.send_response(200)
            self.send_header("content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
        <meta charset="UTF-8"> 
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
        <title>Custom Webpage</title>
            <style>
                body { 
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center; 
                align-items: center; 
                height: 100vh; 
                background-color: #000;
                color: white; 
                font-family: Arial, sans-serif; 
            }

        .container { 
            position: relative; 
            width: 80%;
            height: 80%;
        }

        .container h1 { 
            position: absolute; 
            top: -5%; 
            left: 50%; 
            transform: translateX(-50%); 
            z-index: 2; 
            color: white; 
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8); 
        }

        .background-image {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 70%;
            height: 70%;
            object-fit: cover;
            opacity: 0.7;
            z-index: 1;
        }

        .select-container {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 2;
            text-align: center;
        }

        select {
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            border: none;
            outline: none;
        }

        .content {
            display: none;
            position: absolute;
            top: 80%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 3;
            background-color: rgba(0, 0, 0, 0.8);
            padding: 20px;
            border-radius: 10px;
        }

        .content.active {
            display: block;
        }
    </style>
</head>
<body>
    <div class="container">
        <<h1 style="font-size: 50px;">제목</h1>
        <img src="img.jpg" alt="Background" class="background-image">
        <div class="select-container">
            <select id="contentSelector" onchange="showContent()">
                <option value="">-- Select an option --</option>
                <option value="content1">Option 1</option>
                <option value="content2">Option 2</option>
                <option value="content3">Option 3</option>
            </select>
        </div>
        <div id="content1" class="content">This is the content for Option 1.</div>
        <div id="content2" class="content">This is the content for Option 2.</div>
        <div id="content3" class="content">This is the content for Option 3.</div>
    </div>

    <script>
        function showContent() {
            const selectedValue = document.getElementById("contentSelector").value;
            const contents = document.querySelectorAll(".content");

            contents.forEach(content => {
                content.classList.remove("active");
            });

            if (selectedValue) {
                document.getElementById(selectedValue).classList.add("active");
            }
        }
    </script>
</body>
</html>

    """.encode())

    def do_POST(self): # 숨겨서 보여줌(아이디, 비밀번호)
        print("응답을 받았습니다.")


        # con_length = self.headers.get("content-length",0) #몇 글자인지 확인/못 찾으면 0 가져옴 
        # con_length = int(con_length)
        # 입력한 문자의 길이만큼 읽기 때문에, 읽기한 부분을 변수로 만든 뒤 나중에 출력 할 떄 그 변수를 decode 해야함.
        user_data = self.rfile.read(con_length).decode() #읽기
        un_user = unquote(user_data) #16진수 -> 문자열 #*응답을 읽음
        
        if self.path == '/':  #*self.path가 뭐노.
            self.send_response(200)
            self.send_header("content-type", "text/html; charset=utf-8")
            self.end_headers()

        elif self.path == '/img.jpg':  #* 브라우저가==요청 했다면.
            try: #일단 고 
                with open("img.jpg", "rb") as file: 
                    self.send_response(200)#아는 부분
                    self.send_header("Content-type", "image/jpeg") #아는 부분
                    self.end_headers()#아는 부분
                    self.wfile.write(file.read())#아는 부분
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Image not found")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Page not found")

# 지금 대충 그림 띄우고 그림에 대해서 나누겠다 는 느낌으로 놨음. 하다보면 부족할것임.

# <홈 화면>
# 1. 제목
#    <h1 style="font-size: 50px;">제목</h1>
# 2. 그림 전체의 80% 크기로 띄움. (투명도 70%)
# 3. 선택창 그 위에 select 띄움. (중앙에 가장 보기 좋게)

# <select 선택에 따른 내용>
# 1. 제목 
#    <h1 style="font-size: 50px;">제목</h1>
# 2. 여러개의 버튼을 만들어서 누르면 창에 연결되게끔 할 것.
# 3. 배경 사진을 띄울것.

# <submit 선택에 따른 내용>
# 1. 카톡 같은 느낌으로 만들기.(맨 위 제목)
#   아이콘 뜨게
#   대화 치면 한글자씩 연결되며 뜨게끔.



host = "localhost"
port = 8001

servers = HTTPServer((host, port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")

try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()