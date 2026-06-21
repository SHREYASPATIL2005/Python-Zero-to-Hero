word = "Donkey"

with open("Chapter 9/donkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace("Donkey", "#######")

with open("Chapter 9/donkey.txt", "w") as f:
    f.write(contentNew)
    