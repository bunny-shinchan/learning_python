"""
Few examples of built in functions

print()
len()
type()
range()

"""
# print("Sudhanshu Verma is a ", end =" ")# sep = " " sep is a separator
# print("hero") #end = "/n"
# len() # -> returns an int value
# range() # It takes start, stop, and steps as an argument



"""
User defined functions

The functions that are written by the programmer are called user defined functions.

"""
# def cal_prod(a, b):
#     print(a*b)
#     return a*b
#
# cal_prod() # if we execute this code, then we will get an error and it will ask to pass 2 arguments to call the function
"""
Traceback (most recent call last):
  File "/Users/sudhanshu/Desktop/Study Courses/Python with Mosh/learning_python/functions and Recursions/functions/built_in_function&user_defined_functions.py", line 27, in <module>
    cal_prod() # if we execute this code, then we will get an error and it will ask to pass 2 arguments to call the function
    ^^^^^^^^^^
TypeError: cal_prod() missing 2 required positional arguments: 'a' and 'b'

"""

# In order to pass

"""
Default Parameters 

Assigning a default value to parameter, which is used when no argument is passed.
"""

def cal_prod(a=4, b=2):
    print(a*b)
    return a*b

cal_prod()

cal_prod(3,4)


def cal_prod(a, b=2):
    print(a*b)
    return a*b

cal_prod(1)

# We can also make one value as a default like putting only b =2
# But we wont be able to consider a = 2, and leave b as default

##### As we need first the non default argument and then the default argument.

