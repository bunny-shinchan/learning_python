"""
1️⃣ Count Vowels in a File

Count total vowels (a, e, i, o, u) in the file.

👉 Think:

Loop character by character?

Case sensitivity?

"""
with open("practice4.txt", "w") as f:
    f.write("Hello Sudhanshu!, This is python learning!")
vowels = "aeiouAEIOU"
count =0
with open("practice4.txt", "r") as s:
    data = s.read() #reads the entire file content at once and returns it as one single string.
    for char in data:
        if char in vowels:
          count +=1
print(count)

"""
🧠 Important Distinction

There are three different reading behaviors:

🔹 1️⃣ read()

Reads everything → returns one string.

🔹 2️⃣ readline()

Reads one line at a time.

🔹 3️⃣ for line in file

Automatically reads one line per iteration.
"""