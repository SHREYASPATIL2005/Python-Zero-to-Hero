s = set()
s.add(20)
s.add(20.0)
s.add("20") #The length of the set 's' will be 2, as it contains three distinct elements: the integer 20, the float 20.0, and the string "20". Although 20 and 20.0 are numerically equal, they are considered different types in Python, and thus both are included in the set.
print(s) # This line prints the set 's', which will output {20, 20.0, '20'}, demonstrating that sets can contain elements of different data types and that they are treated as distinct values.

print(len(s)) # This line prints the length of the set 's', which will output 2, as there are two distinct elements in the set: 20 (integer) and 20.0 (float)

#1 == 1.0 is True, but 1 and 1.0 are considered different types in Python.