# -*- coding: utf-8 -*-

import random

Start = 1
Stop = 30
limit = 10

randomListOfIntegers = [random.randint(Start, Stop) for iter in range(limit)]

for i in randomListOfIntegers:
    if i == 5:
        print("Damn five found, breaking")
        break
    else:
        print(i)