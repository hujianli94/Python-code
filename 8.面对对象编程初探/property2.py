#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/13 17:54
# filename: property2.py
class Rectangle:
    # 定义构造方法
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # 定义setsize()函数
    def setsize (self , size):
        self.width, self.height = size
    # 定义getsize()函数
    def getsize (self):
        return self.width, self.height
     # 定义getsize()函数
    def delsize (self):
        self.width, self.height = 0, 0
    # 使用property定义属性
    size = property(getsize, setsize, delsize, '用于描述矩形大小的属性')


print(Rectangle.size.__doc__)

# print(help(Rectangle.size))
rect = Rectangle(3, 4)
print(rect.size)
print(rect.getsize)
rect.size = 7, 8
print(rect.height)
print(rect.width)
del rect.size
print(rect.width)
print(rect.height)
