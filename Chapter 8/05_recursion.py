'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1 = 2
factorial(3) = 3 X 2 X 1 = 6
... and so on.
factorial(n) = n X (n-1) X (n-2) X ... X 3 X 2 X 1

factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {n} is {factorial(n)}.")