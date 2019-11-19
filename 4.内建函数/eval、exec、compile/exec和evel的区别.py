#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/20 23:29
# filename: exec和evel的区别.py
exec("print(\"I love Python \")")  # I love Python
eval("print(\"I love Python \")")  # I love Python

# 两者不同的是：evel执行完要返回结果，而exec执行完不返回结果。
a = 1
exec("a =2")
print(a)  # 2

hu = exec("2+3")  # 直接执行2+3，无返回结果
print(hu)  # None

hu = eval("2+3")  # 执行2+3，有返回结果
print(hu)  # 5
