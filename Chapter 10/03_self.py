class Employee:
    language = "Python" # This is a class attribute
    salary = 100000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    '''def greet(self):
        print("Hello, welcome to the company!")'''
    
    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

harry = Employee()
harry.name = "Harry"   # This is an instance attribute
print(harry.name,harry.language,harry.salary)
harry.greet()

harry.getInfo()  # Employee.getInfo(harry)
