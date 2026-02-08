
"""
🟢 Level 1: Very Basic (Warm-up)
1️⃣ Create a tuple

Create a tuple containing numbers from 1 to 5 and print it.

2️⃣ Access elements

Given:

t = ("apple", "banana", "cherry")


Print:

the first element

the last element

3️⃣ Length of tuple

Write a program to find the number of elements in a tuple.

4️⃣ Loop through a tuple

Given:

colors = ("red", "green", "blue")


Print each color on a new line using a loop.

"""

"""
🟡 Level 2: Basic Logic
5️⃣ Check membership

Given:

nums = (10, 20, 30, 40)


Check if 20 exists in the tuple and print "Found" or "Not Found".

6️⃣ Count elements

Given:

t = (1, 2, 2, 3, 4, 2)


Print how many times 2 appears.

7️⃣ Index of an element

Find the index of "python" in:

langs = ("java", "python", "c", "javascript")

8️⃣ Tuple slicing

Given:

numbers = (5, 10, 15, 20, 25, 30)


Print:

first 3 elements

last 2 elements

"""


"""
2️⃣ Access elements

Given:

t = ("apple", "banana", "cherry")


Print:

the first element

the last element
"""

# t = ("apple", "banana", "cherry")
#
# print(t[0])
# print(t[2])

"""Write a program to print the number of elements in this tuple:"""

# nums = (10, 20, 30, 40, 50)
# print(len(nums))

"""
🟢 Question 4: Loop through a tuple

Given:

colors = ("red", "green", "blue")

👉 Task:

Print each color on a new line using a for loop.

💡 Hint:
for item in tuple_name:
"""
# colors = ("red", "green", "blue")
# for color in colors:
#     print(color)

"""
🟡 Question 5: Check membership in a tuple

Given:

nums = (10, 20, 30, 40)

👉 Task:

Check whether 20 exists in the tuple.

If yes → print "Found"

Else → print "Not Found"

💡 Hint: Use the in keyword.
"""
# nums = (10,20, 30, 40)
# found = False
# for num in nums:
#     if num == 20:
#         found = True
#         break
# if found:
#     print("Found")
# else:
#     print("Not found")

"""
🟡 Question 6: Count elements in a tuple

Given:

t = (1, 2, 2, 3, 4, 2)

👉 Task:

Print how many times 2 appears in the tuple.

💡 Hint:
Tuples have a built-in method just for this.

Write the code and send it here 👇

"""
# t = (1, 2, 2, 3, 4, 2)
# print(t.count(2))


"""
langs = ("java", "python", "c", "javascript")
👉 Task:
Print the index of "python".

💡 Hint:
Tuples have a method for this too 😉


"""
# langs = ("java", "python", "c", "javascript")
#
# print(langs.index("python"))

# langs = ("java", "python", "c", "javascript")
# index =0
# for lang in langs:
#     if lang == "python":
#         print(index)
#         break
#     index +=1

"""
🟡 Question 8: Tuple slicing

Given:

numbers = (5, 10, 15, 20, 25, 30)

👉 Tasks:

Print the first 3 elements

Print the last 2 elements
"""

# numbers = (5, 10, 15, 20, 25, 30)
# print(numbers[:3])
# print(numbers[-2:])

"""
🟢 Question 11: Convert a list into a tuple

Given:

lst = [1, 2, 3, 4]

👉 Task:

Convert this list into a tuple and print the result.
"""

# lst = [1, 2, 3, 4]
# print(tuple(lst)) Built in function

# lst = [1,2,3,4,5]
#
# t = ()
# for item in lst:
#     t +=(item,)
# print(t)

"""
🟢 Back to Question 12 (let’s continue)

Given:

t = ((1, 2), (3, 4), (5, 6))

👉 Tasks:

Print (3, 4)

Print 6

"""

# t = ((1, 2), (3, 4), (5, 6))
# print(t[1])
# print(t[2][1])


"""🟢 Question 13: Find maximum and minimum in a tuple

Given:

nums = (45, 12, 89, 33, 5)

👉 Tasks:

Print the maximum number

Print the minimum number

"""

# nums = (45, 12, 89, 33, 5)
#
# max_num = nums[0]
# min_num = nums[0]
#
# for num in nums:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num
# print(max_num)
# print(min_num)