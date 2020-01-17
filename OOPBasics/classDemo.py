# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:30:36 2020

@author: spiridiv
"""

class Product:
    
    def __init__(self):
        self.name = "Phone"
        self.description = "Can call people"
        self.price = 300
        
p1 = Product()

print(p1.name)
print(p1.description)
print(p1.price)