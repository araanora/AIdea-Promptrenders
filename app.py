from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from datetime import datetime

DetectorFactory.seed = 0  # Ensure consistent language detection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Store last detected user language
last_user_language = {'lang': 'en'}

# Store chat history
chat_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history', methods=['GET'])
def get_history():
    return jsonify(chat_history)

@socketio.on('user_message')
def handle_user_message(data):
    original_message = data.get('message', '')
    try:
        detected_lang = detect(original_message)
        last_user_language['lang'] = detected_lang
        translated = GoogleTranslator(source=detected_lang, target='en').translate(original_message)
    except Exception as e:
        detected_lang = 'unknown'
        translated = original_message

    message_data = {
        'sender': 'user',
        'original': original_message,
        'translated': translated,
        'original_lang': detected_lang,
        'translated_lang': 'en',
        'timestamp': datetime.utcnow().isoformat()
    }

    chat_history.append(message_data)
    emit('chat_message', message_data, broadcast=True)

@socketio.on('agent_message')
def handle_agent_message(data):
    original_message = data.get('message', '')
    target_lang = last_user_language.get('lang', 'en')

    try:
        translated = GoogleTranslator(source='en', target=target_lang).translate(original_message)
    except Exception as e:
        translated = "Translation failed"

    message_data = {
        'sender': 'agent',
        'original': original_message,
        'translated': translated,
        'original_lang': 'en',
        'translated_lang': target_lang,
        'timestamp': datetime.utcnow().isoformat()
    }

    chat_history.append(message_data)
    emit('chat_message', message_data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
