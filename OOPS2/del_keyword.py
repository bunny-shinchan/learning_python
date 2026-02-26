""""
del keyword is used to delete object properties or object itself.

For example:

del s1.name
del s1


"""

class Student:
    def __init__(self, name):
        self.name = name

s1= Student("Sudhanshu")

del s1
print(s1)

"""
Traceback (most recent call last):
  File "/Users/sudhanshu/Desktop/Study Courses/Python with Mosh/learning_python/OOPS2/del_keyword.py", line 19, in <module>
    print(s1)
          ^^
NameError: name 's1' is not defined


We are getting this error because s1 was deleted and then we tried printing it. 

But if we try to print the name before deleting it, it will print the name and then delete the name.
"""

