#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/10 16:23
# filename: 局部函数.py

def get_math_func(type, nn):
    def square(n):
        return n * n

    def cube(n):
        return n * n * n

    def factorial(n):
        result = 1
        for index in range(2, n + 1):
            result *= index
        return result

    if type == "square":
        return square(nn)
    elif type == "cube":
        return cube(nn)
    else:
        return factorial(nn)


print(get_math_func("square", 3))
print(get_math_func("cube", 3))
print(get_math_func("", 3))
