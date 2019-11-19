#!/usr/bin/env python
# -*- coding:utf8 -*-
class Rect:
    def __init__(self, weight, height):
        self.__weight = weight
        self.__height = height

    @property  # 将方法转为属性
    def area(self):
        return self.__weight * self.__height

    @area.setter  # 设置属性的值
    def set_area(self, value):
        if isinstance(value, int):
            self.__weight += value
        else:
            raise ValueError

    @area.deleter
    def delete_are(self):
        print("删除属性.......")


hu = Rect(10, 20)
print(hu.area)

# 不能进行重新赋值，会报错
hu.set_area = 100
print(hu.area)
del hu.delete_are
