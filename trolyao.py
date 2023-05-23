import speech_recognition as sr
import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
from datetime import datetime
import wikipedia

now = datetime.now()
# ghi lại âm thanh 
recognizer = sr.Recognizer()

def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

while True:
	with sr.Microphone() as source:
	    print("Adjusting noise ")
	    recognizer.adjust_for_ambient_noise(source, duration=1)  #thời gian điều chỉnh tiếng
	    print("Recording for 4 seconds")
	    recorded_audio = recognizer.listen(source, timeout=4)  #thời gian nghe 
	    print("Done recording")

	 #Nhận dạng âm thanh
	try:
	    print("Recognizing the text")
	    text = recognizer.recognize_google(recorded_audio, language="vi") # nhận dạng âm thanh và ngôn ngữ
	    print("Decoded Text : {}".format(text))
	except Exception as text:
		text = ""
	print(text)

	if text == "":
		robot_brain = "Nói đê!"
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
	elif "Hẹn gặp lại" in text:
		robot_brain = "Cút!"
		speak(robot_brain)
		print(robot_brain)
		break
	elif text:
		wikipedia.set_lang("vi")
		robot_brain = wikipedia.summary(text, sentences=1)
		speak(robot_brain)
		print(robot_brain)
		#break
	else:
		robot_brain ="Tao không hiểu"
		speak(robot_brain)

		

