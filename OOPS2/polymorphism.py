"""
Polymorphism : Operator Overloading

When the same operator is allowed to have difference meaning according to the context

Operators and Dunder functions

a + b  #addition        a.__add__(b)
a - b #subtraction      a.__sub__(b)
a * b #multiplication   a.__mul__(b)
a / b # division        a.__truediv__(b)
a % b #addition         a.__mod___(b)

decorators: @gettor and @settor :

"""
#This is implicit overloading
print(1+2) #3

print("Sudhanshu" + "Verma") #concatenate

print(type("apna"))
print([1,2,3] + [4, 5 , 6]) #,merge  This is operator overloading

print(type([1,2,3]))
print("#-------------------------------")

#----------------

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real, "i + ", self.img, "j")

    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(5,6)
num2.showNumber()
"""
1 i +  3 j
5 i +  6 j
Now, we would like to add these numbers.
In order to that, we will use the dunder functions
"""

num3 = num1.add(num2)
print("________________")
num3.showNumber()
print("****************")


#------------------------------------------------

#Now lets say we don't want to define a function and use simply num3 = num1 + num2 without getting an error.

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real, "i + ", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(5,6)
num2.showNumber()
"""
1 i +  3 j
5 i +  6 j
Now, we would like to add these numbers.
In order to that, we will use the dunder functions
"""

num3 = num1 + num2
print("________________")
num3.showNumber()

print("________________")

num3 = num1 - num2
print("________________")
num3.showNumber()