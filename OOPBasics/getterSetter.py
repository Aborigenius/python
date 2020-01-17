# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:51:18 2020

@author: spiridiv
"""

class Programmer:
    def setName(self,n):
        self.name=n
    def getName(self):
        return self.name
    
    def setSalary(self,sal):
        self.salary=sal
    def getSalary(self):
        return self.salary
    
    def setTechnologies(self,techs):
        self.technologies=techs
    def getTechnologies(self):
        return self.technologies
    
#Define function/Method
    def display(self):
        print(self.name)
        print(self.technologies)
        print(self.salary)
    
p1=Programmer()
p1.setName("Pesho")
p1.setSalary("100$")
p1.setTechnologies(["Java","More Java","I hate JAVA"])

print(p1.getName())
print(p1.getTechnologies())
print(p1.getSalary()+" because he use Java")

p1.display()