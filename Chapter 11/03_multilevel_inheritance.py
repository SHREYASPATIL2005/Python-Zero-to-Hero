class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)  # Prints the a attribute
# print(o.b)  # This will raise an AttributeError since 'b' is not an attribute of Employee


o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)