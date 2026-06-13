marks = []

f1 = int(input("Enter marks here: "))
marks.append(f1)
f2 = int(input("Enter marks here: "))
marks.append(f2)
f3 = int(input("Enter marks here: "))
marks.append(f3)
f4 = int(input("Enter marks here: "))
marks.append(f4)
f5 = int(input("Enter marks here: "))
marks.append(f5)
f6 = int(input("Enter marks here: "))
marks.append(f6)
f7 = int(input("Enter marks here: "))
marks.append(f7)

marks.sort() # This line sorts the list 'marks' in ascending order. Since the input is taken as strings, the sorting will be done based on the ASCII values of the characters. For example, "10" will come before "2" because "1" has a lower ASCII value than "2". If you want to sort the marks as numbers, you should convert the input to integers before appending them to the list.

print(marks)