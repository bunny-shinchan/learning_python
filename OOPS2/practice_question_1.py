"""
Question1 : Define a class to create a circle with radius r using the constructor.

            Define an Area() method of the class which calculates the area of the circle.
            Define a perimeter() method of the class which allows you to calculate the perimeter of the circle.


Question2 : Define an Employee class with attributes role, department and salary. This
class also has a showDetails() method

Create an Engineer class that inherits properties from Employee and

attributes : name and age
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) *( self.radius ** 2 )
    def perimeter(self):
        return 2*(22/7)*self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


#---------------------------------------------

class Employee:
    def __init__(self, role, dept, salary):
        self.role= role
        self.dept =dept
        self.salary = salary

    def showDetails(self):
        print("role:" , self.role)
        print("dept:", self.dept)
        print("salary :",  self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

engg1 = Engineer("Sudhanshu", 40)
engg1.showDetails()

#****************************************************

"""
Lets create a class called Order which stores item and its price. 

Use dunder function __gt__() to convey that:
    order1 > order2 if price of order1 > price of order2
"""

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, od2):
        return self.price > odr2.price

odr1 = Order("Chips", 20)
odr2 = Order("tea", 15)

print(odr1 > odr2)

