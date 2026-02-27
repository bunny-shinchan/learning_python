"""
Inheritance

When one class(child/derived ) services the properties and methods of another class (parent/base)


class Car:
    ......

class ToyotoCar(Car):
    ......

"""

class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped.")

class TotyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = TotyotaCar("Fortuner")
car2 = TotyotaCar("prius")

print(car1.start())

"""
Types of Inheritance :

1) Single inheritance. 
2) Multi-level Inheritance. 
3) Multiple Inheritance.  
"""

 # Single Inheritance where we have one child class and one parent class.

 # Multi-level Inheritance where the class is derived again from a class class.

 # Multiple Inheritance:
#------------------------------
#multi-level Inheritance
class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped.")

class TotyotaCar(Car):
    def __init__(self,brand):
        self.name = brand

class Fortuner(TotyotaCar):
    def __init__(self, type):
        self.type = type
car1 = Fortuner("diesel ")
car1.start() # This is multi-level inheritance.


#------------------------------

# Mutiple Inderitance.

"Multiple class properties can be inherited"

#For example

class A:
    varA = "Welcome to class A"
class B:
    varB= "Welcome to class B"
class C(A, B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
