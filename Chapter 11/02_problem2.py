class Animals:
    pass

class Pet(Animals):
    pass

class Dog(Pet):

    @staticmethod
    def bark():
        print("Woof! Woof!")

d = Dog()
d.bark()