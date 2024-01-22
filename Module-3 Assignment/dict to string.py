"""
Q. Write a Python program to create a dictionary from a string.
"""

my_dict = {}
name = "w:3resources"

for i in name:
    if i in my_dict.keys():
        my_dict[i] += 1
    else:
        my_dict[i] = 1    
        
print(my_dict)        