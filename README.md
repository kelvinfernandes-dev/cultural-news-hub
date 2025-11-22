# Cultural News Hub

<div align="center">

![Cultural News Hub](https://img.shields.io/badge/Django-5.0-green.svg)
![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![NewsAPI](https://img.shields.io/badge/NewsAPI-Integrated-orange.svg)
![Status](https://img.shields.io/badge/Status-Live-success.svg)

**Agregador inteligente de notícias culturais | Django + NewsAPI**

[🌐 Ver Demo](https://cultural-news-hub.onrender.com) • [📝 Reportar Bug](https://github.com/kelvinfernandes-dev/cultural-news-hub/issues)

</div>

---

## 📋 Sobre o Projeto

**Cultural News Hub** é um agregador de notícias culturais que permite explorar conteúdo global sobre **Cinema, Música, Arte, Literatura, Teatro, Games e TV** através da integração com a NewsAPI.

O projeto foi desenvolvido para demonstrar habilidades em **desenvolvimento backend com Django**, **integração de APIs externas**, **design responsivo** e **deploy em produção**.

A ideia para esse projeto veio de uma reflexão sobre nosso momento atual com a tecnologia. Decidi criar algo que simulasse o algoritmo de nossas redes sociais, mas com um "q" de aleatoriedade, garantindo ao usuário sempre aprender algo novo.
---

##  Funcionalidades

-  **Filtro por Temas Culturais**: Explore notícias por categoria (Cinema, Música, Arte, etc)
-  **Notícia Aleatória**: Descubra conteúdo novo com um clique
-  **100% Responsivo**: Experiência perfeita em mobile, tablet e desktop
-  **Interface Elegante**: Design inspirado no Washington Post
-  **Performance Otimizada**: Cache e otimizações para carregamento rápido
-  **Atualização Automática**: Busca notícias recentes via NewsAPI
-  **Deploy em Produção**: Aplicação rodando no Render

---

## Screenshots

### Home - Seletor de Temas
![Home](screenshots/home.gif)

---

## Tecnologias Utilizadas

### Backend
- **Django 5.2** - Framework web robusto
- **Python 3.13** - Linguagem de programação
- **Django REST Framework** - API REST
- **NewsAPI** - Fonte de notícias em tempo real

### Frontend
- **Tailwind CSS** - Framework CSS utilitário
- **JavaScript (Vanilla)** - Interatividade
- **HTML5** - Estrutura

### Database & Deploy
- **PostgreSQL** - Banco de dados em produção
- **SQLite** - Banco de dados em desenvolvimento
- **Render** - Plataforma de deploy
- **WhiteNoise** - Servir arquivos estáticos
- **Gunicorn** - WSGI HTTP Server

---

## Como Rodar Localmente

### Pré-requisitos

- Python 3.11+
- pip
- virtualenv
- Conta na [NewsAPI](https://newsapi.org/) (grátis)

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/kelvinfernandes-dev/cultural-news-hub.git
cd cultural-news-hub
```

2. **Crie e ative o ambiente virtual:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente:**
```bash
# Crie o arquivo .env na raiz do projeto
SECRET_KEY=sua-secret-key-aqui
DEBUG=True
NEWSAPI_KEY=sua-api-key-newsapi
ALLOWED_HOSTS=localhost,127.0.0.1
```

> **Como obter a NewsAPI Key:**
> 1. Acesse [newsapi.org/register](https://newsapi.org/register)
> 2. Crie uma conta gratuita
> 3. Copie sua API Key
> 4. Cole no arquivo `.env`

5. **Rode as migrações:**
```bash
python manage.py migrate
```

6. **Crie um superusuário (opcional):**
```bash
python manage.py createsuperuser
```

7. **Inicie o servidor:**
```bash
python manage.py runserver
```

8. **Acesse no navegador:**
```
http://127.0.0.1:8000
```

---

## Deploy

O projeto está configurado para deploy no **Render**. Para fazer seu próprio deploy:

1. Faça fork deste repositório
2. Crie uma conta no [Render](https://render.com) (a conta grátis consegue rodar tranquilamente esse projeto)
3. Crie um novo **Web Service**
4. Conecte seu repositório GitHub
5. Configure as variáveis de ambiente:
   - `SECRET_KEY`
   - `DEBUG=False`
   - `NEWSAPI_KEY`
   - `ALLOWED_HOSTS=.onrender.com`
6. Configure os comandos:
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn config.wsgi:application`
7. Deploy!

---

## Estrutura do Projeto
```
cultural-news-hub/
├── config/              # Configurações do Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── news/                # App principal
│   ├── models.py        # Models (Article, Favorite, etc)
│   ├── views.py         # Views
│   ├── services.py      # NewsAPI integration
│   ├── urls.py          # URLs
│   └── admin.py         # Admin config
├── templates/           # Templates HTML
│   └── news/
│       ├── base.html
│       ├── home.html
│       └── article_detail.html
├── static/              # Arquivos estáticos
├── requirements.txt     # Dependências Python
├── build.sh            # Script de build (Render - Basicamente aqui você explica ao render tudo que ele precisa instalar)
├── .env.example        # Exemplo de variáveis
├── .gitignore
└── README.md
```

---

## Roadmap

Funcionalidades planejadas:

- [ ] Sistema de favoritos
- [ ] Busca avançada de notícias
- [ ] Página 404 customizada
- [ ] Histórico de leitura por usuário
- [ ] Notificações de novas notícias
- [ ] Exportar notícias em PDF
- [ ] Modo escuro

---

## Aprendizados

Este projeto me permitiu desenvolver/aprimorar:

- ✅ Integração com APIs externas (NewsAPI)
- ✅ Arquitetura MVT do Django
- ✅ Service Layer para lógica de negócio
- ✅ Deploy em produção com Render
- ✅ Responsividade com Tailwind CSS
- ✅ Gerenciamento de variáveis de ambiente
- ✅ Banco de dados PostgreSQL em produção
- ✅ Otimização de performance (cache, queries)

---

## Autor

**Kelvin Fernandes**

Desenvolvedor Backend com 3 anos de experiência em Python, Django e FastAPI.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-kelvin--fernandes1718-blue?style=flat&logo=linkedin)](https://linkedin.com/in/kelvin-fernandes1718/)
[![GitHub](https://img.shields.io/badge/GitHub-kelvinfernandes--dev-black?style=flat&logo=github)](https://github.com/kelvinfernandes-dev)
[![Email](https://img.shields.io/badge/Email-kelvin.fe%40outlook.com-red?style=flat&logo=gmail)](mailto:kelvin.fe@outlook.com)

---

<div align="center">

**⭐ Se você gostou do projeto, dê uma estrela!**

Made with ❤️ and 🎵(Surfaces - Sunday best) by [Kelvin Fernandes](https://github.com/kelvinfernandes-dev)

Aos jovens que aqui chegaram...

</div>


