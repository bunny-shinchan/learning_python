"""
nested for loop
how to print the coordinates
(x, y)
(0,0)
(0,1)
(0,2)
(1,0)
(1,1)
(1,2)

"""

# for x in range (4):# outer loop
#     for y in range(3):# inner loop
#         print(f'{x}, {y}')

"""

challenge
We need to print this F using the 'x'
xxxxx
xx
xxxxx
xx
xx

Hint! = number = [5,2,5,2,2]
using a for loop, you need to iterate over this list


"""

# numbers = [5,2,5,2,2]
#
# for x_counts in numbers:
#     print("x" * x_counts)

# numbers = [5,2,5,2,2]
#
# for x_counts in numbers:
#     output = ''
#     for count in range(x_counts):
#         output += 'x'
#     print(output)


"""
🟢 Level 1: Small variations
3️⃣ Print numbers instead of stars
Print a square where each row has numbers from 1 to N.
Example (N = 4)
1234
1234
1234
1234
"""


# user_input = int(input("Enter a number")) #take a num from the user : n
#
# for x_count in range(1, user_input +1):# outer loop : x_count is the counter running till n
#                                     # This loop is responsible for number of rows
#     for y_count in range(1, user_input + 1):# inner loop : responsible for printing columns / numbers
#
#         print(y_count , end ="") # this statment prints y_count and 'end = ""' ensure that everything gets printing in single line
#     print() # This will break the line once the inner loop is completed and then goes back till the time inner loop is done iterating.
#

"""
🔹 Level 1: Absolute Basics (Nested Loop Warm-up)
1️⃣ Print a solid square
Print a square of size N using *
Example (N = 3)
***
***
***
Rules:
Use nested for loops
No hardcoded strings
2️⃣ Print numbers in rows
Print numbers from 1 to N in each row, repeat for N rows
Example (N = 4)
1234
1234
1234
1234
🔹 Level 2: Row-Dependent Patterns
3️⃣ Right-angled triangle
Print a triangle where row number = number of stars
Example (N = 5)
*
**
***
****
*****
4️⃣ Reverse right-angled triangle
Example (N = 4)
****
***
**
*
🔹 Level 3: Logic + Dependency (Interview Gold)
5️⃣ Number triangle
Example (N = 4)
1
12
123
1234
6️⃣ Same number per row
Example (N = 4)
1
22
333
4444
🔹 Level 4: Slightly Tricky
7️⃣ Row and column product
Print a multiplication grid
Example (N = 3)
1 2 3
2 4 6
3 6 9
8️⃣ Hollow square
Example (N = 5)
*****
*   *
*   *
*   *
*****
"""


"""
🔹 Level 1: Absolute Basics (Nested Loop Warm-up)
1️⃣ Print a solid square
Print a square of size N using *
Example (N = 3)
***
***
***
Rules:
Use nested for loops
No hardcoded strings
"""
#Example:
# for x in range (4):# outer loop
#     for y in range(3):# inner loop
#         print(f'{x}, {y}')

# user_input = int(input("Enter a number: "))
#
# for row in range(1, user_input + 1):          # outer loop → rows
#     for col in range(1, user_input + 1):      # inner loop → stars
#         print("*", end="")             # print star, stay on same line
#     print()                            # move to next line

#-------
# user_input = int(input("Enter a number: "))
#
# for row in range(user_input):
#     for col in range(user_input):
#         print("*", end ='')
#     print()


"""
🟢 Level 0: “Get comfortable” questions
1️⃣ Print a solid square
(You’ve basically done this already — confidence booster)
Example (N = 3)
***
***
***
"""

# user_input = int(input("Enter a number: "))
#
# for x in range(1, user_input +1):
#     for y in range(1, user_input +1):
#         print("*", end="")
#     print()


"""I suggest 4️⃣ Print the row number:
1111
2222
3333
4444

"""

# user_input = int(input("Enter a number: "))
#
# for x_count in range(1, user_input +1):
#     for y_count in range(1, user_input + 1):
#         print(x_count, end = "")
#     print()

"""
5️⃣ Increasing numbers per row
Example (N = 4):
1
12
123
1234
"""
# user_input = int(input("Enter a number: "))
#
# for row in range(1, user_input + 1):
#     for col in range(1, row + 1):
#         print(col, end ="")
#     print()

