# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:22:49 2020

@author: spiridiv
Dictionaries. Created with {} - key-value pair. Any object can be used as key/value
"""

dict={1:"Ivan",2:"Pesho"}
print(dict)
#Keys or Values only
k=dict.keys()
for i in k:
    print(i)
v=dict.values()
for i in v:
    print(i)
#Print specific key
print(dict[1])
#Remove by index
del dict[1]
print(dict)

dict.get