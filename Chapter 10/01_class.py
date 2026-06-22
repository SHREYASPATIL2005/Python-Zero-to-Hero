class Employee:
    language = "Python" # This is a class attribute
    salary = 100000

harry = Employee()
harry.name = "Harry"   # This is an instance attribute
print(harry.name,harry.language,harry.salary)

rohan = Employee()
rohan.name = "Rohan roro robinson"
print(rohan.name,rohan.language,rohan.salary)  


# Here name is instance attribute and language and salary are class attributes as they directly belong to the class.

