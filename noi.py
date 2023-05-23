import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

def speak(text):
    tts = gTTS(text=text, lang='vi') # thay đổi ngôn ngữ
    filename = 'voice.mp3' #lưu vào file mp3
    tts.save(filename)
    playsound.playsound(filename)

speak("Em chào cô!")