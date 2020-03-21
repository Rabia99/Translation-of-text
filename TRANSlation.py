# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:31:50 2020

@author: HP
"""

#text to translate
from gtts import gTTS
import os  
mytext = 'pragun'
from googletrans import Translator
translator = Translator()
h= translator.translate(mytext, src='english', dest='hindi')
print(h.text)

#speech to text then translate
import speech_recognition as sr
r= sr.Recognizer()
mic=sr.Microphone()
mic=sr.Microphone(device_index=0)
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source)
s=r.recognize_google(audio)
from googletrans import Translator
translator = Translator()
h= translator.translate(s, src='english', dest='hindi')
print(h.text)


