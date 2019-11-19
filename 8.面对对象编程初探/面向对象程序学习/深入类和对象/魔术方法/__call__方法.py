#!/usr/bin/env python
#-*- coding:utf8 -*-
class DistanceFrom(object):
    def __init__(self,orage):
        self.orage = orage

    def __call__(self, x):
        return abs(x + self.orage)

number = [1, 2, 3, 4, 5, 6, 7]
hu = DistanceFrom(10)
for i in number:
    print(hu(2)+i)
