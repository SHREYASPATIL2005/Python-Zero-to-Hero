
with open("Chapter 9/log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"The word 'python' is present in the line. Line no: {lineno}")
        break
    lineno += 1 
else:
    print("The word 'python' is not present in the line")