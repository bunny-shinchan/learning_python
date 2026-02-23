
"""
Methods are function that belongs to objects.

# creating class
Class Student
    def __init__(self, fullname):
        self.name = fullname

#Creating object
s1 = Student("Karan")
s1.hello() | s1 - object name  |  hello() :- method name

#method
def hello(self):
    print("hello", self.name)

"""

"""
Class is collection two things :- 1) Data(attributes) 2) methods 
"""


class Student:
    college_name =  "Sheridan college"

    def __init__(self, name, marks):

        self.name = name #obj attribute  > class attribute
        self.marks = marks

    def welcome(self):
        print("Welcome student", self.name)
    def get_marks(self):
        return self.marks

s1 = Student("Vienna", 98)
s1.welcome()
print(s1.get_marks())

#if we do not write the parameter inside the method : def welcome():
"""
Traceback (most recent call last):
  File "/Users/sudhanshu/Desktop/Study Courses/Python with Mosh/learning_python/OOPS1/understanding_methods.py", line 37, in <module>
    s1.welcome()
TypeError: Student.welcome() takes 0 positional arguments but 1 was given
"""