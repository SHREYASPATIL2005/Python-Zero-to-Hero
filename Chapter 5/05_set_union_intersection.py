s1 = {1, 45, 6}
s2 = {1, 45, 6, 7, 8}

print(s1.union(s2)) # This line prints the union of sets 's1' and 's2' using the union() method. The output will be a set containing all unique elements from both sets, which will be {1, 45, 6, 7, 8}.
print(s1.intersection(s2)) # This line prints the intersection of sets 's1' and 's2' using the intersection() method. The output will be a set containing only the elements that are present in both sets, which will be {1, 45, 6}.


# s1 - s2 will give the difference of sets 's1' and 's2', which is a set containing elements that are present in 's1' but not in 's2'. The output will be an empty set, as all elements of 's1' are also present in 's2'.
print(s1 - s2) # This line prints the difference of sets 's1'
print(s2 - s1) # This line prints the difference of sets 's2' and 's1', which is a set containing elements that are present in 's2' but not in 's1'. The output will be {7, 8}, as these elements are present in 's2' but not in 's1'.