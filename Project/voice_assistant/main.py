import speech_recognition as sr #speech to text
import pyttsx3 # text  to speech
import pywhatkit # third parrty app
import datetime # date nd time
import wikipedia # wikipedia search
import pyjokes # jokes

listener = sr.Recognizer()
engine = pyttsx3.init()
#voice change
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#function to output

def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    try:
        with sr.Microphone() as source: #for microphone instance
           # r.adjust_for_ambient_noise(source,duration=1)                            #ambient noise suppression
            print('listening...')
            voice = listener.listen(source) # to listen
            command = listener.recognize_google(voice) #speech to text        
    except:
        pass
    return command
    
def run():
    var = takeCommand()
    print(var)
    # play songs
    if 'play' in var:
        song = var.replace('play','')
        talk('playing'+song)
    
    # time
    elif 'time' in var :
        time = datetime.now().strftime('%I:%M %P')
        talk('the time is '+ time)

    # web search
    elif 'what is' in var or 'who is' in var :
        item = var.replace('what is', '')   
        item = var.replace('who is', '')
        info = wikipedia.summary(item, 5)
        talk(info)

    # jokes
    elif 'joke' in var :
        talk(pyjokes.get_joke())

    # opens youtube
    elif 'open youtube' in var :
        pywhatkit.playonyt('python')    
        talk('opening youtube...')
    
    else :
        # in case condition isn't fullfilled
        talk('Sorry! unable to recognize')
while True:
    run()