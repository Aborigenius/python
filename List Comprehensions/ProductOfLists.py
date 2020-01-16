# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:52:23 2020

@author: spiridiv
"""
import random

listA=random.sample(range(1,50), 5)
listB=random.sample(range(1,50), 5)
print(listA)
print(listB)

result=[]

for i in range(len(listA)):
    result.append(listA[i]*listB[i])
    
print(result)

#Same with list comprehension
resultC=[listA[i]*listB[i] for i in range(len(listA))]

print(resultC)