#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = '18793'

#堆栈的实现
list = ["apple", "grape", "grape"]
list.append("orange")
print(list)
print("弹出的元素: ",list.pop())
print(list)

#队列的实现
list = ["apple", "grape", "grape"]
list.append("orange")
print(list)
print("弹出的元素: ",list.pop(0))
print(list)