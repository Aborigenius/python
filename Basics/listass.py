# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:36:28 2020

@author: spiridiv
"""

lst=["Albania","Bulgaria","India"]
lst.append("USA")
del(lst[3])
lst.insert(2,"Chile")
print(lst)

s={"Albania","Bulgaria","India"}
s.add("USA")
s.remove("Albania")
print(s)