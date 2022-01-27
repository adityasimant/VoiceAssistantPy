import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour >=0 and hour< 12:
        speak("good morning")
    
    elif hour >=12 and hour< 18:
        speak("good afternoon")
    
    else:
        speak("good evening")
    
    speak("how may i help you?")    

def takeCommand():  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try :
        print("recognising...")
        query= r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print('please say that again....')
        return "none"
    return query    

if __name__ == "__main__" :
    wishMe()
    while True :
        query= takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching..")
            query=query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("according to wikipedia ")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")   
        elif "open google" in query:
            webbrowser.open("www.google.com")   
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")   
        elif "open linkedin" in query:
            webbrowser.open("www.linkedin.com")   
        elif "play music" in query:
            music_dir =  'E:\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

         





