import speech_recognition as sr # speech to text
import pyttsx3 # text to speech
import pywhatkit # third party app
import datetime # to check the date an time.
import wikipedia # for searching wikipedia
import pyjokes # for joke

listener = sr.Recognizer()
engine = pyttsx3.init()
# voice change
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# function to output voice 
def talk(text):
    engine.say(text)
    engine.runAndWait()

# read the command provided
def take_command():
    try:
        with sr.Microphone() as source: # to create a microphone instance 
            print('listning...')
            voice = listener.listen(source) # to listen 
            command = listener.recognize_google(voice) # speach to text
            #if 'tom' in command:
            #print(command)
    except:
        pass
    return command

def run_pro():
    command = take_command()
    # print(command)

    # play the song 
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    # time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %P') # %I for 12 hour time formate and %p for pm and am
        talk('the time is ' + time)
        print('the time is'+ time)
    # search the web 
    elif 'what is ' in command:
        item = command.replace('what is', '')
        info = wikipedia.summary(item, 5)
        talk(info)
        print(info)
    # to get jokes
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    # when the condition is not fulfilled
    else :
        talk(" didn't got that, please repeat")

while True:
    run_pro()