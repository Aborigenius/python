# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:18:10 2020

@author: spiridiv
List is created using []
"""

lst=[10,20,30.25,"ivan",-40,50]
print(lst)
#list support indexing, slicing and repetition. can hold different types of data
#Indexing
print(lst[3])
#slicing
print(lst[3:5])
#Repetition
print(lst*2)
print(len(lst))
#Add/remove elements
lst.append(45)
print(lst)
#lst.remove(45)
del(lst[3])
print(lst)
#Clear all values
#lst.clear()
#Insert on index
lst.insert(3,99)
#print min/max
print(max(lst))
print(min(lst))
#Sort
lst.sort()
print(lst)
#Reverse the sort
lst.sort(reverse=True)
print(lst)