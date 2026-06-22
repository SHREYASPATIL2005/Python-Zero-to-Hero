class Calculator:
    def __init__(self, n):
        self.n = n  

    def square(self):
        print(f"The square of {self.n} is {self.n ** 2}")

    def cube(self):
        print(f"The cube of {self.n} is {self.n ** 3}")

    def squareroot(self):
        print(f"The square root of {self.n} is {self.n ** 0.5}")

    @staticmethod
    def hello():
        print("Hello World!")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()
a.hello()