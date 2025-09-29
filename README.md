# Taverna dos Jogos

Este é um projeto de um site simples para a "Taverna dos Jogos", que exibe cardápios de alimentos, bebidas e jogos.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
.
├── documents/              # Documentos e imagens do projeto
├── src/                    # Código fonte da aplicação
│   └── main.py             # Servidor web em Python
└── web/                    # Arquivos do site
    ├── data/               # Arquivos JSON com os dados dos cardápios
    │   ├── alimentos.json
    │   ├── bebidas.json
    │   └── jogos.json
    ├── site/               # Arquivos públicos do site
    │   ├── index.html      # Página principal
    │   ├── css/
    │   │   └── style.css   # Folha de estilos
    │   ├── image/
    │   │   └── table-lamp.png # Imagens
    │   └── js/
    │       └── script.js   # Scripts JavaScript
    └── template/           # Templates HTML
        ├── template_cardapio.html
        └── template_item.html
```

## Como Executar

Para visualizar o site, você precisa iniciar o servidor web local.

1.  **Pré-requisitos:**

    - Ter o [Python](https://www.python.org/downloads/) instalado.

2.  **Iniciando o Servidor:**

    - Abra um terminal na raiz do projeto.
    - Execute o seguinte comando:

    ```bash
    python src/main.py
    ```

3.  **Acessando o Site:**
    - Abra seu navegador de preferência e acesse a URL: [http://localhost:8000](http://localhost:8000)

O servidor irá servir os arquivos da pasta `web/site`, e a página `index.html` será carregada.
