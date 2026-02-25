"""
Encapsulation
Wrapping data and functions into a single unit(Object)

"""

class Account:
    def __init__(self, balance, account_num):
        self.balance = balance
        self.account_num = account_num
    def debit(self, amount):
        self.balance -= amount
        print(f"This {amount} was debited from the account number ")
        print("Total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance +=amount
        print(f"This {amount} was credited from the account number ")
        print("Total balance = ", self.get_balance())
    def get_balance(self):
        return self.balance

acc1 = Account(10000, 6789)
acc1.debit(5000)
acc1.credit(6000)
acc1.get_balance()

