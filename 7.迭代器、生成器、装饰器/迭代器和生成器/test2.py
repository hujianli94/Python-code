#!/usr/bin/env python
#-*- coding:utf8 -*-
from collections.abc import Iterator,Iterable

a = [1,2,]
iter_rator = iter(a)
print(isinstance(a, Iterable))   #True 可迭代的
print(isinstance(iter_rator, Iterator))   #True 迭代器
print(isinstance((x for x in range(10)), Iterator))
'''
Iterable：判断是不是可以迭代
Iterator：判断是不是迭代器
'''

# 总结
# 凡是可以for循环的，都是Iterable

# 凡是可以next()的，都是Iterator
# list，truple，dict，str，都是Itrable不是Iterator，但可以通过iter()函数获得一个Iterator对象