# 💬 WebChatFuria

**WebChatFuria**  é uma aplicação web de chat em tempo real criada especialmente para os fãs da equipe de eSports FURIA, com foco na comunidade de Counter-Strike. Mais do que um simples chat, a plataforma integra um chatbot com comandos predefinidos, permitindo interações automáticas, como respostas a mensagens específicas, envio de conteúdos temáticos, ou reações baseadas em palavras-chave.
O público-alvo são torcedores que acompanham os jogos da FURIA e querem se informar sobre o time e se divertir com um bot que entende a linguagem da comunidade.

---

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-Cors](https://corydolphin.com/flask-cors/)
- HTML5
- CSS3
- JavaScript

---

## 📁 Estrutura do Projeto

```
WebChatFuria/
├── app.py               # Servidor Flask principal
├── static/
│   ├── style.css        # Estilo da página
│   └── script.js        # Lógica do frontend
├── templates/
│   └── index.html       # Página principal do chat
├── attaches/            # Diretório para arquivos enviados
└── .vscode/             # Configurações do editor (opcional)
```

---

## 🛠️ Como Executar Localmente

### 1. Clone o repositório
```bash
git clone https://github.com/pedrohenriferreira/WebChatFuria.git
cd WebChatFuria
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)
Utilizei o Postman para isso.

### 3. Instale as dependências
```bash
pip install flask
pip install flask-cors
```

### 4. Execute o servidor
```bash
python app.py
```

### 5. Acesse no navegador
```
127.0.0.1:5500/index.html
```

---

## ✨ Funcionalidades

- Comunicação em tempo real via WebSocket.
- Interface web responsiva.
- Um chatbot integrado com comandos predefinidos.
