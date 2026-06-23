class Employee:
	a = 1

	@classmethod
	def show(cls): # cls refers to the class itself
		print(f"The class attribute of a is {cls.a}") # cls.a refers to the class attribute a


e = Employee()
e.a = 45

e.show()
