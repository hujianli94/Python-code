#!/usr/bin/env python
#-*- coding:utf8 -*-
from collections.abc import Iterable,Iterator

"""
Iterable：判断是不是可以迭代
Iterator：判断是不是迭代器
"""

a = [1, 2,]

print(isinstance(a, Iterable))   #list是可迭代的
print(isinstance(a, Iterator))   #list不是迭代器


