import pyautogui
import time
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')

def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        command.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = command.listen(source, timeout=10)  # Set timeout to 5 seconds
    try:
        print("Recognizing")
        query = command.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return "None"  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)
    
def song():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('spotify')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.click(x=148, y=140)
    speak("which song would you like to listen")
    song = takeCommand().lower()
    time.sleep(3)
    pyautogui.typewrite(song)
    time.sleep(3)
    pyautogui.click(x=1258, y=295)
    

