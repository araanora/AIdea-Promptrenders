from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from deep_translator import GoogleTranslator
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize SocketIO
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    original_message = data['message']
    
    # Translate the user's message to English
    try:
        translated_message = GoogleTranslator(source='auto', target='en').translate(original_message)
    except Exception as e:
        translated_message = "Error in translation. Please try again."

    # Define responses based on specific keywords or phrases
    if "facebook" in translated_message.lower() and "open" in translated_message.lower():
        response_message = "If you cannot open your Facebook account, try resetting your password or check if your account has been temporarily locked. You can also visit the Facebook Help Center for assistance."
    elif "how" in translated_message.lower() and "open" in translated_message.lower() and "browser" in translated_message.lower():
        response_message = "To open a browser, locate the browser icon on your desktop or in your applications menu and double-click it."
    elif "how are you" in translated_message.lower():
        response_message = "I'm just a program, but thanks for asking! How can I assist you today?"
    elif "translate" in translated_message.lower():
        response_message = "Sure! Please provide the text you'd like to translate, and specify the target language."
    else:
        response_message = "I'm sorry, I didn't understand that. Can you please rephrase?"

    emit('response', {'original_message': original_message, 'translated_message': response_message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
