fruit_dict = {'apple':5, 'banana':3, 'mango':4, 'orange':1, 'Grapes':2}

# Sort the dictionary in ascending order
sorted_dict_asc = dict(sorted(fruit_dict.items(), key=lambda item: item[1]))
print("Ascending order of dictionary: ",sorted_dict_asc)


# Sort the dictionary in descending order
sorted_dict_desc = dict(sorted(fruit_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order of dictionary: ",sorted_dict_desc)
