name = "Harry"

# Strings are immutable - This means that once a string is created, it cannot be changed. If you try to modify a string, you will get an error. For example, if you try to assign a new value to a character in the string like name[0] = "h", you will get a TypeError because strings do not support item assignment. Instead, you can create a new string by concatenating or slicing the original string. For example, you can create a new string with the first character changed to lowercase by using slicing and concatenation like        new_name = "h" + name[1:] which will result in new_name being "harry".  

nameshort = name[0:3] # Start index is inclusive and end index is exclusive. So it will include characters from index 0 to index 2 (H, a, r) and exclude the character at index 3 (r). Therefore, nameshort will be "Har".
print(nameshort) # This line prints the value of 'nameshort', which is "Har".
character1 = name[1] # This line assigns the character at index 1 of the string 'name' to the variable 'character1'. Since index 1 corresponds to the second character of the string, 'character1' will be assigned the value "a".
print(character1) # This line prints the value of 'character1', which is "a".

nameshort = name[1:3] # Start index is inclusive and end index is exclusive. So it will include characters from index 1 to index 2 (a, r) and exclude the character at index 3 (r). Therefore, nameshort will be "ar".
print(nameshort) # This line prints the value of 'nameshort', which is "ar".
