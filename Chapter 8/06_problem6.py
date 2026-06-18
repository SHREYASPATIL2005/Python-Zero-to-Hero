def inch_to_cms(inches):
   return inches * 2.54

inches = float(input("Enter length in inches: "))
print(f"{inches} inches is equal to {inch_to_cms(inches)} centimeters.")

