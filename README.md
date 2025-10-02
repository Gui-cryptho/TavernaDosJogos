# Taverna dos Jogos

Este é um projeto de um site responsivo para a "Taverna dos Jogos", um estabelecimento que combina jogos de tabuleiro com comidas e bebidas. O site apresenta um carrossel de imagens na página inicial e exibe cardápios de alimentos, bebidas e jogos disponíveis.

## Funcionalidades

- **Carrossel de Imagens**: Apresentação automática de imagens na página inicial

  - Transição automática a cada 2.5 segundos
  - Controles de navegação (botões e pontos)
  - Pausa automática ao passar o mouse
  - Imagens responsivas que se ajustam ao tamanho do container

- **Cardápios Interativos**:

  - Alimentos
  - Bebidas
  - Jogos de Tabuleiro

- **Design Responsivo**:
  - Layout adaptável para diferentes tamanhos de tela
  - Fontes da Google Fonts para melhor legibilidade
  - Ícone personalizado na guia do navegador (favicon)

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
.
├── documents/                    # Documentos e imagens do projeto
│   └── Capturas de tela/        # Capturas de tela do projeto
├── src/                         # Código fonte da aplicação
│   └── main.py                  # Servidor web em Python
└── web/                         # Arquivos do site
    ├── data/                    # Arquivos JSON com os dados dos cardápios
    │   ├── alimentos.json       # Dados dos alimentos
    │   ├── bebidas.json        # Dados das bebidas
    │   └── jogos.json          # Dados dos jogos disponíveis
    ├── site/                    # Arquivos públicos do site
    │   ├── index.html          # Página principal com carrossel
    │   ├── jogos.html          # Página de jogos disponíveis
    │   ├── cardapio.html       # Página do cardápio de alimentos e bebidas
    │   ├── css/
    │   │   └── style.css       # Estilos do site (responsivo)
    │   ├── image/              # Imagens do site
    │   │   ├── knight.png      # Favicon do site
    │   │   ├── king.png        # Imagem do carrossel
    │   │   ├── cerveja.png     # Imagem do carrossel
    │   │   ├── hamburguer.png  # Imagem do carrossel
    │   │   ├── pizza.png       # Imagem do carrossel
    │   │   └── table-lamp.png  # Imagem padrão
    │   └── js/
    │       └── carousel.js     # Script do carrossel de imagens
    └── template/               # Templates HTML para geração dinâmica
        ├── template_cardapio.html  # Template base do cardápio
        └── template_item.html      # Template para itens individuais
```

## Tecnologias Utilizadas

- **Frontend**:

  - HTML5
  - CSS3 (com flexbox e grid)
  - JavaScript (ES6+)
  - Google Fonts (Montserrat)

- **Backend**:
  - Python 3
  - Servidor HTTP integrado
  - Manipulação de JSON

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

## Recursos

- Template system para geração dinâmica de conteúdo
- Dados armazenados em arquivos JSON para fácil manutenção
- Servidor Python customizado com suporte a MIME types
- Interface intuitiva e amigável

## Desenvolvimento

O projeto foi desenvolvido com foco em:

- Código limpo e organizado
- Separação de responsabilidades (HTML, CSS, JS)
- Performance e otimização de imagens
- Experiência do usuário (UX)
- Manutenibilidade e escalabilidade
