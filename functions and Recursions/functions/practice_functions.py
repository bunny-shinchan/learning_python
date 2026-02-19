"""

write a function to print the length of a list. List is the parameter.

Write a function to print the elements of a list in a single line. List is the parameter.

Write a function to define the factorial of n, n is the parameter.

Write a function to convert USD to INR.

"""


# cities = [ "Delhi" , "Mumbai" , "Harayana" ]
# heros = ["Thor", "Iron man", "Captain america"]
#
# def print_len(list):
#     print(len(list))
#
# print_len(cities)
# print_len(heros)

#-------------

"""
Write a function to print the elements of a list in a single line. List is the parameter.
"""
# names = ["Sid", "Verma", "Sharma" ]
#
# def printitems(list) :
#     for name in list:
#         print(name, end=" ")
#
# printitems(names)

"""
Write a function to define the factorial of n, n is the parameter.
"""

# def factor_num(user_input):
#     result =1
#     while user_input > 1:
#         result *= user_input
#         user_input -=1
#     return result
#
# print(factor_num(5))

"""
Write a function to convert USD to INR.
"""
# usd_value = int(input("Enter the USD value to convert into INR"))
#
# def converter(usd_value):
#     inr = usd_value *83
#     print(inr)
# converter(usd_value)

"""
WAF to take a number as a input.

IF the the number is odd and even, print even num and if odd print odd
"""



# def check_num(num):
#     if user_input%2 ==1:
#         print("This number is odd")
#     else:
#         print("This number is even")
#
# user_input = int(input("Enter a number : "))
# check_num(user_input)


#-------------------------------------------------


"""
🧠 2️⃣ Reverse a Number (Without converting to string)

Write a function:

reverse_number(n)


Example:

Input: 1234
Output: 4321


Rules:

Do NOT convert number to string.

Use arithmetic logic only.

👉 This tests:

Modulus %

Integer division //

Loop logic

-----

🧠 3️⃣ Count Vowels in a String

Write a function:

count_vowels(text)


Return the number of vowels in a string.

Handle uppercase and lowercase letters.

Ignore spaces and symbols.

Example:

Input: "Hello World"
Output: 3


👉 Tests:

Loops

Condition checking

String handling
------
🧠 4️⃣ Find Second Largest Number in a List

Write a function:

second_largest(numbers)


Rules:

Do NOT use sort()

Do NOT use max() twice

Solve using logic

Example:

[10, 5, 8, 20, 15]
Output: 15
"""


# def revese_num(i):
#     last_digit = 0
#     reversed_num = 0
#     while i > 0:
#         last_digit = i % 10
#         reversed_num = reversed_num *10 + last_digit
#         i = i // 10
#     return  reversed_num
# i = int(input("Enter a number : "))
#
# print(revese_num(i))


"""
🧠 Prime Number Checker
Problem:

Write a function:

is_prime(n)

Requirements:

Return True if n is prime

Return False otherwise

Handle edge cases:

0

1

Negative numbers

"""

# def is_prime(n):
#
#     if n <=1:
#         return False
#     for i in range(2, n):
#         if n%i == 0:
#             return False
#     return True
#
# n = int(input("Enter a number to check if it is prime or not"))
# print(is_prime(n))


# def is_prime(num):
#     if num <=1:
#         return False
#     for counter in range(2, num):
#         if num%counter == 0:
#             return False
#     return True
#
# num = int(input("Enter a number to check if it prime or not : "))
# print(is_prime(num))

# def count_vowels(text):
#     count = 0
#     vowels = "aeiouAEIOU"
#     for char in text:
#         if char in vowels:
#             count +=1
#     return count
# try:
#     text = input("Enter a word to check the number of vowels")
# except:
#     print("Enter a valid string")
# print(count_vowels(text))
"""
Write a function:

count_vowels(text)

Requirements:

Return the number of vowels in the string

Count both uppercase and lowercase vowels

Ignore spaces and symbols

Do NOT use built-in shortcuts like count() repeatedly

🔎 Example
Input: "Hello World"
Output: 3


Because:

e

o

o

"""
vowels = "aeiouAEIOU"

def count_vowels(text):
    count = 0
    for char in text:
        if char in vowels:
            count +=1

    return count

text = input("Enter a word and check how many vowels are there")
print(count_vowels(text))


































