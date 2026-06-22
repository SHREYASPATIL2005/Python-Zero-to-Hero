class Employee:
    language = "Python" # This is a class attribute
    salary = 100000

    def __init__(self, name, language, salary):   # dunder method which is auto matically called when an object is created. It is used to initialize the attributes of the class.
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an employee object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

harry = Employee("Harry", "Python", 100000)
print(harry.name, harry.language, harry.salary)
harry.greet()

harry.getInfo()  # Employee.getInfo(harry)

rohan = Employee("Rohan", "Java", 90000)
print(rohan.name, rohan.language, rohan.salary)
rohan.greet()

rohan.getInfo()  # Employee.getInfo(rohan)
