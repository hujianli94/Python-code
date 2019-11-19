#!/usr/bin/env python
#-*- coding:utf8 -*-
list1 = list(range(10))
string = "I love python"
# print(dir(list1))     #查看是否支持可迭代 __iter__或者__getitem__
# print(dir(string))
t = iter(list1)

# print(t.__next__))
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())

s = iter(string)
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())

