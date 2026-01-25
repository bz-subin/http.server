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
        <title>page</title>
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
        <h1 style="font-size: 50px;">제목</h1>
        <img src="crycat.PNG" alt="Background" class="background-image">
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
        const titles = ["1번임", "2번임", "3번임", "4번임", "5번임"];
        const buttons = ["1번", "2번", "3번", "4번", "5번"];

        function showContent() {
            const selectedValue = document.getElementById("contentSelector").value;
            if (selectedValue === "content1") {
                showScreen(0);
            } else if (selectedValue === "content2") {
                showScreen(1);
            } else if (selectedValue === "content3") {
                showScreen(2);
            }
        }

        function showScreen(index) {
            const title = titles[index];
            const buttonHtml = buttons.map(btn => `<button>${btn}</button>`).join('');
            document.body.innerHTML = `
                <div style="height:50px; display:flex; align-items:center; justify-content:center;">
                    <h1>${title}</h1>
                </div>
                <div style="display:flex; flex-wrap:wrap;">
                    ${buttonHtml}
                </div>
            `;
        }

        function showDetail(num) {
            const title = num === 1 ? "첫번째" : "두번째";
            document.body.innerHTML = `
                <h1>${title}</h1>
                <input type="text" id="chatInput" placeholder="메시지를 입력하세요">
                <button onclick="sendMessage()">전송</button>
                <div id="messages" style="border:1px solid #ccc; height:200px; overflow-y:scroll;"></div>
                <div style="height:10px; position:fixed; bottom:0; width:100%; background-color:lightgray; text-align:center; line-height:10px; font-size:10px;">모든 내용은 저녁 12시에 삭제됩니다</div>
            `;
            loadMessages();
        }

        function sendMessage() {
            const input = document.getElementById('chatInput');
            const msg = input.value.trim();
            if (msg) {
                const messages = JSON.parse(localStorage.getItem('chatMessages') || '[]');
                messages.push(msg);
                localStorage.setItem('chatMessages', JSON.stringify(messages));
                input.value = '';
                displayMessages();
            }
        }

        function loadMessages() {
            displayMessages();
            // 매일 00:00에 메시지 삭제
            setInterval(() => {
                const now = new Date();
                if (now.getHours() === 0 && now.getMinutes() === 0 && now.getSeconds() === 0) {
                    localStorage.removeItem('chatMessages');
                    displayMessages();
                }
            }, 1000); // 1초마다 체크
        }

        function displayMessages() {
            const messages = JSON.parse(localStorage.getItem('chatMessages') || '[]');
            const div = document.getElementById('messages');
            div.innerHTML = messages.map(m => `<p>${m}</p>`).join('');
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

        elif self.path == '/crycat.PNG':  #* 브라우저가==요청 했다면.
            try: #일단 고 
                with open("crycat.PNG", "rb") as file: 
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

host = "localhost"

port = 8001

servers = HTTPServer((host, port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")

try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()