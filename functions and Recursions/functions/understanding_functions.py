"""
Functions in python

Block of statements that perform a specific task.

def function_name(param1, param2)

    return val

function_name(agr1, arg2.. ) #function call


It takes input - We can consider this as parameters
output - it is the return
"""

#For example

a = 5
b = 10

sum = a+b
print(sum)

# lets assume we have more lines of code like we have to use the same logic of this sum again and again.
# if the code is repeating or getting redundant, then we need to use functions

def calc_sum(a, b): #def- means, we are defining
    sum = a+ b
    return sum

# Now we can use this function by calling it.

print(calc_sum(3,4)) #a and b are arguments -[supplying the value]

#function definition
def calculate_sum(a,b): # parameters
    return a + b

sum = calculate_sum(2,5) # function call, arguments
print(sum)


def print_hello():
    print("Hello")

print_hello()
print_hello()
print_hello()
print_hello()# We can call the function as many times as we would like.

#----------------------------------------------

print(print_hello())
"""This will return none"""
# None

"""If we do not have any return in the function, then it will return none"""

# create a function to calculate the average of 3 numbers


def avg(a,b,c):
    average = (a+b+c)/3

    return average

print(avg(2,3,4))

