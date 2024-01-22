"""
Q. Differentiate between append () and extend () methods?

Ans.      Append                                  Extend
  
  1. This method is used to add          1. This method is used to add multiple items
    a single item in given list.            in a single list .
    
  2. It can take a single value such     2. It takes a single iterable value such as list,
     as value , variable etc..              tuple , or string.

  3. Example -:                          3. Example -:
  
    l1 = [1,2,3,4]                          l1 = [23,4,5,12]
    l1.append(5)                            l1.extend(66,8)
    print (l1)                              print (l1) 

"""