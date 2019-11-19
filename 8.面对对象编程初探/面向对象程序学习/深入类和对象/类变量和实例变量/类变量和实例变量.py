#!/usr/bin/env python
#-*- coding:utf8 -*-
class A:
    #类变量
    bb = 11
    def __init__(self,x,y):
        #实例变量
        self.x = x
        self.y = y

a = A(2,3)
A.bb = 111111
print(a.x,a.y,a.bb)    # 2 3 111111
print(A.bb)            # 111111

a.bb = 2222     #实际上会在实例对象a里面新建一个属性bb
print(a.bb)          # 2222
print(A.bb)          # 111111