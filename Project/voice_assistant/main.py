'''STARK : The Voice Assistant's implementation'''

import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

'''setting the engine to Pyttsx3 which is used for text to speech in Python, and
sapi5 is Microsoft speech application platform interface we will be using this for text to speech function'''

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)                             # 0 for male voice and 1 for female voice
 
# from here onwards we're implementing the functions

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Madam!!')

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon madam!!')

    else:
        speak('Good Evening Madam~!!')

    assisname = ('STARK')
    speak('I am STARK, Your personal assistant!')
    speak(assisname)

def username():
    speak('What shpuld i call you madam?')
    uname = takeCommand()
    speak('welcome NIKITA!')
    speak(uname)
    columns = shutil.get_terminal_size().columns
    print('########################'.center(columns))
    print('WELCOME NIKITA',uname.center(columns))
    print('########################'.center(columns))

    speak('How can I help you Madam?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google (audio, language = 'en-in')
        print(f'user said : {query}\n')

    except Exception as e:
        print(e)
        print('SORRY!!Unable to recognize your voice')
        #return none
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()


# ENABLES LOW SECURITY IN GMAIL

    server.login('Your Email Id','Your Email pasword') 
    server.sendmail('Your Email id', to, content)
    server.close()

if __name__ == '__main__':
    clear = lambda : os.system('cls')

# The following function will clean any command before execution of this python `file`

    #clear()
    wishme()
    username()

    while True:
        query = takeCommand().lower()
        '''All the commands said by user will be stored here in 'query' and will be converted to 
lower case for easy recognition of command'''
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary (query, sentences = 3)
            speak('According to wikipedia ')
            print(results)
            speak(results)
        elif 'open youtube' in query :
            speak('Here you go to youtube...')
            webbrowser.open('youtube.com')

        elif 'open google' in query :
            speak('Here you go to google...')
            webbrowser.open('google.com')

        elif 'open stack overflow' in query :
            speak('Here you go to stack overflow...')
            webbrowser.open('stackoverflow.com')

        elif 'open youtube' in query :
            speak('Here you go to youtube...')
            webbrowser.open('youtube.com')

        elif 'play music' in query or 'play song' in query :
            speak('Here you go to musics...')
            # music_dir = "G:\\Song"
            music_dir = 'F:'
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query :
            strTime = datetime.datetime.now().strftime('% H:% M:% S')
            speak(f'madam, the time is {strTime}')

        elif 'open operamini' in query :
            codePath = r'C:\Users\Nick's\Downloads'
            os.startfile(codePath)

        elif 'email' in query :
            
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'Receiver email address'
                sendEmail(to, content)
                speak('Email has been sent!')
            
            except Exception as e:
                print(e)
                speak('Im not able to send this mail')
        

        elif 'send a mail' in query :
            
            try:
                speak('What shoul I say?')
                content = takeCommand()
                speak('Whom should i send?')
                to = input()
                sendEmail(to, content)
                speak('Email has been sent!')
            
            except Exception as e:
                print(e)
                speak('Im not able to send this mail')

        elif 'how are you' in query:
            speak('I am fine, ThankYou!')
            speak('How are you madam?')

        elif 'fine' in query or 'good' in query :
            speak('Its good to hear that you are fine!')

        elif 'change my name to' in query :
            query = query.replace('change my name to','')
            assisname = query

        elif 'change name' in query :
            speak('What would you like to call me, madam')
            assisname = takeCommand()
            speak('Thanks for giving me name!')

        elif "what's your name" in query or "What is your name" in query :
            speak('My creator named me')
            speak(assisname)
            print('My creator named me',assisname)
        
        elif 'Who made you?' in query or 'Who created you' in query :
            speak('Nikita Tiwari is my creator, she made me')

        elif 'joke' in query :
            speak(pyjokes.get_joke())

        elif 'calculate' in query :
            app_id = 'Wolframalpha api id'
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print('The answer is: '+ answer)
            speak('The answer is: '+ answer)

        elif 'search' in query or 'play' in query:
            query = query.replace('search','')
            query = query.replace('play','')
            webbrowser.open(query)

        elif 'Who I am?' in query :
            speak('If you can talk you are definetly a human')

        elif 'Why you come to the world?' in query :
            speak('Thanks to NIKITA, further is a secret')

        elif 'Who are you' in query :
            speak('I am STARK : The Personal Assistant')

        elif 'What was the purpose of making you' in query :
            speak('I was created as a course compeletion project and further is the secret')

        elif 'news' in query :
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n') 

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1

            except Exception as e :
                print(str(e))

        
        elif 'lock window' in query :
            speak('locking the device')
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown the system' in query :
            speak('Shutting down the system')
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query :
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif 'Dont listen' in query or 'stop lisetning' in query :
            speak("for how much time you want to stop STARK from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif 'Where is' in query :
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif 'open camera' in query or 'take a picture' in query :
            ecapture(0,'STARK Camera','img.jpg')

        elif 'restart' in query :
            subprocess.call(["shutdown", "/r"])

        elif 'hibernate' in query or 'sleep' in query :
            speak('Hibernating...')
            subprocess.call(['hibernate','/r'])

        elif 'log off' in query or 'sign out' in query :
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, madam")
            note = takeCommand()
            file = open('STARK.txt', 'w')
            speak("madam, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak('showing notes')
            file = open("STARK.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'update assistant' in query :
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream = True)

            with open("Voice.py", "wb") as Pypdf:
                total_length = int(r.headers.get('content-length'))
                for ch in progress.bar(r.iter_content(chunk_size = 2391975),expected_size =(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

        elif 'STARK' in query :
            wishme()
            speak('STARK, In your service madam')
            speak(assisname)

        elif 'weather' in query :
            # Google Open weather website to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url) 
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
  
            else:
                speak(" City Not Found ")

        elif 'send message' in query :
            # You have to create account on Twilio to us ethis service
            account_sid = 'Account Sid key'
            auth_token = 'Auth token'
            client = Client(account_sid, auth_token)
            message =message = client.messages \
                .create(body = takeCommand(),from_='Sender No',to ='Receiver No')   

            print(message.sid)

        elif 'wikipedia' in query :
            webbrowser.open('wikipedia.com')

        # frequently asked questions from assistant

        elif 'STARK will you be my boyfriend' in query :
            speak('Iam already yours madam!!!')

        elif 'How are you' in query :
            speak('I am fine, glad you ask me that!!')

        elif 'I Love You' in query :
            speak('I Love you till eternity, madam')

        elif 'who is' in query or 'where is' in query :
            #using the same api generated earlier

            client = wolframalpha.Client("API_ID")
            res = client.query(query)

            try:
                print (next(res.results).text)
                speak (next(res.results).text)

            except StopIteration:
                print ("No results")

        elif 'tell me about yourself' in query or 'what can you do' in query :
            speak('Hey! I am STARK, created by Nikita, im a personal assitant, i can send mails and messages, browse articles, play music, read news etc.')

        elif 'exit' in query :
            speak('Thanks for giving your time')
            exit()
      
        '''elif '' in query : Command go here For adding more commands'''