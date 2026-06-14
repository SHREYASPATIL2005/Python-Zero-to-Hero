marks = {
    "Harry": 85,
    "Ron": 78,
    "Hermione": 92,
}


d = {} # This line initializes an empty dictionary 'd' using curly braces {}.
print(d) # This line prints the empty dictionary 'd', which will output {}.
print(marks, type(marks)) # This line prints the dictionary 'marks' and its type. The output will be {'Harry': 85, 'Ron': 78, 'Hermione': 92} <class 'dict'>.
print(marks["Harry"]) # This line accesses the value associated with the key "Harry"


# Properties of a dictionary:
# 1. Dictionaries are unordered collections of items.
# 2. Dictionaries are mutable, meaning their contents can be changed.
# 3. Dictionaries are indexed by keys, which can be of any immutable type (e.g., strings, numbers, tuples).
# 4. Dictionaries do not allow duplicate keys; each key must be unique within a dictionary.