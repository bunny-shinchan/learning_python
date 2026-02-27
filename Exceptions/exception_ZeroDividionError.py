"""try:
    age = int(input('Age: '))
    income = 20000
    risk = income /age
    print(age)
except ValueError:
    print("Invalid value")"""

# Age: 0
# Traceback (most recent call last):
#   File "/Users/sudhanshu/Desktop/Study Courses/Python with Mosh/learning_python/Exceptions/exception_ZeroDividionError.py", line 4, in <module>
#     risk = income /age
#            ~~~~~~~^~~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1

try:
    age = int(input('Age: '))
    income = 20000
    risk = income /age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print("Invalid value")