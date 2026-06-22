class Employee:
    language = "Python" # This is a class attribute
    salary = 100000

harry = Employee()
harry.language = "JavaScript"   # This is an instance attribute
print(harry.language,harry.salary)


# Instance attribute will override the class attribute if they have the same name. In this case, harry.language will print "JavaScript" instead of "Python" because we have assigned a new value to the instance attribute language for the harry object.