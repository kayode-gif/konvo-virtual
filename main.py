
import os.path
import webbrowser
import speech_recognition as sr 
import time
import os
import playsound
import random
from gtts import gTTS
from time import ctime
import wolframalpha
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#function takes in user audio input(Kayode is speaking!!!)
def play_audio(ask = False):
    r = sr.Recognizer()
    #using the microphone as a input source
    with sr.Microphone() as input: 
        if ask:
            konvo_speak(ask)
        #listen to the input
        audio = r.listen(input)
        speech_output = ""
        try:
            #using gtts, recognise the speech and print
            speech_output = r.recognize_google(audio)
            print(speech_output)
            #if speech jammed then no
        except LookupError:
            konvo_speak("Speech is unclear")
    return speech_output.lower()


# function that plays out text to ear (Konvo is speaking!!!)
def konvo_speak(text):
    tts = gTTS(text = text, lang = 'en')
    rand = random.randint(1,10000000)
    file = 'voice-' + str(rand) + '.mp3'
    tts.save(file)
    playsound.playsound(file)
    print(text)
    os.remove(file)


# basic functionalities, name, feelings, time and date
def basics(voice):
    if "who are you" in voice:
        konvo_speak("I am Konvo, your personal voice assistant, ready to help!")
    elif "name" in voice:
        konvo_speak("My name is Konvo")
    elif "old" in voice:
        konvo_speak("That is very personal")
    elif "from" in voice:
        konvo_speak("Born and raised in Peckham")
    elif "time" in voice:
        konvo_speak(ctime())
    elif "how are you" in voice:
       konvo_speak("I am fine, how are you?")
    elif "fine" in voice or "good" in voice:
        konvo_speak("Amazing")


# exiting konvo 
def leave_konvo(voice):
    if "exit" in voice or "quit" in voice: 
        return exit()
    
# open and searches on applications, locates specific locations on google maps 
def konvo(voice):
    if "open" in voice:
        if "google" in voice:
            konvo_speak("Open Google")
            webbrowser.open("http://www.google.co.uk/")
        elif "youtube" in voice:
            konvo_speak("Open YouTube")
            webbrowser.open("https://www.youtube.com/")
        elif "spotify" in voice:
            konvo_speak("Open Spotify")
            webbrowser.open("https://open.spotify.com/")
        elif "netflix" in voice:
            konvo_speak("Open Netflix")
            webbrowser.open("https://www.netflix.com/gb/")
        elif "reddit" in voice:
            konvo_speak("Open Reddit")
            webbrowser.open("https://www.reddit.com/")
        elif "stack overflow" in voice:
            konvo_speak("Open Stack Overflow")
            webbrowser.open("https://stackoverflow.com/")
        else:
            konvo_speak("Application not found!")
    elif "youtube" in voice:
        i = voice.split().index("youtube")
        search = voice.split()[i + 1:]
        webbrowser.open("https://www.youtube.com/results?search_query=" + "+".join(search))
        konvo_speak("Searching" + str(search) + " on youtube")
    elif "search" in voice:
        i = voice.split().index("search")
        search = voice.split()[i + 1:]
        webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
        konvo_speak("Searching" + str(search) + " on google")
    elif "google" in voice:
        i = voice.split().index("google")
        search = voice.split()[i + 1:]
        webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
        konvo_speak("Searching" + str(search) + " on google")

    if "where is" in voice:
        i = voice.split().index("is")
        area = voice.split()[i+1:]
        link = "https://www.google.com/maps/place/" + " ".join(area)
        konvo_speak("This is where " + str(area) + "is")
        webbrowser.open(link)

def konvo_sums(voice):
    if "calculate" in voice:
        id = "737G5L-EA7UVLGUWQ"
        client = wolframalpha.Client(id)
        i = voice.split().index("calculate")
        text = voice.split()[i+1:]
        res = client.query(" ".join(text))
        answer = next(res.results).text
        konvo_speak("The answer is " + str(answer))
    if "work out" in voice:
        id = "737G5L-EA7UVLGUWQ"
        client = wolframalpha.Client(id)
        i = voice.split().index("out")
        text = voice.split()[i+1:]
        res = client.query(" ".join(text))
        answer = next(res.results).text
        konvo_speak("The answer is " + str(answer))

# provides verication 
ssl._create_default_https_context = ssl._create_unverified_context

time.sleep(1)
while(1):
    user_voice = play_audio() # get the voice input
    basics(user_voice)
    konvo_sums(user_voice)
    konvo(user_voice)
    leave_konvo(user_voice)