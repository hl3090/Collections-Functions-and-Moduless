"""
 Write a Python program to remove duplicates from a list.

"""

l1 = [12,32,34,12,45,6,89,4,6,32]

new_list = []

for i in l1:
    if i not in new_list:
        new_list.append(i) 
        
print (new_list)        
        
    
    