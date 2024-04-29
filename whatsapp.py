import pyautogui
import time
import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine in the global scope
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

def whatsapp():
    speak("Opening WhatsApp")
    pyautogui.press('win')
    pyautogui.typewrite("whatsapp")
    pyautogui.press('enter')
    time.sleep(4)
    speak("Who do you want to chat with?")
    naming = takeCommand().lower()
    pyautogui.click(x=215, y=148)
    time.sleep(2)
    pyautogui.typewrite(naming)
    time.sleep(1)
    pyautogui.click(x=250, y=253)
    speak("Tell me the message to send")
    talk = takeCommand().lower()
    pyautogui.typewrite(talk)
    pyautogui.press('enter')


