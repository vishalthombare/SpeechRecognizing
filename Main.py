import sounddevice as sd
import speech_recognition as sr
from scipy.io.wavfile import write
import numpy as np
import webbrowser


def Myreco():
 fs = 48000
 seconds = 5
 myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
 sd.wait()
 Savef(fs, myrecording)


def Savef(fs, myrecording):
 y = (np.iinfo(np.int32).max * (myrecording / np.abs(myrecording).max())).astype(np.int32)
 write("Audio_File1.wav", fs, y)
 Convert()


def Convert():
 r = sr.Recognizer()
 with sr.AudioFile('Audio_File1.wav') as source:
  audio = r.record(source)
 try:
  command = r.recognize_google(audio, language='en-US')
  Webb(command)
 except:
  Webb("How to use Speech recognizer")



def Webb(command):
 webbrowser.open('https://www.google.com/search?source=hp&ei=Pk8TX_HkNfrtz7sP9raH0AE&q=' + command, new=2)


print("Enter the Hi ya Hello")


key =    {
     'hi':' If you want Search any think so... Speak',
     'hello':' If you want Search any think so... Speak'
    }

while True:

 a=input()
 a = a.lower()
 try:
  print(key[a])

 except:
  print("try agin")

 if a:
  Myreco()
