import speech_recognition as sr
import pyttsx3
import os
import datetime
import wikipedia
import webbrowser
import requests
import decouple

r = sr.Recognizer()
engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
speak("I am your assistant. How can I help you today?")

def take_user_input():
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak("processing")
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query

def open_camera():
    os.system('start microsoft.windows.camera:')

def open_notepad():
    os.startfile("C:\\Program Files\\Notepad++\\notepad++.exe")

def open_discord():
    os.startfile("C:\\Users\\KIIT\\AppData\\Local\\Discord\\app-1.0.9156\\Discord.exe")

def open_cmd():
    os.system('start cmd')

def open_calculator():
    os.startfile("C:\\Windows\\System32\\calc.exe")

greet_user()

while True:
    query = take_user_input().lower()

    if 'open camera' in query:
        open_camera()

    elif 'open notepad' in query:
        open_notepad()

    elif 'open discord' in query:
        open_discord()

    elif 'open cmd' in query:
        open_cmd()
        
    elif 'open calculator' in query:
        open_calculator()

    # Search Wikipedia
    elif 'what is' in query:
        speak('Searching Wikipedia...')
        query = query.replace('what is', '')
        results = wikipedia.summary(query, sentences=2)
        speak(results)

    # Search the web
    elif 'search' in query:
        speak('Searching the web...')
        query = query.replace('search', '')
        webbrowser.open(f"https://www.google.com/search?q={query}")

    # Get the current date and time
    elif 'what is the time' in query:
        speak(f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}")

    # Get the current date
    elif 'what is the date' in query:
        speak(f"The current date is {datetime.date.today()}")

    # Exit the chatbot
    elif 'exit' in query or 'stop' in query:
        hour = datetime.now().hour
        if hour >= 21 and hour < 6:
            speak("Good night sir, take care!")
        else:
            speak('Have a good day sir!')
        exit()