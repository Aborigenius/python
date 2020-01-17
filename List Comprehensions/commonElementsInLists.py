# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:13:22 2020

@author: spiridiv
"""
import random

listA=random.sample(range(1,50), 5)
listB=random.sample(range(1,50), 5)

result=[]

for i in listA:
    if i in listB:
        result.append(i)
  
#Another Way of doing this is;
result1=[i for i in listA if i in listB]
 
print(result1)
      
print(result)
