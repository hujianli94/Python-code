#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/17 23:36
# filename: lambda函数.py

def calcylate(option):
    if option == "+":
        return lambda x, y: x + y
    elif option == "-":
        return lambda x, y: x - y

    else:
        return


f1 = calcylate("+")
f2 = calcylate("-")
print("1 + 2的值为{0}".format(f1(1, 2)))
print("3 + 1的值为{0}".format(f2(3, 1)))

