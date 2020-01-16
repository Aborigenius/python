# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:37:35 2020

@author: spiridiv
"""

num=int(input("Please enter a number:"))
x=0
while x <= num:
    x+=1
    if x%10 == 0:
        continue
    elif x > 100:
        break
    else:
        print(x)
   