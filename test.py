import pyttsx3
import speech_recognition as sr
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 200)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)


def news_updates():
    url = "https://google-news13.p.rapidapi.com/latest"
    headers = {
	"X-RapidAPI-Key": "Your-Api-key",
	"X-RapidAPI-Host": "google-news13.p.rapidapi.com"
}
    querystring = {"lr":"en-US"}

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()

        if response.status_code == 200:
            news_data = response.json()
            if 'data' in news_data:
                headlines = [news['title'] for news in news_data['data']]
                for headline in headlines:
                    speak(headline)
            else:
                print("No news results found.")
        else:
            print("Failed to fetch news updates. Status code:", response.status_code)

    except requests.RequestException as e:
        print("Error fetching news updates:", e)
        
news_updates()
