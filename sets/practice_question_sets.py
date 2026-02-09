# You are given a list of subjects for students. Assume
# one classroom is required for 1 subject.
#How many classrooms are needed by all students?


"""
"python, "java" ,"c++", "Python", "Javascript",
"java", "python", "java", "C++" , "C"

"""


# Python - We need one classroom
#C++ - We need one classroom
#java - We need one classroom

# subjects = {"python", "java" ,"C++", "Python", "Javascript",
# "java", "python", "java", "C++" , "C"}
#
# print(subjects)
# print(len(subjects))


#Figure out a way to store 9 and 9.0 as separate values
#in the set.

"""values = {9, 9.0}
print(values) # as the python library will treat 9 and 9.0 same
#{9}

values= {8 , "8.0"}
print(values)

values = {
    ("float" , 9.0),
    ("int", 9)
}
print(values)"""

"""
🟢 Level 1: Understanding Basics

Create a set containing the numbers 1, 2, 3, 4, 5.

What happens if you create a set like {1, 2, 2, 3, 3}?

Can a set contain mixed data types? Try creating one.

Create an empty set. (Don’t use {}.)
"""

# set1 = {1,2,3,4,5}
# print(set1)
# set2 = {2,3,3,4,5,4,5,4}
# print(set2)
#
# set = {}
# print(type(set))
# set = {()}
# print(type(set))
#

"""
🟢 Level 2: Adding and Removing Elements

Create a set {10, 20, 30} and add 40 to it.

Remove 20 from the set {10, 20, 30, 40}.

What is the difference between remove() and discard()? Try both on a value that doesn’t exist.

Clear all elements from a set.
"""
# set =  {10, 20, 30}
# set.add(40)
# print(set)
#
# set.remove(30)
# print(set)
#
# set.discard(30)
# print(set)

# set.remove(30)
# print(set)
#Traceback (most recent call last):
"""  File "/Users/sudhanshu/Desktop/Study Courses/Python with Mosh/learning_python/sets/practice_question_sets.py", line 83, in <module>
    set.remove(30)
KeyError: 30"""

# set.clear()
# print(set)


"""
🟢 Level 3: Membership & Length

Check whether 5 exists in the set {1, 3, 5, 7}.

Find the number of elements in the set {2, 4, 6, 8, 8, 8}.
"""

# set = {1, 3, 5, 7}
# print(5 in set)

"""
🟢 EASY (Core Set Understanding)
1️⃣ Check for Duplicates

Given a list of integers, determine whether it contains any duplicate values.

Example:
Input: [1, 2, 3, 4, 1]
Output: True

2️⃣ Remove Duplicates

Given a list of integers, return a new list with all duplicate values removed.

Constraint:

Order does not matter.

3️⃣ Unique Characters in a String

Given a string, check if all characters in the string are unique.

Example:
Input: "abcde" → True
Input: "hello" → False

🟡 MEDIUM (Logical + Set Operations)
4️⃣ Common Elements Between Two Lists

Given two lists of integers, return all elements that appear in both lists.

Example:
Input: [1, 2, 3, 4], [3, 4, 5, 6]
Output: {3, 4}

5️⃣ Find Missing Numbers

Given a list of integers from 1 to n with some numbers missing, find all the missing numbers.

Example:
Input: [1, 2, 4, 6], n = 6
Output: {3, 5}

6️⃣ Intersection of Multiple Sets

Given a list of sets, find elements common to all sets.

Example:
Input: [{1,2,3}, {2,3,4}, {2,3,5}]
Output: {2, 3}

🔴 HARD (Interview Favorite Thinking Problems)
7️⃣ Longest Consecutive Sequence

Given an unsorted list of integers, find the length of the longest consecutive sequence.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
(Sequence: 1, 2, 3, 4)

8️⃣ Find the First Repeating Element

Given a list of integers, find the first element that repeats.

Example:
Input: [10, 5, 3, 4, 3, 5, 6]
Output: 3

9️⃣ Is Subset Problem

Given two lists, determine whether the second list is a subset of the first.

Example:
Input:
List A = [1, 2, 3, 4, 5]
List B = [2, 3, 4]
Output: True

"""

"""
1️⃣ Check for Duplicates

Given a list of integers, determine whether it 
contains any duplicate values.

Example:
Input: [1, 2, 3, 4, 1]
Output: True

"""
# my_list = list(map(int, input("Enter the values").split()))
# my_set = set(my_list)
# if len(my_list) != len(my_set):
#     print("True")


"""
🟢 EASY – Question 2: Remove Duplicates
🧩 Problem Statement

Given a list of integers, remove all duplicate values and return a collection that contains only unique elements.

📌 Notes (read carefully)

Order does not matter

Use sets as your main tool

Input will be taken from the user (similar to the previous question)

"""

# user_input = list(map(int, input("Enter the values").split()))
#
# my_set = set(user_input)
# updated_list = list(my_set)
# print(updated_list)


"""
🟢 EASY – Question 3: Unique Characters in a String
🧩 Problem Statement

Given a string, determine whether all characters in the string are unique.

📌 Conditions

Use sets to solve the problem

The function / program should return:

True → if all characters are unique

False → if any character repeats

"""

# user_input = list(map(str, input("Enter a word to check if there is duplicate letter")))
# my_set = set(user_input)
#
# if len(user_input) == len(my_set):
#     print("True")
# else:
#     print("False")

"""
🟡 MEDIUM – Question 4: Common Elements Between Two Lists
🧩 Problem Statement

Given two lists of integers, find and return the elements that appear in both lists.

📌 Conditions

Use sets

Order does not matter

Output should contain unique common elements

"""

# list1 = list(map(int, input("Enter the first list").split()))
# list2 = list(map(int, input("Enter the second list").split()))
#
# set1 = set(list1)
# set2 = set(list2)
#
#
# print(set1.intersection(set2))


"""
🟡 MEDIUM – Question 5: Find Missing Numbers
🧩 Problem Statement

You are given:

A list of integers containing numbers from 1 to n

Some numbers are missing

Your task is to find all the missing numbers.

📌 Conditions

Use sets

Order does not matter

Output should contain unique missing values
"""

nums = list(map(int, input("Enter the list values ").split()))
n = int(input("Enter the value of n: "))

full_set = set(range(1, n +1))
nums_set = set(nums)

missingNumbers = full_set -nums_set
print(missingNumbers)