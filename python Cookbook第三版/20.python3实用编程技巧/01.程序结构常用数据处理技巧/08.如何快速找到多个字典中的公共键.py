#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/18 11:37
# filename: 08.如何快速找到多个字典中的公共键.py
from random import randint, sample
from functools import reduce

d1 = {k: randint(1, 4) for k in sample('abcdefgh', randint(3, 6))}
d2 = {k: randint(1, 4) for k in sample('abcdefgh', randint(3, 6))}
d3 = {k: randint(1, 4) for k in sample('abcdefgh', randint(3, 6))}

# 1.使用字典的keys()方法，得到一个字典keys的集合
# 2.使用map函数，得到每个字典keys的集合
# 3.使用reduce，取所有字典keys集合的交集

dl = [d1, d2, d3]
# 找到三个字典中相同的keys
result = reduce(lambda a, b: a & b, map(dict.keys, dl))
print(result)
