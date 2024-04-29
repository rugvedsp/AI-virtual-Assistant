import requests
import json
import pyttsx3
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 200)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

def speak_news():
    r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=caccfa1e9c554e7d875c7b7be9df4685')
    data = r.json()
    speak("The top news for today are")

    if 'articles' in data:
        articles = data['articles']
        for article in articles[:4]:  # Limiting to first 4 articles
            title = article.get('title')
            if title:
                
                speak(title)
                time.sleep(1)
    else:
        print("No articles found.")


speak_news()
