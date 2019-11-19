#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = '18793'

list1 = ["apple", "banana", "grape", "orange", 'C']
print(list1.index("apple"))  # 打印apple的索引
print(list1.index("orange"))  # 打印orange的索引
print("orange" in list1)  # 判断orange是否在列表中

list1.sort()  # 排序
print("Sorted list :", list1)

list1.reverse()  # 反转
print("Reversed list:", list1)

index = list1.index("C")
# list1.pop(index)
del list1[index]
print(list1)
