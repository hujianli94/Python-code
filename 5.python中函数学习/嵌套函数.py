#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/17 23:25
# filename: 嵌套函数.py
def calcylate(n1, n2, option):
    multiple = 2

    # 定义加函数
    def add(a, b):
        return (a + b) * multiple

    # 定义减函数
    def sub(a, b):
        return (a - b) * multiple

    if option == "+":
        return add(n1, n2)
    elif option == "-":
        return sub(n1, n2)
    else:
        return


if __name__ == '__main__':
    print(calcylate(10, 20, "+"))
    print(calcylate(10, 30, " "))
