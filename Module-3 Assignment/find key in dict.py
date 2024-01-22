"""
Q. Write a Python script to check if a given key already exists in a dictionary.
"""

my_dict ={
    "mobile": 1,
    "tv" : 2,
    "laptop" : 3    
}

check_key = input("Enter the key you want to know: ")

if check_key in my_dict:
    print("Given key already exists in dictionary")
else:
    print("Given does not exists in dictionary")    