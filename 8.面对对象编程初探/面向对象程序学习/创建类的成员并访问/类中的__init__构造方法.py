#!/usr/bin/env python
# -*- coding:utf8 -*-
class INIT_class:
    def __init__(self, x, y=0):
        self.x = x
        self.y = y

    def mycalc(self):
        return self.x + self.y


diaoyong1 = INIT_class(2)
print("调用myclac方法1")
print(diaoyong1.mycalc())
print("".center(100, "*"))
print("调用myclac方法2")
diaoyong2 = INIT_class(5, 6)
print(diaoyong2.mycalc())
