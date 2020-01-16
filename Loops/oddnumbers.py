# -*- coding: utf-8 -*-

x=int(input("Enter starting number:"))
y=int(input("Enter ending number:"))

if x % 2 == 0:
    x+=1
    
i=x
while (i <= y):
    print(i)
    i+=2