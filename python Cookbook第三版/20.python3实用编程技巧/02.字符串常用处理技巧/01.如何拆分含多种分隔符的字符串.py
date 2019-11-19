#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/18 22:45
# filename: 01.如何拆分含多种分隔符的字符串.py

s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'


# 第一种方式
def my_split(s, seps):
    res = [s]
    for sep in seps:
        t = []
        list(map(lambda ss: t.extend(ss.split(sep)), res))
        res = t
    return res


s1 = my_split(s, ',;|\t')
print(s1)  # ['ab', 'cd', 'efg', 'hi', 'jkl', 'mn', 'opq', 'rst', 'uvw', 'xyz']

# 第二种方式
import re

s2 = re.split('[,;|\t]+', s)
print(s2)  # ['ab', 'cd', 'efg', 'hi', 'jkl', 'mn', 'opq', 'rst', 'uvw', 'xyz']
