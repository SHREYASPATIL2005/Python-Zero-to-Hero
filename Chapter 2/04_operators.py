# Aithmetic Operators
a = 10
b = 3
c = a + b  # Addition
d = a - b  # Subtraction
e = a * b  # Multiplication
f = a / b  # Division
g = a % b  # Modulus (remainder)
print("Addition:", c)        # Output: 13
print("Subtraction:", d)     # Output: 7
print("Multiplication:", e)  # Output: 30
print("Division:", f)        # Output: 3.3333333333333335
print("Modulus:", g)         # Output: 1



# Assignment Operators
z = 4-2 # Assignment operator that assigns the value of 4-2 to the variable z
print("Value of z:", z)  # Output: 2
x = 5
x += 3  # Equivalent to x = x + 3 # Increment x by 3
print("After += 3:", x)  # Output: 8

x -= 2  # Equivalent to x = x - 2 # Decrement x by 2
print("After -= 2:", x)  # Output: 6

# Comparison Operators

d = 5 < 10  # Less than
e = 5 > 10  # Greater than
print("5 < 10:", d)  # Output: True
print("5 > 10:", e)  # Output: False

p = 10
q = 20
print("p == q:", p == q)  # Output: False
print("p != q:", p != q)  # Output: True
print("p < q:", p < q)    # Output: True
print("p > q:", p > q)    # Output: False
print("p <= q:", p <= q)  # Output: True
print("p >= q:", p >= q)  # Output: False


# Logical Operators

x = True or False  # Logical OR # The result is True because at least one operand (True) is true.
y = True and False  # Logical AND # The result is False because both operands are not true.
z = not True  # Logical NOT # The result is False because the operand (True) is negated.
print("True or False:", x)  # Output: True
print("True and False:", y)  # Output: False
print("Not True:", z)        # Output: False

print(not(True))
print(not(False))