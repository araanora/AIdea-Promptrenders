# Multilingual Chat Translator

A real-time chat application built with **Flask** and **Socket.IO** that automatically translates user and agent messages into the appropriate language.  
It uses **GoogleTranslator** from `deep-translator` for translations and `langdetect` to detect the user’s language.

---

## 🚀 Features

- Detects the user’s language automatically.
- Translates user messages into English for the agent.
- Translates agent responses back into the user’s language.
- Real-time messaging with **WebSockets** (`flask-socketio`).
- Maintains a chat history (retrievable via `/history` endpoint).

---

## 📦 Requirements

All dependencies are listed in `requirements.txt`:

- Flask `3.0.3`
- Flask-SocketIO `5.3.6`
- Deep-Translator `1.11.4`
- Python-SocketIO `5.11.2`
- Python-EngineIO `4.9.1`
- Langdetect (installed automatically with `deep-translator`)

---

## 🔧 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/multilingual-chat.git
   cd multilingual-chat

## Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

## Install dependencies:

pip install -r requirements.txt

## Run the app.py

python app.py

## Follow the link or open your browser at:

http://127.0.0.1:5000/

## ⚠️ Notes

- The app uses deep-translator which relies on Google Translate. Rate limits or failures may occur.
- Chat history is stored in memory and will reset when the server restarts.
- For production, update the SECRET_KEY in app.py.
