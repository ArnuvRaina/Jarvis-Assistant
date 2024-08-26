import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import groq
from config import apikey
import datetime
import sys
import numpy as np
import getpass
import wikipedia
import ctypes 
import win32gui
import win32con

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    

def wishMe():
    user = getpass.getuser()
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://w  ww.google.com"], ["gmail", "https://mail.google.com"]]
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
        
    speak("I am your assistant. How can I help you today?")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"
        
        
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
    
def exit_jarvis():
    speak("Exiting, goodbye!")
    sys.exit()
    
def minimize_program():
    user32 = ctypes.windll.user32
    hWnd = user32.GetForegroundWindow()
    user32.ShowWindow(hWnd, 6)  # 6 = SW_MINIMIZE
    speak("Minimizing the current window")

def close_program():
    hWnd = win32gui.GetForegroundWindow()
    ctypes.windll.user32.PostMessageW(hWnd, win32con.WM_CLOSE, 0, 0)
    speak("Closing the current program")


chatStr = ""
'''def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"{query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]'''


'''def ai(prompt):
    openai.api_key = apikey
    text = f"AI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)'''


if __name__ == '__main__':
    speak("Welcome to Jarvis A I")
    wishMe() 
    user = getpass.getuser()  
        
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"], ["gmail", "https://mail.google.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]}...")
                webbrowser.open(site[1])

        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak(f"The current time is {hour} hours and {min} minutes ")

        elif "open spotify" in query.lower():
            os.startfile(r"C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.244.405.0_x64__zpdnekdrzrea0\\Spotify.exe")
            speak("Opening Spotify Desktop Application")
            chatStr = ""

        elif "open chrome" in query.lower() or "open google chrome" in query.lower():
            os.startfile(r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            speak("Opening Google Chrome Browser")
            chatStr = ""

        # elif "using artificial intelligence" in query.lower():
        #     ai(prompt=query)

        elif "goodbye" in query.lower() or "bye" in query.lower() or "exit" in query.lower():
            speak("Goodbye, have a great day!")
            break

        elif "reset chat" in query.lower():
            chatStr = ""

        elif 'open camera' in query.lower():
            open_camera()
            speak("Opening Camera")

        elif 'open notepad' in query.lower():
            open_notepad()
            speak("Opening Notepad")

        elif 'open discord' in query.lower():
            open_discord()
            speak("Opening Discord")

        elif 'open cmd' in query.lower():
            open_cmd()
            speak("Opening Command Prompt")
        
        elif 'open calculator' in query.lower():
            open_calculator()
            speak("Opening Calculator")

        
        elif 'what is' in query.lower():
            speak('Searching Wikipedia...')
            query = query.replace('what is', '')
            try:
                results = wikipedia.summary(query, sentences=2)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Your query is too ambiguous. Please be more specific.")
                print(e.options)
            except Exception as e:
                speak("Sorry, I couldn't find any relevant information.")
                print(e)
                
        elif 'tell me more about' in query.lower():
            speak('Searching Wikipedia...')
            query = query.replace('tell me more about', '')
            try:
                results = wikipedia.summary(query, sentences=2)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Your query is too ambiguous. Please be more specific.")
                print(e.options)
            except Exception as e:
                speak("Sorry, I couldn't find any relevant information.")
                print(e)
                
        elif 'search' in query.lower():
            speak('Searching the web...')
            query = query.replace('search', '')
            webbrowser.open(f"https://www.google.com/search?q={query}")
            
        elif "close assistant" in query.lower():
            exit_jarvis()
        
        elif "close program" in query.lower():
            close_program()
            
        elif "minimise" in query.lower():
            minimize_program()

















































