"""Q2. Age Category
Write a program that:
Takes age
If age is 18 or more:
If age is 60 or more, print "Senior Citizen"
Else print "Adult"
Else:
Print "Minor"
"""
from unicodedata import category

age= int(input("Enter your age: "))

if age>=18:
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Adult")
else:
    print("Minor")


"""
Q4. Marks Validation + Grade
Write a program that:
Takes marks
If marks are between 0 and 100:
Assign grade:
≥90 → A
≥75 → B
≥50 → C
Else → Fail
Else:
"Invalid marks"
"""

marks = int(input("Enter your marks: "))

if 0<=marks<=100:
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    elif marks >= 50:
        print("C")
    else:
        print("Fail")
else:
    print("Invalid marks")

'''
Q5. ATM Withdrawal (Simple Logic)
Write a program that:
Takes balance and withdraw_amount
If withdraw_amount ≤ balance:
If withdraw_amount is a multiple of 100:
"Withdrawal successful"
Else:
"Enter amount in multiples of 100"
Else:
"Insufficient balance"
'''
balance = int(input("Enter your balance: "))
withdraw_amount = int(input("Enter your withdraw_amount: "))

if withdraw_amount <= balance:
    if withdraw_amount %100 == 0:
        print("Withdrawal successful")
    else:
        print("Enter amount in multiples of 100")
else:
    print("Insufficient balance")

'''
Takes username and password
If username is "admin":
Check if password is "1234"
If yes → "Login successful"
Else → "Wrong password"
Else:
"Invalid username"
'''

username = input("Enter your username: ")
password = input("Enter your password: ")

if username.lower() == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Inavlid username")



"""
🔹 Q1. Bank Account Status (Very Common)
Write a program that:
Takes balance
If balance is greater than 0:
If balance ≥ 10000 → print "Premium Account"
Else → print "Standard Account"
Else:
Print "Account is empty or overdrawn"
"""

balance = int(input("Enter your balance : "))

if balance > 0:
    if balance >= 10000:
        print("Premium Account")
    else:
        print("Standard Account")
else:
    print("Account is empty or overdrawn")


"""
Q5. Electricity Bill Slab (Classic Interview)
Write a program that:
Takes units
If units > 0:
If units ≤ 100 → "Low usage"
Else if units ≤ 300:
If units ≤ 200 → "Medium usage"
Else → "High usage"
Else → "Very high usage"
Else:
"Invalid units"
"""

units = int(input("Enter the units"))

if units >0:
    if units <=100:
        print("Low usage")
    elif units <=300:
        if units <=200:
            print("Medium Usage")
        else:
            print("High usage")
    else:
        print("Very High usage")
else:
    print("Invalid units")

    """
    🔹 Q3. Login + Role Check (Real System Logic)
Write a program that:
Takes username, password
If username is "admin":
If password is "1234":
Print "Welcome Admin"
Else → "Wrong password"
Else if username is "user":
If password is "abcd":
Print "Welcome User"
Else → "Wrong password"
Else:
"Unknown user"
👉 This forces multiple nesting paths."""

username = input("Enter your username ")
password = input("Enter your password")

if username.lower() == "admin":
    if password == "1234":
        print("Welcome Admin")
    else:
        print("Wrong password")
elif username.lower()== "user":
        if password == "abcd":
            print("Welcome user")
        else:
            print("Wrong password")
else:
    print("Unknown user")


"""
🔥 Q1. Bank Loan Eligibility System (Multi-Factor)
Write a program that takes:
age
monthly_income
credit_score
Rules:
If age is between 21 and 60:
If income ≥ 30,000:
If credit score ≥ 750 → "Loan Approved"
Else if credit score ≥ 600 → "Loan Approved with Higher Interest"
Else → "Low Credit Score"
Else → "Income too low"
Else → "Age not eligible"
👉 This tests deep nesting + ordered checks.
"""

age = int(input("Enter your age? "))
monthly_income = int(input("Enter your monthly income"))
credit_score = int(input("Enter your credit score"))

if 20<age<61:
    if monthly_income >= 30000:
        if credit_score>= 750:
            print("Loan Approved")
        elif credit_score>=600:
            print("Loan Approved with Higher Interest")
        else:
            print("Low Credit score")
    else:
        print("Income too low")
else:
    print("Age not eligible")

"""
🔥 Q4. University Admission System (Brutal Logic)
Take:
marks
entrance_exam ("pass" / "fail")
category ("general" / "reserved")
Rules:
If marks ≥ 50:
If entrance exam is "pass":
If category is "general":
If marks ≥ 75 → "Admission Confirmed"
Else → "Waitlisted"
Else (reserved):
If marks ≥ 65 → "Admission Confirmed"
Else → "Waitlisted"
Else → "Entrance exam failed"
Else → "Marks too low"
⚠️ This is pure nested hell (in a good way).
"""

marks = int(input("Enter your marks: "))
entrance_exam =input('Enter the extrance exam results("pass" / "fail") ')
category = input("Enter your category")

if marks>=50:
    if entrance_exam == "pass":
        if category =="general":
            if marks >=75:
                print("Admission confirmed")
            else:
                print("Waitlisted")
        elif category =="reserved":
            if marks >=65:
                print("Admission confirmed")
            else:
                print("Waitlisted")
        else:
            print("Invalid category")
    else:
        print("Entrance exam failed")
else:
    print("Marks too low")