weight = int(input("Enter your weight "))
unit = input("(l)bs or (k)g: ")

if unit == "L":
    print(weight*0.453592)
elif unit =="K":
    print(weight*2.2)

#------

"""
1️⃣ Positive & Even
Write a program to check if a number is positive and even.
"""
num = int(input("Enter the number : "))

if num > 0 and num %2 ==0:
    print("number is +ve and even number")

"""
10️⃣ Temperature Status
Input temperature:
Above 30 → "Hot"
Between 15 and 30 → "Normal"
Below 15 → "Cold"
"""

temp = int(input("Enter the temp: "))

if temp > 30:
    print("Hot")
elif 15 <= temp <= 30:
    print("Normal")
else:
    print("Cold")

"""
1️⃣3️⃣ Leap Year Check
A year is leap if:
divisible by 4 and
not divisible by 100
or divisible by 400
"""

year = int(input("Enter the year :"))

if (year/4 ==0 and  year/100 !=0) or (year/400 ==0):
    print("It is a leap year")
else:
    print("This is not a leap year")

"""
1️⃣4️⃣ Triangle Validity
Check if 3 sides can form a triangle:
sum of any two sides > third side
"""

side1 = int(input("Please type the first side of the triangle"))
side2 = int(input("Please type the first side of the triangle"))
side3 = int(input("Please type the first side of the triangle"))

if (side1 + side2 > side3) and (side3 + side2 > side1) and (side3 +side1 > side2):
    print("It can form a triangle ")
else:
    print("This cannot form a triangle becasue one side cant be greater than 2 sides")

    """
    1️⃣1️⃣ Exam Grade System
≥ 90 → A
≥ 75 and < 90 → B
≥ 50 and < 75 → C
< 50 → Fail

    """
grade = int(input("Type your grade"))

if grade >= 90:
    print("A")
elif (grade >= 75) and (grade<90):
    print("B")
elif (grade >= 50) and (grade < 75):
        print("C")
else:
    print("Fail")

    """
    1️⃣5️⃣ Electricity Bill Category
        Units:
        ≤ 100 → Low usage
        101–300 → Medium usage
        300 → High usage
    """
units =int(input("Enter the units consumption"))

if units <=100:
    print("Low usage")
elif(units>100) and (units<=300):
    print("Medium usage")
else:
    print("High usage")
"""
1️⃣3️⃣ Leap Year Check
A year is leap if:
divisible by 4 and
not divisible by 100
or divisible by 400

"""

year = int(input("Enter the year"))

if (year%4==0 and year%100!=0) or (year %400 ==0):
    print("This year is leap year")
else:
    print("This year is non leap year")


"""
You’re building a login validation system.
Rules:
Username must be "admin"
Password must be "1234"
OTP must be "9999"
Output:
If all three are correct → "Login successful"
If username is wrong → "Invalid username"
If username is correct but password is wrong → "Invalid password"
If username & password are correct but OTP is wrong → "Invalid OTP"
"""

username = input("Please type the username").lower()
password = input("Please type the password")
otp = input("Please type the OTP")

if (username== "admin") and (password=="1234") and (otp=="9999"):
    print("Login successful")
elif(username=="admin") and (password!="1234"):
    print("Invalid password")
elif(username== "admin") and (password=="1234") and (otp!="9999"):
    print("Invalid OTP")
else:
    print("Invalid username")


""""
🔥 Interview Question 2: Income Tax Slab Validator
🧠 Problem
Create a tax eligibility system.
Rules:
Age < 18 → "No tax"
Age ≥ 18 and income ≤ 250000 → "No tax"
Income between 250001 and 500000 → "5% tax"
Income between 500001 and 1000000 → "20% tax"
Income > 1000000 → "30% tax"
"""

age = int(input("Enter your age"))
income = int(input("Enter your income"))

if age < 18:
    print("No Tax")
elif income<=250000:
        print("No Tax")
elif income<=500000:
        tax =income*0.05
        print(f"Tax will be 5 %, hence {tax}")
elif income <= 1000000:
        tax = income * 0.20
        print(f"Tax will be 20 %, hence {tax}")
else:
        tax =income*.30
        print(f"Tax will be 30 %, hence {tax}")

"""
You are building a bank loan eligibility system.
Inputs:
age
salary
credit_score
existing_loan → (yes / no)
✅ Eligibility Rules
Step 1️⃣ (Age Gate – Mandatory)
If age < 21 → "Not eligible for loan" (STOP checking further)
Step 2️⃣ (Salary Check)
Salary must be ≥ 25,000
If salary < 25,000 → "Salary too low"
Step 3️⃣ (Credit Score Logic)
If credit score ≥ 750 → "Loan Approved"
If credit score between 650 and 749:
If existing_loan == "no" → "Loan Approved"
Else → "Existing loan detected"
If credit score < 650 → "Low credit score"
⚠️ Interview Traps (VERY IMPORTANT)

"""

age=int(input("TYpe your age"))
salary=int(input("TYpe your salary"))
credit_score=int(input("Type your credit score"))
existing_loan = input("Please tell us if you are have existing loan? 'YES' or 'NO'")

if age < 21:
    print("No eligible for loan")
elif salary < 25000:
    print("Salary too low")
elif credit_score >=750:
    print("Loan approved")
elif (credit_score >= 650) or (credit_score<750):
    if existing_loan == "NO":
        print("Loan Approved ")
    else:
        print("Existed Loan Detected")
else:
    print("Low Credit score")

