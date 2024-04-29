import openai
import pyttsx3
import speech_recognition as sr
import time

# Set your OpenAI API key

openai_api_key = os.getenv("OPENAI_API_KEY")


# Initialize the text-to-speech engine
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",  # Use the GPT-3 model
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def chatbot():
    while True:
        # Wait for user to say "Genius"
        print("Say 'start recording' to start recording your question...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "start recording":
                    # Record audio
                    filename = "input.wav"
                    print("Say your question...")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())
                    # Transcribe audio to text
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print("You said:", text)
                        # Generate response using GPT-3
                        response = generate_response(text)
                        print("GPT-3 says:", response)
                        # Read response using text-to-speech
                        speak_text(response)
            except Exception as e:
                print("An error occurred:", e)


if __name__ =="__main__":
    chatbot()
