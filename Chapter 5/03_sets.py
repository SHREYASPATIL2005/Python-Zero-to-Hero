s = {1, 5, 32, 54, 5, 5, 5, "Harry"} # This line initializes a set 's' with the values 1, 5, 32, 54, and multiple occurrences of 5. Sets automatically remove duplicates, so only one instance of 5 will be stored.
print(s)

print(s,type(s)) # This line prints the type of 's', which will output <class 'set'>.

e = set() # This line initializes an empty set 'e' using the set() constructor.
# Dont't use e = {} to create an empty set, as it will create an empty dictionary instead.

print(e) # This line prints the empty set 'e', which will output set().


# Properties of sets:
# 1. Sets are unordered collections of unique items.
# 2. Sets are mutable, meaning their contents can be changed.
# 3. Sets are indexed by their values ( unindexed ) , not by position.
# 4. Sets do not allow duplicate values; each value must be unique within a set


