"""
Print the total number of lines in a file.

👉 Think:

.read() vs .readlines()

Or loop line by line?

----


3️⃣ Count Total Words

Count how many words are in the file.

👉 Think:

What separates words?

Which string method helps?
---

4️⃣ Print Only Even Numbers (One Per Line)

If file contains numbers separated by commas,
print only even numbers (each on new line).
"""


"""

Print the total number of lines in a file.

👉 Think:

.read() vs .readlines()

Or loop line by line?
"""
# count =0
# with open("practice.txt" ,"r") as f:
#     for line in f:
#         count +=1
# print(count)


# Now solving using readline()

# count = 0
# with open("practice.txt", "r") as s:
#     line = s.readline()
#     while line != "":
#         count +=1
#         line = s.readline()
# print(count)

"""
✅ Why This Works

First line is read before the loop.

while line != "" checks if file still has content.

Inside the loop:

You count the current line.

You update line with the next line.

When file ends, readline() returns "".

Loop stops naturally.
"""



# 🟢 Similar Question (Level Upgrade 1)
# 📌 Question:
#
# Count how many non-empty lines are present in the file.
#
# Example file:
#
# Hello
#
# Python
#
# File I/O
#
# Total lines = 5
# Non-empty lines = 3

with open("practice3.txt", "w") as f:
    f.write("""Hello
    
Python
    
FileI/O
    
""")
count_non_empty =0
count_all_lines =0
with open("practice3.txt", "r") as s:
    line = s.readline()
    while line != "":
        count_all_lines +=1  #count every line

        if line.split():   # Non-empty line(after removing whitespace)
            count_non_empty+=1
        line = s.readline()   # move to next line

print("Total lines = ", count_all_lines)
print("Non-empty lines =", count_non_empty)

