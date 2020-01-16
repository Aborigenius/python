# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:41:27 2020

@author: spiridiv
"""
lst=[5,10,15,20]
import functools
result = functools.reduce(lambda x,y:x+y, lst)
print(result)
