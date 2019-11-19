#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/20 16:36
# filename: random模块.py
import random

# 0.0 <= x <=1.0随机数
print("0.0 <= x <=1.0随机数")
for i in range(0, 10):
    x = random.random()
    print(x)

# 0 <= x < 5 随机数
print("0 <= x < 5 随机数")
for i in range(0, 10):
    x = random.randrange(5)
    print(x, end=" ")
print()

# 5 <=x <=10 随机数
print("5 <=x <=10 随机数")
for i in range(0, 10):
    x = random.randrange(5, 10)
    print(x, end=" ")
print()

# 5 <=x <=10 随机数
print("5 <=x <=10 随机数")
for i in range(0, 10):
    x = random.randint(5, 10)
    print(x, end=" ")

print()
print("".rjust(100, "-"))

import random

print(random.random())  # 0~1随机浮点数
print(random.randint(1, 7))  # 随机整数1~7
print(random.randrange(1, 7))  # 随机整数，不包括7

print(random.choice('hello world'))  # 获取一个最近元素
print(random.choice(['1', '2', '3', ]))

print(random.sample([1, 2, 3, 4, 5], 4))
