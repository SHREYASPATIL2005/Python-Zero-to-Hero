# 2. Write a program to input name, marks and phone number of a student and format it
# using the format function like below:
#
# "The name of the student is Harry, his marks are 72 and phone number is 999999888"

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
phone = input("Enter your phone number: ")

s = "The name of the student is {} and his marks are {} and his phone number is {}".format(name, marks, phone)
print(s)  # Output: The name of the student is Shreyas and his marks