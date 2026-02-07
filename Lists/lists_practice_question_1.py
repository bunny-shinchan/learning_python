# Write a program to find the largest number in a list



# numbers = [1, 2,5, 6,22,40,45,64]
#
# max = numbers [0]
#
# for number in numbers:
#     if number > max:
#         max =number
# print(max)

# Create a list of 5 integers and print each element using a for loop.

# numbers = [3,4,5,6,7,]
#
# for num in numbers:
#     print(num)

"""
🟢 Beginner Level (Lists Basics)
Create a list of integers and print all elements using a loop.

Find the sum of all elements in a list.

Find the largest element in a list.

Count how many even numbers are present in a list.

Reverse a list without using built-in reverse methods.

🟡 Intermediate Level (Logic Building)

Remove duplicate elements from a list.

Find the second largest number in a list.

Split a list into even and odd number lists.

Check whether a list is a palindrome.

Rotate a list to the right by K positions.

🟠 Upper-Intermediate Level (Interview-Style)
Find the first non-repeating element in a list.

Move all zeros to the end while maintaining order.

Find the intersection of two lists.

Find all pairs whose sum equals a given number.

Flatten a nested list into a single list.

🔴 Advanced Level (Think Like a Developer)
Remove duplicates in-place without using extra space.

Find the maximum subarray sum.

Implement merge sort using lists.

Find the majority element (appears more than n/2 times).

Rotate a matrix (list of lists) by 90 degrees.

"""

# Find the sum of all elements in a list.

"""numbers = [2,5,6,7,8,8,44,55]
total = 0
for num in numbers:
    total = total + num
print(total)"""

# Find the largest element in a list.

"""numbers = [1,3,45,64,34,67,87,65]
max_num =1
for num in numbers:
    if num > max_num:
        max_num = num
print(max_num)"""

#Count how many even numbers are present in a list.

"""numbers = [2,5,6,4,7,8,9,10,3,4,5,6,7,6,5,4]
counter = 0

for num in numbers:
    if num %2 ==0:
        counter+= 1
print(counter)"""

#5 – Reverse a list without using reverse() or slicing
"""
numbers = [4,5,6,7,8,9,1]

for i in range(len(numbers) -1, -1 , -1):
    print(numbers[i])
    """
"""numbers = [4,5,6,7,8,9,1]

for i in range(len(numbers) -1 , -1 , -1):
    print(numbers[i])
"""
"""numbers = [4, 5, 6, 7, 8]
start = 0
end = len(numbers) -1

while start < end:
    temp = numbers[start]
    numbers[start] = numbers[end]
    numbers[end] = temp
    start += 1
    end -=1
print(numbers)
"""

# numbers = [4, 5, 6, 7, 8, 9, 1]
#
# start = 0
# end = len(numbers) - 1
#
# print("Initial list:", numbers)
# print("-" * 40)
#
# while start < end:
#     print(f"Before swap → start={start}, end={end}")
#     print("List:", numbers)
#
#     print(f"Swapping {numbers[start]} and {numbers[end]}")
#
#     temp = numbers[start]
#     numbers[start] = numbers[end]
#     numbers[end] = temp
#
#     print("After swap :", numbers)
#     print("-" * 40)
#
#     start += 1
#     end -= 1
#
# print("Final reversed list:", numbers)


"""numbers = [4, 5, 6, 7, 8, 9, 1]
start = 0
end = len(numbers) -1

while start  < end:
    temp = numbers[start]
    numbers[start] = numbers[end]
    numbers[end] = temp

    start+=1
    end -=1
print(numbers)
"""

"""Count how many even numbers are present in a list."""

# numbers = [4, 5, 6, 7, 8, 9, 1]
# count = 0
#
# for num in numbers:
#     if num%2 == 0:
#         count+=1
# print(count)

"""numbers = [2,3,5,6,5,6,7,8]
count = 0

for num in numbers:
    if num %2 ==0:
        count +=1
print(count)"""


"""
🟡 Intermediate Question #1
Remove duplicate elements from a list
📌 Problem statement

Given a list, remove duplicate elements and keep only unique values.
"""

# numbers = [1,4,5,6,5,4,3]
#
# newlist1 =[]
#
# for num in numbers:
#     if num not in newlist1:
#         newlist1.append(num)
# print(newlist1)

"""
Find the second largest element in a list
📌 Problem statement

Given a list of integers, find the second largest number.

Example:

Input:  [10, 5, 20, 8, 15]
Output: 15
"""
#
# numbers = [10, 5, 20, 8, 15]
#
# if len(numbers) < 2: # A second largest element exists when length ≥ 2
#     print("Second largest element does not exist ")
# else:
#     if numbers[0] > numbers[1]:
#         largest_num= numbers[0]
#         sec_largest_num = numbers[1]
#     else:
#         largest_num = numbers[1]
#         sec_largest_num = numbers[0]
#     """
#     You compared the first two elements
#
#     You initialized correctly
#
#     This handles:
#
#     unordered input
#
#     negative numbers
#
#     interview edge cases
#     """
#     for num in numbers[2:]:
#         if num > largest_num:
#             sec_largest_num = largest_num
#             largest_num = num
#         elif num < largest_num and num > sec_largest_num:
#             sec_largest_num = num
#
#     print("Second largest number is:", sec_largest_num)


"""numbers = [10, 5, 20, 8, 15]
if len(numbers) < 2:
    print("Second largest number does not exist")
else:
     if numbers[0] > numbers[1]:
         largest_num = numbers[0]
         second_largest_num = numbers[1]
     else:
         largest_num = numbers[1]
         sec_largest_num = numbers[0]

     for num in numbers[2:]:
         if num > largest_num:
             sec_largest_num = largest_num
             largest_num = num
         elif num <largest_num and num >second_largest_num:
             sec_largest_num = num

     print("Second largest number is:", sec_largest_num)
"""

"""numbers = [10, 5, 20, 8, 15]
if len(numbers) < 2:
    print("Second largest number does not exist")
else:
    if numbers[0] > numbers[1]:
        largest_num = numbers[0]
        second_largest_num = numbers[1]
    else:
        largest_num = numbers[1]
        second_largest_num = numbers[0]
    for num in numbers[2:]:
        if num > largest_num:
            second_largest_num = largest_num
            largest_number = num
        elif num < largest_num and num > second_largest_num:
            sec_largest_num = num
    print("Second Largest number is ", second_largest_num)"""


"""
🟡 Intermediate Question #3
Move all zeros to the end of the list (while maintaining order)
📌 Problem statement

Given a list, move all 0s to the end without changing the order of non-zero elements.

Example
Input:  [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]


Another example:

Input:  [1, 0, 2, 0, 0, 3]
Output: [1, 2, 3, 0, 0, 0]
"""

# numbers = [0, 1, 0, 3, 12]
#
# placement_index = 0
#
# # Step 1: Move all non-zero elements to the front
# for num in numbers:
#     if num != 0:
#         numbers[placement_index] = num
#         placement_index += 1
#
# # Step 2: Fill the remaining positions with zeros
# for i in range(placement_index, len(numbers)):
#     numbers[i] = 0
#
# print(numbers)

numbers = [2,3,4,5,5,6,7,8,7,8,5]
new_list =[]

for nummber in numbers:
    if nummber not in new_list:
        new_list.append(nummber)
print(new_list)

























