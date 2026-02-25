"""
Create student class that takes name and marks of 3 subjects as arguments in constructor.
Then create a method to print the average.
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum +=value
        print("Hi,", self.name, "your average score is : ", sum/3)

s1 = Student("Sudhanshu Verma", [90,89,98])
s1.get_avg()

"""
Create Account class with 2 attributes -balance and account number.
Create methods for debit, credit and printing the balance.
"""

class Account:

    def __init__(self, balance, account_num):
        self.balance = balance
        self.account_num = account_num

    def debit(self, amount):
        self.balance -= amount
        print("Rs. ", amount, "was debited")
        print("Total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs. ", amount, "was credited")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 1234)
acc1.debit(1000)
acc1.credit(5000)
acc1.credit(40000)
