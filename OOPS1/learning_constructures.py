"""
__int__ Function
Constructor

ALl classes have a function called __init__(), which is always executed when the object is being initiated.

#Creating a class
class Student:
    def __init__(self, fullname):
        self.name = fullname

#Creating object
s1 = Student("Sudhanshu")
print(s1.name)


The self parameter is a reference to the current instance of the class, and is used to access variables that
belongs to the class.
"""

class Student:
    name = "Sudhanshu Verma"
    def __init__(self):
        print(self) # <__main__.Student object at 0x100af1610>
        print("adding new student in Database.")

s1 = Student() # WHen we create an object, the init function is called by itself
            #():-> This is being used to call the constructor
            # self-> The new object is the self.
            # We get the print automaticall when we create an object as the constructors invoke by itself
print(s1) #<__main__.Student object at 0x1001d2ad0>

#----------------------------------------------------
class Student:
    name = "Sudhanshu Verma"
    def __init__(self,fullname):
        self.name = fullname
        print("Adding new student in Database.. ")
s1 = Student("Vienna")

print(s1.name)

#self -> The self parameter is a reference to the current instance of the class (object), and use used to access variables
#that belongs to the class.


s2 = Student("Arjun")
print(s2.name)


#--------------------------------------

class Student:
    name = "Sudhanshu Verma"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

        print("Adding new student in Database.. ")
s1 = Student("Vienna", 98)
print(s1.name, s1.marks)



s2 = Student("Arjun", 99)
print(s2.name, s2.marks)

#--------------------------------------

class Student:

    #defualt constructors
    def __init__(self):
        pass

    #parameterized constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

        print("Adding new student in Database.. ")
s1 = Student("Vienna", 98)
print(s1.name, s1.marks)



s2 = Student("Arjun", 99)
print(s2.name, s2.marks)