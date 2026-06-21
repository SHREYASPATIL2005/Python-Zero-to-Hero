f = open("Chapter 9/poem.txt", "r") # open() function is used to open the file in read mode
content = f.read()
if("twinkle" in content):
    print("The word 'twinkle' is present in the content")
else:
    print("The word 'twinkle' is not present in the content")
f.close()