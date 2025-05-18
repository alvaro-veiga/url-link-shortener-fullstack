# URL Link Shortener

Um aplicativo fullstack moderno para encurtamento de URLs, construído com Django e React.

![URL Shortener](https://img.shields.io/badge/URL-Shortener-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)
![React](https://img.shields.io/badge/React-18-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)
![Material-UI](https://img.shields.io/badge/Material--UI-5.0-purple)

## 🚀 Funcionalidades

- ✨ Encurtamento de URLs
- 📊 Estatísticas de cliques
- 📋 Cópia rápida para área de transferência
- 🎨 Interface moderna e responsiva
- 🔒 URLs únicas e seguras
- 📱 Design mobile-friendly

## 🛠️ Tecnologias Utilizadas

### Backend
- Django 5.2
- Django REST Framework
- SQLite (desenvolvimento)
- CORS Headers

### Frontend
- React 18
- TypeScript
- Material-UI
- Axios
- Vite

## 📋 Pré-requisitos

- Python 3.8+
- Node.js 16+
- npm ou yarn

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/url-link-shortener-fullstack.git
cd url-link-shortener-fullstack
```

2. Configure o ambiente virtual Python:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências do backend:
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

4. Em outro terminal, configure o frontend:
```bash
cd frontend
npm install
npm run dev
```

## 🌐 Uso

1. Acesse o frontend em `http://localhost:5173`
2. Cole a URL que deseja encurtar
3. Clique em "Encurtar URL"
4. Use o botão de copiar para compartilhar sua URL encurtada

## 📚 API Endpoints

### Criar URL encurtada
```http
POST /api/urls/
Content-Type: application/json

{
    "original_url": "https://exemplo.com"
}
```

### Obter estatísticas
```http
GET /api/stats/{short_code}/
```

### Redirecionar para URL original
```http
GET /{short_code}/
```

## 🎨 Interface

O projeto utiliza Material-UI para uma interface moderna e responsiva, com:
- Design limpo e minimalista
- Feedback visual para ações do usuário
- Estatísticas em tempo real
- Suporte a temas claro/escuro

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📫 Contato


Link do Projeto: [https://github.com/alvaro-veiga/url-link-shortener-fullstack](https://github.com/alvaro-veiga/url-link-shortener-fullstack)
