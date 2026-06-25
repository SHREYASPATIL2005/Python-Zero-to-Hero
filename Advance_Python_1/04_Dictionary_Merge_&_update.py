dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = dict1 | dict2  # Merging dictionaries using the | operator (Python 3.9+)
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Merging dictionaries using the update() method
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}
