#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/17 23:31
# filename: 函数类型.py
def calcylate(option):
    multiple = 2

    # 定义加函数
    def add(a, b):
        return (a + b) * multiple

    # 定义减函数
    def sub(a, b):
        return (a - b) * multiple

    if option == "+":
        return add
    elif option == "-":
        return sub
    else:
        return


if __name__ == '__main__':
    f1 = calcylate("+")
    f2 = calcylate("-")
    print(type(f1))
    print(f1(1, 2))
    print(f2(3, 1))
