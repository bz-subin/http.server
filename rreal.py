from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

class MyHttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Initial Page</title>
            <style>
                body { font-family: sans-serif; text-align: center; }
            </style>
        </head>
        <body>
            <h1>옵션을 선택하세요</h1>
            <form action="/" method="post">
                <select name="option">
                    <option value="option1">Option 1</option>
                    <option value="option2">Option 2</option>
                    <option value="option3">Option 3</option>
                </select>
                <button type="submit">제출</button>
            </form>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(post_data)

        if 'option' in params:
            self.show_button_grid(params['option'][0])
        elif 'button_choice' in params:
            option = params.get('previous_option', ['unknown'])[0]
            button_num = params['button_choice'][0]
            self.show_final_page(option, button_num)

    def show_button_grid(self, option):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        buttons_html = ""
        for i in range(15):
            buttons_html += f'<button type="submit" name="button_choice" value="{100 + i}">{100 + i}</button>'

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