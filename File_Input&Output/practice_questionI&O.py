"""
Create a new file "practice.txt" using python. Add the following data in it

Hi everyone
We are learning File I/O
using java
I like programming in Java.

"""
import re

# with open("practice.txt", "w") as f:
#     f.write("""Hi everyone
# We are learning File I/O
# using java
# I like programming in Java.""")

"""
WAF that replace all occurences of "Java" with "python" in above file.
"""

# with open("practice.txt", "r") as s:
#     data = s.read()
#
# new_data = data.replace("Java", "Python")
# print(new_data)
# with open("practice.txt", "w") as s:
#     s.write(new_data)


""""
Search if the word "learning" exists in the file or not.
"""

def findword():
    word ="learning"
    with open("practice.txt", "r") as s:
        data = s.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not found")
# In order to convert this into a function we can define a function.


"""
WAF to find in which line of the file does the word "learning" occur first.
Print -1 if word not found.
"""

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no=1
#     with open("practice.txt", "r") as s:
#         while data:
#             data = s.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# check_for_line()

"""
From a file containing numbers separated by comma, print the count of even numbers.

"""

# with open("practice2.txt", "w") as d:
#     d.write("1,2,76,84,98,99,43,24")
count =0
with open("practice2.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if(int(val)%2 ==0):
            count+=1
print(count)
# Since the data in a string format, we would have to convert each number into int first

"""
    1) individual number
    2) parse the values into int 
    If we want to convert, we can use the split method.
"""

"""    num = ""
    for i in range(len(data)):
        if(data[i] == ","):  (When we reach the comma, we will assume that it is our number)
            print(int(num))  (Typecasting this into int)
            num =""
        else:
            num += data[i] (This will keep adding the number till the time we reach the comma)
            
"""




