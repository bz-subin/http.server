from http.server import HTTPserver, BaseHTTPRequestHandler
import datetime
date=datetime.datetime.now()
    class Myhandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.sent.response(200)
            self.sent.head("content-type, text/html; encoding=utf-8")
            self.sent.header()
            self.wfile.write("<h1>제목이에용, {now}</h1>")
