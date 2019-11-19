#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/13 15:47
# filename: 函数变量使用.py

"""
将函数本身赋值给变量
"""


def pow(base, exponent):
    result = 1
    for i in range(1, exponent - 1):
        result *= base
    return result


# 将pow函数赋值给my_fun，则my_fun可以被当成pow使用
my_fun = pow

print(my_fun(3, 4))


def area(width, height):
    return width * height


my_fun2 = area

#将area函数赋值给my_fun2，则my_fun2可以被当做area使用
print(my_fun2(4,5))
