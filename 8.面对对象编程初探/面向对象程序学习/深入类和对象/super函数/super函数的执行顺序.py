#!/usr/bin/env python
#-*- coding:utf8 -*-
class A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        print('B')
        super(B, self).__init__()


class C(A):
    def __init__(self):
        print('C')
        super().__init__()


class D(B,C):
    def __init__(self):
        print('D')
        super(D, self).__init__()

if __name__ == '__main__':
    print(D.__mro__)          #(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
    d = D()