"""Q1️⃣ Print numbers
Write a program that prints numbers from 1 to 10 using a while loop."""
from turtledemo.penrose import start

# num = 1
# while num <= 10:
#     print(num)
#     num+= 1
"""
Q2️⃣ Reverse counting
Print numbers from 10 to 1 using a while loop.
"""
# i=10
#
# while i>=1:
#     print(i)
#     i-=1


"""
Q3️⃣ Even numbers
Print all even numbers between 1 and 20 using a while loop.
"""
# i = 1
#
# while i <=20:
#     if i%2==0:
#         print(i)
#     i+=1

"""
Q4️⃣ Hello Python
Print "Hello Python" 5 times using a while loop.
"""

# i =1
# while i <= 5:
#     print("Hello Python ")
#     i+=1

""""
🟡 Level 2: Input + Loop
Q5️⃣ Sum of numbers
Take a number n from the user and print the sum of numbers from 1 to n.
"""

# user_input = int(input("Type a number : "))
# counter = 1
# total = 0
# while counter <= user_input:
#     total += counter # total = total +counter
#     counter += 1
# print(total)

"""
1️⃣ Count till n
Take a number n from the user and print numbers from 1 to n.
"""

# user_input = int(input("Type a number"))
# count = 1
#
# while user_input >= count:
#     print(count)
#     count += 1

"""
🟢 Level 1: Reinforce the Basics
1️⃣ Count till n
Take a number n from the user and print numbers from 1 to n.
2️⃣ Reverse count
Take a number n and print numbers from n to 1.
3️⃣ Even numbers sum
Take a number n and print the sum of all even numbers from 1 to n.
4️⃣ Odd numbers sum
Take a number n and print the sum of all odd numbers from 1 to n.
5️⃣ Multiplication table
Take a number n and print its table up to 10.
🟡 Level 2: Loop + Conditions
6️⃣ Count evens
Take a number n and count how many even numbers exist between 1 and n.
7️⃣ Count digits
Take a number from the user and count how many digits it has.
Example:
Input: 34567
Output: 5
8️⃣ Sum of digits
Take a number from the user and print the sum of its digits.
Example:
Input: 1234
Output: 10
9️⃣ Reverse a number
Take a number from the user and print its reverse.
Example:
Input: 508
Output: 805
🟠 Level 3: Real Logic Thinking
🔟 Factorial
Take a number n and print its factorial.
Example:
Input: 5
Output: 120
1️⃣1️⃣ Prime check
Take a number and check whether it is prime or not.
1️⃣2️⃣ Guess the number
Keep asking the user to guess a number until they guess 7.
🔥 Level 4: Mini Challenges
1️⃣3️⃣ Password loop
Keep asking for a password until the user enters "python123".
1️⃣4️⃣ ATM menu
Start with balance = 10000.
Show a menu until the user chooses exit:
1. Check balance
2. Withdraw
3. Exit
"""

"""
2️⃣ Reverse count
Take a number n and print numbers from n to 1.
"""
# user_input = int(input("Type a number: "))
#
#
# while user_input>=1:
#     print(user_input)
#     user_input = user_input -1

# user_input = int(input("Type a number: "))
#
# while user_input >= 1:
#     if user_input%2== 0:
#         print(user_input)
#     user_input = user_input-1
"""
3️⃣ Even numbers sum
Take a number n and print the sum of all even numbers from 1 to n.

lets take a number : user_input
count =1
"""
# user_input = int(input("Type a number: "))
# count =1
# total =0
#
# while user_input>=count:
#     if count%2==0:
#         total = total+ count # sum of even numbers
#         #now we need to stop the loop
#     count+=1
# print(total)

"""
1️⃣ Sum of odd numbers (very similar)
Take a number n and print the sum of all odd numbers from 1 to n.
"""
# user_input = int(input("Type a number: "))
# count = 1
# total =0
#
# while user_input>= count:
#     if count%2 ==1:
#         total = total +count
#
#     count = count+1
# print(total)

"""
2️⃣ Sum of numbers divisible by 3
Take a number n and print the sum of all numbers divisible by 3 from 1 to n.
"""



# while user_input>= count:
#     if count %3 == 0:
#         total = total + count
#     count = count +1
#
# print(total)


"""Count even numbers
Take a number n and count how many even numbers exist from 1 to n.
(Notice: count instead of sum — only 1 small change)"""

# user_input = int(input("Enter a number: "))
# count =1
# count_even =0
#
# while user_input >= count:
#     if count %2 ==0:
#         count_even = count_even+1
#
#     count = count+1
# print(count_even)

"""
4️⃣ Count odd numbers
Take a number n and count how many odd numbers exist from 1 to n.
"""

# user_input = int(input("Enter a number: "))
# count =1
# count_odd = 0
#
# while user_input >= count:
#     if count %2 == 1:
#         count_odd = count_odd +1
#     count +=1
# print(count_odd)


"""
🟡 Slight Twist (Same logic, more thinking)
5️⃣ Sum of numbers in a range
Take two numbers:
start
end
Print the sum of all numbers between them (inclusive).
Example:
Input: 3, 7
Output: 25   (3+4+5+6+7)
"""

# start = int(input("Enter the first number: "))
# end = int(input("Enter the second number: "))
# total = 0
#
# while start <=end:
#     total = total +start
#     start = start +1
# print(total)

"""
A1️⃣ Sum of odd numbers between start and end
Take two numbers and print the sum of all odd numbers in that range.
👉 Only change from last problem:
even → odd
"""

# first_num = int(input("Enter the first number"))
# sec_num = int(input("Enter the second number"))
#
# total = 0
#
# while first_num<=sec_num:
#     if first_num %2 == 1:
#         total = total + first_num
#     first_num = first_num + 1
# print(total)

"""
A2️⃣ Count numbers between start and end
Take two numbers and print how many numbers exist in that range.
👉 Only change:
Add 1 instead of adding the number.
"""

first_num = int(input("Enter the first number"))
sec_num = int(input("Enter the second number"))

count_num =0

while first_num <=sec_num:
    count_num = count_num +1
    first_num +=1

print(count_num)