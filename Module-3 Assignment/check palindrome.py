"""
Q. Write a python function that checks whether a passed string is palindrome or not.
"""

def check_palindrome(string):
    return string == string[::-1]  

print(check_palindrome("MOM"))
print(check_palindrome("string"))