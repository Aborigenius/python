# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:36:45 2020

Count objects created under class
@author: spiridiv
"""

class objectCounter:
    numberOfObject = 0
    def __init__(self):
        objectCounter.numberOfObject+=1

    @staticmethod        
    def displayCount():
        print(objectCounter.numberOfObject)
        
        
o1 = objectCounter()
o2 = objectCounter()
o3 = objectCounter()

objectCounter.displayCount()