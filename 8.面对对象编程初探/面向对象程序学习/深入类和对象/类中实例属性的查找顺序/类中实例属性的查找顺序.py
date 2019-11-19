#!/usr/bin/env python
#-*- coding:utf8 -*-
class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B,C):
    pass

#顺序：A,B,C,D
#__mro__,类的属性查找顺序
print(A.__mro__)      #(<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)