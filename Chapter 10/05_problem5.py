from random import randint

class Train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train number {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"The status of train number {self.trainNo} is running on time.")

    def getFare(self, fro, to):
        print(f"The fare for train number {self.trainNo} from {fro} to {to} is {randint(10,1000)}")


t = Train(374023)
t.book("Delhi", "Mumbai")
t.getStatus()
t.getFare("Delhi", "Mumbai")