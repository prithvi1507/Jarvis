import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#pprint(voices[0].id)
engine.setProperty('voices',voices[0].id)
def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak("Good Morning!")
  
  elif hour>=12 and hour<18:
    speak("good afternoon!")
  
  else:
    speak("good evening!")

    speak("I am Jarvis Sir. Please tell me how may i help you")

def takeCommand():
  #it takes microphone input from the user and returns string output
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

  try:
    print("Recognizing...")
    query = r.recognize_google(audio,language="en-IN")
    print("User-said:",query)
    
  except Exception as e:
    #print(e)
    print("Say that again please...")
    return"None"
  return query

if __name__ == "__main__":
    wishMe()
    takeCommand()

