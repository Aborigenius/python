# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:49:05 2020

@author: spiridiv
"""
#Strings
s="  I am awesome   "
s1="""I am awesome
on multiple
lines
"""
print(s,s1)
#Select something from string - Indexing
print(s[6])
#Print many time a string - Repeatition
print(s*4)
#Print lenght
print(len(s))
#Slicing
print(s[0:6])
print(s[0:])
print(s[:9])
#Print End
print(s[-5:])
#Print Every Second from begining to 9 - actually to 8 it's 1 before 9
print(s[0:9:2])
#Reverse
print(s[12::-1])
print(s[::-1])
#Strip empty spaces
print(s.strip())
#Clear from begining or end only
print(s.lstrip())
print(s.rstrip())
#Find part of the string
print(s.find("some",0,len(s)))
#Count occurences
print(s.count("w"))
#Replace
print(s.replace("awesome","super"))
#print lower, upper-case or title case
print(s.lower())
print(s.upper())
print(s.title())
#Collections

#List

#Set - doesn't allow duplicates

#Dictionaries = key:value pairs