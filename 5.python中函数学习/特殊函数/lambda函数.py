#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
普通的方法

def add(x):
    x += 3
    return x
nums = list(range(10))
new_num = []
for i in nums:
    new_num.append(add(i))
print(new_num)
'''

# 使用列表解析的方法
'''
nums = list(range(10))
new_nums = [ i+3 for i in nums]
print(new_nums)
'''
# 使用lambda函数后的方法
'''
nums = list(range(10))
lam = lambda x:x+3
n2 = []
for i in nums:
    n2.append(lam(i))
print(n2)


g = lambda x,y:x+y
print(g(6, 7))
'''
g_hu = lambda x, y: x ** y
# print(g_hu(5, 2))

n = 4
print(list(g_hu(n, i) for i in range(n)))
