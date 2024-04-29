import pyttsx3
import speech_recognition as sr
import requests

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)
    
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

def get_weather():
    speak("Please say the name of the city")
    city = takeCommand()
    if city != "None":
        rapidapi_key = "Your-Api-key"
        rapidapi_host = "open-weather13.p.rapidapi.com"
        
        url = "https://open-weather13.p.rapidapi.com/city/mumbai/EN"

        headers = {
	"X-RapidAPI-Key": "your-api-key",
	"X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
}

        response = requests.get(url, headers=headers)

        data = response.json()

        if "error" in data:
            speak("City not found.")
        else:
            temperature = data.get("main", {}).get("temp")
            weather_description = data.get("weather", [{}])[0].get("description")
            if temperature and weather_description:
                speak(f"The temperature in {city} is {temperature} degrees farenheit with {weather_description}.")
            else:
                speak("Temperature information not available.")
    else:
        speak("Sorry, I couldn't recognize the city. Please try again.")
        



