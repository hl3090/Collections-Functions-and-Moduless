"""
Q. Write a python program to calculate surface volume and area of a cylinder 
    
"""

radius = int(input("Enter the value of radius: "))
height = int(input("Enter the value of height: "))

area = 2 * 3.14 * radius * (radius + height)
volume = 3.14 * radius * radius * height

print ("Area of cylinder is: ",area)
print ("Volume of cylinder is: ",volume)