with open("Chapter 9/log.txt") as f:
    content = f.read()

if "python" in content:
    print("The word 'python' is present in the content")
else:
    print("The word 'python' is not present in the content")