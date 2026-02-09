#set.add()


collections =set()
collections.add(1)
collections.add(2)
collections.add(2)
print(collections)

#set.remove(el)
collections.remove(2)
print(collections)

#if we try to remove any element that does not exist, it will throw an error
#collections.remove(7)
"""
  File "/Users/sudhanshu/Desktop/Study Courses/Python with Mosh/learning_python/sets/set_methods.py", line 15, in <module>
    collections.remove(7)
KeyError: 7

"""
collections.add((1,2,3))
print(collections)

# trying to add a list
# collections.add([1,2,3,4])
# print(collections) #TypeError: unhashable type: 'list'

"""
Traceback (most recent call last):
  File "/Users/sudhanshu/Desktop/Study Courses/Python with Mosh/learning_python/sets/set_methods.py", line 26, in <module>
    collections.add([1,2,3,4])
TypeError: unhashable type: 'list'

"""
"""
unhashable type: 'list'
In sets, we have hashable values which is immutable.
The value of the variable cannot be changed.

And when we used list, since the values can be changed and the hash values can be changed


"""

print(len(collections))


#set.clear() # emties the v
collections.clear()
print(collections)

# set.pop
# This will remove a random value

collections={"hello", "world", "Sudhanshu", "python"}

print(collections.pop())
# set()

print(collections.pop())
# hello
print(collections)
#{'hello', 'Sudhanshu'}

#--------------------------

#Sets important methods

# set.union(set2) Combines both set values and return new

set1 = {1,2,3,4,8}
set2 = {5,6,7,8}

print(set1.union(set2))
#{1, 2, 3, 4, 5, 6, 7, 8}
print(set1)
# {1,2,3,4}
print(set2)
# {5,6,7,8}


#set.intersection() This wil combine values and returns new

print(set1.intersection(set2))
#{8}


