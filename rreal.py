from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote
import re

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
        <img src="cat.PNG" alt="Background" class="background-image">
        <div class="select-container">
            <select id="contentSelector" onchange="showContent()">
                <option value="">-- Select an option --</option>
                <option value="content1">Option 1</option>
                <option value="content2">Option 2</option>
                <option value="content3">Option 3</option>
            </select>
        </div>
    <script> //*동작이나 상호작용 추가

        function showContent() //*함수1
        {
            const selectedValue = document.getElementById("contentSelector").value;
            if (selectedValue) /*selectedValue가 저기 왜 있지? if문인데?*/ 
            { 
                fetch("http://localhost:8001", 
                {
                    method: "POST",
                    headers: 
                    {"Content-Type": "application/x-www-form-urlencoded"},
                    body: `option=${selectedValue}`,
                })
                .then(response => response.text())
                .then(data =>{
                    document.body.innerHTML = `
                        <div style="height:50px; display:flex; align-items:center; justify-content:center;">
                            <h1>${data}</h1>
                        </div>
                    `;
                            })
                .catch(error => console.error("Error:", error));
            }
        }
    </script>
</body>
</html>

    """.encode())
            
    # 파싱을 해야함. 왜? 맞는 부분을 찾아서 화면에 연결해야하기 때문
    # 어떻게 하지?
    # 일단 self.wfile_write를 변수에 넣음.
    # 그리고 그 변수를 split을 통해 <div>를 뿌셔서 나눔.
    #그럼 많은 부분이 나올거임. 걍 포킹 하면 안됨?


    def do_POST(self):
        con_length = int(self.headers.get("content-length",0)) #몇 글자인지 확인/못 찾으면 0 가져옴 
        user_data = self.rfile.read(con_length).decode() #읽기
        un_user = unquote(user_data) #16진수 -> 문자열 #*응답을 읽음

        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        if "content1" in un_user: #*여기가 잘 안 되는듯?
            print("1번 응답을 받았습니다.")
            self.wfile.write("""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                </head>
                <body>
                    <h1>This is the response for Option 1</h1>
                </body>
                </html>
                """.encode())
        elif "content2" in get_write:
            print("2번 응답을 받았습니다.")
            




        # elif selected_option == 'content2':
        #     print("2번 응답을 받았습니다.")
        #     self.wfile.write(response_content.encode('utf-8'))
        # elif selected_option == 'content3':
        #     print("3번 응답을 받았습니다.")
        #     self.wfile.write(response_content.encode('utf-8'))
        # else:
        #     print("4번 응답을 받았습니다.")
        #     self.wfile.write(response_content.encode('utf-8'))

        # 응답 전송




        
        # if self.path == '/':  #*self.path가 뭐노.
        #     self.send_response(200)
        #     self.send_header("content-type", "text/html; charset=utf-8")
        #     self.end_headers()

        # elif self.path == '/crycat.PNG':  #* 브라우저가==요청 했다면.
        #     try: #일단 고 
        #         with open("crycat.PNG", "rb") as file: 
        #             self.send_response(200)#아는 부분
        #             self.send_header("Content-type", "image/jpeg") #아는 부분
        #             self.end_headers()#아는 부분
        #             self.wfile.write(file.read())#아는 부분
        #     except FileNotFoundError:
        #         self.send_response(404)
        #         self.end_headers()
        #         self.wfile.write(b"Image not found")
        # else:
        #     self.send_response(404)
        #     self.end_headers()
        #     self.wfile.write(b"Page not found")

host = "localhost"

port = 8001

servers = HTTPServer((host, port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")

try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()