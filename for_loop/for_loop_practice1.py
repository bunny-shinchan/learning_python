"""
Write a program of all the items in a shopping cart
to calculate the total cost of all the items in a shopping cart
"""

"""
prices = [10, 20, 30]
total = 0
for price in prices:
    total = total + price
print(f"Total : {total}")
"""

"""
🔹 Level 1: Absolute Basics (Warm-up)
Print 1 to N
Print numbers from 1 to N.
Constraint: Use a single for loop.
Print N to 1
Print numbers from N down to 1.
Constraint: No while loop.
Print Even Numbers
Print all even numbers between 1 and N.
Print Odd Numbers
Print all odd numbers between 1 and N.
Multiplication Table
Print the table of a given number up to 10.
🔹 Level 2: Logic + Conditions (Interview Gold)
FizzBuzz (Classic)
(You already know this 😄)
Print numbers from 1 to N:
“Fizz” for multiples of 3
“Buzz” for multiples of 5
“FizzBuzz” for multiples of both
Constraint: Single loop only.

Divisible by 3 or 5 (but not both)
Print numbers between 1 and N that are divisible by 3 or 5, but not both.

Count Evens and Odds
From 1 to N, count how many even and odd numbers exist.

Sum of Numbers
Find the sum of numbers from 1 to N using a for loop.

Sum of Even Numbers
Find the sum of all even numbers between 1 and N.

🔹 Level 3: Patterns Without Nested Loops
Print Stars in a Line
Print ***** for a given number N.
Constraint: No nested loops.
Print Numbers on One Line
Input: N
Output: 1 2 3 4 5 ... N
Repeat a Character N Times
Print a character (like #) N times in a single line.
"""

"""
Print 1 to N
Print numbers from 1 to N.
Constraint: Use a single for loop.
"""
# range (start, end) if you would like to include n then you would need to range(start, end + 1)
# user_input = int(input("type a number"))
#
# for num in range(1, user_input+1):
#     print(num)

"""
Print N to 1
Print numbers from N down to 1.
Constraint: No while loop.
"""

"""user_input = int(input("type a number"))

for num in range(user_input , 0, -1):
    print(f"user input : {user_input} and num is {num}" )"""

"""
Print Even Numbers
Print all even numbers between 1 and N.
"""

# user_input = int(input("type a number"))
#
# for even_num in range(1, user_input+1):
#     if even_num %2 == 0:
#         print(even_num)
#     else:
#         print(f"not even {even_num}")

"""
Print Odd Numbers
Print all odd numbers between 1 and N.
"""

# user_input = int(input("type a number"))
#
# for odd_num in range(1, user_input + 1):
#     if odd_num%2 ==1:
#         print(f"This is odd{odd_num}")

"""
Multiplication Table
Print the table of a given number up to 10.
"""
# user_input = int(input("type a number"))
#
# for mutiply_num in range(1 , 10 + 1):
#     product = mutiply_num *user_input
#     print(f"{user_input} * {mutiply_num} = {product}")

"""
🔹 Level 2: Logic + Conditions (Interview Gold)
FizzBuzz (Classic)
(You already know this 😄)
Print numbers from 1 to N:
“Fizz” for multiples of 3
“Buzz” for multiples of 5
“FizzBuzz” for multiples of both
Constraint: Single loop only.
"""

# user_input = int(input("type a number"))
#
# for nums in range(1, user_input + 1):
#     if (nums % 3 == 0) and (nums % 5 == 0):
#         print("FizzBuzz")
#     elif nums %3 == 0:
#         print("Fizz")
#     elif nums % 5 == 0:
#         print("Buzz")
#     else:
#         print(nums)
#

"""
Divisible by 3 or 5 (but not both)
Print numbers between 1 and N that are divisible by 3 or 5, but not both.
"""

# user_input = int(input("type a number"))
#
# for nums in range(1, user_input +1):
#     if (nums %3 == 0 or nums %5 == 0) and not (nums %3 == 0 and nums %5 == 0):
#         print(nums)


"""
Count Evens and Odds
From 1 to N, count how many even and odd numbers exist.
"""
# user_input = int(input("type a number"))
# count_odd = 0
# count_even = 0
#
# for num in range(1, user_input + 1):
#     if num %2 == 0:
#         count_even = count_even +1
#
#     else:
#         count_odd = count_odd +1
#
# print(f"even:  {count_even}")
# print(f"odd : {count_odd}")


"""
Sum of Numbers
Find the sum of numbers from 1 to N using a for loop.
"""

# user_input = int(input("type a number"))
# total = 0
#
# for num in range (1, user_input +1):
#     total = total + num
#
# print(f"Total is {total}")

"""
Sum of Even Numbers
Find the sum of all even numbers between 1 and N.
"""

user_input = int(input("type a number"))
sum_of_even =0
for num in range(1, user_input + 1):
    if num %2 ==0:
     sum_of_even+= num
print(sum_of_even)