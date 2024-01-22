"""
Q. Write a Python function that takes a list and returns a new list with unique elements of the first list.

"""

l1 = [1,2,3,4,5,6,7,4,1,18,3,90]

# To find duplicates
new_list = []
duplicate_list =[]

for i in l1:
    if i not in new_list:
        new_list.append(i)
    else:
        duplicate_list.append(i)
        
print("New List : ",new_list)
print("Duplicate List : ",duplicate_list)            