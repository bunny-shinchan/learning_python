"""
1️⃣ Print numbers from n to 1

Example:

Input: 5
Output:
5
4
3
2
1
----

2️⃣ Print numbers from 1 to n

Same as above — but reversed thinking.

3️⃣ Sum of first n natural numbers

Example:

Input: 4
Output: 10   # 4 + 3 + 2 + 1


👉 Ask yourself:
How can sum(n) be written using sum(n-1)?

---
4️⃣ Factorial

You already know this one:

5! = 5 × 4 × 3 × 2 × 1


👉 What is the smallest factorial case?
-----

"""

# def print_num(n):
#     if (n == 0):
#         return
#     else:
#         print(n)
#         return print_num(n-1)
#
# print_num(5)


"""
🟡 Level 2 – Slightly More Thinking
5️⃣ Count digits in a number

Example:

Input: 54321
Output: 5


👉 How can you reduce the number each time?

6️⃣ Sum of digits

Example:

Input: 1234
Output: 10


👉 Think about:

Last digit

Remaining number

7️⃣ Reverse a string

Example:

Input: "hello"
Output: "olleh"


👉 How do you reduce the string each step?

"""

"""
🟠 Level 3 – Good Practice
8️⃣ Check if a string is palindrome
"madam" → True
"hello" → False


👉 Compare which characters?
"""


""""

1️⃣ Print numbers from n to 1

Example:

Input: 5
Output:
5
4
3
2
1

"""

# def print_num(n):
#     if n == 0:
#         return 1
#     else:
#         print(n)
#         return print_num(n-1)
#
# print_num(5)

# def fact(n):
#     if (n == 0 or n ==1 ):
#         return 1
#     else:
#         print(n)
#         return n * fact(n-1)
# print(fact(6))


# def sum_num(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum_num(n -1)
#
# print(sum_num(5))



"""
Mentally it should be like this.

sum_num(5)
= 5 + sum_num(4)

= 5 + (4 + sum_num(3))

= 5 + (4 + (3 + sum_num(2)))

= 5 + (4 + (3 + (2 + sum_num(1))))

= 5 + (4 + (3 + (2 + (1 + sum_num(0)))))

"""


# def power_fun(x , y):
#     if y == 0:
#         return 1
#     else:
#         return x * power_fun(x , y-1)
#
# print(power_fun(3,3))


"""
🔶 Problem: Sum of Digits

Write a recursive function that returns the sum of digits of a number.

Example:
sum_digits(1234) → 10


Because:

1 + 2 + 3 + 4 = 10
"""


# def sum_of_digits(n):
#     if (n ==0 ):
#         return 0
#     else:
#         last_digit = n %10
#         return last_digit + sum_of_digits(n//10)
# print(sum_of_digits(1234))













