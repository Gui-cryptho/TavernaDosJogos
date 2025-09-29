import http.server
import socketserver
import os

# Define a porta na qual o servidor irá rodar
PORT = 8000

# Define o diretório que contém os arquivos do site
web_dir = os.path.join(os.path.dirname(__file__), '..', 'web', 'site')
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor rodando na porta {PORT}")
    print(f"Acesse http://localhost:{PORT} para ver o site.")
    httpd.serve_forever()
