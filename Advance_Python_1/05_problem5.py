n = int(input("Enter a number to generate its multiplication table: "))


table = [n*i for i in range(1, 11)]  # List comprehension to create a multiplication table for n
with open("Advance_Python_1/multiplication_table.txt", "a") as f:
    f.write(f"Multiplication table for {n}: {table}\n")  # Write the multiplication table to the file