import http.server
import socketserver
import json
import os

PORT = 8000
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
WEB_DIR = os.path.join(ROOT_DIR, 'web')
STATIC_DIR = os.path.join(WEB_DIR, 'site')


def render_template_section(template_path, json_path):
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            item_template = f.read()
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        items_html = ""
        for item in data:
            temp_item_html = item_template
            item_data = item.copy() # Cria uma cópia para não modificar o original

            # Garante que a chave 'imagem' exista e tenha um valor válido
            if 'imagem' not in item_data or not item_data['imagem']:
                item_data['imagem'] = "image/table-lamp.png" # Caminho para a imagem local padrão

            # Preenche o template com todos os dados da cópia
            for key, value in item_data.items():
                temp_item_html = temp_item_html.replace(f'{{{{{key}}}}}', str(value))
            
            items_html += f"<li>{temp_item_html}</li>"
        
        return items_html
    except FileNotFoundError as e:
        return f"<li>Erro: Arquivo não encontrado - {e.filename}.</li>"
    except Exception as e:
        return f"<li>Erro ao renderizar seção: {e}</li>"


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def do_GET(self):
        item_template_path = os.path.join(WEB_DIR, 'template', 'template_item.html')

        try:
            if self.path == '/cardapio.html':
                cardapio_path = os.path.join(STATIC_DIR, 'cardapio.html')
                bebidas_json_path = os.path.join(WEB_DIR, 'data', 'bebidas.json')
                alimentos_json_path = os.path.join(WEB_DIR, 'data', 'alimentos.json')

                html_bebidas = render_template_section(item_template_path, bebidas_json_path)
                html_alimentos = render_template_section(item_template_path, alimentos_json_path)

                with open(cardapio_path, 'r', encoding='utf-8') as f:
                    final_html = f.read()
                
                final_html = final_html.replace('<!--BEBIDAS_AQUI-->', html_bebidas)
                final_html = final_html.replace('<!--ALIMENTOS_AQUI-->', html_alimentos)

                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(final_html.encode('utf-8'))
            
            elif self.path == '/jogos.html':
                jogos_page_path = os.path.join(STATIC_DIR, 'jogos.html')
                jogos_json_path = os.path.join(WEB_DIR, 'data', 'jogos.json')

                html_jogos = render_template_section(item_template_path, jogos_json_path)

                with open(jogos_page_path, 'r', encoding='utf-8') as f:
                    final_html = f.read()

                final_html = final_html.replace('<!--JOGOS_AQUI-->', html_jogos)

                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(final_html.encode('utf-8'))

            else:
                super().do_GET()
                
        except Exception as e:
            self.send_error(500, f'Erro ao processar a requisição: {e}')


with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Servidor rodando na porta {PORT}")
    print(f"Acesse http://localhost:{PORT}/cardapio.html para ver o cardápio.")
    print(f"Acesse http://localhost:{PORT}/jogos.html para ver os jogos.")
    httpd.serve_forever()
