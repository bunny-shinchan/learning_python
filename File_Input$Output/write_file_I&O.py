# TO overwrite any data, we would be using the w mode

"""f = open("demo.txt", "w")


f.write("I would like to replace the data of this file")


f.close()"""
# To add anything at the end of the data.  we will use a which means append

f = open("demo.txt", "a")


f.write("This is a new data.")
#Output :
"""
I ran this twice thats why we have I would like to replace line twice

I would like to replace the data of this fileI would like to replace the data of this fileThis is a new data.

"""

f.close()


