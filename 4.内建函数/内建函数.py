#!/usr/bin/env python
#-*- coding:utf8 -*-
alst = [1,2,3,4,5]
print(list(filter(lambda x: x % 2,alst)))   #去重复，filter可以去掉列表中的重复元素
print(list(map(lambda x: x*2,alst)))        #map配合lambda函数一起使用，将列表中的元素扩大两倍

from functools import reduce
a = reduce(lambda x, y:x+y,alst)            #reduce()对list的每个元素反复调用函数f，并返回最终结果值
print(a)

#匿名函数
a = lambda x,y:x+y
print(a(2, 4))