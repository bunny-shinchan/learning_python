# Exception can be used to handle errors.

"""
age = int(input('Age: '))
print(age)

"""

# Age: asd
# Traceback (most recent call last):
#   File "/Users/sudhanshu/Desktop/Study Courses/Python with Mosh/learning_python/Exceptions/exception.py", line 3, in <module>
#     age = int(input('Age: '))
#           ^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'asd'

#Process finished with exit code 1
#Exit code 1 - means the program crashed because we passed a string instead of int.


# Let's try to handle this situation.
# We can use try and except constructs to handle

try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print("Invalid value")

# Age: shda
# Invalid value

#Process finished with exit code 0 which means the program completed successfully.


