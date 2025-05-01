import speech_recognition as sr
import pyttsx3
import datetime 
import webbrowser
import wikipedia
import pywhatkit
import os

audio = sr.Recognizer()
maquina = pyttsx3.init()

maquina.say("Olá, eu sou a Luzia, Como posse te ajudar?")
maquina.runAndWait()