# Mega Project 1 - Jarvis

Jarvis is a simple voice assistant that listens for the wake word "Jarvis", recognizes spoken commands, and answers with Gemini when the command is not handled locally.

## What it does

- Listens for the wake word with `speech_recognition`
- Speaks replies with `pyttsx3` and `gTTS`
- Opens common websites and music links directly
- Uses Gemini for general questions and fallback responses

## Setup

1. Install the Python packages listed in the workspace `requirements.txt`.
2. Create a local `.env` file in the workspace root with:
   - `GEMINI_API_KEY=your_api_key_here`
   - `GEMINI_MODEL=gemini-2.0-flash`
3. Run `main.py` from this folder.

## Notes

- The code is intentionally kept small and readable.
- If Gemini is unavailable or rate-limited, Jarvis returns a local fallback message instead of crashing.
- Keep `.env` out of version control.