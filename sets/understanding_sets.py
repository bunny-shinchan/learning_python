collection = {1,2,3,4,5,"Hello ", "World"}
print(collection)
print(type(collection))

# Sets cannot duplicate the values.
# For example : if you store int = 2 in collection, it will ignore the duplicate values
#sets are mutable but the elements inside sets are immutable

#Also it will print in unordered manner
# for example: {1, 2, 3, 4, 5, 'World', 'Hello '}

print(len(collection)) #total number of items, it will ignore duplicate values


"""
NOTE: duplicate values are not allowed in a sets
It always have unique values
"""

collection = {}#empty dictionary
print(type(collection))

"""
To create an empty set, you would have to define it
"""
collection = set()
print(type(collection))