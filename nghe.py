import speech_recognition as sr

recognizer = sr.Recognizer()

#ghi lại âm thanh

with sr.Microphone() as source:
    print("Adjusting noise ")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Recording for 4 seconds")
    recorded_audio = recognizer.listen(source, timeout=4)
    print("Done recording")

#Nhận dạng âm thanh
try:
    print("Recognizing the text")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="vi"
        )
    print("Decoded Text : {}".format(text))

except Exception as text:
    print(text)