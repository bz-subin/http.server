from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHendler(BaseHTTPRequestHandler):
    def do_GET(self):  # GET 요청 처리
        if self.path == '/':
            self.send_response(200)
            self.send_header("content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(
                """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Dynamic Webpage</title>
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
                            width: 70%;
                            height: 70%;
                        }

                        .background-image {
                            position: absolute;
                            top: 50%;
                            left: 50%;
                            transform: translate(-50%, -50%);
                            width: 70%;
                            height: 70%;
                            object-fit: cover;
                            opacity: 0.7; /* 투명도 70% */
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

                            // 모든 콘텐츠를 숨김
                            contents.forEach(content => {
                                content.classList.remove("active");
                            });

                            // 선택된 콘텐츠만 표시
                            if (selectedValue) {
                                document.getElementById(selectedValue).classList.add("active");
                            }
                        }
                    </script>
                </body>
                </html>
                """.encode()
            )
        elif self.path == '/img.jpg':  # 이미지 요청 처리
            try:
                with open("img.jpg", "rb") as file:
                    self.send_response(200)
                    self.send_header("Content-type", "image/jpeg")
                    self.end_headers()
                    self.wfile.write(file.read())
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