# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:49:40 2020

@author: spiridiv
"""
import sympy

num=int(input("Please enter a number:"))
if (sympy.isprime(num) == True):
    print("Number %i is Prime"%(num))
else:
    print("Number %i is not prime"%(num))
