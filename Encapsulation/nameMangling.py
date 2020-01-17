# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:22:10 2020

@author: spiridiv
"""

class Student:
    def __init__(self):
        self.__id=123
        self.__name="Pesho"
    
    def display(self):
        print(self.__id)
        print(self.__name)
        
s1 = Student()

s1.display()

#Name mangling - hidden/private fields can be accessed by entering
# _ClassName__Property

print(s1._Student__id);