"""
🔥 Interview-Level OOP Question (No Hints)

Design a class called InventoryItem with the following requirements:

The constructor should take:

name

price

quantity

The class should:

Prevent setting a negative price or quantity.

Automatically calculate total value (price * quantity).

Implement:

A method restock(amount) that increases quantity.

A method sell(amount) that decreases quantity only if enough stock exists.

A method __str__() that returns a clean string representation of the item.

A method __add__(other) so that adding two InventoryItem objects returns the combined total value (not a new object, just the numeric total value).

Make sure:

Data is properly encapsulated.

Direct modification of price and quantity is controlled.

"""

#Ans


class InventoryItem:
    def __init__(self, name, price, quantity):
        if (price <0) or (quantity < 0) :
            raise ValueError("Price and quantity cannot be negative")
        self.name = name
        self.__price =price
        self.__quantity = quantity


    def total_value(self):
        return self.__price *self.__quantity

    def restock(self, amount):
        if amount <=0:
            raise ValueError("Amount should be in +postive number and more than 0")
        self.__quantity +=amount

    def sell(self, amount):
        if amount <=0:
            raise ValueError("Amount should be in +postive number and more than 0")
        if amount > self.__quantity :
            raise ValueError("Quantity should be more than the input amount")
        self.__quantity -= amount
    def __str__(self):
        return f"Name: {self.name} , Price :{self.__price} , Quantity: {self.__quantity}, | Total Value: {self.total_value()}"

inv1 = InventoryItem("apple", 2, 2)
print(inv1)
inv1.restock(20)
print(inv1)
inv1.sell(10)
print(inv1)