# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:10:54 2020

@author: spiridiv
"""

def decor(func):
    def innerFunc():
        result = func()
        return result*2
    return innerFunc

def num():
    return 5

resultFunc = decor(num)
print(resultFunc())

#Another way to use decorator is by using @ - if we want the decorator to apply always

@decor
def num():
    return 5

print(num())