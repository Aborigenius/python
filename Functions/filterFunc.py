# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:30:09 2020

@author: spiridiv
"""

import random

lst = random.sample(range(1,50),10)
print(lst)
result = list(filter(lambda x:x%2==0,lst))
print(result)

for i in result:
    print(i)