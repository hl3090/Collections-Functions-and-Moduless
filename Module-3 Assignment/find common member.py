"""
Q. Write a Python function that takes two lists and returns true if they have at least one common member.
    """
    
l1 = [23,45,12,78,5]
l2 = [2,55,90,0,5]

common_numbers = []

for i in l1:
    if i in l2:
        common_numbers.append(i)
        
if common_numbers:
    print (i)
else:
    print ("False")            