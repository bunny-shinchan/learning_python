"""
Abstraction:
Hiding the implementation details of a class and only showing the essential features to the user.
"""

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("Car started ... ")



car1 = Car() #This is called abstraction when we make an object but we do not care about the
            # details of them. We just want to use them.
            # This is considered as abstraction 
car1.start()