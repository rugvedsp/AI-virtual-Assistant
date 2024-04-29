import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk 
import os
import pyautogui
import cv2
import time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 200)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

def wish():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 17:
        speak("Good Afternoon")
    else:
        speak("Good evening!")
    speak("Hello, I am Callisto. How can I help you today?")
   
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
    
def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")
    
def take_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("photo.jpg", frame)
        speak("Photo taken successfully!")
    else:
        speak("Failed to capture photo. Please try again.")
    cap.release()



if __name__ == "__main__":
    
    while True:
        query = takeCommand()
        if 'hello' in query:  
            wish()
            
        elif 'stop the program' in query:
            exit(0)
            
        elif 'tell me top news of today' in query:
            from news import news_updates
            news_updates()

        elif 'what is' in query:
            speak('searching in wiki..')                       
            query = query.replace("what is", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple possible results. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                speak("Sorry, I couldn't find any information on that topic.")

            
        elif 'open whatsapp' in query:
            from whatsapp import whatsapp
            whatsapp()
            
        elif 'open chatbot' in query:
            from chatbot import chatbot
            chatbot()
            
        elif 'tell me about weather' in query:
            from weather import get_weather
            get_weather()
            
        elif 'tell time' in query or 'what time is it' in query:
            tell_time()
            
        elif "i want to listen to some songs" in query :
            from spotify import song
            song()
    
        elif "take photo" in query:
            take_photo()

        elif 'open google' in query:
            speak("what do you want to search ?")
            query = takeCommand().lower()
            webbrowser.open(f"{query}")
            results = wikipedia.summary(query, sentences=1)
            speak(results)
        
        elif 'open youtube' in query:
            speak("what will you like to watch ? ")
            qry = takeCommand().lower()
            wk.playonyt(f"{qry}") 

        elif 'take note' in query:
            speak("Sure, what do you want to write?")
            content = takeCommand().lower()
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.typewrite('notepad', interval=0.3)
            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.write(content, interval=0.2)
            pyautogui.hotkey('ctrl', 's')
            time.sleep(1)    
            speak("Please provide a file name for the text file")
            file_name = takeCommand().lower() + ".txt"
            pyautogui.write(file_name, interval=0.2)
            pyautogui.press('enter')
        
        elif "open visual code studio" in query:
            os.system("code")
        
        elif "open obs studio" in query :
            pyautogui.press('win')
            pyautogui.typewrite('obs')
            pyautogui.press('enter')
            
        elif "open vlc media player" in query :
            pyautogui.press('win')
            pyautogui.typewrite('vlc')
            pyautogui.press('enter')
           
        elif "open steam" in query :
            pyautogui.press('win')
            pyautogui.typewrite('steam')
            pyautogui.press('enter') 
        
        elif "take screenshot" in query:
            speak("tell me name for the file")
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif 'mute' or 'unmute' in query:
            pyautogui.press("volumemute")

        elif 'start Chrome' in query:
            speak("opening chrome")
            pyautogui.press('win')
            pyautogui.typewrite("chrome")
            pyautogui.press('enter')
            
        elif 'shut down' in query:
            os.system("shutdown /s /t 5")

        elif 'restart system' in query:
            os.system("shutdown /r /t 5")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
            
            
       
            
            

        
        
            
            

        
            


        


       

        

        


                    





        

        

        






