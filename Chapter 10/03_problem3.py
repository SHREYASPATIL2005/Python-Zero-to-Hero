class Demo:
    a = 4

d1 = Demo()
print(d1.a) # Prints the class attribute because instance attribute is not present
d1.a = 1 # Instance attribute is set

print(d1.a) # Prints the instance attribute because instance attribute is present. Instance attribute will override the class attribute if they have the same name.

print(Demo.a)  # class attribute is not changed because we have changed the instance attribute a for the object d1. The class attribute a is still 4.