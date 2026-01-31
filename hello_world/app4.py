from pyexpat.errors import messages

first = 'John'
last = 'Smith'
message = first + '[ ' + last + ' ]' + 'is a coder '
print (message)
msg = f'{first} [{last}] is a coder ' # formatted string
print(msg)

#-----

#Python Strings
course = 'Python for Beginners'
print(len(course))

print(course.upper())
print(course.lower())
print(course)

print(course.find('P'))

print(course.find('o')) # This returns the index of the characters

print(course.replace('Beginner', 'absolute Beginner'))

print('python' in course) # it produces a boolean value

len() # To count the length of the string
