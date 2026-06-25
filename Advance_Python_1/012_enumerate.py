l = [3, 513, 53, 535]

'''
index = 0
for item in l:
    print(f"Index: {index}, Item: {item}")
    index += 1
'''

# This can be simplified using the enumerate() function, which returns both the index and the item in each iteration.

for index, item in enumerate(l):
    print(f"Index: {index}, Item: {item}")