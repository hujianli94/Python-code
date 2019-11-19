#!/usr/bin/env python
#-*- coding:utf8 -*-
class D:
    pass

class E:
    pass

class C(E):
    pass

class B(D):
    pass

class A(B,C):
    pass

#顺序：A,B,D,C,E
#__mro__,类的属性查找顺序
print(A.__mro__)

#(<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class 'object'>)
