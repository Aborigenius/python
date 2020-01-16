# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:25:27 2020

@author: spiridiv
"""

def customGen(x,y):
    while x<y:
        yield x
        x+=1
        
result = customGen(20,30)
for i in result:
    print(i)