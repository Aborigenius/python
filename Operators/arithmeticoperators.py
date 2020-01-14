# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:42:49 2020

@author: spiridiv
Arithmetic Operators
Standard + - * /
% - remainder of division (modulus)
** - powerof (exponent)
// - integer division (floor division) - remove decimal value if any
"""

a,b=10,5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#Remainder - in this case 0
print(a%b)
#PowerOff
print(a**b)

print(a//b)

"""
#Assignment operators
=
+= or -= or *= or /=
Selfexplaining
"""
a=b=c=10
print(a,b,c)

"""
Comparison operators - return True Or False
== equal
!= not equal
> greather then
< smaller then
>= greater or equal 
<= smaller or equal
"""

"""
Logical operators - they operate against booleans - assign or evaluate 
multiple conditions
and - X and Y must be true
or - X or Y must be true
not - neither X or Y must be true
X=True 
X=a>b
"""
x=20
y=30

print((x==20 and y==30))
print(not(x==20 and y==30))