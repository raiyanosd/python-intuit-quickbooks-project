import speech_recognition as sr

# Create instance of recognizer
r = sr.Recognizer()

# Use microphone as source for audio input
with sr.Microphone() as source:
print('Speak Anything : ')

# Adjust ambient noise to enhance speech recognition
r.adjust_for_ambient_noise(source)

# Record audio
audio = r.listen(source)

# Speech recognition
try:

text = r.recognize_google(audio)
print('You said : {}'.format(text))

except:
print('Sorry, could not recognize your voice.')

# Save text output in a file
with open("output.txt", "w") as f:
f.write(text)
