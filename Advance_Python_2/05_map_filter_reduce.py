from functools import reduce

# MAP EXAMPLE

l  = [1, 2, 3, 4, 5]

square = lambda x: x * x   # Lambda function to calculate square


sqList = list(map(square, l))  # Using map to apply the square function to each element in the list
print(sqList)  # Output: [1, 4, 9, 16, 25]

# FILTER EXAMPLE

def isEven(n):
    if(n % 2 == 0):
        return True
    return False

onlyEven = list(filter(isEven, l))  # Using filter to get only even numbers from the list
print(onlyEven)  # Output: [2, 4]

# REDUCE EXAMPLE
def add(x, y):
    return x + y

mul = lambda x, y: x * y  # Lambda function to calculate product

print(reduce(add, l))  # Using reduce to sum all elements in the list, Output: 15
print(reduce(mul, l))  # Using reduce to multiply all elements in the list, Output: 120