import speech_recognition as sr
import pyttsx3
import datetime 
import webbrowser
#import pywhatkit#
import os

audio = sr.Recognizer()
maquina = pyttsx3.init()

maquina.say("Olá, eu sou a Luzia, Como posso te ajudar?")
maquina.runAndWait()

def falar(texto):
    maquina.say(texto)
    maquina.runAndWait()


#add loop para perguntar qlqr coisa e add um break pra poder sair do loop e encerrar o assistente#