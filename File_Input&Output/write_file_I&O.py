# TO overwrite any data, we would be using the w mode

"""f = open("demo.txt", "w")


f.write("I would like to replace the data of this file")


f.close()"""
# To add anything at the end of the data.  we will use a which means append
#
# f = open("demo.txt", "a")
#
#
# f.write("This is a new data.")
# #Output :
#
# f.close()
"""
I ran this twice thats why we have I would like to replace line twice

I would like to replace the data of this fileI would like to replace the data of this fileThis is a new data.

"""

# In order to write in the next line, we can use

f = open("demo.txt", "a")

f.write("\n After that node.js")

f.close()

"""Output: I would like to replace the data of this file. I would like to replace the data of this fileThis is a new data.
 After that node.js"""

# f = open("sample.txt", "w")
#
# f.close()
#
# #-----------
#
# f = open("sample_data", "w+")
#
# f.write("Sudhanshu Verma is learning python")



"""
With Syntax

"""

# With syntax
with open("sample_data.txt", "r") as f:
    data = f.read()
    print(data)

# with helps us to open and close the file automatically, therefore we dont have to close the file while using with syntax.
with open("sample_data.txt", "w") as f:
    f.write("Hello World! This is Sudhanshu Verma ")


# Deleting a file
# using the os module
#
# Module : like a code library is a file written by another programmer that generally has a function we can use

#import os
#os.remove(filename)


# There are many modules that are pre-installed in python which is os.

# If we do not have any pre- installed module and we are trying to import it. Then we would have to install it
# using pip install "modeule_name"

# import tenserflow

"""
Since we do not have any module installed with the name tenser flow, we will get this error.

Traceback (most recent call last):
  File "/Users/sudhanshu/Desktop/Study Courses/Python with Mosh/learning_python/File_Input&Output/write_file_I&O.py", line 78, in <module>
    import tenserflow
ModuleNotFoundError: No module named 'tenserflow'

We would have to install this manuall from the internet in order to use.
"""

import os

os.remove("sample_data.txt") # This will delete the file.
