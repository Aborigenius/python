# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:57:23 2020

@author: spiridiv
"""
#New Line
print("I am awesome \n again")
#Separator
a=20
b=35
print(a,b,sep=" | ")

name="Pesho"
marks=87.3789

print("Name is",name, "Marks are",marks)
#Placeholders %i - int %s - string %f - float %.2f prints 2 symbols after the decimal point
print("Name is %s, Marks are %.2f"%(name,marks))
#Placeholder, but cannot restrict symbols after decimnal points
print("Name is {}, Marks Are {}".format(name,marks))