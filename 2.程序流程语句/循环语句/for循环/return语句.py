#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/10 15:41
# filename: return语句.py

def test():
    for i in range(10):
        for j in range(10):
            print("i的值是：%d,j的值是：%d" % (i, j))
            if j == 1:
                return
            print("return后的输出语句")

test()