#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/28 13:12
# filename: 04. 查找最大或最小的 N 个元素.py
import heapq

"""
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# 寻找列表中最大的3个数
print(heapq.nlargest(3, nums))

# 寻找列表中最小的3个数
print(heapq.nsmallest(3, nums))

"""

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
cheap2 = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print(cheap)
print(cheap2)
