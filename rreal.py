from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
# parse_qs : URL의 쿼리스트링을 파싱하여 딕셔너리 형태로 반환하는 친구

class MyHttpRequestHandler(BaseHTTPRequestHandler): #class 선언
    def do_GET(self): #do_GET 생성
        self.send_response(200) #서버 상태 200
        self.send_header("Content-type", "text/html; charset=utf-8") #헤더 설정
        self.end_headers() #헤더 설정 끝!
        
        html = """  /*# 대충 맨 처음에 뜨는 화면인듯*/
        <!DOCTYPE html>
        <html>
        <head>
            <title>Page</title>
            <style>
                body { font-family: sans-serif; text-align: center; }
            </style>
        </head>
        <body>
            <h1 style="margin-top:380px">옵션을 선택하세요</h1>
            <form action="/" method="post">
                <select name="option">
                    <option value="button_choice">button_choice</option>
                    <option value="option1">Option 1</option>
                    <option value="option2">Option 2</option>
                    <option value="option3">Option 3</option>
                </select>
                <button type="submit">전송</button>
            </form>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8")) #맞네

    def do_POST(self): #이게 대충 사용자의 입력에 따른 결과를 보여주겠다 이거잖슴
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8') #읽은게 쿼리스트링인가?
        params = parse_qs(post_data)  #이게 그거잔슨 그 쿼리스트링을 파싱해서 딕셔너리로 바꾸는

        if 'option' in params: #사용자의 선택에 "option"이 포함됨?

# show_button_grid에 read내용 안에서 option의 0번째를 쓰겠다.
# option1을 고르던 option2를 고르던 어짜피 값은 option[0]
            self.show_button_grid(params['option'][0]) 


        elif 'button_choice' in params: # 사용자의 선택에 "버튼초이스"가 포함됨?
            option = params.get('previous_option', ['unknown'])[0]
            button_num = params['button_choice'][0]
            self.show_final_page(option, button_num)
        # else:


    def show_button_grid(self, option): #버튼 뭐 보여주다 그리드
        self.send_response(200) 
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        


        buttons_html = "" #버튼 html은 없음.
        for i in range(15):#반복한다. 15번. i에는 0~14까지 넣을것.
            buttons_html += f'<button type="submit" name="button_choice" value="{100 + i}">{100 + i}</button>'
            #버튼 html에 더하고 넣는다(반복함) submit라는 버튼을 
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Button Grid</title>
            <style>
                body {{ text-align: center; }}
                h1 {{ margin-top: 30px; }}
                .button-container {{
                    margin-top: 30px;
                    display: grid;
                    grid-template-columns: repeat(5, 1fr);
                    gap: 10px;
                    justify-items: center;
                    max-width: 800px;
                    margin-left: auto;
                    margin-right: auto;
                }}
                .button-container button {{
                    width: 100px;
                    height: 50px;
                    font-size: 20px;
                    position: relative;
                }}
            </style>
        </head>
        <body>
            <h1>제목</h1>
            <form action="/" method="post">
                <input type="hidden" name="previous_option" value="{option}">
                <div class="button-container">
                    {buttons_html}
                </div>
            </form>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

    def show_final_page(self, option, button_num):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Final Page</title>
            <style>
                body {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
            </style>
        </head>
        <body>
            <h1>선택한 번호: {button_num} (이전 선택: {option})</h1>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

def run(server_class=HTTPServer, handler_class=MyHttpRequestHandler, port=8001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

port = 8001

servers = HTTPServer((host, port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")

try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()

port = 8001

servers = HTTPServer((host, port), MyRequestHendler)
print(f"서버가 시작되었습니다. http://{host}:{port}로 접속하세요!")

try:
    servers.serve_forever()
except KeyboardInterrupt:
    servers.server_close()