from flask import Flask, render_template, request, jsonify
import pyttsx3
import speech_recognition as sr

app = Flask(__name__)

# Инициализация движка для синтеза речи
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_command', methods=['POST'])
def process_command():
    command = request.form['command']

    # Здесь вы можете добавить дополнительные команды
    if command.lower() == "привет":
        response = "Привет! Как я могу помочь?"
    elif command.lower() == "как дела?":
        response = "У меня всё хорошо, спасибо за вопрос!"
    else:
        response = "Извините, я не понимаю команду."

    # Озвучиваем ответ
    speak(response)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)