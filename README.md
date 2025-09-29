# 🌐 Real-time Translator Chat

A Flask + Socket.IO based **real-time bilingual chat application**.  
It lets a **User** and an **Agent** communicate in different languages while messages are automatically translated back and forth using **Google Translate** (via [deep-translator](https://pypi.org/project/deep-translator/)).

---

## 🚀 Features

- 🧑‍🤝‍🧑 **Dual chat panels** (User & Agent) side-by-side  
- 🌍 **Automatic language detection** (with `langdetect`)  
- 🔄 **Bi-directional translation** with `deep-translator`  
- ⚡ **Real-time communication** using Flask-SocketIO  
- 📜 **Chat history persistence** (in-memory for now)  
- 💾 **Download transcript** as `.txt`  
- 📎 **File attachment placeholders** (filename display)  
- 😀 **Emoji picker placeholder** (UI ready for integration)  

---

## 📂 Project Structure

realtime-translator-chat/
│── app.py # Flask backend with translation & sockets
│── requirements.txt # Python dependencies
│── templates/
│ └── index.html # Chat frontend (User + Agent panels)
└── README.md # Documentation

---

## 🛠️ Installation & Setup

Follow these steps to run the project on any machine:

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/realtime-translator-chat.git
cd realtime-translator-chat


# Create virtual environment
python -m venv venv

# Activate on Mac/Linux
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py

# By default, run on
http://127.0.0.1:5000/



