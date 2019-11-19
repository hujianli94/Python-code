#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/13 16:05
# filename: 使用函数作为函数形参.py
def map(data, fn):
    result = []
    # 遍历data的所有数据，并进行计算
    for e in data:
        result.append(fn(e))
    return result

# 计算平方的函数
def square(n):
    return n * n

# 计算立方的函数
def cube(n):
    return n * n * n

# 定义一个计算阶乘的函数
def factorial(n):
    result = 1
    for index in range(2, n + 1):
        result *= index
    return result


data = [3, 4, 5, 6, 7]
print("原数据：{}".format(data))

print("计算数据的平方")
print(map(data, square))

print("计算数据的立方")
print(map(data, cube))

print("计算数据的阶乘")
print(map(data, factorial))
