"""
🟢 Question 1 — Constructor & self (Easy)

Create a class Book:

Requirements:

Constructor should take title and author

Store them inside the object

Create a method display_info() that prints:

Title: <title>
Author: <author>

👉 Create one object and call the method.

Focus:

Proper use of __init__

Proper use of self

🟢 Question 2 — Encapsulation (Easy–Medium)

Create a class BankAccount:

Requirements:

Private variable __balance

Constructor takes initial balance

Method deposit(amount)

Method withdraw(amount) (only if balance is sufficient)

Method get_balance()

Test:

Create an object

Deposit money

Withdraw money

Print balance

Focus:

Use __balance

Do not allow negative withdrawals

🟢 Question 3 — Abstraction (Medium)

Create a class Car.

Requirements:

Public method start()

Inside start(), call two private methods:

__fuel_check()

__engine_on()

User should only call:

car.start()

Focus:

Hide internal working

Demonstrate abstraction clearly

🟢 Question 4 — Static Method (Medium)

Create a class MathUtils.

Requirements:

Static method is_even(number)

Returns True if even, False otherwise

Test it without creating an object.

Focus:

Use @staticmethod

No self

🟢 Question 5 — Understanding __int__ vs __init__ (Concept + Code)

Create a class Number:

Requirements:

Constructor takes a number and stores it

Define __int__() method that returns double the number

Test:

n = Number(5)
print(int(n))

Focus:

Difference between constructor and type conversion method

"""



#Answer 1

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Title: " , self.title, "Author: ", self.author)

book1 = Book("abs","Sudhanshu")

book1.display_info()

"""
🟢 Ready for Question 2 (Encapsulation)?

Write the BankAccount class with:

Private __balance

deposit()

withdraw()

get_balance()
"""

#Answer 2

class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("You have this amount in your account : ", self.__balance , ". Hence, you can't withdraw the requested money" )
    def get_balance(self):
        return self.__balance

acc1 = BankAccount(10000)
acc1.deposit(5000)
print(acc1.get_balance())

"""
🟢 Question 3 — Abstraction (Medium)

Create a class Car.

Requirements:

1️⃣ Public method:

start()

2️⃣ Inside start() call two private methods:

__fuel_check()

__engine_on()

3️⃣ User should only call:

car = Car()
car.start()

The user should NOT be able to directly call:

__fuel_check()

__engine_on()

That is abstraction.
"""

#Answer 3)

class Car:
    def __fuel_check(self):
        print("Checking fuel ... ")
    def __engine_on(self):
        print("Engine is on...")
    def start(self):
        self.__fuel_check()
        self.__engine_on()

Car1 = Car()
Car1.start()

"""
🟢 Question 4 — Static Method (Medium)

Create a class MathUtils.

Requirements:

1️⃣ Create a static method:

is_even(number)

2️⃣ It should:

Return True if number is even

Return False if number is odd

3️⃣ You must call it without creating an object.

Example usage:

MathUtils.is_even(4)
🧠 Important Rules

Use @staticmethod

Do NOT use self

Do NOT create an object
"""

class MathUtils:

    @staticmethod
    def is_even(number):
        if number %2 == 0:
            return True
        else:
            return False

print(MathUtils.is_even(6))

"""
🟢 Question 5

Create a class called Number.

Requirements:

1️⃣ Constructor:

Accept one number

Store it inside the object

2️⃣ Define a special method:

def __int__(self):

3️⃣ __int__() should:

Return double the stored number

🧠 Important Concept

When you call:

n = Number(5)
print(int(n))
"""


class Number:
    def __init__(self,number):
        self.number = number

    def __int__(self):
        return self.number * 2

n1 = Number(7)
print(int(n1))