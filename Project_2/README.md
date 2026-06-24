# Project 2: The Perfect Guess

## Overview
This project is a simple number guessing game in Python.

The program should:
- Generate a random number.
- Ask the user to guess it.
- Tell the user to go lower if the guess is too high.
- Tell the user to go higher if the guess is too low.
- Continue until the correct number is guessed.
- Display the total number of guesses taken.

Hint: Use the `random` module.

## Learning Goals
- Use the `random` module.
- Practice `while` loops.
- Use conditional statements (`if`, `elif`, `else`).
- Count attempts with a counter variable.

## Suggested Logic
1. Import `random`.
2. Generate a secret number (for example, between 1 and 100).
3. Initialize guess counter to 0.
4. Start a loop:
   - Take user input.
   - Increase guess counter.
   - Compare input with secret number.
   - Print hint (`Higher number please` or `Lower number please`).
5. When guessed correctly, print success message and guess count.

## Example Interaction
```text
Guess the number (1-100): 50
Higher number please
Guess the number (1-100): 75
Lower number please
Guess the number (1-100): 68
You guessed it right in 3 guesses!
```

## Run the Project
From the `Project_2` folder:

```powershell
python main.py
```

## File Structure
- `main.py` -> Main game program
- `README.md` -> Project explanation and instructions
