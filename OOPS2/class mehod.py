"""
A class method is bound to the class and receieves the class
as an imlplicit first argument.

Note: static method cant access or modify and generally for utility.

#-------------
class Student:
    @classmethod  #decorator
    def collage(cls):
        pass

"""

class Person:
    name = "anonymous"

    # def changeName(self, name):
    #     self.__class__.name = "Rahul"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Sudhanshu Verma")
print(p1.name) #Sudhanshu Verma
print(Person.name) #anonymous

"""
1) Static methods
2) class methods  (cls)
3) instance methods (self)
"""