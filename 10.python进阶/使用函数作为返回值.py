#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/13 16:16
# filename: 使用函数作为返回值.py
def get_math_func(type):
    # 定义一个计算平方的局部函数
    def square(n):
        return n * n

    # 计算立方
    def cube(n):
        return n * n * n

    # 计算阶乘
    def factorial(n):
        result = 1
        for index in range(2, n + 1):
            result *= index
        return result

    # 返回局部函数
    if type == "square":
        return square
    if type == "cube":
        return cube
    else:
        return factorial


if __name__ == '__main__':
    math_func = get_math_func("cube")  # 得到cube函数
    print(math_func(6))
    math_func2 = get_math_func("square")  # 得到square函数
    print(math_func2(8))
    math_func3 = get_math_func("other")  # 得到factorial函数
    print(math_func3(5))
