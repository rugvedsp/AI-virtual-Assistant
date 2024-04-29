import requests
import pyttsx3
import speech_recognition as sr
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 200)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
    
def news_updates():
        url = "https://google-api31.p.rapidapi.com/"

        payload = {
            "text": "India",
            "region": "wt-wt",
            "max_results": 25
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "your-api-key",
            "X-RapidAPI-Host": "google-api31.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)

        data = response.json()
        # Extract titles from the 'news' list
        if 'news' in data:
            for i, news_article in enumerate(data['news']):
                if i < 6:  # Iterate only 6 times
                    title = news_article['title']
                    speak(title)
                else:
                    break  # Stop iterating after printing 6 titles
                
news_updates()

