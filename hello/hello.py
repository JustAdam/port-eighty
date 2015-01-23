import SimpleHTTPServer
import StringIO
import SocketServer
import os
import sys

PORT = int(os.environ['PORT'])
MESSAGE = ' '.join(sys.argv[1:])

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def send_head(self):
        self.send_response(200)
        self.send_header("Content-type", 'text/plain')
        self.end_headers()
        return StringIO.StringIO(MESSAGE)

httpd = SocketServer.TCPServer(("", PORT), MyHandler)

print "serving at port", PORT
httpd.serve_forever()
