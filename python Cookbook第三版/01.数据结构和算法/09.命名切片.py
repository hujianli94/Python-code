#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/28 19:37
# filename: 09.命名切片.py
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])

b = slice(0, 5, 2)
print(b.start)
print(b.stop)
print(b.step)
print(items[b])

print("分割线".center(100, "*"))
items[a] = [10, 11]
print(items)

del items[a]
print(items)
