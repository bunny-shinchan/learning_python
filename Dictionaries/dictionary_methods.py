student ={

    "name" : "Sudhanshu Verma",
    "subjects": {
        "phy" : 99,
        "chem" : 98,
        "math" : 95
    }
}

print(student.keys())
# dict_keys(['name', 'subjects'])

print(list(student.keys()))# this is typcasting into lists
# we can typecaste list any data types by putting the required data outside the value

print(len(list(student.keys())))
# We can use differnt functions in python like this

print(student.values())
# dict_values(['Sudhanshu Verma', {'phy': 99, 'chem': 98, 'math': 95}])

print(list(student.values()))
#['Sudhanshu Verma', {'phy': 99, 'chem': 98, 'math': 95}]

# print the dict in tuples
print(list(student.items()))
#[('name', 'Sudhanshu Verma'), ('subjects', {'phy': 99, 'chem': 98, 'math': 95})]

pairs = list(student.items())
print(pairs[0])
#('name', 'Sudhanshu Verma')


student.update({"}city" : "Chennai"})
print(student)
# We can use this method in other way too

new_list = {"city" : "Chennai", "age": 19}
student.update(new_list)
print(student)

