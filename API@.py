import speech_recognition as sr
from gtts import gTTS
import os

# initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# microphone as source
with sr.Microphone() as source:
    print ("Speak Anything: ")
    audio = r.listen( source)
try:
    text = r.recognize_google (audio)
    print("You said : {}" . format (text))
    #Convert the text to speech
    tts = gTTS(text)
    #save the audio file
    tts.save("audio.mp3")
    #play the audio file
    os.system("mpg321 audio.mp3")
except:
    print("Sorry could not recognize what you said")

