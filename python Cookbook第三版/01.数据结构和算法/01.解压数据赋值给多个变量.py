#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/28 12:36
# filename: 01.解压数据赋值给多个变量.py

data = ["hujianli", 50, 91.1, (2019, 7, 28)]
_, shares, price, tuples = data
print(shares)
print(price)
print(tuples)
print(tuples[0])