"""
🧠 Rule #4: Stop memorizing code, start memorizing roles
Instead of remembering syntax, remember roles:
Concept	            Role
row	                which line
col	                position inside the line
inner loop range	how many items
print(end="")	    same line
print()	            next line
These roles don’t change across problems.
"""

"""
🎯 Target Pattern: Reverse Triangle
For N = 4, we want:
1234
123
12
1
"""

# user_input = int(input("Enter a number: "))
#
# for row in range(user_input , 0 , -1):
#     for col in range(1, row +1):
#         print(col, end ="")
#     print()
"""
output
Enter a number: 4
1234
123
12
1

"""

# user_input = int(input("Enter a number: "))
#
# for row in range(user_input , 0 , -1):
#     for col in range(row, 0  ,  -1):
#         print(col, end ="")
#     print()

"""
output
Enter a number: 4
4321
321
21
1

"""


"""
4️⃣ Reverse right-angled triangle
Example (N = 4)
****
***
**
*
"""
# user_input = int(input("Enter a number: "))
#
# for row in range(user_input , 0 , -1):
#     for col in range(row):
#         print("*" , end=" ")
#     print()

# user_input = int(input("Enter a number: "))
#
# for row in range(1, user_input + 1):
#     for col in range(row):
#         print("*", end =" ")
#     print()


"""
9️⃣ Reverse number triangle
Example (N = 4):
1234
123
12
1
"""


# user_input = int(input("Enter a number: "))
#
# for row in range(user_input , 0 , -1):
#     for col in range(1, row +1):
#         print(col, end ="")
#     print()

#----------------------------------------------
"""
🔟 Multiplication grid
Example (N = 3):
1 2 3
2 4 6
3 6 9
"""

# user_input = int(input("Enter a number: "))
#
# for row in range(1, user_input + 1):
#     for col in range(1, user_input+1):
#         print(row *col, end = " ")
#     print()

"""
8️⃣ Hollow square
Example (N = 5)
*****
*   *
*   *
*   *
*****
"""
# user_input = int(input("Enter a number: "))
#
# for row in range(1, user_input +1):
#     for col in range(1, user_input + 1):
#         if (row == 1 or row == user_input) or (col == 1 or col == user_input):
#             print("*", end ="")
#         else:
#             print(" ", end = "")
#     print()

"""
🧠 Why this solution is correct
1️⃣ Loop structure (spot on)

for row in range(1, user_input + 1):
Controls rows
Runs N times

for col in range(1, user_input + 1):

Controls columns
Runs N times for each row

This creates an N × N grid.

2️⃣ Border logic (this is the key)
if (row == 1 or row == user_input) or (col == 1 or col == user_input):

This means:
Top border (row == 1)
Bottom border (row == user_input)
Left border (col == 1)
Right border (col == user_input)

If any of these is true → print *.

That’s exactly what “hollow” means.
"""


#--------------
"""
🟢 Quick Warm-ups (very short)
1️⃣ Print a diagonal
Example (N = 5)
*
 *
  *
   *
    *
👉 Hint: row == col
2️⃣ Print the other diagonal
Example (N = 5)
    *
   *
  *
 *
*
👉 Hint: row + col == N + 1
🟡 Slightly Logical (still easy)
3️⃣ X pattern
Example (N = 5)
*   *
 * *
  *
 * *
*   *
👉 Hint: two diagonals together
4️⃣ Hollow rectangle
Example (rows = 3, cols = 6)
******
*    *
******
👉 Hint: hollow square logic + different row/col limits
🟠 Thinking Pattern (last one before switching topic)
5️⃣ Number pyramid (left-aligned)
Example (N = 4)
1
12
123
1234
(You’ve basically done this — confidence booster.)
"""
#-------------
"""
4️⃣ Hollow rectangle
Example (rows = 3, cols = 6)
******
*    *
******
👉 Hint: hollow square logic + different row/col limits
"""

# row = int(input("Enter a row: "))
# col = int(input("Enter a col: "))
# for r in range(1, row +1):
#     for c in range(1, col + 1):
#         if (r == 1 or r == row) or (c == 1 or c == col):
#             print("*", end ="")
#         else:
#             print(" " , end ="")
#     print()

"""
🟠 Thinking Pattern (last one before switching topic)
5️⃣ Number pyramid (left-aligned)
Example (N = 4)
1
12
123
1234
"""

user_input = int(input("Enter a number "))

for row in range(1, user_input + 1):
    for col in range(1, row+ 1):
        print(col , end ="")
    print()
