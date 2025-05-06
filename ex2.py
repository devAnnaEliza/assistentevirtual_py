import tkinter as tk
from tkinter import Label, Button

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

def falar(texto):
    maquina.say(texto)
    maquina.runAndWait()

#comandos de voz
def dizer_horas():
    horas = datetime.datetime.now().strftime("%H?%M")
    falar(f"Agora são {horas}")
    print(f"Agora são {horas}")

def abrir_youtube():
    webbrowser.open("https://www.youtube.com")
    falar("Abrindo YouTube")

def abrir_calculadora():
    loc = 'C:\\Windows\\System32\\calc.exe'
    os.startfile(loc)
    falar("Abrindo calculadora")

def encerrar_assistente():
    falar("Até mais!")
    root.destroy()
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
    
#loop 
def iniciar_assistente():
    falar("Olá, eu sou a Luzia. Como posso ajudar?")
    while True:
        comando = ouvir_comando()
        if comando:
            interpretar_comando(comando)

#interface
root = tk.Tk()
root.Title("Assistente Virtual Luzia")
root.geometry("400x300")

label = Label(root, text="Assistente Virtual Luzia", font=("Arial", 16))
Label.pack(pady=20)

botao_iniciar = Button(root, text="Iniciar Assistente", command=iniciar_assistente, font=("Arial", 14))
botao_iniciar.pack(pady=10)

botao_encerrar = Button(root, text="Encerrar Assistente",command=encerrar_assistente, font=("Arial", 14))
botao_encerrar.pack(pady=10)

falar("Bem-vindo a Assistente Virtual Luzia!")