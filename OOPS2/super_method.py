#Super method is used to access methods of the parent class

#This is related to inheritance
#For example:

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped.")

class TotyotaCar(Car):
    def __init__(self,name):
        super().__init__(type)
        self.name = name
        super().start()

car1 = TotyotaCar("prius")
print(car1.type) # if we try to print this without defining the super method, we will get an error shown below.

"""
Traceback (most recent call last):
  File "/Users/sudhanshu/Desktop/Study Courses/Python with Mosh/learning_python/OOPS2/super_method.py", line 23, in <module>
    print(car1.type)
          ^^^^^^^^^
AttributeError: 'TotyotaCar' object has no attribute 'type'
"""

# When we write super(), we are generally referring to the parent.

