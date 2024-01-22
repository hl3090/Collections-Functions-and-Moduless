"""
Q. Write a python program to returns sum of all divisors of a number

"""

num = int(input("Enter a number: "))
sum = 0

i = 1
while i <= num:
    if num % i == 0: 
        sum += i 
    i += 1

print("The sum of all divisors of the number is: ",sum)