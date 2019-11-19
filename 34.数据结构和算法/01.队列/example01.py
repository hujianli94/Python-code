#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/12 11:40
# filename: example01.py
import collections

de = collections.deque([1, 2, 3, ])
de.extend([4, 5, 6])

print("The deque after extending deque at end is :")
print(de)

de.extend([7, 8, 9])
print("The deque after extending deque at end is :")
print(de)

de.rotate(-3)
print("The deque after extending deque at end is :")
print(de)

de.reverse()
print("The deque after extending deque at end is :")
print(de)