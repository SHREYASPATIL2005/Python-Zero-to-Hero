myList = [1, 2, 9, 5, 3, 5, 7, 8, 4, 6]

'''
squaredList = []
for item in myList:
    squaredList.append(item *item)
'''

squaredList = [item * item for item in myList]  # List comprehension to create a new list with squared values
print(squaredList)