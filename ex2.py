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

def executar_comando():

    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language = "pt-BR")
            comando = comando.lower()
            print(comando)

            if 'luzia' in comando:
                comando = comando.replace('luzia', '')
                #maquina.say(comando)
                print(comando)
                maquina.runAndWait()

    except:
        print("Microfone não encontrado")

    return comando

def falar(texto):
    

#add loop para perguntar qlqr coisa e add um break pra poder sair do loop e encerrar o assistente#