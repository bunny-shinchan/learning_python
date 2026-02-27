
# 🔹 Question 1: Basic Inheritance
#
# Create a class Vehicle with:
#
# attribute: brand
#
# method: start() → prints "Vehicle is starting"
#
# Now create a class Car that inherits from Vehicle and:
#
# adds attribute: model
#
# creates an object of Car
#
# calls the start() method
#
# 👉 Goal: Understand how child class accesses parent methods.

class Vehicle:
    def __init__(self, brand):
        self.brand= brand

    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
c1 = Car("Toyota", "Camry")
c1.start()

# 🚗 Question: Multi-Attribute Inheritance
# 🔹 Step 1: Create a Parent Class Employee
#
# Attributes:
#
# name
#
# employee_id
#
# salary
#
# Methods:
#
# display_info() → prints all details
#
# calculate_bonus() → returns 10% of salary
#
# 🔹 Step 2: Create a Child Class Manager (inherits from Employee)
#
# Additional attributes:
#
# department
#
# team_size
#
# Requirements:
#
# Use super() properly to initialize parent attributes.
#
# Override calculate_bonus():
#
# Managers get 20% bonus instead of 10%.
#
# Add a new method:
#
# display_manager_info() → prints everything including department and team size.
#
# 🔹 Step 3: Create an Object
#
# Create a Manager object and:
#
# Print employee details
#
# Print bonus
#
# Print manager details

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print("Name: ", self.name)
        print("employee ID: ", self.employee_id)
        print("Salary: ", self.salary)
    def calculate_bonus(self):
        return self.salary * 0.10

class Manager(Employee):
    def __init__(self, name, employee_id, salary,department, team_size):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.team_size = team_size

    def calculate_bonus(self):
        return self.salary * 0.20
    def display_manager_info(self):
        super().display_info()
        print("Department : ", self.department)
        print("Team Size : ", self.team_size)

class SeniorManager(Manager):
    def __init__(self, name, employee_id, salary,department, team_size, region):
        super().__init__(name, employee_id, salary, department, team_size)
        self.region = region
    def calculate_bonus(self):
        return super().calculate_bonus() * 1.5


m1 = Manager("Sudhanshu", "1234", 200000, "IT", 10)
m1.display_info()
print(m1.calculate_bonus())
m1.display_manager_info()


class Payment:
    def __init__(self, amount):
        self.amount = amount
    def process_payment(self):
        print("Processing generic payment of ", self.amount)
    def calculate_fee(self):
        return self.amount * 0.02
class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number
    def calculate_fee(self):
        return super().calculate_fee() + (self.amount * 0.01)

class CreditCardPayment(CardPayment):
    def __init__(self, amount, card_number, reward_points):
        super().__init__(amount, card_number)
        self.reward_points = reward_points
    def calculate_fee(self):
        return super().calculate_fee() + (self.amount * 0.02)
    def process_payment(self):
        super().process_payment()
        print("Reward points earned: ", self.reward_points)
payments = [Payment(20000),  CardPayment(20000, 4567),  CreditCardPayment(20000, 4567, 2000)]

for p in payments:
    p.process_payment()
    print("Fee: ", p.calculate_fee())
    print()




























