#!/usr/bin/env python
#-*- coding:utf8 -*-
a = 4
b = 5
c = a if a > b else b
print(c)


if a > b:
    print(a)
else:
    print(b)


if a<=b:
    minalue = a
else:
    minalue = b



minalue = a if a<=b else b