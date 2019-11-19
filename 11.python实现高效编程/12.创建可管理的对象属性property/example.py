#!/usr/bin/env python
#-*- coding:utf8 -*-
from math import pi

class Circle(object):
    def __init__(self,radius):
        self.radius = radius

    @property
    def getRadius(self):
        return self.radius

    @getRadius.setter
    def setRadius(self,value):
        if not isinstance(value,(int, float)):
            raise ValueError("wrong type")
        self.radius = float(value)
    @property
    def getArea(self):
        return self.radius ** 2 ** pi

if __name__ == '__main__':
    c = Circle(3.2)
    print(c.getRadius)
    print(c.getArea)
    c.setRadius = 4.2
    print(c.getRadius)
    print(c.getArea)
