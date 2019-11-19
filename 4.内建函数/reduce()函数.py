#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/17 23:51
# filename: reduce()函数.py
from functools import reduce

a = (1, 2, 3, 4)
a_reduce = reduce(lambda acc, i: acc + i, a)
print(a_reduce)
b_reduce = reduce(lambda acc, i: acc + i, a, 2)
print(b_reduce)
