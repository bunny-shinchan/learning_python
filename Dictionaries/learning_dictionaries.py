"""
dict =
{
    "key" : "value",
}
"""
"""info ={

    "name" : "Sudhanshu",
    "age" : 20,
    "city" : "delhi"
}
print(info)"""

# We can also add lists and tuples in dictionary

"""info ={

    "name" : "Sudhanshu",
    "age" : 20,
    "city" : "delhi",
    "subjects": ["Python", "C", "Java"],
    "topics": ("dict", "set")
}
print(info)"""

# NOTE
# We can take key as any datatype like string, int, float. But we cant take key as list as it can change
# Since the dictionary is mutable, you can change it like lists.
# Dictionaries are un ordered, mutable and don't allow to duplicate keys

#to print specific value via keys
"""print(info["name"])
print(info["subjects"])
print(info["topics"])"""

# to change the values

info ={
    "name" : "Sudhanshu",
    "age" : 20,
    "city" : "delhi",
    "subjects": ["Python", "C", "Java"],
    "topics": ("dict", "set"),
}
info["name"] = "sid"
info["surname"] = "Verma"
print(info)



# How to create a null dictionary
null_dict = {}
print(null_dict)
null_dict["name"] = "Sudhanshu"
print(null_dict)

