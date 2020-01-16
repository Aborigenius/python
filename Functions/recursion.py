# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:49:44 2020

@author: spiridiv
"""

def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result  

print(factorial(3))