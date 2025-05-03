import speech_recognition as sr
import pyttsx3
import datetime 
import webbrowser
import wikipedia
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

def comando_voz_usuario():
    comando = executar_comando()

    if 'horas' in comando:
        horas = datetime.datetime.now().strftime('%H:%M')
        maquina.say("Agora são " + horas)
        print(f'Agora são {horas}.')
        maquina.runAndWait()
    elif 'youtube' in comando:
        webbrowser.open('https://www.youtube.com')
        exit()
    elif 'procurar por' in comando:
        procurar = comando.replace('procurar por', '')
        wikipedia.set_lang('pt-BR')
        resultado = wikipedia.summary(procurar, 2)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'calculadora' in comando:
        loc = 'C:\\Windows\\System32\\calc.exe'
        os.startfile(loc)
    
    elif 'tchau' in comando:
        maquina.say('Adeus, até mais!')
        maquina.runAndWait()

comando_voz_usuario()