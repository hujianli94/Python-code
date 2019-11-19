#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/6 12:26
# filename: 05.了解切割序列的办法.py
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("First four:", a[:4])
print("Last four:", a[-4:])
print('Middle two:', a[3:-3])
print()
b = a[4:]
print("Before: ", b)
b[1] = 99
print("After: ", b)
print("No change: ", a)
