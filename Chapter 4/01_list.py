friends = ["Apple", "Orange", 5, 345.06, False, "Akash", "Rohan"]

print(friends)
print(friends[0]) # This line prints the first element of the list 'friends', which is "Apple".
friends[0] = "Grapes" #Unlike strings, lists are mutable, which means we can change their elements. Here, we are changing the first element of the list 'friends' from "Apple" to "Grapes".
print(friends[0]) # This line prints the first element of the list 'friends', which is now "Grapes".

print(friends[6]) # This line prints the seventh element of the list 'friends', which is "Rohan".

print(friends[-1]) # This line prints the last element of the list 'friends', which is "Rohan". In Python, negative indexing allows us to access elements from the end of the list, with -1 being the last element.
print(friends[1:4]) # This line prints a slice of the list 'friends', starting from index 1 up to (but not including) index 4. The output will be ["Orange", 5, 345.06].