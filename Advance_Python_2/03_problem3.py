
# 3. A list contains the multiplication table of 7. write a program to convert it to
# vertical string of same numbers.

table = [str(7 * i) for i in range(1, 11)]  # List comprehension to create multiplication table of 7
vertical_string = "\n".join(table)  # Joining the list elements with newline character to create a vertical string
print(vertical_string)  # Output: 7\n14\n21\n28\n35\n