#!/usr/bin/env python
#-*- coding:utf8 -*-
from functools import total_ordering

@total_ordering
class Rectangle(object):
    def __init__(self,w,h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __lt__(self, other):
        print("__lt__")
        return self.area() < other.area()

    def __eq__(self, other):
        print("__eq__")
        return self.area() == other.area()

r1 = Rectangle(5, 3)
r2 = Rectangle(4, 4)
# print(r1 < r2)
print(r1 <= r2)
print(r1 >= r2)