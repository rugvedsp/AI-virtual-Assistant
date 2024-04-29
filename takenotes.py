import pyttsx3
import pyautogui
import time
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        command.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = command.listen(source, timeout=10)  # Set timeout to 10 seconds
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

if __name__ == "__main__":
    speak("Sure, what do you want to write?")
    content = takeCommand().lower()
    
    # Open Notepad
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('notepad', interval=0.3)
    pyautogui.press("enter")
    time.sleep(2)
    
    # Write the content to Notepad
    pyautogui.write(content, interval=0.2)

    # Save the file
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)    
    speak("Please provide a file name for the text file")
    file_name = takeCommand().lower() + ".txt"
    pyautogui.write(file_name, interval=0.2)
    pyautogui.press('enter')
