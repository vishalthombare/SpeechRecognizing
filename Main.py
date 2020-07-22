from distutils import command
import sounddevice as sd
import speech_recognition as sr
from scipy.io.wavfile import write
import numpy as np
import os
import webbrowser
import subprocess

print("Enter the Hi ya Hello")


key =    {
     'hi':' If you want Search any think so... Speck',
     'hello':' If you want Search any think so... Speck'
    }

while True:

 z=input()
 z = z.lower()
 try:
  a=key[z]
 except:
  a=None
  print("try agin")


 if a:

  def Myreco():
   frequency = 440
   fs=48000
   seconds=5

   myrecording=sd.rec(int(seconds*fs), samplerate=fs, channels=2)
   sd.wait()
   Savef(fs,myrecording)
   # write('Audio_File.wav',fs, myrecording)

  def Savef(fs,myrecording):
   y=(np.iinfo(np.int32).max * (myrecording/np.abs(myrecording).max())).astype(np.int32)
   write("Audio_File1.wav", fs, y)
   Convert()

  def Convert():
   r=sr.Recognizer()
   with sr.AudioFile('Audio_File1.wav') as source:
     audio=r.record(source)
   command=r.recognize_google(audio, language='en-US')
   #Webb(command)
   command=command.lower()
   #os.system(command)
   def Webb(command):
    webbrowser.open('https://www.google.com/search?source=hp&ei=Pk8TX_HkNfrtz7sP9raH0AE&q='+command, new=2)

  #Myreco()
   #os.system(command)
   #command=subprocess.call("ls -l")

 #else:
  #print("Pleage try again")