#!/usr/bin/env python
#-*- coding:utf8 -*-
from random import randint
from itertools import chain
chinese = [randint(60, 100) for _ in range(40)]
math = [randint(60, 100) for _ in range(40)]
english = [randint(60,100) for _ in range(40)]

count = 0
for s in chain(chinese,math,english):
    if s > 90:
        count += 1
print(count)



