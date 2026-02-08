# numbers = [5,2,1,7,4]
# numbers.append(20)
# print(numbers)

"""numbers = [5,2,1,7,4]
numbers.insert(0, 20)
print(numbers)
"""
#insert needs index and the value to insert the value in the list

"""numbers = [5,2,1,7,4]
numbers.remove(5)
print(numbers)"""

#clear will empty the list

# numbers = [5,2,1,7,4]
# numbers.clear()
# print(numbers)

"""
numbers = [5,2,1,7,4]
numbers.pop() # this will remove the last index value from the list.
print(numbers)"""

"""numbers = [5,2,1,7,4]
print(numbers.index(5)) #0
# index tell you the index of the list
"""


"""numbers = [5,2,1,7,4]
print(50 in numbers) #False
numbers = [5,2,1,7,4]
print(5 in numbers) #True
"""

"""numbers = [5,2,1,7,4,5]
print(numbers.count(5)) # returns 2 becasue we have 2 '5'"""

"""numbers = [5,2,1,7,4,5]
numbers.sort()
print(numbers)"""

"""numbers = [5,2,1,7,4,5]
numbers.sort()
numbers.reverse()
print(numbers)"""

"""numbers = [5,2,1,7,4,5]
numbers2 = numbers.copy() 
numbers.append(10)
print(numbers)
print(numbers2)"""

"""
Write a program to remove the duplicates in list

"""
#remove the duplicate from the list
numbers = [2,3,4,4,5,6,7,8]
new_list = []

for num in numbers:
    if num not in new_list:
        new_list.append(num)
print(new_list)


