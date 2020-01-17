# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 13:03:32 2020

@author: spiridiv
"""

class Student:
    major = "CSE"
    
    def __init__(self,rollNum,name):
        self.rollNum=rollNum
        self.name=name
    #Define function/Method
    def display(self):
        print(self.rollNum, self.name)
        
        
s1=Student(1,"Pesho")
s2=Student(2,"Big Pesho")

s1.display()
s2.display()
    