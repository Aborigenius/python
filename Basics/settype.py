# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:04:11 2020

@author: spiridiv
SET doesn't allow duplicates and doesn't guarantee any order. Created with {}
"""

s={1,34,56,"KUR",1,34}
#Add elements
s.update([88,99])
print(s)
#Remove 
s.remove(99)
print(s)
#Set could be forzen
fr=frozenset(s)
