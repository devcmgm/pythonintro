import SimpleHTTPServer
import SocketServer

PORT = 8000

#Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    
  def do_GET(self):
   # self.send_header("Content-type", "text/html")
    self.send_response(200, "Works")
    
Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()