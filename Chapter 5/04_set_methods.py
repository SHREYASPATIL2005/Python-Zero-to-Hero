s = {1, 5, 32, 54, 5, 5, 5, "Harry"} # This line initializes a set 's' with the values 1, 5, 32, 54, and multiple occurrences of 5. Sets automatically remove duplicates, so only one instance of 5 will be stored.
print(s)


# methods of set
s.add(100) # This line adds the value 100 to the set 's' using the add() method. If 100 is already present in the set, it will not be added again.
print(s) # This line prints the updated set 's', which will include the value 100 if it was not already present.

s.remove(32) # This line removes the value 32 from the set 's' using the remove() method. If 32 is not present in the set, it will raise a KeyError.
print(s) # This line prints the updated set 's', which will no longer include the value 32.

s.discard(54) # This line removes the value 54 from the set 's' using the discard() method. If 54 is not present in the set, it will not raise an error.
print(s) # This line prints the updated set 's', which will no longer include the value 54.

# len() function can be used to find the number of elements in a set
print(len(s)) # This line prints the number of elements in the set 's' using the len() function. The output will depend on the current contents of the set 's'.

#pop() method removes and returns an arbitrary element from the set. If the set is empty, it raises a KeyError.
print(s.pop()) # This line removes and returns an arbitrary element from the set 's' using the pop() method. The output will be the value of the removed element, which can be any element from the set 's'.

#clear() method removes all elements from the set, leaving it empty.
s.clear() # This line removes all elements from the set 's' using the clear() method, resulting in an empty set.
print(s) # This line prints the now empty set 's', which will output set().

# subset and superset
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
print(s1.issubset(s2)) # This line checks if set 's1' is a subset of set 's2' using the issubset() method. The output will be True, as all elements of 's1' are present in 's2'.
print(s2.issuperset(s1)) # This line checks if set 's2' is a superset of set 's1' using the issuperset() method. The output will be True, as all elements of 's1' are present in 's2'.