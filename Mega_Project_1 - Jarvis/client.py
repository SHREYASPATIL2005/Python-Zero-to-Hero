import os
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv


# Load settings from the workspace .env file when present.
load_dotenv(Path(__file__).resolve().parents[1] / ".env")


def build_model():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("Set GEMINI_API_KEY before running this example.")

    genai.configure(api_key=api_key)
    return genai.GenerativeModel(os.getenv("GEMINI_MODEL", "gemini-1.5-flash"))


model = build_model()

response = model.generate_content("Write a one-sentence bedtime story about a unicorn.")

print(response.text)