class Number:
    
    def __init__(self, value):
        self.value = value

    def __add__(one,two): # __dunder__ method for addition  
            return Number(one.value + two.value)

    def __sub__(one,two): # __dunder__ method for subtraction
            return Number(one.value - two.value)

    def __mul__(one,two): # __dunder__ method for multiplication
            return Number(one.value * two.value)

    def __truediv__(one,two): # __dunder__ method for division
            if two.value == 0:
                raise ValueError("Cannot divide by zero")
            return Number(one.value / two.value)

    def __str__(self):
        return str(self.value)
    
p1 = Number(10)
p2 = Number(5)

print(p1 + p2) # 15 # p1.__add__(p2) is called
print(p1 - p2) # 5  # p1.__sub__(p2) is called
print(p1 * p2) # 50 # p1.__mul__(p2) is called
print(p1 / p2) # 2.0 # p1.__truediv__(p2) is called


# __str__() # Used to return a string representation of the object. It is called when we use the print() function on an object.
# __len__() # Used to return the length of the object. It is called when we use the len() function on an object.
