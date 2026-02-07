"""
3️⃣ Even numbers sum
Take a number n and print the sum of all even numbers from 1 to n.
4️⃣ Odd numbers sum
Take a number n and print the sum of all odd numbers from 1 to n.

"""
from math import factorial

# user_input = int(input("Enter the number"))
# counter = 1
# sum = 0
#
# while user_input>=counter:
#     if counter%2 ==0:
#         sum = sum + counter
#     counter +=1
# print(sum)

# user_input = int(input("Enter the number"))
# counter = 1
# sum_odd = 0
#
# while user_input >= counter:
#     if counter %2 ==1:
#         sum_odd = sum_odd + counter
#     counter = counter +1


"""
🧠 Practice Question (Two Inputs)
🟡 Count numbers divisible by 3 between two numbers
Problem statement:
Take two integers from the user:
start
end
Print how many numbers between start and end (inclusive) are divisible by 3.
"""
# first_num = int(input("Enter the first number"))
# sec_num = int(input("Enter the second number"))
# count_num = 0
#
# while first_num <= sec_num:
#     if first_num %3 ==0:
#         count_num = count_num +1
#     first_num +=1
# print(count_num)

"""
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

""""
5️⃣ Multiplication table
Take a number n and print its table up to 10.
"""

# user_input = int(input("Enter a number: "))
# counter = 1
#
# while counter <= 10:
#
#     multiply = user_input * counter
#     print(f"{user_input} * {counter} = {multiply}")
#     counter +=1

"""
2️⃣ Print the multiplication table of a number from 10 to 1 (reverse order).
"""
# user_input = int(input("Enter a number: "))
# counter = 10
#
# while counter>=1:
#     multiply = user_input *counter
#     print(f"{user_input} * {counter} = {multiply}")
#     counter = counter -1

"""
3️⃣ Print only even multiples of a number (e.g., for 5 → 5×2, 5×4, …, 5×10).
"""

# user_input = int(input("Enter a number: "))
# counter = 1
# product =0
# while counter<=10:
#     if counter %2 ==0:
#         product = user_input*counter
#         print(f"{user_input} * {counter} = {product}")
#     counter +=1


"""
4️⃣ Print the multiplication table of a number up to n
Take:
a number x
a limit n
Print the table of x up to n.

Input: x = 4, n = 6
Output:
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
"""

# user_input = int(input("Enter a number : "))
# limit_num = int(input("Enter a limit number:  "))
# counter = 1
# product = 0
# while limit_num>=counter:
#     product = user_input * counter
#     print(f"{user_input} * {counter} = {product}")
#     counter +=1


"""
7️⃣ Count digits
Take a number from the user and count how many digits it has.
Example:
Input: 34567
Output: 5
"""

# user_input = int(input("Enter a number "))
# digit_count = 0
#
# while user_input > 0:
#     user_input = user_input //10
#     digit_count +=1
# print(digit_count)

"""
🔢 Sum of digits
Take a number and print the sum of its digits.
Example:
Input: 1234
Output: 10

"""

# user_input = int(input("Enter a number "))
# total = 0
# while user_input > 0:
#     last_digit = user_input % 10
#     total = total + last_digit
#     user_input = user_input //10
# print(total)

"""
9️⃣ Reverse a number
Take a number from the user and print its reverse.
Example:
Input: 508
Output: 805
"""
# user_input = int(input("Enter a number "))
# last_digit = 0
# reverse_num =0
# while user_input > 0:
#     last_digit = user_input %10
#
#     user_input = user_input // 10
#     reverse_num = reverse_num*10 + last_digit
#
# print(reverse_num)


"""
🧠 Interview Question
Problem:
Take a positive integer from the user.
Print how many EVEN digits it contains.
🧪 Example
Input: 48291
Output: 3
Explanation:
Digits: 4, 8, 2, 9, 1
Even digits: 4, 8, 2 → count = 3
"""

# user_input = int(input("Enter a number "))
# count_even= 0
# while user_input > 0:
#     last_digit = user_input %10
#     user_input= user_input // 10
#     if last_digit %2 ==0:
#         count_even = count_even +1
# print(count_even)


"""
🧠 Interview Problem: Palindrome Number
Question:
Take a positive integer and check whether it is a palindrome.
A palindrome number:
reads the same forward and backward
🧪 Examples
121  → Palindrome
123  → Not Palindrome
505  → Palindrome
10   → Not Palindrome
"""

# user_input = int(input("Enter a number "))
# reverse_num = 0
# original_num = user_input
# while user_input> 0:
#     last_digit = user_input %10
#     user_input = user_input //10
#     reverse_num = reverse_num *10 + last_digit
#
# if original_num == reverse_num:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

"""

🧠 Interview Problem: Palindrome Number
Question:
Take a positive integer and check whether it is a palindrome.
A palindrome number:
reads the same forward and backward
🧪 Examples
121  → Palindrome
123  → Not Palindrome
505  → Palindrome
10   → Not Palindrome
"""

# user_input = int(input("Enter a number: "))
# reverse_num = 0
# original_num =user_input
# while user_input > 0:
#     last_digit = user_input %10
#     user_input = user_input //10
#     reverse_num = reverse_num *10 +last_digit
#
# if original_num == reverse_num:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

"""
🟠 Level 3: Real Logic Thinking
🔟 Factorial
Take a number n and print its factorial.
Example:
Input: 5
Output: 120
"""

# user_input = int(input("Enter a number to find its factorial"))
# #factorial n! = n *(n-1) *(n-2) * ... * 1
# counter =1
# total = 1
# while user_input >= counter:
#     total = total * counter
#     print(f" {user_input} * {counter} = {total}")
#     counter+=1
#
# print(total)








"""
🟠 Level 3: Real Logic Thinking
🔟 Factorial
Take a number n and print its factorial.
Example:
Input: 5
Output: 120
"""

# user_input = int(input("Enter a number to check its factorial"))
# counter = 1
# total = 1
#
# while user_input >= counter:
#     total = total * counter
#     print(f"{user_input} * {counter} = { total}")
#     counter+= 1
# print(total)
#



"""

🧠 Interview Problem: Palindrome Number
Question:
Take a positive integer and check whether it is a palindrome.
A palindrome number:
reads the same forward and backward
🧪 Examples
121  → Palindrome
123  → Not Palindrome
505  → Palindrome
10   → Not Palindrome
"""

user_input = int(input("Enter a number to check if it is palindrome"))
reverse_num = 0
original_num = user_input

while user_input > 0:
    last_digit = user_input %10
    user_input = user_input // 10
    reverse_num = reverse_num * 10 + last_digit

if original_num == reverse_num:
    print("It is a palindrome")
else:
    print("This number is not palindrome")



# user_input = int(input("Enter a number: "))
# reverse_num = 0
# original_num =user_input
# while user_input > 0:
#     last_digit = user_input %10
#     user_input = user_input //10
#     reverse_num = reverse_num *10 +last_digit
#
# if original_num == reverse_num:
#     print("Palindrome")
# else:
#     print("Not a palindrome")











