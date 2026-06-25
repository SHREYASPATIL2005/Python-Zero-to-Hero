'''
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if b == 0:
    raise ZeroDivisionError("Division by zero is not allowed.")
else:
    print(f"The division of {a} by {b} is: {a / b}") '''


try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a/b)
except ZeroDivisionError as z:
    print("Infinite")