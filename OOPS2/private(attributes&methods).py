"""
Private (like) attributes and Methods

Conceptual Implementations in Python


Private attributes and methods are meant to be used only within the class and are not
accessible from outside the class.

OOPS - Private and public
"""

#Public class
class Student:
    def __init__(self, name):
        self.name = name

s1= Student("Sudhanshu")
print(s1.name)

#private class

# class Account:
#     def __init__(self, acc_num, acc_pass):
#         self.__acc_num = acc_num # when we make the variable private, we wont be able to access it
#                                     #if it is outside the class.
#         self.__acc_pass = acc_pass
#
# acc1 = Account("1234", "abdcde")
#
# print(acc1.acc_num)
# print(acc1.acc_pass)

"""
Traceback (most recent call last):
  File "/Users/sudhanshu/Desktop/Study Courses/Python with Mosh/learning_python/OOPS2/private(attributes&methods).py", line 31, in <module>
    print(acc1.acc_num)
          ^^^^^^^^^^^^
AttributeError: 'Account' object has no attribute 'acc_num'


This will be the error message if we try to access any private attribute outside the class. 
"""


class Account:
    def __init__(self, acc_num, acc_pass):
        self.__acc_num = acc_num
        self.__acc_pass = acc_pass

    def reset_pass(self):  # we can define a method
        print(self.__acc_pass)

acc1 = Account("1234", "abdcde")
print(acc1.reset_pass())


# We can also put __ before the function to make them private.

class Person:
    __name = "anonymous"

    def  __hello(self, name):
        print("hello person!")

    def welcome(self):
        self.__hello()


p1 = Person()

print(p1.name)
print(p1.welcome()) # we wont be able to print this too as we have made the function __hello private.

# Private attributes and methods are meant to be used only within  the class and are not
# accessible from outside the class.
