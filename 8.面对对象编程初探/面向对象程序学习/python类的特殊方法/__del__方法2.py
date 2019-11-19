#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/22 9:10
# filename: __del__方法2.py
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def __del__(self):
        """  析构函数 """
        print("complex 不存在了")


x = Complex(3.0, -4.5)
print(x.r,x.i)
print(x)
del x


class Test(object):
    def __init__(self):
        print("这个是构造函数....")

    def __del__(self):
        print("这个是析构函数....，结束时自动调用...")

hu = Test()