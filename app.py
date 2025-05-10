from flask import Flask, request, jsonify
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

app = Flask(__name__)

# Inicializa o reconhecimento de voz e o mecanismo de síntese de voz
maquina = pyttsx3.init()

def falar(texto):
    maquina.say(texto)
    maquina.runAndWait()

@app.route('/comando', methods=['POST'])
def processar_comando():
    data = request.json
    comando = data.get('comando', '').lower()

    if "horas" in comando:
        horas = datetime.datetime.now().strftime('%H:%M')
        resposta = f"Agora são {horas}"
    elif "youtube" in comando:
        webbrowser.open('https://www.youtube.com')
        resposta = "Abrindo o YouTube"
    elif "calculadora" in comando:
        os.startfile('C:\\Windows\\System32\\calc.exe')
        resposta = "Abrindo a calculadora"
    elif "tchau" in comando:
        resposta = "Encerrando o assistente. Até mais!"
    else:
        resposta = "Desculpe, não entendi o comando."

    falar(resposta)
    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)