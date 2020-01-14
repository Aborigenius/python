# -*- coding: utf-8 -*-
#by default input is string
# =============================================================================
# s=input("Enter your input please:")
# print(s)
# 
# i=int(input("Enter an integer:"))
# print(i)
# =============================================================================

#lst = [x for x in input("Enter something separated by space:").split()]


#to Convert to int or float wrap the x 
#lst = [int(x) for x in input("Enter something separated by space:").split()]

#Split can set the separator
lst = [int(x) for x in input("Enter something separated by space:").split("|")]
print(lst)