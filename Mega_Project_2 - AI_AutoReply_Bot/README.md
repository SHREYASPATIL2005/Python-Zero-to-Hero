# Mega Project 2 - AI Auto Reply Bot

This project watches a chat window, copies the visible conversation, and asks Gemini to generate a reply in a Naruto-themed style.

## What it does

- Uses `pyautogui` to select and copy chat text
- Reads the clipboard with `pyperclip`
- Sends the pasted chat history to Gemini
- Copies the generated reply back into the chat box

## Setup

1. Create a local `.env` file in the workspace root with:
   - `GEMINI_API_KEY=your_api_key_here`
   - `GEMINI_MODEL=gemini-2.0-flash`
2. Install the Python packages listed in the workspace `requirements.txt`.
3. Adjust the screen coordinates in `03_bot.py` for your display if needed.

## Notes

- The sample transcript file is only for learning and can be edited freely.
- The script is intentionally simple so it is easier to follow and modify.
- Keep `.env` private and do not commit it.