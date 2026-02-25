"""

Attributes: Variable or a data

Class attribute: that means it is common for the whole class
object attribute: It will be different for difference objects.

For example:
    if we have a class called Student()
    Student() -> s1,s2,s3,s4
        Now, s1 can have its own name
             s2 can have its own name...
             s3 ...
             s4....

        Now, as we have many instances or objects for the class Student.
        name should be an instance/onject attribute
        In that case, when the data is different for every object/instance, we notify that as a self.name ()
"""
# Let's say, we are creating a database for students for a particular college. in that case, we won't be passing college
#   as a parameter as we are not going to change the name of the college.

class Student:
    college_name =  "Sheridan college"
    name ="anonymous"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database.. ")

s1 = Student("Vienna", 98)
print(s1.name, s1.marks)
print(s1.college_name)
print()


#----------------------------------------

class Student:
    college_name =  "Sheridan college"
    name ="anonymous" # class attribute
    def __init__(self, name, marks):
        self.name = name #obj attribute  > class attribute
        self.marks = marks
        print("Adding new student in Database.. ")

s1 = Student("Vienna", 98)
print(s1.name, s1.marks)
print(s1.college_name)
print(s1.name) #This will print object attribute as it has a higher priority