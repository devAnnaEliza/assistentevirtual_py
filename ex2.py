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


#add loop para perguntar qlqr coisa e add um break pra poder sair do loop e encerrar o assistente#