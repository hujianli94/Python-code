#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/31 18:17
# filename: 递归函数.py
def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 2 * fn(n - 1) + fn(n - 2)


# 输出fn(10)的结果
print("输出fn(10)的结果:{}".format(fn(10)))
