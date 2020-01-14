# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:11:07 2020

@author: spiridiv
Range - Created with range(5) - if single value it starts from 0 and ends with at the 
provided value. If two values are provided it starts with the first and at the last
range(4,10). Can have steps, for example range(1,15,3) will be 1,4,7,10,13
"""

r=range(5)
print(r)
r=range(4,10)
for i in r:
    print(i)