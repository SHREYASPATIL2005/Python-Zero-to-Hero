import pyautogui
import time
import pyperclip
import os
from pathlib import Path

from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv(Path(__file__).resolve().parents[1] / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("Set GEMINI_API_KEY before running the auto-reply bot.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(os.getenv("GEMINI_MODEL", "gemini-1.5-flash"))

def is_last_message_from_sender(chat_log, sender_name="Sasuke Uchiha"):
    lines = [line.strip() for line in chat_log.splitlines() if line.strip()]

    if not lines:
        return False

    return sender_name in lines[-1]


def build_prompt(chat_history, max_chars=6000):
    return chat_history[-max_chars:]
    
    

    # Step 1: Click on the chrome icon at coordinates (1639, 1412)
pyautogui.click(1639, 1412)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo(972,202)
    pyautogui.dragTo(2213, 1278, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(1994, 281)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()
    chat_history = build_prompt(chat_history)

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = model.generate_content(
            [
                "You are a person named Naruto who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only).",
                "Do not start like this [21:02, 12/6/2024] Sasuke Uchiha: ",
                chat_history,
            ]
        )

        response = completion.text or ""
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(1808, 1328)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')