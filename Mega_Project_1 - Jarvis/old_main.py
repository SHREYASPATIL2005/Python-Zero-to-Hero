import os
from pathlib import Path

import speech_recognition as sr

import webbrowser

import pyttsx3

import musicLibrary

import pygame

from gtts import gTTS
from dotenv import load_dotenv
import google.generativeai as genai


# Load settings from the workspace .env file when present.
load_dotenv(Path(__file__).resolve().parents[1] / ".env")



# pip install pocketsphinx

# pip instal gTTS

# pip install pygame



recognizer = sr.Recognizer()

engine = pyttsx3.init()



# Voice settings

engine.setProperty("volume", 1.0)      # Max volume

engine.setProperty("rate", 170)        # Speaking speed



voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)   # voices[1] for female voice



def aiProcess(Command):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("Set GEMINI_API_KEY before running this legacy entry point.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(os.getenv("GEMINI_MODEL", "gemini-1.5-flash"))

    completion = model.generate_content(Command)

    return completion.text.strip() if completion.text else ""



def speak(text):

    print("Jarvis:", text)

    engine.say(text)

    engine.runAndWait()



def speak_gtts(text):

    tts = gTTS(text=text, lang='en')

    tts.save("temp.mp3")

    os.system("start temp.mp3")  # For Windows, use "start" to play the audio



    # Initialize pygame mixer to play the audio

    pygame.mixer.init()



    # Load and play the audio

    pygame.mixer.music.load("temp.mp3")



    # Play the MP3 file

    pygame.mixer.music.play()



    # Keep the program running until the audio finishes playing

    while pygame.mixer.music.get_busy():

        pygame.time.Clock().tick(10)



    os.remove("temp.mp3")  # Clean up the temporary file

    

    





def processCommand(c):

    print("Command:", c)

    c = c.lower().strip()



    # ---------------- PLAY SONG ----------------

    if c.startswith("play"):

        try:

            song = c.replace("play", "", 1).strip()



            if song in musicLibrary.music:

                speak(f"Playing {song}")

                webbrowser.open(musicLibrary.music[song])

            else:

                speak(f"Sorry, I couldn't find {song} in the music library.")



        except Exception as e:

            print(e)

            speak("Sorry, something went wrong while playing the song.")

        return



    # ---------------- NEWS ----------------

    if "news" in c:

        speak("Opening Google News.")

        webbrowser.open("https://news.google.com")

        return



    # ---------------- OPEN WEBSITES ----------------

    if "open" in c:

        if "youtube" in c:

            speak("Opening YouTube")

            webbrowser.open("https://www.youtube.com")



        elif "google" in c:

            speak("Opening Google")

            webbrowser.open("https://www.google.com")



        elif "github" in c:

            speak("Opening GitHub")

            webbrowser.open("https://github.com")



        elif "gmail" in c:

            speak("Opening Gmail")

            webbrowser.open("https://mail.google.com")



        elif "twitter" in c:

            speak("Opening Twitter")

            webbrowser.open("https://twitter.com")



        elif "facebook" in c:

            speak("Opening Facebook")

            webbrowser.open("https://www.facebook.com")



        elif "instagram" in c:

            speak("Opening Instagram")

            webbrowser.open("https://www.instagram.com")



        elif "linkedin" in c:

            speak("Opening LinkedIn")

            webbrowser.open("https://www.linkedin.com")



        elif "stackoverflow" in c:

            speak("Opening Stack Overflow")

            webbrowser.open("https://stackoverflow.com")



        else:

            # Let OpenAI handle the request

            output = aiProcess(c)

            speak(output)



        return



    speak("Sorry, I didn't understand the command.")





if __name__ == "__main__":

    speak("Initializing Jarvis")



    while True:

        r = sr.Recognizer()



        print("Recognizing...")



        try:

            # Listen for wake word

            with sr.Microphone() as source:

                print("Listening...")

                r.adjust_for_ambient_noise(source, duration=1)

                audio = r.listen(source, timeout=4, phrase_time_limit=5)



            word = r.recognize_google(audio)

            print(f"Wake Word: {word}")



            if "jarvis" in word.lower():

                print("Wake word detected!")



                speak("Yes, how can I assist you?")

                speak("What can I do for you?")



                # Listen for command

                with sr.Microphone() as source:

                    print("Jarvis Active")

                    r.adjust_for_ambient_noise(source, duration=0.5)

                    audio = r.listen(source, timeout=5, phrase_time_limit=8)



                command = r.recognize_google(audio)

                print(f"Command: {command}")



                processCommand(command)



        except sr.WaitTimeoutError:

            print("Listening timed out.")



        except sr.UnknownValueError:

            print("Could not understand audio.")



        except sr.RequestError as e:

            print(f"Speech Recognition Error: {e}")



        except Exception as e:

            print(f"Error: {e}")