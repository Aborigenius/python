# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:18:29 2020

@author: spiridiv
Bytes & ByteArray
Byte cannot be modified, byte array can. bOTH DOESN'T SUPPORT SLICING OR REPETITION
"""

lst = [20,30,40,55,255]
b=bytes(lst)
b1=bytearray(lst)
b1.append(66)
print(b1)