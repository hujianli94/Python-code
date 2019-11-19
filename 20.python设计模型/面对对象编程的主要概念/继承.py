#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
    继承表示一个雷可以继承父类的（大部分）功能
    继承被描述为重用基类中定义的功能，并允许对原始软件的实现进行独立扩展的选项
    继承可以利用不同类的对象之间的关系建立层次结构，python支持多重继承（继承多个基类）
    B类继承了A类，B类可以访问A类的方法
'''

class A(object):
    def a1(self):
        print("a1")

class B(A):
    def b(self):
        print("b")

b = B()
b.a1()
