"""a = 5
b = 20

sum = a+ b
print(sum)

diff = a-b
print(diff)
"""
# Now This is considered as procedural programming

# Then function taught how to decrease the redundancy and enhance reusability

# Then we do Object oriented porgamming, in order to decrease redundancy and increase reusability, we use OOPS

# What can we consider an object example: keyboard, mouse and so on

# First we make a class before creating an object
# Consider a school has a class and inside class there is students(objects)

# Few examples of Objects in python are : Lists, Strings

"""
Class: It is a blueprint for creating objects.

Example : 

class Student:
    name="Sudhanshu Verma"
We always start the name of the class with uppercase character.

# creating Object (instance)
s1 = Student()
print(s1.name)
"""

class Student:
    name = "Sudhanshu Verma"

#creating objects (instance or instances of class)
s1 = Student()
print(s1)
#output: <__main__.Student object at 0x104a5d610>

print(s1.name)
#Output: Sudhanshu Verma

#-----------------------------------------------------

"""
One more example: Lets make car class and write its attrributes
"""

#First lets make a class
class Car:
    color="black"
    brand = "Mercedes"
    model = "SVG"
# Lets create objects using the class attributes
car1 = Car()
print(car1.color)
print(car1.brand)
print(car1.model)

#----------------------



