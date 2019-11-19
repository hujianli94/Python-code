#!/usr/bin/env python
# -*- coding:utf8 -*-
import random

randomdict = {i: random.randint(10, 100) for i in range(1, 5)}
print(randomdict)
print()

name = ["hujianli", "xiaojian", "jianlihu", "mengxi"]
xingzhuo = ["水瓶座", "射手座", "天蝎座", "处女座"]
dict1 = {i: a for i, a in zip(name, xingzhuo)}
print(dict1)

print()

D = {k: v for (k, v) in zip(["q", "b", "d"], [1, 2, 3])}
print(D)

D1 = {x: x ** 2 for x in range(1, 5)}
print(D1)

D = {c: c * 4 for c in 'SPAM'}
print(D)

D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D)

# 利用字典推导式把字典的key和value做转换：{key:value}变成{value:key}的形式
# 字典推导式的用法
my_dict = {'derek1': 11, 'derek2': 22, 'derek3': 33}
reversed_dict = {value: key for key, value in my_dict.items()}
print(reversed_dict)  # {11: 'derek1', 22: 'derek2', 33: 'derek3'}

input_dict = {"one": 1, "tow": 2, "three": 3, "four": 4}
out_dict = {k: v for k, v in input_dict.items() if v % 2 == 0}
print(out_dict)

out_dict2 = {k for k, v in input_dict.items() if v % 2 == 0}
print(out_dict2)