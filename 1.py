import speech_recognition as sr
import pyttsx3
import datetime 
import webbrowser
import wikipedia
#import pywhatkit#
import os

audio = sr.Recognizer()
maquina = pyttsx3.init()

maquina.say("Olá, eu sou a Luzia, Como posse te ajudar?")
maquina.runAndWait()

with sr.Microphone() as source:
    print("Ouvindo...")
    voz = audio.listen(source)
    comando = audio.recognize_google(voz, language = "pt-BR")
    comando = comando.lower()
    print(comando)

    if 'luzia' in comando:
        comando = comando.replace('luzia', '')
        maquina.say(comando)
        maquina.runAndWait()