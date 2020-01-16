# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:38:38 2020

@author: spiridiv
"""

import random

lst = random.sample(range(1,50),10)
print(lst)
result = list(map(lambda n:n*2, lst))
print(result)