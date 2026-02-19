"""
1) WA recurdive function to calculate the sum of first n natural numbers.

2) Write a recursive function to print all elements in a list.
Hint: use list and index as parameters

"""
#1)
# def natural_sum(n):
#     if (n == 0):
#         return 0
#
#     return natural_sum(n - 1) + n
#
# sum = natural_sum(5)
# print(sum)

#2)
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx +1)

fruits = ["mango" , "apple" , "watermelon"]
print_list(fruits)
