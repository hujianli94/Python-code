#!/usr/bin/env python
# -*- coding:utf8 -*-
class A:
    attr = 1


class B(A):
    pass


class C(A):
    attr = 2


class D(B, C):
    pass


if __name__ == '__main__':
    x = D()
    print(x.attr)




class A:
    attr = 1


class B(A):
    pass


class C(A):
    attr = 2


class D(B, C):
    attr = B.attr


if __name__ == '__main__':
    x = D()
    print(x.attr)