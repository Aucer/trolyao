import speech_recognition as sr
import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
from datetime import datetime
import wikipedia

now = datetime.now()
# initialize the recognizer
r = sr.Recognizer()

def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

while True:
	with sr.Microphone() as source:
		# read the audio data from the default microphone
		audio_data = r.record(source, duration=5)
		#print("Regnizing...")
		# convert speech to text
		try:
			text = r.recognize_google(audio_data, language="vi")
		except:
			text = ""
		print(text)

		if text == "":
			robot_brain = "Sủa đê!"
			speak(robot_brain)
			print(robot_brain)
		elif "Xin chào" in text:
			robot_brain = "Tao chào mày"
			speak(robot_brain)
			print(robot_brain)
		elif "ngày bao nhiêu" in text:
			robot_brain = now.strftime("hôm nay là ngày %d/%m/%Y")
			speak(robot_brain)
			print(robot_brain)
		elif "mấy giờ" in text:
			robot_brain = now.strftime("bây giờ là %H:%M:%S")
			speak(robot_brain)
			print(robot_brain)
		elif "Goodbye Trần Quỳnh Mai" in text:
			robot_brain = "Cút!"
			speak(robot_brain)
			print(robot_brain)
			break
		elif text:
			wikipedia.set_lang("vi")
			robot_brain = wikipedia.summary(text, sentences=1)
			speak(robot_brain)
			print(robot_brain)
			break
		
		else:
			robot_brain ="Mở cái mồm ra"
			speak(robot_brain)

		

