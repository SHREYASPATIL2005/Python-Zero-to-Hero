a = (1,45,342,3424,False,"Harry")
print(a)

no = a.count(342) # This line counts the number of occurrences of the value 342 in the tuple 'a'. The output will be 1, as 342 appears once in the tuple.
print(no) # This line prints the count of occurrences of 342 in the tuple 'a', which is 1.

i = a.index(3424) # This line finds the index of the first occurrence of the value 3424 in the tuple 'a'. The output will be 3, as 3424 is located at index 3 in the tuple.
print(i) # This line prints the index of the first occurrence of 3424 in the tuple 'a', which is 3. If the value is not found, it will raise a ValueError.

#repeating a tuple
b = (1,2,3)
c = b * 3
print(c) # This line prints the tuple 'c', which is the result of repeating the tuple 'b' three times. The output will be (1, 2, 3, 1, 2, 3, 1, 2, 3).


# 1 in my_tuple = (1, 2, 3, 4, 5)
my_tuple = (1, 2, 3, 4, 5)
print(1 in my_tuple) # This line checks if the value 1 is present in the tuple 'my_tuple'. The output will be True.

#length of tuple
print(len(my_tuple)) # This line prints the length of the tuple 'my_tuple', which is 5, as there are five elements in the tuple.

#Unpacking a tuple
my_tuple = (1, 2, 3)
a, b, c = my_tuple # This line unpacks the elements of the tuple 'my_tuple' into three separate variables: 'a', 'b', and 'c'. The first element (1) is assigned to 'a', the second element (2) to 'b', and the third element (3) to 'c'.
print(a) # This line prints the value of the variable 'a', which is 1
print(b) # This line prints the value of the variable 'b', which is 2
print(c) # This line prints the value of the variable 'c', which is 3