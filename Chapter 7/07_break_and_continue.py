for i in range(100):
    if i == 34:
        break  # This will break the loop when i is 34
    print(i)

for i in range(100):
    if i % 2 == 0:
        continue  # This will skip the current iteration when i is even
    print(i)