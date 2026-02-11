
"""
🟢 EASY (Foundations)
E1

Create a dictionary from the following two lists:

keys = ["name", "age", "city"]
values = ["Amit", 23, "Delhi"]


📌 Hint when stuck: Think about pairing items at the same index.

E2

Given a dictionary:

student = {"name": "Riya", "age": 21, "course": "Python"}


Check if the key "salary" exists.
If it doesn’t, add "salary" with value 0.

📌 Hint when stuck: One dictionary method avoids errors when a key is missing.

E3

Given:

marks = {"Math": 78, "Science": 85, "English": 74}


Print only the subjects where marks are greater than 80.

📌 Hint when stuck: You’ll need to loop over both key and value.

🟡 MEDIUM (Logic Building)
M1

Given a list:

nums = [1, 2, 3, 2, 4, 1, 3, 2]


Create a dictionary that stores the frequency of each number.

📌 Hint when stuck: Start with an empty dictionary and update counts safely.

M2

Given a dictionary:

prices = {"apple": 120, "banana": 40, "orange": 60}


Increase all prices by 10% and store the updated values in the same dictionary.

📌 Hint when stuck: You cannot change keys while looping, but values are fine.

M3

Given:

data = {"a": 10, "b": 5, "c": 20, "d": 15}


Find the key with the maximum value.

📌 Hint when stuck: Track both the current maximum value and its key.

🔴 HARD (Interview / Real-World Thinking)
H1

Given a sentence:

text = "python is easy and python is powerful"


Create a dictionary that stores the count of each word.

📌 Hint when stuck: Split the sentence first.

H2

Given a dictionary:

employees = {
    "emp1": {"name": "Amit", "salary": 50000},
    "emp2": {"name": "Neha", "salary": 65000},
    "emp3": {"name": "Rahul", "salary": 48000}
}


Print the name of the employee with the highest salary.

📌 Hint when stuck: Nested dictionaries → access inner values carefully.

H3

Given:

data = {"a": 1, "b": 2, "c": 3}


Reverse the dictionary so that values become keys and keys become values.

📌 Hint when stuck: Make sure the new keys are unique.

✅ How to Practice (Important)

Try E → M → H in order

Don’t rush to hints

If stuck for more than 5–7 minutes, ask for only the hint

After solving, we can review your logic line by line

When you’re ready, start with E1 and ping me with your code 👀
"""




# student_info = {
#     "name": "Amit",
#     "age" : 23,
#     "city" : "Delhi"
# }
# print(student_info)

"""
🟢 E2 (Easy)

Given a dictionary:

student = {
    "name": "Riya",
    "age": 21,
    "course": "Python"
}


Task:

Check if the key "salary" exists in the dictionary.

If it does not exist, add "salary" with value 0.
"""

# student = {
#     "name": "Riya",
#     "age": 21,
#     "course": "Python"
# }
#
# print(student.get("salary"))
# print(student.update({"salary": 0}))
# print(student)

"""
🟢 E3 (Easy)

Given a dictionary:

marks = {
    "Math": 78,
    "Science": 85,
    "English": 74
}


Task:

Print only the subject names whose marks are greater than 80.


"""

# marks = {
#     "Math": 78,
#     "Science": 85,
#     "English": 74
# }
#
# for item in marks.items():
#     sub, mark = item
#     if mark > 80:
#         print(sub)

"""
🟡 M1 (Medium)

Given a list:

nums = [1, 2, 3, 2, 4, 1, 3, 2]

Task:

Create a dictionary that stores the frequency of each number.

Example meaning (⚠️ not the answer):

If a number appears 3 times, its value should be 3.
"""
# nums = [1, 2, 3, 2, 4, 1, 3, 2]
#
# my_dic={}
# for num in nums:
#     if num in my_dic:
#         my_dic[num] +=1
#     else:
#         my_dic[num] = 1
# print(my_dic)


"""
🟡 M2 (Medium)

Given a dictionary:

prices = {
    "apple": 120,
    "banana": 40,
    "orange": 60
}

Task:

Increase all prices by 10%

Store the updated prices in the same dictionary

"""

# prices = {
#     "apple": 120,
#     "banana": 40,
#     "orange": 60
# }
#
# for item, price in prices.items():
#     newprice = price + price *0.10
#     prices[item] = newprice
#     #prices.update({item: newprice}) We can use update method of dictionary to update the values of any key
# print(prices)


"""
🟡 M3 (Medium)

Given a dictionary:

data = {
    "a": 10,
    "b": 5,
    "c": 20,
    "d": 15
}

Task

Find the key that has the maximum value.

Expected meaning (not the answer):

If 20 is the highest value,

You should return/print the key associated with it, not the number itself.
"""

data = {
    "a": 10,
    "b": 5,
    "c": 20,
    "d": 15
}
max_value = 0
max_key = ""
for key, value in data.items():
    if value > max_value:
        max_value = value
        max_key = key
print(max_key)