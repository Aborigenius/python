# -*- coding: utf-8 -*-

def display(name):
    def message():
        return "Hello "
    result = message()+name
    return result

print(display('Ivan'))