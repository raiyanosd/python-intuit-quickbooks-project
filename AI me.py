# Personal Assistant Code in Python

# Import necessary libraries 
import speech_recognition as sr 
import webbrowser 
import time 
import playsound 
import os 
import random 
from gtts import gTTS 

 # Record audio and return it as a string 
def record_audio(ask=False):  
    r = sr.Recognizer() # Create a Recognizer instance  

    with sr.Microphone() as source: # Use the default microphone as the audio source  

        if ask:  
            speak(ask) # Speak the question if there is one  

        audio = r.listen(source) # Listen for the user's response  

        voice_data = ''  

        try:  
            voice_data = r.recognize_google(audio) # Use Google Speech Recognition to convert the audio into text  

        except sr.UnknownValueError: # Error: Recognition could not understand audio  

            speak('Sorry, I did not get that')  

        except sr.RequestError: # Error: Could not request results from Google Speech Recognition service  

            speak('Sorry, my speech service is down')  

        return voice_data # Return the data   

     # Get string and make a computer voice say it   
def speak(audio_string):   

    tts = gTTS(text=audio_string, lang='en') # Create a gTTS instance with the given text and language   

    r = random.randint(1, 10000000) # Generate a random number between 1 and 10 million for use as an audio file name    

    audio_file = 'audio-' + str(r) + '.mp3' # Create an mp3 file name based on the random number    

    tts.save(audio_file) # Save the TTS instance as an mp3 file    

    playsound.playsound(audio_file) # Play the mp3 file    

    print(audio_string) # Print what was said for debugging purposes    

    os.remove(audio_file) # Delete the mp3 file after it has been played 
