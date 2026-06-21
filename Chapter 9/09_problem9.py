with open("Chapter 9/this.txt", "r") as f:
    content = f.read()

with open("Chapter 9/copy.txt", "r") as f:
    content2 = f.read()

if content == content2:
    print("The content of both files is the same")
else:
    print("The content of both files is different")