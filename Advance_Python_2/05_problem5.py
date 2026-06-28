
# 5. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [-2,-3,-7,0,1,2,3,78,4,5]

def greater(x, y):
    if x > y:
        return x
    else:
        return y
    
print(reduce(greater, l))  # Output: 78