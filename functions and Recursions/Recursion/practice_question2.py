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

def fact(n):
    if (n == 0 or n ==1):
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))
































