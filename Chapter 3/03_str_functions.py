name = "Harry are you there?"

print(len(name)) # This line prints the length of the string 'name', which is 21 since "Harry are you there?" has 21 characters.
print(name.endswith("there?")) # This line checks if the string 'name' ends with the substring "there?" and prints the result as a boolean value (True or False). In this case, it will print True since "Harry are you there?" does indeed end with "there?".
print(name.count("r")) # This line counts the number of occurrences of the character "r" in the string 'name' and prints the result. In this case, it will print 2 since there are two "r" characters in "Harry are you there?".
print(name.startswith("ha")) # This line checks if the string 'name' starts with the substring "ha" and prints the result as a boolean value (True or False). In this case, it will print True since "Harry are you there?" starts with "ha" (lowercase h).
print(name.upper()) # This line converts all characters in the string 'name' to uppercase and prints the result.
print(name.capitalize()) # This line capitalizes the first character of the string 'name' and converts the rest to lowercase, then prints the result. In this case, it will print "Harry are you there?" since the first character is already capitalized and the rest are lowercase.