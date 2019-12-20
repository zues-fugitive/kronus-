import pyttsx3
import speech_recognition as sr 
import datetime 
import wikipedia
import webbrowser
import os 
import smtplib
import random
import sys
import pylint
import pyaudio
import multiprocessing
import PIL.ImageFile
import microphone.pyaudio_
import vexmessage
import pluginmanager

#print("Initializing Jarvis")

MASTER = "CHARLES"
 
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id )

#Speak functon would pronounce the string which is passed to it 
def speak(audio):
    print('computer: '+ audio)
    engine.say(audio)
    engine.runAndWait()

#This function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour) 

    if hour>=0 and hour <12:
        speak("Good Morning!!.." + MASTER)

    elif hour>=12 and hour<18:
        speak("Good. Afternoon!!.." + MASTER)

    else:
        speak("Good. Evening!!.." + MASTER)
    
    speak("WELCOME SIR!!!!..")
    speak("I am KRONUS!!!..")
    speak("How may i be of assistance today. SIR!?")

# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
         
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, Language = 'en-us')  
        print(f"user said: {query}\n")

    except Exception as e:
        speak("please can you repeat that")
        query = None

    return query 
     
#Main program starts here...
speak("Initializing..KRONUS.....")
wishMe()
query = takeCommand()

# Logic for executing tasks as per the query
if 'Wikipedia' in query.lower(): 
    speak('searching wikipedia....')
    results = wikipedia.summary(query, sentences=2)
    query = query.replace("wikipedia", "")   
    print(results)
    speak(results)

if 'open youtube' in query.lower():
        webbrowser.open("youtube.com")
elif 'music' in query.lower():
    print("opening music")
elif'video' in query.lower():
    print("opening videos now")
    speak("opening videos sir...")
