with open("Chapter 9/old.txt", "r") as f:
    content = f.read()

with open("Chapter 9/new.txt", "w") as f:
    f.write(content)