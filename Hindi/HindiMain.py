from k2 import speak
# from k2 import takeCommand
import pyttsx3
import speech_recognition as sr
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',200)

def takeCommand():
     # It takes microphone input from user and returns str output

     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("Listening......")
          r.pause_threshold = 1
          r.non_speaking_duration=0.1
          audio = r.listen(source)
     
     try:
          print("Recognizing....")
          query = r.recognize_google(audio, language='hi')
          print(f"user said : {query}\n")

     except Exception as e:
          # print(e)
          # speak("I didn't get that can you say that again")
          print("Say that again please....")
          return "None"
     return query

speak("नमस्ते मुझसे आपको मदद कैसे मिल सकती है")

while True:
     query = takeCommand().lower()
     # print(query)
     if 'गाना' in query:
          speak("कौन सा गाना है सर")
          song = takeCommand().lower()
          speak("ठीक है सर")
          Music = song.replace("song","")
          Music=str(Music)
          pywhatkit.playonyt(Music)









