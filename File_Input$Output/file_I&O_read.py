# Understanding on how to open and close a file
# f = open("demo.txt", "r")
#
# data = f.read()
# print(data)
# print(type(data))
#
# f.close()# it is quite important to close the file as anybody can change/modify the data in the file.


# If I would want to read a specific data in the file

# f = open("demo.txt", "r")
#
# data = f.read(5)
# print(data)
# print(type(data))
#
# f.close()# it is quite important to close the file as anybody can change/modify the data in the file.


# Inorder to read any line, we write readline()

f = open("demo.txt", "r")
data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()# it is quite important to close the file as anybody can change/modify the data in the file.