#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/18 22:54
# filename: 04.如何对字符串进行左, 右, 居中对齐.py

s = 'abc'

print(s.ljust(10))  # abc
print(s.ljust(10, "*"))  # abc*******
print(s.rjust(10))  # abc
print(s.rjust(10, "*"))  # *******abc
print(s.center(10))  # abc
print(s.center(10, "*"))  # ***abc****

# 把字典以左对齐的形式打印出来
d = {
    "hujianli": "19940722",
    'name': 'xiaojian',
    'address': '北京朝阳区',
    'age': '20'
}

w = max(map(len, d.keys()))  # 计算所有2key中字符最长的是多少
print(w)        #8


for k, v in d.items():
    print(k.ljust(w), ":", v)

"""
hujianli : 19940722
name     : xiaojian
address  : 北京朝阳区
age      : 20
"""