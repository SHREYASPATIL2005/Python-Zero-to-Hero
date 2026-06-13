a = (1, 2, 3, 4, 5) # This line creates a tuple 'a' with the values 1, 2, 3, 4, and 5. Tuples are ordered collections of items that are immutable (cannot be changed after creation).
print(a) # This line prints the tuple 'a', which will output (1, 2, 3, 4, 5).
# a[0] = 34 # This line attempts to change the first element of the tuple 'a' to 34. However, since tuples are immutable, this will raise a TypeError indicating that 'tuple' object does not support item assignment.

print(type(a)) # This line prints the type of the variable 'a', which will output <class 'tuple'>, confirming that 'a' is indeed a tuple.


b = () # This line creates an empty tuple 'b'. An empty tuple is defined by a pair of parentheses with no elements inside.
print(b) # This line prints the empty tuple 'b', which will output ().  
print(type(b)) # This line prints the type of the variable 'b', which will output <class 'tuple'>, confirming that 'b' is an empty tuple.

c = (1,) # This line creates a tuple 'c' with a single element, which is the integer 1. The comma is necessary to indicate that this is a tuple; without the comma, it would be interpreted as an integer in parentheses.
print(c) # This line prints the tuple 'c', which will output (1,).
print(type(c)) # This line prints the type of the variable 'c', which will output <class 'tuple'>, confirming that 'c' is a tuple with a single element.


a = (1,45,342,3424,False,"Harry") # This line creates a tuple 'a' with multiple elements of different data types, including integers, a boolean, and a string.
print(a) # This line prints the tuple 'a', which will output (1, 45, 342, 3424, False, 'Harry').
print(a[0]) # This line prints the first element of the tuple 'a', which is 1.
print(a[5]) # This line prints the sixth element of the tuple 'a', which is "Harry".
print(a[-1]) # This line prints the last element of the tuple 'a', which is "Harry". In Python, negative indexing allows us to access elements from the end of the tuple, with -1 being the last element.
print(a[0:4]) # This line prints a slice of the tuple 'a', starting from index 0 up to (but not including) index 4. The output will be (1, 45, 342, 3424).
print(type(a[0:4])) # This line prints the type of the slice a[0:4], which will output <class 'tuple'>, confirming that slicing a tuple results in another tuple.