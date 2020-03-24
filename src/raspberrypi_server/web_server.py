import http.server, socketserver

PORT = 15556
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(('', PORT), Handler, True)
print("Serveur Web actif sur le port :", PORT)
httpd.serve_forever()