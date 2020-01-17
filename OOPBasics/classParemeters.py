# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:36:06 2020

@author: spiridiv
"""

class Course:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
    
    def average(self):
        ratingsNumber=len(self.ratings)
        average = sum(self.ratings)/ratingsNumber
        print("Average Ratings For ",self.name, " is ",average)
        
c1 = Course("Python",[1,2,3,4,5])
print(c1.name)
print(c1.ratings)
c1.average()

c2 = Course("Java",[1,1,1,1])    
print(c2.name)
print(c2.ratings)
c2.average()