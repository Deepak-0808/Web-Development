import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Deepak!")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon Deepak!")

    else:
        speak("Good Evenong Deepak!")

    speak("I am jarvis sir. Please tell me how can i help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("I couldn't catch that. Please Say that again..")
        speak("I couldn't catch that. Please Say that again..")
        return "None"
    return query


if __name__ == '__main__':
    # speak("Deepak and samaksh is a good boy")
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query
