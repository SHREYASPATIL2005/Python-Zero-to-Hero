import random

def game():
    print("You are playing the game...")
    score = random.randint(1, 100) # generate a random score between 1 and 100
    # Fetch the hiscore from the file
    with open("Chapter 9/hiscore.txt", "r") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score is: {score}")
    if (score > hiscore):
        # write this hiscore to the file
        with open("Chapter 9/hiscore.txt", "w") as f:
            f.write(str(score))

if __name__ == "__main__":
    game()