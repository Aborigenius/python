# -*- coding: utf-8 -*-

x=123 #global

def someF():
    x=456 #Local
    print(x)
    print(globals()['x'])
    
#print(x)
#someF()
#use function as variable
z = someF
z()