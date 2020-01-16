# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:19:46 2020

@author: spiridiv
"""


def decorFunc(func):
    def innerFunc(n):
        result = func(n)
        result += " ,How are you?"
        return result
    return innerFunc

@decorFunc
def hello(name):
    return "Hello "+name

print(hello("Pesho"))