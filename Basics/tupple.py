# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:53:19 2020

@author: spiridiv
TUPLE - same as list but cannot be modified
no insert, clear and so on. It is created using ()
"""

tpl=(40,50,40,"XYZ")
print(tpl)
#Indexing,Repetition,Count,length are supported
print(tpl[2])
print(tpl.index(50))
print(tpl*3)
print(tpl.count(40))
print(len(tpl))

#List to tuple
lst=[13,45,67,"XYZ"]
tpl1=tuple(lst)
print(tpl1)