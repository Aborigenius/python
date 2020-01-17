# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:44:08 2020

@author: spiridiv
"""

class Car:
    def __init__(self,make,year):
        self.make=make
        self.year=year
        
    class Engine:
        def __init__(self,number):
            self.number=number
        def start(self):
            print("Engine Roars")
            
c = Car("Mechka",2007)
e = c.Engine(12345678)

print(c.make,c.year,e.number)
e.start()
        