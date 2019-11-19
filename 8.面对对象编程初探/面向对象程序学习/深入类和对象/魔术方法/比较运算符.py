#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/15 14:40
# filename: 比较运算符.py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 定义setSize()函数
    def setSize(self, size):
        self.width, self.height = size

    # 定义getSize()函数
    def getSize(self):
        return self.width, self.height

    # 使用property定义属性
    size = property(getSize, setSize)

    # 定义gt方法
    def __gt__(self, other):
        # 判断是否是Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError(">比较要求目标是Rectangle")
        return True if self.width * self.height > other.width * other.height else False

    # 定义eq方法
    def __eq__(self, other):
        # 判断是否是Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError("==比较要求目标是Rectangle")
        return True if self.width * self.height == other.width * other.height else False

    # 定义ge方法
    def __ge__(self, other):
        # 判断是否是Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError(">=比较要求目标是Rectangle")
        return True if self.width * self.height >= other.width * other.height else False


    def __repr__(self):
        return "Rectangle(width={},height={})".format(self.width, self.height)


r1 = Rectangle(4, 5)
r2 = Rectangle(3, 4)
print(r1 > r2)
print(r1 == r2)
print(r1 >= r2)
print(r1 != r2)

r3 = Rectangle(2, 6)
print(r2 > r3)
print(r2 == r3)
print(r2 >= r3)
print(r2 != r3)

print(r1)
print(r2)
print(r3)