import speech_recognition as sr
import pyttsx3
import datetime 
import webbrowser
#import pywhatkit#
import os
from transformers import pipeline

audio = sr.Recognizer()
maquina = pyttsx3.init()

nlp = pipeline("text-classification", model="distilbert-base-uncased")

maquina.say("Olá, eu sou a Luzia, Como posso te ajudar?")
maquina.runAndWait()

def falar(texto):
    maquina.say(texto)
    maquina.runAndWait()

#comandos de voz
def dizer_horas():
    horas = datetime.datetime.now().strftime("%H?%M")
    falar(f"Agora são {horas}")
    print(f"Agora são {horas}")

def encerrar_assistente():
    falar("Adeus, até logo!")
    exit()

def abrir_youtube():
    webbrowser.open("https://www.youtube.com")
    falar("Abrindo YouTube")

def abrir_calculadora():
    loc = 'C:\\Windows\\System32\\calc.exe'

def encerrar_assistente():
    falar("Até mais!")
    exit()

def interpretar_comando(comando):
    resultado = nlp(comando)
    print(f"Interpretação do resiltado: {resultado}")
    label = resultado[0]["label"]
    if "time" in label or "hour" in comando:
        dizer_horas()
    elif "youtube" in comando:
        abrir_youtube()
    elif "exit" in comando or "bye" in comando:
        encerrar_assistente()
    else:
        falar("Desculpe, não entendi.")
    
def ouvir_comando():
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language="pt-BR")
            comando = comando.lower()
            print(f"Você disse: {comando}")
            return comando
    except sr.UnknownValueError:
        falar("Desculpe, não entendi o que você disse.")
        return ""
    except sr.RequestError:
        falar("Desculpe, não consigo acessar o serviço de reconhecimento de voz.")
        return ""
    
#add loop para perguntar qlqr coisa e add um break pra poder sair do loop e encerrar o assistente#