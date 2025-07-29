# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# # from openai import OpenAI
# from murf import Murf

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# # Create a client (it reads your OPENAI_API_KEY from environment variable)
# # client = OpenAI(api_key="")

# # client = OpenAI(api_key="", base_url="https://api.deepseek.com")

# client = Murf(
#     api_key="" # Not required if you have set the MURF_API_KEY environment variable
# )

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def aiProcess(command):
#     response = client.chat.completions.create(
#         model="deepseek-chat",
#         messages=[
#             {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please."},
#             {"role": "user", "content": command}
#         ], 
#         stream=False
#     )
#     return response.choices[0].message.content

# def processCommand(c):
#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")
#     elif "open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")
#     elif "open linkedin" in c.lower():
#         webbrowser.open("https://linkedin.com")
#     else:
#         output = aiProcess(c)
#         speak(output)

# if __name__ == "__main__":
#     speak("Hello, Ayush")
#     while True:
#         try:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)

#             word = recognizer.recognize_google(audio)
#             print(word)

#             if word.lower() == "jarvis":
#                 speak("Yes, sir")
#                 with sr.Microphone() as source:
#                     print("Initialising Jarvis ...")
#                     audio = recognizer.listen(source)
#                     command = recognizer.recognize_google(audio)
#                     print("Command received:", command)
#                     processCommand(command)
#         except Exception as e:
#             print("Error:", e)

import speech_recognition as sr
import webbrowser
import pyttsx3
from openai import OpenAI
from gtts import gTTS
import pygame
import os

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "<Your Key Here>"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    # elif c.lower().startswith("play"):
    #     song = c.lower().split(" ")[1]
    #     link = musicLibrary.music[song]
    #     webbrowser.open(link)

    # elif "news" in c.lower():
    #     r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
    #     if r.status_code == 200:
    #         # Parse the JSON response
    #         data = r.json()
            
    #         # Extract the articles
    #         articles = data.get('articles', [])
            
    #         # Print the headlines
    #         for article in articles:
    #             speak(article['title'])

    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output) 



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))


