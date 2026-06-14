marks = {
    "Harry": 85,
    "Ron": 78,
    "Hermione": 92,
    0 : "Karry"
}

print(marks)
print(marks.items()) # This line prints the items of the dictionary 'marks' as a view object, which will output dict_items([('Harry', 85), ('Ron', 78), ('Hermione', 92), (0, 'Karry')]).
print(marks.keys()) # This line prints the keys of the dictionary 'marks' as a view object, which will output dict_keys(['Harry', 'Ron', 'Hermione', 0]).
print(marks.values()) # This line prints the values of the dictionary 'marks' as a view object, which will output dict_values([85, 78, 92, 'Karry']).
marks.update({"Harry": 90, "Renuka": 88}) # This line updates the value associated with the key "Harry" in the dictionary 'marks' to 90.
print(marks) # This line prints the updated dictionary 'marks', which will output {'Harry': 90, 'Ron': 78, 'Hermione': 92, 0: 'Karry', 'Renuka': 88}.

print(marks.get("Harry")) # This line retrieves the value associated with the key "Harry" in the dictionary 'marks' using the get() method, which will output 90.
print(marks.get("Draco", "Not Found")) # This line attempts to retrieve the value associated with the key "Draco" in the dictionary 'marks' using the get() method. Since "Draco" is not a key in the dictionary, it will return the default value "Not Found".
print(marks.get("Draco")) # This line attempts to retrieve the value associated with the key "Draco" in the dictionary 'marks' using the get() method. Since "Draco" is not a key in the dictionary, it will return None.


print(marks.get("Harry2")) # Prints None
print(marks["Harry2"]) # Returns an error

