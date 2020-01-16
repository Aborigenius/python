# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:34:19 2020

@author: spiridiv
"""

x = int(input("Enter a number:"))
if x == 0:
    print(x,"is zero")
elif x%2 == 0:
    print(x," is even")
else:
    print(x," is odd")