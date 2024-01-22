"""
Q. Why Do You Use the Zip () Method in Python?
Ans.
    It is used when we have two different lists in which one list contains keys and other list contains values.By using
    'zip()' function we can create a dictionary from 2 lists in python.
"""
# Example of Zip

l1 = ['Name','Language','Framework']
l2 = ['Hatim','Python','Django']

# using zip function to create a dictionary
my_dict = dict(zip(l1,l2))
print(my_dict)