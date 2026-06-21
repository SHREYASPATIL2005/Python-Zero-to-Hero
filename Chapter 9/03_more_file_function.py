f = open("Chapter 9/file.txt")

'''
lines = f.readlines() # readlines() function is used to read all the lines of the file and return them as a list

print(lines, type(lines)) # print the list of lines and its type
'''
'''
line1 = f.readline() # readline() function is used to read a single line from the file
print(line1, type(line1)) # print the line and its type

line2 = f.readline() 
print(line2, type(line2))

line3 = f.readline() 
print(line3, type(line3))

line4 = f.readline() 
print(line4, type(line4)) 

line5 = f.readline()
print(line5, type(line5))

line6 = f.readline()
print(line6, type(line6))
'''
line = f.readline()
while line != "":
    print(line,end="")
    line = f.readline()

f.close() # close() function is used to close the file

# Modes of opening a file:
# r - read mode
# w - write mode
# a - append mode
# r+ - read and write mode
# b - binary mode
# rb - read binary mode
# rt - read text mode