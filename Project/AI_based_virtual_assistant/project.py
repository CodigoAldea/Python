import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
# voice chagne
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source: # to create a microphone instance 
            print('listning...')
            voice = listener.listen(source) # to listen 
            command = listener.recognize_google(voice) # speach to text
            #if 'tom' in command:
            print(command)
    except:
        pass
    return command

def run_pro():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    if 'what is' in command:
        text = command.replace('what is', '')
        talk('searching for' + text)
        pywhatkit.search(text)


run_pro()