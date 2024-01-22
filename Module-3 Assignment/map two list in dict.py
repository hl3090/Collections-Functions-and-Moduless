"""
Q. Write a Python program to map two lists into a dictionary
"""

l1 = [1,2,3]
l2 = ["Python","Java","PHP"]

new_dict = dict(zip(l1,l2))
print(new_dict)