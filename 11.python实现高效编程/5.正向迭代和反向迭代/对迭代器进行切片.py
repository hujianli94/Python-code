#!/usr/bin/env python
#-*- coding:utf8 -*-
from itertools import islice
#对文件进行迭代
'''
t1 = open("/varr/log/message","r")
for i in islice(t1,100,200):
    print(i)
'''

#对内存数据进行迭代
l = range(20)
t = iter(l)
for x in islice(t,5,10):
    print(x, end=" ")
print()
for x in t:
    print(x)