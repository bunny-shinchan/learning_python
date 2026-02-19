# Recursion
# When a function calls itself repeatedly.

# The things that we can do with the loop, we can also do it via recursion and vice versa

"""def show(n):
    print(n)

show(5)"""

"""
Now lets say we want to print #5 #4 #3 #2 #1 in the same function.
For that we will use recursion 
"""

# First tell the function what work it needs to do?

def show(n):
    if(n ==0): # This will stop the function when the n will be 0
        return
    print(n)
    show(n-1)
show(5)

# Call Stack : When we call the function one function, second function , ....... this it is
# referred to call stack.


#Example: To find a factorial of a number

def fact(n):
    if(n == 0 or n ==1):# base case (stopping case)
        return 1
    else:
        return n * fact(n-1)

print(fact(4))
