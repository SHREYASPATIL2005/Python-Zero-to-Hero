class Employee:
	a = 1

	def __init__(self):
		self.fname = "Default"
		self.lname = "Name"

	@property
	def name(self):
		return f"{self.fname} {self.lname}"

	@name.setter
	def name(self, value):
		self.fname = value.split(" ")[0]
		self.lname = value.split(" ")[1]

	@classmethod
	def show(cls):
		print(f"The class attribute of a is {cls.a}")


e = Employee()
e.a = 45

e.name = "Harry Khan"
print(e.fname, e.lname)

e.hello = "Hello World"
e.world = "07"
e.show()