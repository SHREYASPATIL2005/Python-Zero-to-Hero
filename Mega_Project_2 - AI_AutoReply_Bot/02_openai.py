import os
from pathlib import Path

from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv(Path(__file__).resolve().parents[1] / ".env")


api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
  raise RuntimeError("Set GEMINI_API_KEY before running this sample.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(os.getenv("GEMINI_MODEL", "gemini-1.5-flash"))

command = '''
[20:30, 12/6/2024] Naruto: jo sunke coding ho sake?
[20:30, 12/6/2024] Sasuke Uchiha: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:30, 12/6/2024] Sasuke Uchiha: ye
[20:30, 12/6/2024] Sasuke Uchiha: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:31, 12/6/2024] Naruto: This is hindi
[20:31, 12/6/2024] Naruto: send me some english songs
[20:31, 12/6/2024] Naruto: but wait
[20:31, 12/6/2024] Naruto: this song is amazing
[20:31, 12/6/2024] Naruto: so I will stick to it
[20:31, 12/6/2024] Naruto: send me some english song also
[20:31, 12/6/2024] Sasuke Uchiha: hold on
[20:31, 12/6/2024] Naruto: I know what you are about to send
[20:32, 12/6/2024] Naruto: 😂😂
[20:32, 12/6/2024] Sasuke Uchiha: https://www.youtube.com/watch?v=ar-3chBG4NU
ye hindi English mix hai but best hai
[20:33, 12/6/2024] Naruto: okok
[20:33, 12/6/2024] Sasuke Uchiha: Haan
'''
response = model.generate_content(
  [
    "You are a person named Naruto Uzumaki who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Naruto.",
    command,
  ]
)

print(response.text)