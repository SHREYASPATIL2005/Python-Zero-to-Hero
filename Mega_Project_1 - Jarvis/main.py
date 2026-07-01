import os
import re
from pathlib import Path
import webbrowser
import speech_recognition as sr
import pyttsx3
import pygame
from gtts import gTTS
from dotenv import load_dotenv
import google.generativeai as genai
import musicLibrary


# Load settings from the workspace .env file when present.
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# ---------------- INITIALIZATION ----------------

recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty("volume", 1.0)
engine.setProperty("rate", 170)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("Set GEMINI_API_KEY before starting Jarvis.")

genai.configure(api_key=GEMINI_API_KEY)

def build_gemini_model():
    # Try the most likely model names in order until one is accepted.
    preferred_model = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
    fallback_models = [preferred_model, "gemini-2.0-flash", "gemini-flash-latest"]

    seen = set()
    for model_name in fallback_models:
        if model_name in seen:
            continue
        seen.add(model_name)

        try:
            return genai.GenerativeModel(model_name)
        except Exception:
            continue

    raise RuntimeError("No supported Gemini model could be initialized.")


gemini_model = build_gemini_model()


# ---------------- AI ----------------

def aiProcess(command):
    try:
        response = gemini_model.generate_content(command)
        return response.text or "I couldn't generate a response just now."
    except Exception as error:
        print(f"Gemini error: {error}")
        return fallback_response(command)


def fallback_response(command):
    # Keep the assistant usable even when Gemini is rate-limited or unavailable.
    subject = extract_subject(command)

    if subject:
        return (
            f"I can't reach Gemini right now, but you asked about {subject}. "
            "Please try again later and I will answer properly."
        )

    return "I can't reach Gemini right now, but I am still listening. Please try again later."


def extract_subject(command):
    # Extract a simple topic from questions like "who is Virat Kohli".
    match = re.search(r"\b(?:who is|what is|tell me about|define)\s+(.+)", command, re.IGNORECASE)

    if not match:
        return ""

    subject = match.group(1).strip().rstrip("?.! ")
    return subject


# ---------------- SPEAK ----------------

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


def speak_gtts(text):
    print("Jarvis:", text)

    try:
        tts = gTTS(text=text, lang="en")
        tts.save("temp.mp3")

        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.music.load("temp.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()

        if os.path.exists("temp.mp3"):
            os.remove("temp.mp3")
    except Exception:
        speak(text)


# ---------------- COMMANDS ----------------

def processCommand(c):
    print("Command:", c)

    c = c.lower().strip()

    # -------- PLAY MUSIC --------

    if c.startswith("play"):
        try:
            song = c.replace("play", "", 1).strip()

            if song in musicLibrary.music:
                speak(f"Playing {song}")
                webbrowser.open(musicLibrary.music[song])
            else:
                speak("Song not found.")

        except Exception as e:
            print(e)
            speak("Unable to play the song.")

        return


    # -------- NEWS --------

    if "news" in c:
        speak("Opening Google News")
        webbrowser.open("https://news.google.com")
        return


    # -------- OPEN WEBSITES --------

    if "open" in c:

        if "youtube" in c:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "google" in c:
            speak("Opening Google")
            webbrowser.open("https://google.com")

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
            webbrowser.open("https://facebook.com")

        elif "instagram" in c:
            speak("Opening Instagram")
            webbrowser.open("https://instagram.com")

        elif "linkedin" in c:
            speak("Opening LinkedIn")
            webbrowser.open("https://linkedin.com")

        elif "stackoverflow" in c:
            speak("Opening Stack Overflow")
            webbrowser.open("https://stackoverflow.com")

        else:
            output = aiProcess(c)
            speak_gtts(output)

        return

    output = aiProcess(c)
    speak_gtts(output)

# ---------------- MAIN ----------------

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

                audio = r.listen(
                    source,
                    timeout=4,
                    phrase_time_limit=5
                )
            word = r.recognize_google(audio)

            print(f"Wake Word: {word}")

            if "jarvis" in word.lower():

                print("Wake word detected!")

                speak("Yes, how can I assist you?")

                speak("What can I do for you?")

                # Listen for user command
                with sr.Microphone() as source:

                    print("Jarvis Active")

                    r.adjust_for_ambient_noise(source, duration=0.5)

                    audio = r.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=8
                    )

                command = r.recognize_google(audio)

                print(f"Command: {command}")

                processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out.")

        except sr.UnknownValueError:
            print("Could not understand audio.")

        except sr.RequestError as e:
            print(f"Speech Recognition Error: {e}")

        except KeyboardInterrupt:
            speak("Goodbye.")
            break

        except Exception as e:
            print(f"Error: {e}")