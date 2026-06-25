n = int(input("Enter a number to generate its multiplication table: "))


table = [n*i for i in range(1, 11)]  # List comprehension to create a multiplication table for n
print(f"Multiplication table for {n}: {table}")