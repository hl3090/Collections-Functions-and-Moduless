"""
Q. Write a Python program to find the second smallest number in a list.

"""


l1 = []

for i in range(1,6):
    num = int(input("Enter a number: "))
    l1.append(num)

l1.sort()

print("The sorted list: ",l1)
print ("Second smallest number: ",l1[1])    