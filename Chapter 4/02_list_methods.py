friends = ["Apple", "Orange", 5, 345.06, False, "Akash", "Rohan"]
print(friends)

friends.append("Harry") # This line adds the string "Harry" to the end of the list 'friends'.
print(friends) # This line prints the updated list 'friends', which now includes "Harry" at the end.

l1 = [1, 34, 62, 2, 6, 11]
l1.sort() # This line sorts the list 'l1' in ascending order.
print(l1) # This line prints the sorted list 'l1'.
l1.reverse() # This line reverses the order of the elements in the list 'l1'.
print(l1) # This line prints the reversed list 'l1'.

l1.insert(3, 333333) # This line inserts the integer 333333 at index 3 of the list 'l1'.
print(l1) # This line prints the updated list 'l1', which now includes 333333 at index 3.


value = l1.pop(3) # This line removes the element at index 3 of the list 'l1', which is 333333.
print(value) # This line prints the value that was removed from the list 'l1', which is 333333. 
print(l1) # This line prints the updated list 'l1', which no longer includes 333333.


#remove() method removes the first matching value, not a specific index. If the value is not found, it raises a ValueError.
l1.remove(6) # This line removes the first occurrence of the value 6 from the list 'l1'.
print(l1) # This line prints the updated list 'l1', which no longer includes