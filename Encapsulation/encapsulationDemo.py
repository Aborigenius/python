# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:41:59 2020

@author: spiridiv
"""


class Patient:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    
    def setId(self,idN):
        self.idN=idN
    def getId(self):
        return self.idN
    
    def setSSN(self,ssn):
        self.ssn=ssn
    def getSSN(self):
        return self.ssn
    
#Define function/Method
    def display(self):
        print(self.idN)
        print(self.name)
        print(self.ssn)
#Print on single line
        print(self.idN,self.name,self.ssn)
        
p1=Patient()
p1.setId(13)
p1.setName("Pesho")
p1.setSSN(123450987)

p1.display()