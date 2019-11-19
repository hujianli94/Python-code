#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/6 12:39
# filename: 07.不要使用含有两个以上表达式的列表推导式.py
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

squared = [[x ** 2 for x in row] for row in matrix]
print(squared)  # [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

squared2 = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]
print(squared2)  # [[6], [9]]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]

print(b)  # [6, 8, 10]
print(c)  # [6, 8, 10]
"""
1.列表推导式支持多级循环，每一项循环也支持多项条件
2.超过两个以上的表达式的列表推导是很难理解的，应该尽量避免
"""