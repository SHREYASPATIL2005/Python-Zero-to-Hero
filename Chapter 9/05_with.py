f = open("Chapter 9/file.txt", "r") # open() function is used to open the file in read mode
data = f.read()
print(data)
f.close()

# The same can be done using the with statement which automatically closes the file after the block of code is executed
with open("Chapter 9/file.txt", "r") as f:
    print(f.read())

# you dont have to explicitly close the file when using the with statement as it automatically closes the file after the block of code is executed
