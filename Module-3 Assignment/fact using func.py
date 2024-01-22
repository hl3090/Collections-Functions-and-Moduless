"""
Q. Write a Python function to calculate the factorial of a number (a nonnegative integer)...

"""

def factorial(num):
    f = 1
    for i in range(1,num+1):
        f *= i
        
    print(f)    

n = int(input("Enter a number: "))
factorial(n)