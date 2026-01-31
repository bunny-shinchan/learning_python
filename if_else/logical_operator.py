""""
logical operator
and : Both conditions should be true
or
not ->

"""

has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and not has_criminal_record:
    print("Eligible for loan")


"""
comparision operators 
< 
>
<=
>=
==
!=

"""

temp = 30

if temp > 30:
    print("Its is hot day")
else:
    print("Its not a hot day")

----

name = input("Enter your name")

if name> str(3):
    print("Name must be at least 3 characters")
elif name < str(50):
    print("name can be maximum of 50 characters")
else:
    print("name looks good")


name="J"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) < 50:
    print("name can be maximum of 50 characters")
else:
    print("Name is good")

#-----
"""
Operator	Meaning	                    Example
==	        Equal to	                a == b
!=	        Not equal to	            a != b
>	        Greater than	            a > b
<	        Less than	                a < b
>=	        Greater than or equal to	a >= b
<=	        Less than or equal to	    a <= b
"""
